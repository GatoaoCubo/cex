"""Fixed-size chunking strategy."""

from __future__ import annotations

from typing import List

from cex_sdk.knowledge.chunking.base import ChunkingStrategy
from cex_sdk.knowledge.document import Document


class FixedChunking(ChunkingStrategy):
    """Split by fixed character count with overlap."""

    def chunk(self, document: Document) -> List[Document]:
        text = document.content
        if len(text) <= self.chunk_size:
            return [document]

        chunks = []
        start = 0
        i = 0
        while start < len(text):
            end = min(start + self.chunk_size, len(text))
            chunks.append(Document(
                content=text[start:end],
                meta_data={**document.meta_data, "chunk_index": i, "strategy": "fixed"},
            ))
            # Advance by at least 1 char to avoid infinite loops
            advance = max(end - self.chunk_overlap, start + 1)
            if advance >= len(text):
                break
            start = advance
            i += 1
        return chunks
