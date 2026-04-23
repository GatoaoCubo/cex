"""
cex_sdk.vectordb.base -- Abstract base for vector databases.

Absorbed from: agno/vectordb/base.py
CEX version: 8.3.0 | Pillar: P01/P10
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from cex_sdk.knowledge.document import Document


@dataclass
class SearchResult:
    """A single search result with score."""
    document: Document
    score: float = 0.0


class VectorDb(ABC):
    """Abstract base for vector databases."""

    def __init__(self, name: str = "vectordb", collection: str = "default"):
        self.name = name
        self.collection = collection

    @abstractmethod
    def create(self) -> None:
        """Create/initialize the collection."""
        ...

    @abstractmethod
    def insert(self, documents: List[Document]) -> None:
        """Insert documents with embeddings."""
        ...

    @abstractmethod
    def search(self, query_embedding: List[float], limit: int = 5) -> List[SearchResult]:
        """Search by embedding vector."""
        ...

    @abstractmethod
    def delete(self, ids: List[str]) -> None:
        """Delete documents by ID."""
        ...

    def upsert(self, documents: List[Document]) -> None:
        """Insert or update. Default: delete + insert."""
        ids = [d.id for d in documents if d.id]
        if ids:
            self.delete(ids)
        self.insert(documents)

    def exists(self) -> bool:
        """Check if collection exists. Default: True."""
        return True
