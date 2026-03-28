---
kind: architecture
id: bld_architecture_retriever
pillar: P10
llm_function: INJECT
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: EDISON
quality: null
tags: [architecture, retriever, P10, RAG, vector-search, component-map]
---
# Architecture: retriever

## Component Inventory

| Component | Role | Examples |
|-----------|------|---------|
| query_encoder | Converts query text to embedding vector | OpenAI Embeddings, Cohere Embed, nomic-embed-text |
| vector_store | Persists and indexes document vectors + metadata | Chroma, Pinecone, FAISS, Qdrant, Weaviate, Milvus |
| similarity_engine | ANN search over stored vectors | HNSW, IVF_FLAT, ScaNN, DiskANN |
| keyword_index | BM25/TF-IDF inverted index (hybrid only) | Elasticsearch, Qdrant sparse, Weaviate BM25 |
| fusion_layer | Combines vector + keyword scores (hybrid only) | RRF (k=60), weighted alpha blend |
| metadata_filter | Pre-filters document scope before similarity | Where clauses, payload filters |
| reranker | Second-pass precision scoring of top_k results | Cohere rerank, ColBERT, cross-encoder |
| result_formatter | Packages chunks + metadata for downstream LLM | Document objects, score + source metadata |

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

## P04 Position in RAG Pipeline

```
[document_loader] --> [embedding store] --> [retriever] --> [LLM generator]
   (ingestion)          (persistence)        (query)         (generation)
```
Retriever is stateless at query time — it reads, never writes to the store.
