
import streamlit as st

from pdf_chat.pdf.extractor import extract_pages


def main():
    """Display the PDF Chat AI application."""
    st.set_page_config(
        page_title="PDF Chat AI",
        page_icon="📄",
        layout="wide",
    )

    st.title("PDF Chat AI")
    st.write("Upload a PDF to extract its text.")

    uploaded_file = st.file_uploader(
        "Choose a PDF document",
        type=["pdf"],
        help="Select a PDF file from your device.",
    )

    if uploaded_file is not None:
        st.success(f"Selected: {uploaded_file.name}")

        try:
            pages = extract_pages(uploaded_file.getvalue())

            if not any(page["text"].strip() for page in pages):
                st.warning(
                    "No selectable text was found. "
                    "This PDF may contain scanned images."
                )
            else:
                st.success(
                    f"Successfully processed {len(pages)} pages."
                )

                for page in pages:
                    with st.expander(
                        f"Page {page['page_number']}"
                    ):
                        st.text(page["text"] or "No text on this page.")

        except ValueError as error:
            st.error(str(error))


if __name__ == "__main__":
    main()
