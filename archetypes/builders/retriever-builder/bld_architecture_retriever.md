---
kind: architecture
id: bld_architecture_retriever
pillar: P10
llm_function: CONSTRAIN
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.1
tags: [architecture, retriever, P10, RAG, vector-search, component-map]
density_score: 1.0
title: Architecture ISO - retriever
---
# Architecture: retriever

## Component Inventory

| Component | Role | Examples |
|-----------|------|---------|
| query_encoder | Converts query to embedding vector | OpenAI, Cohere, nomic-embed |
| vector_store | Persists document vectors + metadata | Chroma, Pinecone, FAISS, Qdrant |
| similarity_engine | ANN search over vectors | HNSW, IVF_FLAT, ScaNN |
| keyword_index | BM25/TF-IDF (hybrid only) | Elasticsearch, Qdrant sparse |
| fusion_layer | Combines vector+keyword scores | RRF (k=60), weighted blend |
| metadata_filter | Pre-filters before similarity | Where clauses, payload filters |
| reranker | Second-pass precision scoring | Cohere rerank, cross-encoder |
| result_formatter | Packages chunks for LLM | Document objects, score+source |

## Dependency Graph (ASCII)

```
user_query
    |
    v
[query_encoder]  (same model as ingestion-time encoder)
    |
    v
[metadata_filter]  (pre-filter, reduces search space)
    |
    +---> [similarity_engine] (vector ANN search)
    |             |
    +---> [keyword_index]    (BM25, hybrid only)
                  |
                  v
           [fusion_layer]   (RRF or weighted, hybrid only)
                  |
                  v
           [reranker]       (optional, fires on top_k > 20)
                  |
                  v
         [result_formatter] --> chunks + metadata -> LLM
```

## Dependency Table

| From | To | Requirement |
|------|----|-------------|
| retriever | document_loader | Chunks + embeddings MUST exist in store before retrieval |
| retriever | embedding_model | SAME model used at ingestion and query time (dimension match) |
| retriever | vector_store | Store must be running and accessible |
| LLM / agent | retriever | Retriever output feeds generation context window |

## Boundary Table

| IS (retriever) | IS NOT (delegate to) |
|----------------|---------------------|
| Local vector store search | Web search via external API (search_tool) |
| Query encoding for similarity | File reading, chunking, embedding storage (document_loader) |
| ANN / BM25 / hybrid over local index | SQL / GraphQL queries (db_connector) |
| Metadata filtering on stored documents | REST API calls to external services (api_client) |
| Reranking retrieved local chunks | Generating answers from retrieved context (LLM) |

## Layer Map

```
INPUT     : raw user query (string)
ENCODING  : query_encoder -> dense vector (+ sparse for hybrid)
FILTER    : metadata_filter -> scoped document subset
SEARCH    : similarity_engine + keyword_index -> candidate set (top_k)
FUSION    : fusion_layer -> merged ranked list (hybrid only)
RANKING   : reranker -> precision-ranked top results (optional)
OUTPUT    : list of (chunk_text, metadata, score) tuples
```

## RAG Position
`[document_loader] → [embedding store] → [retriever] → [LLM generator]`
Stateless at query time — reads, never writes.
## Confusion Zones
| Scenario | Seems Like | Actually Is | Rule |
|---|---|---|---|
| Search web for info | retriever | search_tool | search_tool=external API; retriever=local index |
| Load PDF into store | retriever | document_loader | loader=ingest; retriever=query existing store |
| Query SQL database | retriever | db_connector | db_connector=structured SQL; retriever=vector/keyword |
## Decision Tree
- Search local vector/keyword index? → retriever
- Search external web API? → search_tool
- Ingest files into chunks? → document_loader
- Query structured database? → db_connector
## Neighbor Comparison
| Dimension | retriever | search_tool | Difference |
|---|---|---|---|
| Source | Local index | External API | retriever is self-hosted |
| Latency | <100ms | 200-2000ms | Local is faster |
| Control | Full (index, model) | Provider-dependent | retriever is costmizable |
