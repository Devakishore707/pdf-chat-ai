# PDF Chat AI — Architecture

## Project Vision

Build a cloud-hosted application that allows users to upload PDF documents and ask questions answered using relevant document content.

## Core Requirements

- Operate independently of the developer's personal computer.
- Use free-tier resources and open-source software wherever possible.
- Ground answers in retrieved PDF content.
- Provide source-page references when available.
- Acknowledge when the document does not contain sufficient evidence.
- Protect API keys and uploaded documents.
- Use modular, testable, maintainable code.

## Planned Components

1. **User Interface:** PDF upload, chat, and source display.
2. **Document Processing:** PDF text extraction and page tracking.
3. **Retrieval Pipeline:** Text chunking, embeddings, and relevant passage retrieval.
4. **LLM Integration:** Generate answers using retrieved evidence.
5. **Application Configuration:** Environment variables and protected secrets.
6. **Testing:** Unit tests, integration tests, and answer-grounding checks.
7. **Cloud Deployment:** Host the application independently of the developer's computer.

## Initial Technology Candidates

- Python
- Streamlit
- PyMuPDF
- ChromaDB or another suitable retrieval solution
- An eligible free-tier LLM service or a viable hosted open model
- GitHub for source control

Final choices will be confirmed after checking free-tier limits, privacy terms, and deployment compatibility.

## Reliability Principles

- Never expose secrets in source code.
- Do not invent document citations.
- Handle scanned PDFs and extraction failures explicitly.
- Treat uploaded document content as untrusted input.
- Avoid relying on temporary storage for documents that must persist.
- Document known limitations and resource constraints.

## Deployment Requirement

The deployed application must run without local project files on the developer's computer. Source code must be stored in GitHub, and runtime dependencies must be available in the deployment environment.

## Cost Policy

The target operating cost is zero. The project must not silently depend on paid services. Free-tier quotas and service limitations must be documented and monitored.

## Development Workflow

Implement one component at a time, add tests, verify its behavior, and commit changes through GitHub before proceeding to the next component.
