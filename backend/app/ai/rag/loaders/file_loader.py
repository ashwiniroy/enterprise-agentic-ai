from pathlib import Path

from app.ai.rag.loaders.pdf_loader import load_pdf
from app.ai.rag.loaders.text_loader import load_text
from app.ai.rag.loaders.excel_loader import load_excel


SUPPORTED_EXTENSIONS = {
    ".pdf",
    ".txt",
    ".xlsx",
}


def load_file(file_path: str):
    path = Path(file_path)

    extension = path.suffix.lower()

    if extension not in SUPPORTED_EXTENSIONS:
        raise ValueError(
            f"Unsupported file type: {extension}"
        )

    if extension == ".pdf":
        return load_pdf(file_path)

    if extension == ".txt":
        return load_text(file_path)

    if extension == ".xlsx":
        return load_excel(file_path)

    raise ValueError(
        f"Unable to load file: {file_path}"
    )