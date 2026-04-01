"""Cohere reranker."""

from __future__ import annotations

from typing import List, Optional, Tuple

from cex_sdk.knowledge.document import Document
from cex_sdk.knowledge.reranker.base import Reranker


class CohereReranker(Reranker):
    def __init__(self, model: str = "rerank-v3.5", api_key: Optional[str] = None):
        self.model = model
        self.api_key = api_key

    def rerank(self, query: str, documents: List[Document], top_k: int = 5) -> List[Tuple[Document, float]]:
        try:
            import cohere
        except ImportError:
            raise ImportError("pip install cohere")
        import os
        client = cohere.Client(api_key=self.api_key or os.environ.get("COHERE_API_KEY"))
        texts = [d.content for d in documents]
        response = client.rerank(model=self.model, query=query, documents=texts, top_n=top_k)
        return [(documents[r.index], r.relevance_score) for r in response.results]
