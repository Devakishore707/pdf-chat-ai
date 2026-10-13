
import fitz
import pytest

from src.pdf_chat.pdf.extractor import extract_pages


def create_test_pdf() -> bytes:
    """Create a small two-page PDF entirely in memory."""
    document = fitz.open()

    first_page = document.new_page()
    first_page.insert_text((72, 72), "Hello from page one.")

    second_page = document.new_page()
    second_page.insert_text((72, 72), "Hello from page two.")

    pdf_bytes = document.tobytes()
    document.close()

    return pdf_bytes


def test_extracts_text_and_page_numbers():
    pages = extract_pages(create_test_pdf())

    assert len(pages) == 2
    assert pages[0]["page_number"] == 1
    assert "Hello from page one." in pages[0]["text"]
    assert pages[1]["page_number"] == 2
    assert "Hello from page two." in pages[1]["text"]


def test_rejects_empty_input():
    with pytest.raises(ValueError, match="empty"):
        extract_pages(b"")


def test_rejects_invalid_pdf():
    with pytest.raises(ValueError, match="valid readable PDF"):
        extract_pages(b"This is not a PDF.")
