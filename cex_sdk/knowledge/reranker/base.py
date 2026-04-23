"""
cex_sdk.knowledge.reranker.base -- Reranker ABC.

CEX version: 8.4.0 | Pillar: P01 | 8F: INJECT (F3)
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List, Tuple

from cex_sdk.knowledge.document import Document


class Reranker(ABC):
    """Abstract base for reranking search results."""

    @abstractmethod
    def rerank(self, query: str, documents: List[Document], top_k: int = 5) -> List[Tuple[Document, float]]:
        """Rerank documents by relevance to query.

        Returns list of (document, score) tuples, sorted by relevance.
        """
        ...
