
import streamlit as st

def main():
    """Display the PDF Chat AI application."""
    st.set_page_config(
        page_title="PDF Chat AI",
        page_icon="📄",
        layout="wide",
    )

    st.title("PDF Chat AI")
    st.write("Upload a PDF to prepare it for question answering.")

    uploaded_file = st.file_uploader(
        "Choose a PDF document",
        type=["pdf"],
        help="Select a PDF file from your device.",
    )

    if uploaded_file is not None:
        st.success("PDF selected successfully.")
        st.write("**Filename:**", uploaded_file.name)
        st.write("**File size:**", f"{uploaded_file.size:,} bytes")

        st.info(
            "PDF text extraction and AI question answering "
            "will be connected next."
        )


if __name__ == "__main__":
    main()
