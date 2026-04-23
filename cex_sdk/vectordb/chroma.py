"""ChromaDB backend -- zero-config local vector store."""

from __future__ import annotations

from typing import List, Optional

from cex_sdk.knowledge.document import Document
from cex_sdk.vectordb.base import SearchResult, VectorDb


class ChromaDb(VectorDb):
    """ChromaDB -- embedded vector database for development."""

    def __init__(self, collection: str = "cex_knowledge", persist_dir: Optional[str] = None):
        super().__init__(name="chroma", collection=collection)
        self.persist_dir = persist_dir
        self._client = None
        self._collection = None

    def _get_collection(self):
        if self._collection is not None:
            return self._collection
        try:
            import chromadb
        except ImportError:
            raise ImportError("pip install chromadb")

        if self.persist_dir:
            self._client = chromadb.PersistentClient(path=self.persist_dir)
        else:
            self._client = chromadb.Client()
        self._collection = self._client.get_or_create_collection(self.collection)
        return self._collection

    def create(self) -> None:
        self._get_collection()

    def insert(self, documents: List[Document]) -> None:
        col = self._get_collection()
        ids = [d.id or str(i) for i, d in enumerate(documents)]
        texts = [d.content for d in documents]
        metadatas = [d.meta_data for d in documents]
        embeddings = [d.embedding for d in documents if d.embedding] or None
        col.add(ids=ids, documents=texts, metadatas=metadatas, embeddings=embeddings)

    def search(self, query_embedding: List[float], limit: int = 5) -> List[SearchResult]:
        col = self._get_collection()
        results = col.query(query_embeddings=[query_embedding], n_results=limit)

        search_results = []
        if results["documents"]:
            for i, doc_text in enumerate(results["documents"][0]):
                score = 1.0 - (results["distances"][0][i] if results.get("distances") else 0)
                search_results.append(SearchResult(
                    document=Document(
                        content=doc_text,
                        id=results["ids"][0][i] if results.get("ids") else None,
                        meta_data=results["metadatas"][0][i] if results.get("metadatas") else {},
                    ),
                    score=score,
                ))
        return search_results

    def search_text(self, query: str, limit: int = 5) -> List[SearchResult]:
        """Search by text (uses Chroma's built-in embeddings)."""
        col = self._get_collection()
        results = col.query(query_texts=[query], n_results=limit)
        search_results = []
        if results["documents"]:
            for i, doc_text in enumerate(results["documents"][0]):
                search_results.append(SearchResult(
                    document=Document(content=doc_text, id=results["ids"][0][i]),
                    score=1.0,
                ))
        return search_results

    def delete(self, ids: List[str]) -> None:
        col = self._get_collection()
        col.delete(ids=ids)
