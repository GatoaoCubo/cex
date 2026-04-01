"""Ollama local embeddings."""

from __future__ import annotations

from typing import List

from cex_sdk.knowledge.embedder.base import Embedder


class OllamaEmbedder(Embedder):
    """Local embeddings via Ollama."""

    def __init__(self, model: str = "nomic-embed-text", host: str = "http://localhost:11434", dimensions: int = 768):
        self.model = model
        self.host = host
        self.dimensions = dimensions

    def embed(self, text: str) -> List[float]:
        try:
            import ollama
        except ImportError:
            raise ImportError("pip install ollama")
        client = ollama.Client(host=self.host)
        response = client.embeddings(model=self.model, prompt=text)
        return response["embedding"]
