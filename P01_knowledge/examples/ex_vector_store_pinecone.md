---
id: p01_vdb_pinecone
kind: vector_store
pillar: P01
title: "Example — Pinecone Vector Database Backend"
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: builder_agent
backend: pinecone
collection: cex_knowledge
dimensions: 1536
distance_metric: cosine
index_type: hnsw
domain: vector_store
quality: 9.1
tags: [vector-store, pinecone, vector, rag, cloud]
tldr: "Pinecone serverless backend — 1536 dims, cosine similarity, 3 namespaces (kc/memory/artifact), auto-scales."
when_to_use: "Production vector storage when managed serverless is preferred over self-hosted"
keywords: [pinecone, vectordb, serverless, cosine, hnsw, rag]
density_score: null
---

# VectorDB Backend: Pinecone Serverless

## Configuration
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| backend | pinecone | Fully managed, serverless, auto-scaling |
| cloud | aws | us-east-1 region for low latency |
| index_name | cex-knowledge | One index per environment |
| dimensions | 1536 | Matches text-embedding-3-small |
| metric | cosine | Standard for normalized embeddings |
| spec | serverless | No capacity planning needed |

## Namespace Strategy
| Namespace | Content | Est. Vectors |
|-----------|---------|-------------|
| kc | Knowledge cards (114 kinds) | ~2,200 |
| memory | Builder memories, observations | ~500 |
| artifact | Built artifacts from all pillars | ~5,000 |

## Performance
| Metric | Value |
|--------|-------|
| Query latency (p50) | ~20ms |
| Query latency (p99) | ~80ms |
| Upsert throughput | 100 vectors/request |
| Max metadata per vector | 40 KB |
| Max vectors per namespace | 1B (serverless) |

## Query Example
```python
from pinecone import Pinecone
pc = Pinecone(api_key=os.environ["PINECONE_API_KEY"])
index = pc.Index("cex-knowledge")

results = index.query(
    namespace="kc",
    vector=query_embedding,
    top_k=5,
    include_metadata=True,
    filter={"pillar": {"$eq": "P01"}, "kind": {"$eq": "knowledge_card"}}
)
```

## Comparison to Alternatives
| Backend | Managed | Cost (1M vectors) | Latency | Local Dev |
|---------|---------|-------------------|---------|-----------|
| **Pinecone** | **yes** | **$0.33/mo** | **~20ms** | **no** |
| pgvector | self | $0 (infra cost) | ~5ms | yes |
| Chroma | self | $0 | ~10ms | yes |
| Qdrant | both | $0-25/mo | ~15ms | yes |
| FAISS | local | $0 | ~1ms | yes |

## Migration Path
```
Development: FAISS (local, zero deps)
    ↓
Staging: Chroma (local server, persistent)
    ↓
Production: Pinecone (managed, auto-scale)
```

## Boundary
vector_store IS: storage and query config for embedding vectors with indexing and similarity search.
vector_store IS NOT: an embedder provider (vector generation), a retriever (query pipeline), or a chunk strategy.
