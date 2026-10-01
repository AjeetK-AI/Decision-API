#Parse the relevant document or section from POLICY

from pypdf import PdfReader

def parse_pdf(file_path:str) ->str:
    reader = PdfReader(file_path)

    text =""

    for page in reader.pages:
        page_text = page.extract_text()

        if page_text:
            text += page_text+ "\n"

            return text