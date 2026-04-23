"""Recursive character text splitting -- most popular strategy."""

from __future__ import annotations

from typing import List, Optional

from cex_sdk.knowledge.chunking.base import ChunkingStrategy
from cex_sdk.knowledge.document import Document


class RecursiveChunking(ChunkingStrategy):
    """Split recursively using multiple separators (LangChain-style)."""

    def __init__(
        self,
        chunk_size: int = 4000,
        chunk_overlap: int = 200,
        separators: Optional[List[str]] = None,
    ):
        super().__init__(chunk_size, chunk_overlap)
        self.separators = separators or ["\n\n", "\n", ". ", " "]

    def chunk(self, document: Document) -> List[Document]:
        text = document.content
        if len(text) <= self.chunk_size:
            return [document]

        chunks = self._split(text, self.separators)
        return [
            Document(
                content=c,
                meta_data={**document.meta_data, "chunk_index": i, "strategy": "recursive"},
            )
            for i, c in enumerate(chunks) if c.strip()
        ]

    def _split(self, text: str, separators: List[str]) -> List[str]:
        if not separators:
            return self._force_split(text)

        sep = separators[0]
        remaining_seps = separators[1:]
        parts = text.split(sep) if sep else [text]

        result: List[str] = []
        current = ""

        for part in parts:
            candidate = current + sep + part if current else part
            if len(candidate) <= self.chunk_size:
                current = candidate
            else:
                if current:
                    result.append(current)
                if len(part) > self.chunk_size:
                    result.extend(self._split(part, remaining_seps))
                    current = ""
                else:
                    current = part

        if current:
            result.append(current)
        return result

    def _force_split(self, text: str) -> List[str]:
        chunks = []
        start = 0
        while start < len(text):
            end = min(start + self.chunk_size, len(text))
            chunks.append(text[start:end])
            start = end - self.chunk_overlap
        return chunks
