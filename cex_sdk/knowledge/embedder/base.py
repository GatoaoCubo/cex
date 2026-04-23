"""
cex_sdk.knowledge.embedder.base -- Embedder ABC.

CEX version: 8.3.0 | Pillar: P01 | 8F: INJECT (F3)
# Originally from agno. Licensed under MPL-2.0.
"""

from __future__ import annotations

from abc import ABC, abstractmethod
from typing import List


class Embedder(ABC):
    """Abstract base for text embedding providers."""

    dimensions: int = 0

    @abstractmethod
    def embed(self, text: str) -> List[float]:
        """Embed a single text string."""
        ...

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        """Embed multiple texts. Default calls embed() per text."""
        return [self.embed(t) for t in texts]

    def get_dimensions(self) -> int:
        return self.dimensions
