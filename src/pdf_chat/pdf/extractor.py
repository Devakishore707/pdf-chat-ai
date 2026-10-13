
"""Extract page-level text from PDF documents."""

import fitz


def extract_pages(pdf_bytes: bytes) -> list[dict[str, object]]:
    """Extract text and 1-based page numbers from PDF bytes.

    Args:
        pdf_bytes: The contents of a PDF file.

    Returns:
        A list of dictionaries containing page_number and text.

    Raises:
        ValueError: If the input is empty or is not a valid PDF.
    """
    if not pdf_bytes:
        raise ValueError("The uploaded PDF is empty.")

    try:
        with fitz.open(stream=pdf_bytes, filetype="pdf") as document:
            if document.is_encrypted:
                raise ValueError(
                    "Password-protected PDFs are not supported yet."
                )

            return [
                {
                    "page_number": page_number,
                    "text": page.get_text("text"),
                }
                for page_number, page in enumerate(document, start=1)
            ]

    except (fitz.FileDataError, RuntimeError) as error:
        raise ValueError("The uploaded file is not a valid readable PDF.") from error
