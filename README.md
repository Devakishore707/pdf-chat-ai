# PDF Chat AI

A cloud-hosted AI application designed to answer questions about uploaded PDF documents using Retrieval-Augmented Generation (RAG).

## Project Status

**Current stage:** Foundation and architecture planning.

The application is under active development. Features described below are planned and are not yet implemented.

## Objectives

- Ask natural-language questions about PDF documents.
- Generate answers grounded in relevant document passages.
- Provide verifiable source-page references.
- Support follow-up questions.
- Clearly identify when sufficient evidence is unavailable.
- Operate independently of the developer's local computer.
- Target a zero-cost deployment using eligible free-tier resources.

## Planned Technology

- Python
- Streamlit
- PyMuPDF
- Embeddings and retrieval
- A suitable LLM provider
- GitHub for version control

Final technology choices will depend on compatibility, privacy, and free-tier availability.

## Architecture

The planned system separates document processing, retrieval, model integration, application workflows, and user interface code.

See the [architecture document](docs/architecture.md) and [project structure](docs/project-structure.md).

## Development Principles

- Modular, maintainable code
- Automated testing
- Secure secret management
- Document-grounded answers
- Verifiable citations
- Explicit handling of service limits and errors
- No mandatory paid dependencies

## Current Limitations

The application is not yet functional. Cloud deployment, model integration, persistent storage, authentication, and PDF question answering remain to be implemented.

Free services may impose usage limits, sleep during inactivity, or change their terms.

## Development

Development will proceed incrementally. Each feature will be implemented, tested, and documented before the next stage.

## License

No open-source license has been selected yet.
