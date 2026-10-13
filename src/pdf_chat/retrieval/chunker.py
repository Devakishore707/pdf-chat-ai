
"""Split extracted PDF pages into overlapping text chunks."""


def chunk_pages(
    pages: list[dict[str, object]],
    chunk_size: int = 1000,
    overlap: int = 150,
) -> list[dict[str, object]]:
    """Split page text into chunks while retaining page references.

    Args:
        pages: Page dictionaries produced by the PDF extractor.
        chunk_size: Maximum number of characters in each chunk.
        overlap: Number of characters shared between adjacent chunks.

    Returns:
        Chunk dictionaries containing text, page number, and chunk index.
    """
    if chunk_size <= 0:
        raise ValueError("chunk_size must be greater than zero.")

    if overlap < 0 or overlap >= chunk_size:
        raise ValueError("overlap must be non-negative and smaller than chunk_size.")

    chunks = []

    for page in pages:
        text = str(page.get("text", "")).strip()
        page_number = int(page["page_number"])

        if not text:
            continue

        start = 0
        while start < len(text):
            end = min(start + chunk_size, len(text))
            chunk_text = text[start:end].strip()

            if chunk_text:
                chunks.append(
                    {
                        "text": chunk_text,
                        "page_number": page_number,
                        "chunk_index": len(chunks),
                    }
                )

            if end == len(text):
                break

            start = end - overlap

    return chunks
