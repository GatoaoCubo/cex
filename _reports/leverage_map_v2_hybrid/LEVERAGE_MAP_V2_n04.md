The RAG tools are mapped as follows:

* `cex_preflight.py` uses Haiku semantic rerank for Phase 2 (CLOUD, cheap)
* `cex_reranker.py` uses BM25 with title match for lexical reranking
* Other tools mention "reranker_config" or use terms like "retrieval", "ranking", and "BM25"

Next, I will analyze the reranker quality.