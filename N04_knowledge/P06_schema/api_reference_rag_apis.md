---
id: p06_ar_rag_apis
kind: api_reference
pillar: P06
nucleus: n04
title: "API Reference -- RAG and Vector Store APIs"
version: "1.0.0"
quality: 9.1
tags: [api_reference, rag, vector_store, supabase, pinecone, chroma, pgvector, n04, P06]
domain: knowledge retrieval APIs
status: active
created: "2026-04-17"
updated: "2026-04-17"
author: n04_knowledge
tldr: "Canonical API reference for RAG/vector store APIs used by N04: pgvector (Supabase), Pinecone, ChromaDB, and the CEX internal retrieval API. Covers embedding, upsert, query, and delete operations."
density_score: null
---

# API Reference: RAG and Vector Store APIs

## Overview

N04 interacts with three external vector store APIs and one internal CEX retrieval API.
This document is the authoritative reference for all N04 retrieval integrations.

---

## 1. pgvector (via Supabase)

Primary vector store for CEX production deployments.

### Base URL
```
https://{project-ref}.supabase.co/rest/v1/rpc/
```

### Authentication
```
Authorization: Bearer {SUPABASE_KEY}
apikey: {SUPABASE_ANON_KEY}
```

### Endpoint: `match_documents`

Semantic similarity search using cosine distance.

**Request**
```http
POST /rpc/match_documents
Content-Type: application/json

{
  "query_embedding": [float, ...],  // 1536-dim for text-embedding-3-small
  "match_threshold": 0.65,          // minimum similarity score
  "match_count": 10,                // top-k results
  "filter_kind": "knowledge_card",  // optional metadata filter
  "filter_pillar": "P01"            // optional metadata filter
}
```

**Response**
```json
[
  {
    "id": "uuid",
    "content": "string",
    "metadata": { "kind": "knowledge_card", "pillar": "P01", "path": "..." },
    "similarity": 0.87
  }
]
```

**Errors**
| Code | Meaning |
|------|---------|
| 400 | Invalid embedding dimension |
| 401 | Invalid or missing API key |
| 429 | Rate limit exceeded (500 req/min free tier) |

### Endpoint: `upsert_document`

Insert or update a document with its embedding.

**Request**
```http
POST /rpc/upsert_document
{
  "doc_id": "string",
  "content": "string",
  "embedding": [float, ...],
  "metadata": { "kind": "...", "pillar": "...", "path": "..." }
}
```

---

## 2. Pinecone

Fallback vector store for high-throughput scenarios.

### Base URL
```
https://{index-name}-{project-id}.svc.{environment}.pinecone.io
```

### Authentication
```
Api-Key: {PINECONE_API_KEY}
```

### Endpoint: `query`

**Request**
```http
POST /query
{
  "vector": [float, ...],
  "topK": 10,
  "includeMetadata": true,
  "filter": { "kind": { "$eq": "knowledge_card" } },
  "namespace": "cex_artifacts"
}
```

**Response**
```json
{
  "matches": [
    {
      "id": "string",
      "score": 0.84,
      "metadata": { "kind": "...", "path": "..." }
    }
  ]
}
```

### Endpoint: `upsert`

**Request**
```http
POST /vectors/upsert
{
  "vectors": [
    { "id": "string", "values": [float, ...], "metadata": { ... } }
  ],
  "namespace": "cex_artifacts"
}
```

**Rate Limits**
| Operation | Free tier | Starter |
|-----------|-----------|---------|
| Query | 100 req/s | 1000 req/s |
| Upsert | 100 vec/s | 1000 vec/s |
| Max dimensions | 1536 | 20000 |

---

## 3. ChromaDB (local)

Development and local-only deployments.

### Base URL
```
http://localhost:8000
```

### Endpoint: `query`

**Request**
```http
POST /api/v1/collections/{collection_name}/query
{
  "query_embeddings": [[float, ...]],
  "n_results": 10,
  "where": { "kind": "knowledge_card" },
  "include": ["documents", "metadatas", "distances"]
}
```

**Response**
```json
{
  "documents": [["text ..."]],
  "metadatas": [[{"kind": "...", "path": "..."}]],
  "distances": [[0.18]]
}
```

*Note: ChromaDB distances are L2 (lower = more similar). Convert to similarity: `1 - (dist / 2)`*

---

## 4. CEX Internal Retrieval API (`cex_retriever.py`)

### Python Interface

```python
from cex_sdk.retriever import CexRetriever

retriever = CexRetriever(
    corpus="cex_artifacts",        # corpus selection
    mode="hybrid",                 # dense | sparse | hybrid | graph
    top_k=10,
    score_threshold=0.65,
    rerank=True
)

results = retriever.query(
    query_text="8F pipeline reasoning",
    filters={"kind": "knowledge_card", "pillar": "P01"},
    output_format="passages"       # passages | summaries | full_docs | citations_only
)
```

### CLI Interface

```bash
python _tools/cex_retriever.py \
  --query "RAG architecture" \
  --corpus cex_artifacts \
  --mode hybrid \
  --top-k 10 \
  --format passages
```

### Response Format

```python
[
    {
        "content": "string",       # retrieved passage text
        "score": 0.84,             # similarity score
        "source": "path/to/file.md",
        "metadata": {
            "kind": "knowledge_card",
            "pillar": "P01",
            "nucleus": "n04"
        }
    }
]
```

---

## Embedding API Reference

N04 uses OpenAI-compatible embedding endpoints.

### text-embedding-3-small (default)
- **Dimensions**: 1536
- **Max tokens**: 8191
- **Best for**: semantic search, hybrid retrieval

### text-embedding-3-large (high-precision)
- **Dimensions**: 3072
- **Max tokens**: 8191
- **Best for**: complex domain reasoning, long documents

### Request (OpenAI-compatible)
```http
POST https://api.openai.com/v1/embeddings
{
  "input": "text to embed",
  "model": "text-embedding-3-small",
  "encoding_format": "float"
}
```

---

## Error Handling Reference

| Error | Cause | N04 Response |
|-------|-------|-------------|
| `EmbeddingDimensionMismatch` | Wrong embedding model | Use model specified in index config |
| `RateLimitExceeded` | Too many requests | Exponential backoff: 1s, 2s, 4s, max 3 retries |
| `CorpusNotFound` | Unknown corpus name | Fall back to `cex_artifacts` |
| `VectorStoreUnavailable` | DB offline | Fall back to BM25 sparse retrieval |
| `NoResultsAboveThreshold` | Score threshold too high | Reduce threshold by 0.10, retry once |

---

## Integration Map

| Consumer | API Used | Operation |
|---------|---------|-----------|
| `search_tool_n04.md` | CEX Internal + pgvector | query |
| `retriever_n04.md` | pgvector primary, Pinecone fallback | query + rerank |
| `document_loader_n04.md` | pgvector + ChromaDB | upsert |
| `embedding_config_knowledge.md` | OpenAI Embeddings | embed |
