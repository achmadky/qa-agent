from pathlib import Path
import pdfplumber
import docx
from bs4 import BeautifulSoup


def load_document(file_path):

    path = Path(file_path)
    ext = path.suffix.lower()

    if ext in [".md", ".txt"]:
        return path.read_text()

    elif ext == ".pdf":
        text = ""
        with pdfplumber.open(file_path) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
        return text

    elif ext == ".docx":
        doc = docx.Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs)

    elif ext == ".html":
        with open(file_path) as f:
            soup = BeautifulSoup(f, "html.parser")
            return soup.get_text()

    else:
        raise ValueError("Unsupported file format")