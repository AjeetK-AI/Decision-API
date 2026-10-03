# FastAPI
from fastapi import FastAPI, UploadFile, File, HTTPException

from app.models.gmail import EmailRequest, DecisionResponse
from app.decision.engine import decide
from app.services.llm_policy_parser import extract_policy_rules_with_llm
from app.policy.store import active_policy_rules
from app.services.policy_preprocessor import preprocess_policy

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


        # 5. Preprocess policy

        preprocessed_policy = preprocess_policy(text)

        rule_blocks = preprocessed_policy["rules"]


        # 6. Send individual rule blocks to LLM

        rules = extract_policy_rules_with_llm(
            rule_blocks
        )


        # 7. Safety check
        # Make sure no rules were lost

        expected_ids = {
            rule["rule_id"]
            for rule in rule_blocks
        }

        actual_ids = {
            rule.rule_id
            for rule in rules
        }

        if expected_ids != actual_ids:

            missing_ids = expected_ids - actual_ids
            unexpected_ids = actual_ids - expected_ids

            raise HTTPException(
                status_code=500,
                detail={
                    "error": "Policy extraction incomplete",
                    "expected_rule_count": len(expected_ids),
                    "actual_rule_count": len(actual_ids),
                    "missing_rules": sorted(missing_ids),
                    "unexpected_rules": sorted(unexpected_ids),
                }
            )


        # 8. Only activate validated policy

        active_policy_rules.clear()

        active_policy_rules.extend(rules)


        # 9. Return result

        return {
            "filename": file.filename,
            "pages": len(reader.pages),
            "characters": len(text),
            "rule_count": len(rules),
            "rules": rules
        }


    finally:

        # 10. Delete temporary file

        os.remove(temp_path)