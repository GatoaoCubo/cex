---
id: n00_vector_store_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "Vector Store -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, vector_store, p01, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Vector Store defines the vector database backend configuration for similarity search in RAG pipelines. It specifies the database type, connection parameters, index configuration, and persistence strategy. The vector_store is the runtime storage layer that receives embeddings produced by embedding_config and serves queries from retriever_config.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `vector_store` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Store name and backend |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| backend | enum | yes | chroma\|qdrant\|weaviate\|pinecone\|pgvector\|faiss |
| persist_path | string | no | Local persistence directory (for embedded backends) |
| collection_name | string | yes | Collection or index name |
| dimensions | int | yes | Vector dimensionality (must match embedder) |
| index_type | enum | yes | HNSW\|IVF\|flat -- ANN algorithm |
| distance_metric | enum | yes | cosine\|dot_product\|euclidean |

## When to use
- When deploying a new RAG pipeline requiring vector storage
- When migrating from one vector DB backend to another
- When configuring multi-tenant vector collections

## Builder
`archetypes/builders/vector_store-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind vector_store --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (N04 or N05)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- engineers deploying retrieval infrastructure
- `{{DOMAIN_CONTEXT}}` -- scale, latency, and persistence requirements

## Example (minimal)
```yaml
---
id: vector_store_cex_chroma
kind: vector_store
pillar: P01
nucleus: n04
title: "CEX Chroma Local Vector Store"
version: 1.0
quality: null
---
backend: chroma
persist_path: ".cex/vector_db/chroma"
collection_name: cex_knowledge
dimensions: 768
index_type: HNSW
distance_metric: cosine
```

## Related kinds
- `embedding_config` (P01) -- produces vectors stored here
- `retriever_config` (P01) -- queries this store for similarity search
- `embedder_provider` (P01) -- the model generating the stored vectors
