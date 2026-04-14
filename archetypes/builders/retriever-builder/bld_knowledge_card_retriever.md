---
id: p09_kc_retriever_domain
kind: knowledge_card
pillar: P09
llm_function: INJECT
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.1
tags: [knowledge_card, retriever, P09, RAG, vector-search, embedding, hybrid-search]
tldr: "Domain knowledge for retriever artifacts: stores, metrics, hybrid search, reranking, metadata filtering."
density_score: 1.0
when_to_use: "Apply when domain knowledge for retriever artifacts: stores, metrics, hybrid search, reranking, metadata fil..."
keywords: [knowledge-card, spec, summary, domain, knowledge]
axioms:
  - "AVOID: No embedding_model specified — dimension mismatch breaks silently at query time"
  - "AVOID: Cosine on unnormalized embeddings — use dot_product or normalize first"
  - "AVOID: top_k too high without reranking — noise drowns signal above k=20"
linked_artifacts:
  primary: null
  related: []
title: Knowledge Card ISO - retriever
---
# Domain Knowledge: retriever

## Executive Summary
Retrievers are the core of RAG — they find relevant documents from local stores using vector
similarity, keyword matching, or hybrid approaches. Quality retrieval determines generation
quality: garbage in, garbage out applies strictly.

## Spec Table

| Property | Value |
|----------|-------|
| Pillar | P04 (Runtime Tools) |
| llm_function | INJECT |
| Layer | runtime |
| Core | true |
| Machine format | yaml |
| Max body bytes | 2048 |

## Vector Store Comparison

| Store | Hosting | Scale | Notable |
|-------|---------|-------|---------|
| Chroma | local / cloud | small-medium | easy local dev, persistent or in-memory |
| Pinecone | managed cloud | large | serverless, namespaces, metadata filtering |
| FAISS | local (CPU/GPU) | medium-large | no persistence, fast exact/ANN search |
| Qdrant | local / cloud | large | payload filtering, sparse+dense hybrid |
| Weaviate | local / cloud | large | GraphQL API, built-in BM25 hybrid |
| Milvus | local / cloud | very large | enterprise scale, GPU acceleration |
| Elasticsearch | local / cloud | large | mature BM25, kNN plugin for dense |

## Similarity Metric Guide

| Metric | Use When | Avoid When |
|--------|----------|------------|
| cosine | embeddings not normalized; OpenAI, sentence-transformers | raw integer vectors |
| dot_product | embeddings natively normalized (Cohere embed-v3, some ST models) | unnormalized vectors |
| euclidean | image embeddings, spatial data | high-dimensional text (curse of dimensionality) |
| manhattan | sparse embeddings | dense semantic embeddings |

## Search Patterns

- **Vector search**: dense embedding -> ANN (HNSW/IVF) -> top_k results
- **Keyword search**: BM25/TF-IDF over inverted index -> exact term ranking
- **Hybrid (RRF)**: vector_rank + keyword_rank -> 1/(k+rank) fusion, k=60 standard
- **Hybrid (weighted)**: alpha * vector_score + (1-alpha) * keyword_score, alpha ~0.7
- **Reranking**: first-pass top_k=50 (cheap retrieval) -> cross-encoder reranks -> return top 5-10
- **Metadata pre-filter**: filter by category/date/source BEFORE similarity search (reduces search space)

## Embedding Model Reference

| Model | Provider | Dimensions | Metric |
|-------|----------|------------|--------|
| text-embedding-3-small | OpenAI | 1536 | cosine |
| text-embedding-3-large | OpenAI | 3072 | cosine |
| embed-english-v3.0 | Cohere | 1024 | dot_product |
| nomic-embed-text | Ollama/local | 768 | cosine |
| all-MiniLM-L6-v2 | sentence-transformers | 384 | cosine |
| bge-large-en-v1.5 | BAAI/local | 1024 | cosine |

## Anti-Patterns

- No embedding_model specified — dimension mismatch breaks silently at query time
- Cosine on unnormalized embeddings — use dot_product or normalize first
- top_k too high without reranking — noise drowns signal above k=20
- No metadata filters on large stores — full-collection scan degrades latency
- Confusing retriever with search_tool — retriever searches LOCAL; search_tool queries WEB
- Confusing retriever with document_loader — loader ingests; retriever queries what was ingested
- top_k=1 for generation — too brittle; use k=3-5 minimum for robustness

## Reranker Reference

| Model | Type | Latency | Quality |
|-------|------|---------|---------|
| rerank-english-v3.0 | Cohere API | ~200ms | high |
| ms-marco-MiniLM-L-6-v2 | cross-encoder local | ~50ms | medium |
| colbert-ir/colbertv2.0 | ColBERT local | ~100ms | high |
| bge-reranker-large | BAAI local | ~150ms | high |

## References
LangChain BaseRetriever, LlamaIndex QueryEngine, Haystack, ColBERT, BEIR benchmark.
