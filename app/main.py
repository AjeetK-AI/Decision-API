# FastAPI
from fastapi import FastAPI, UploadFile, File, HTTPException
from app.models.gmail import EmailRequest, DecisionResponse
from app.decision.engine import decide
from app.policy.engine import check_policy
from app.policy.parser import extract_policy_rules
from app.policy.store import active_policy_rules

from pypdf import PdfReader
import tempfile
import os


app = FastAPI(
    title="Gmail Decision API",
    version="1.01.2"
)


@app.get("/health")
def health():
    return {
        "status": "Ok"
    }


@app.post(
    "/v1/gmail/decide",
    response_model=DecisionResponse
)
def gmail_decision(email: EmailRequest):

    return decide(email)


@app.post("/v1/policies/upload")
async def upload_policy(file: UploadFile = File(...)):

# 1. Check that the uploaded file is a PDF
    if file.content_type != "application/pdf":
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are supported"
        )

# 2. Create temporary PDF file
    with tempfile.NamedTemporaryFile(
        delete=False,
        suffix=".pdf"
    ) as temp_file:

        contents = await file.read()
        temp_file.write(contents)
        temp_path = temp_file.name

    try:

        # 3. Read PDF
        reader = PdfReader(temp_path)

        text = ""

        # 4. Extract text from every page
        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        # 5. Return extracted information
        rules = extract_policy_rules(text)

        active_policy_rules.clear()
        active_policy_rules.extend(rules)


         # 6. Return extracted information

        return {
            "filename": file.filename,
            "pages": len(reader.pages),
            "characters": len(text),
            "text": text,
            "rules": rules
        }

    finally:

        # 6. Delete temporary file
        os.remove(temp_path)