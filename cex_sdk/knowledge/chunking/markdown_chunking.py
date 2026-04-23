"""Markdown-aware chunking -- splits by headers."""

from __future__ import annotations

import re
from typing import List

from cex_sdk.knowledge.chunking.base import ChunkingStrategy
from cex_sdk.knowledge.document import Document


class MarkdownChunking(ChunkingStrategy):
    """Split markdown by headers (## or ###), keeping context."""

    def chunk(self, document: Document) -> List[Document]:
        text = document.content
        if len(text) <= self.chunk_size:
            return [document]

        # Split by headers
        sections = re.split(r"(?=^#{1,3}\s)", text, flags=re.MULTILINE)
        chunks: List[Document] = []

        current = ""
        for section in sections:
            if len(current) + len(section) <= self.chunk_size:
                current += section
            else:
                if current.strip():
                    chunks.append(Document(
                        content=current.strip(),
                        meta_data={**document.meta_data, "chunk_index": len(chunks), "strategy": "markdown"},
                    ))
                current = section

        if current.strip():
            chunks.append(Document(
                content=current.strip(),
                meta_data={**document.meta_data, "chunk_index": len(chunks), "strategy": "markdown"},
            ))

        return chunks or [document]
