"""
cex_sdk.knowledge.chunking.base -- Chunking strategy ABC.

CEX version: 8.2.0 | Pillar: P01 | 8F: INJECT (F3)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List

from cex_sdk.knowledge.document import Document


class ChunkingStrategy(ABC):
    """Abstract base for document chunking strategies."""

    def __init__(self, chunk_size: int = 4000, chunk_overlap: int = 200):
        self.chunk_size = chunk_size
        self.chunk_overlap = chunk_overlap

    @abstractmethod
    def chunk(self, document: Document) -> List[Document]:
        """Split a document into chunks."""
        ...
