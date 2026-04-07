---
kind: examples
id: bld_examples_vector_store
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of vector_store artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: vector-store-builder
## Golden Example
INPUT: "Configure Chroma for local RAG development with 1536-dim OpenAI embeddings"
OUTPUT:
```yaml
id: p01_vdb_chroma
kind: vector_store
pillar: P01
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: "builder_agent"
backend: "chroma"
connection:
  host: "localhost"
  port: 8000
  api_key_env: null
  tls: false
  database: null
collection: "cex_knowledge"
dimensions: 1536
distance_metric: cosine
index_type: hnsw
hnsw:
  M: 16
  ef_construction: 200
  ef_search: 100
max_vectors: null
metadata_filtering: true
metadata_schema:
  pillar: string
  kind: string
  created: date
  domain: string
persistence: auto
namespace_strategy: "collection_per_domain"
cloud_region: null
pricing: null
domain: vector_storage
quality: null
tags: [vector-store, chroma, hnsw, local]
tldr: "Chroma — local, HNSW, 1536d (OpenAI), cosine, auto-persist, metadata filtering for RAG dev"
keywords: [chroma, vectordb, hnsw, local, rag]
linked_artifacts:
  primary: null
  related: [p01_emb_openai_text_embedding_3_small]
data_source: "https://docs.trychroma.com/"
## Boundary
vector_store IS: storage and indexing config for Chroma (HNSW index, 1536 dimensions, cosine).
vector_store IS NOT: embedder_provider, model_provider, retriever, chunker.
## Backend Matrix
| Parameter | Value | Source |
|-----------|-------|--------|
| Backend | chroma | https://docs.trychroma.com/ |
| Version | 0.5.x | https://github.com/chroma-core/chroma/releases |
| Host | localhost:8000 | https://docs.trychroma.com/docs/run-chroma/client-server |
| Auth | none (local) | https://docs.trychroma.com/docs/run-chroma/client-server |
| Dimensions | 1536 | Upstream: p01_emb_openai_text_embedding_3_small |
| Distance Metric | cosine (L2-normalized embeddings) | Mathematical property |
| Index Type | HNSW (default) | https://docs.trychroma.com/ |
| Max Vectors | unlimited (disk-bound) | https://docs.trychroma.com/ |
| Persistence | auto (persist_directory) | https://docs.trychroma.com/docs/run-chroma/persistent-client |
| Metadata Filtering | where, where_document operators | https://docs.trychroma.com/docs/guides/querying |
## Index Configuration
| Parameter | Value | Effect |
|-----------|-------|--------|
| M | 16 | Connections per node. Higher = better recall, more RAM. 16 optimal for <1M vectors |
| ef_construction | 200 | Build-time search width. Higher = better index quality, slower initial build |
| ef_search | 100 | Query-time search width. Higher = better recall, slower queries. Tune per latency SLA |
Scale guidance:
- < 10K vectors: flat index sufficient, HNSW overhead unnecessary
- 10K-1M vectors: HNSW with M=16, ef_construction=200 (default)
- > 1M vectors: consider Pinecone/Qdrant for distributed scaling
## Namespace Strategy
- One collection per knowledge domain: `cex_knowledge`, `cex_marketing`, `cex_commercial`
- Metadata field `pillar` enables cross-domain queries with filtering
- Never mix embedding models across collections — dimension mismatch breaks everything
## Lifecycle Operations
1. **Create**: `chroma_client.create_collection("cex_knowledge", metadata={"hnsw:space": "cosine"})`
2. **Reindex**: Delete collection + recreate + re-embed all documents (triggered by embedder model change)
3. **Backup**: Copy `persist_directory` contents (SQLite + parquet files)
4. **Restore**: Replace `persist_directory` and restart Chroma server
## Anti-Patterns
1. Mixing 1536-dim and 768-dim vectors in one collection — Chroma silently accepts, similarity becomes meaningless
2. Not setting persist_directory — ephemeral mode loses all data on restart
3. Using HNSW for < 1K vectors — flat brute-force is faster and exact at small scale
4. Querying without metadata filter on multi-domain collections — returns cross-domain noise
## References
- docs: https://docs.trychroma.com/
- github: https://github.com/chroma-core/chroma
- querying: https://docs.trychroma.com/docs/guides/querying
```
WHY THIS IS GOLDEN:
- Every Backend Matrix row has Source URL (never `-`)
- Dimensions match upstream embedder_provider explicitly
- Distance metric justified by normalization property
- HNSW parameters with scale guidance
- Lifecycle: create, reindex, backup, restore all documented
- quality: null
- Anti-patterns are backend-specific with concrete consequences
## Anti-Example
INPUT: "Setup vector database"
BAD OUTPUT:
```yaml
id: my_vectordb
kind: vectordb
backend: ChromaDB
dimensions: "auto"
distance: cosine
quality: 9.0
ChromaDB is a powerful vector database that makes it easy to
build AI applications. Simply install and start using it.
```
FAILURES:
1. id: no `p01_vdb_` prefix — H02 FAIL
2. kind: "vectordb" not "vector_store" — H04 FAIL
3. backend: "ChromaDB" not lowercase "chroma" — H07 FAIL
4. dimensions: string "auto" not integer — H08 FAIL
5. distance: "distance" not "distance_metric" — schema violation
6. quality: self-assigned 9.0 — H05 FAIL
7. No HNSW parameters — S02 FAIL
8. No persistence config — S03 FAIL
9. Body: marketing prose, no Backend Matrix — density FAIL
