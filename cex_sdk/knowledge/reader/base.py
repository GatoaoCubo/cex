"""
cex_sdk.knowledge.reader.base -- Abstract base for document readers.

Absorbed from: agno/knowledge/reader/base.py
CEX version: 8.1.0 | Pillar: P01 | 8F: INJECT (F3)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from pathlib import Path
from typing import IO, List, Optional, Union

from cex_sdk.knowledge.document import Document


class Reader(ABC):
    """Abstract base for reading files into Documents."""

    chunk_size: int = 4000
    chunk: bool = True
    separators: Optional[list[str]] = None

    @abstractmethod
    def read(self, source: Union[str, Path, IO]) -> List[Document]:
        """Read source and return list of Documents."""
        ...

    def _simple_chunk(self, text: str, meta: dict) -> List[Document]:
        if not self.chunk or len(text) <= self.chunk_size:
            return [Document(content=text, meta_data=meta)]

        seps = self.separators or ["\n\n", "\n", ". ", " "]
        chunks = []
        remaining = text

        while remaining:
            if len(remaining) <= self.chunk_size:
                chunks.append(remaining)
                break

            split_at = self.chunk_size
            for sep in seps:
                idx = remaining.rfind(sep, 0, self.chunk_size)
                if idx > 0:
                    split_at = idx + len(sep)
                    break

            chunks.append(remaining[:split_at])
            remaining = remaining[split_at:]

        return [
            Document(content=c, meta_data={**meta, "chunk_index": i})
            for i, c in enumerate(chunks) if c.strip()
        ]
