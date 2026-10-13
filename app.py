
import streamlit as st


def main():
    """Display the initial PDF Chat AI application."""
    st.set_page_config(
        page_title="PDF Chat AI",
        page_icon="📄",
        layout="wide",
    )

    st.title("PDF Chat AI")
    st.write(
        "Ask questions about your PDF documents. "
        "Document processing and AI features are coming next."
    )

    st.info(
        "The application foundation is ready. "
        "PDF upload and question answering are not implemented yet."
    )


if __name__ == "__main__":
    main()
