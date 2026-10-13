# PDF Chat AI — Project Structure

## Design Principles

- Separate presentation, business logic, document processing, retrieval, and model integration.
- Keep configuration separate from application logic.
- Use small modules with clearly defined responsibilities.
- Make core functionality testable without deploying the application.
- Keep secrets, user documents, generated indexes, and temporary data out of source control.

## Planned Structure

```text
pdf-chat-ai/
├── .github/
│   └── workflows/
├── docs/
│   ├── architecture.md
│   ├── requirements.md
│   └── project-structure.md
├── src/
│   └── pdf_chat/
│       ├── __init__.py
│       ├── config.py
│       ├── pdf/
│       ├── retrieval/
│       ├── llm/
│       └── services/
├── tests/
├── .gitignore
├── .env.example
├── requirements.txt
├── app.py
└── README.md
```

## Module Responsibilities

### app.py
Application entry point and user interface.

### config.py
Centralized configuration validation and environment-based settings.

### pdf/
PDF validation, text extraction, page tracking, and extraction errors.

### retrieval/
Text chunking, embeddings, indexing, and relevant passage retrieval.

### llm/
Model-provider integration, prompt construction, and response handling.

### services/
Coordinates PDF processing, retrieval, and answer generation.

### tests/
Unit tests, integration tests, and regression tests for answer quality.

### docs/
Architecture decisions, requirements, setup instructions, and technical documentation.

## Security and Storage

- Never commit API keys or credentials.
- Exclude virtual environments, caches, temporary uploads, and generated data from Git.
- Treat uploaded documents as untrusted input.
- Do not assume temporary cloud storage is persistent.
- Define document ownership, retention, and deletion behavior before supporting multiple users.

## Implementation Strategy

Create only the files needed for each milestone. Add tests alongside each feature and update documentation when architectural decisions change.

The exact deployment, database, and model-provider choices will be finalized after checking free-tier limits, compatibility, and privacy terms.
