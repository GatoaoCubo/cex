---
kind: knowledge_card
id: bld_knowledge_card_retriever_config
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for retriever_config production
sources: LangChain retriever module, LlamaIndex query engines, vector DB documentation, hybrid search research (BM25+dense), reranking (Cohere, cross-encoder)
---

# Domain Knowledge: retriever_config
## Executive Summary
Retrieval parameters — how to search and rank chunks from a vector/hybrid store. Produced as P01 artifacts with concrete parameters and rationale.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P01 |
| llm_function | CONSTRAIN |
| Max bytes | 2048 |
| Density min | 0.8 |
| Machine format | yaml |
## Patterns
| Pattern | Description | When to use |
|---------|-------------|-------------|
| Dense-only | Pure vector similarity search (cosine/dot) | Homogeneous corpus, semantic queries |
| Sparse-only | BM25/TF-IDF keyword search | Exact-match needs, technical terminology |
| Hybrid | Combine dense + sparse with weighted fusion | General-purpose, best recall+precision |
| Reranked | Retrieve top_k*3 then rerank with cross-encoder | High-precision needs, acceptable latency |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| top_k too low | Misses relevant chunks, especially with imprecise queries |
| No score threshold | Returns irrelevant results when no good match exists |
| Dense-only for keyword queries | Semantic search fails on exact terms, codes, IDs |
| No reranker on large top_k | Returns many results but wrong order |
## Application
1. Identify the use case and constraints
2. Select apownte pattern from the table above
3. Define concrete parameter values with rationale
4. Validate against SCHEMA.md required fields
5. Check body size <= 2048 bytes
6. Verify id matches `^p01_retr_[a-z][a-z0-9_]+$`
## References
- LangChain BaseRetriever, LlamaIndex BaseRetriever, Haystack Retriever, ChromaDB, Pinecone, Weaviate, FAISS
- LangChain retriever module, LlamaIndex query engines, vector DB documentation, hybrid search research (BM25+dense), reranking (Cohere, cross-encoder)
