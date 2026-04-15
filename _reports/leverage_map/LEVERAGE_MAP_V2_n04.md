The tool added is `cex_reranker.py` in the `_tools` directory, which implements BM25 reranking over candidate docs with title boost.

The BM25 math appears to be correct, as it matches the standard BM25 formula:

`bm25_score(query_tokens, doc_tokens, avg_len, doc_freqs, n_docs, k1=1.5, b=0.75)`

The tool fits with `cex_retriever.py`, which is used for semantic search via TF-IDF similarity.

### Verification

* Tool added: Yes
* BM25 math correct: Yes
* Fits with cex_retriever.py: Yes

### New Wired Tools (since V1)

* `_tools/cex_reranker.py`

### Still Missing

* Vector DB
* Hybrid search
* Knowledge graph
* Reranker tuning