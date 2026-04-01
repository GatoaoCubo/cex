"""OpenAI embeddings provider."""

from __future__ import annotations

from typing import List, Optional

from cex_sdk.knowledge.embedder.base import Embedder


class OpenAIEmbedder(Embedder):
    """OpenAI text-embedding models."""

    def __init__(self, model: str = "text-embedding-3-small", dimensions: int = 1536, api_key: Optional[str] = None):
        self.model = model
        self.dimensions = dimensions
        self.api_key = api_key

    def _get_client(self):
        try:
            from openai import OpenAI
        except ImportError:
            raise ImportError("pip install openai")
        import os
        return OpenAI(api_key=self.api_key or os.environ.get("OPENAI_API_KEY"))

    def embed(self, text: str) -> List[float]:
        client = self._get_client()
        response = client.embeddings.create(model=self.model, input=text)
        return response.data[0].embedding

    def embed_batch(self, texts: List[str]) -> List[List[float]]:
        client = self._get_client()
        response = client.embeddings.create(model=self.model, input=texts)
        return [d.embedding for d in response.data]
