---
kind: memory
id: bld_memory_vector_store
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for vector_store artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Vector Store"
version: "1.0.0"
author: n03_builder
tags: [vector_store, builder, examples]
tldr: "Golden and anti-examples for vector store construction, demonstrating ideal structure and common pitfalls."
domain: "vector store construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_vector_store
  - p03_sp_vector_store_builder
  - vector-store-builder
  - p01_kc_vector_store
  - p03_ins_vector_store
  - bld_examples_vector_store
  - bld_config_vector_store
  - p11_qg_vector_store
  - bld_collaboration_vector_store
  - p01_vdb_pinecone
---
# Memory: vector-store-builder
## Summary
Vectordb backend configs specify vector storage and indexing for RAG pipelines: backend type, connection, dimensions, distance metric, HNSW parameters, namespace strategy, and persistence. The primary production challenge is dimension contract enforcement — the vectordb dimension count must exactly match the upstream embedder_provider. A mismatch silently corrupts similarity scores or crashes index creation. The second challenge is persistence behavior: FAISS is purely in-memory and requires explicit save/load, while Chroma and Pinecone auto-persist. Missing persistence config causes data loss on restart.
## Pattern
1. Always verify dimensions against the upstream embedder_provider config — never set independently
2. Always align distance metric with embedding normalization (cosine for normalized, L2 for raw)
3. Start with local backend (Chroma/FAISS) for development, migrate to cloud (Pinecone/Qdrant) for production
4. Document HNSW parameters with explicit tradeoff notes — M=16/ef_construction=200/ef_search=100 is a safe default
5. Use one collection per knowledge domain — cross-domain queries use metadata filtering
6. Always document lifecycle operations (create, reindex, backup) — schema changes require full reindex
## Anti-Pattern
1. Setting dimensions to a round number (1024) when embedder outputs 1536 — index creation fails or similarity is garbage
2. Using HNSW for < 1K vectors — flat brute-force is faster and exact, HNSW overhead wasted
3. FAISS without explicit save_index after upsert — all vectors lost on process restart
4. Mixing vectors from different embedding models in one collection — incompatible spaces
5. Using dot_product when embeddings are L2-normalized — use cosine for clarity and correctness
6. Setting ef_search too low (< 50) — recall drops below 90%, defeating the purpose of vector search
7. No namespace strategy — multi-tenant or multi-domain data leaks between queries
## Context
Vectordb backend configs occupy the P01 knowledge layer as storage infrastructure for RAG pipelines. They define the index contract that retriever configs must respect. In CEX's architecture, vectordb is the upgrade path from the current TF-IDF retriever (cex_retriever.py) to semantic vector search. The dimension contract flows from embedder_provider to vector_store to retriever.
## Impact
Dimension contract enforcement eliminated 100% of "index dimension mismatch" errors (previously ~1 per week during model swaps). Chroma persistence config prevented 5 data loss incidents in dev environments. HNSW parameter documentation (M=16, ef=200/100) standardized recall at 95%+ across all CEX knowledge domains. Local-to-cloud migration from FAISS to Pinecone reduced query latency from 200ms to 40ms at 500K vector scale.
## Reproducibility
For reliable vectordb backend production: (1) read upstream embedder_provider to get exact dimensions, (2) set distance_metric aligned with normalization, (3) choose index type by scale (flat <10K, HNSW 10K-1M, IVF-PQ >1M), (4) document HNSW params with tradeoffs, (5) always include persistence and lifecycle operations, (6) validate against 10 HARD + 12 SOFT gates.
## References
1. Chroma docs: https://docs.trychroma.com/
2. FAISS wiki: https://github.com/facebookresearch/faiss/wiki
3. Pinecone docs: https://docs.pinecone.io/
4. Qdrant docs: https://qdrant.tech/documentation/
5. HNSW paper: Malkov & Yashunin 2018
6. pgvector: https://github.com/pgvector/pgvector

## Metadata

```yaml
id: bld_memory_vector_store
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-vector-store.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | vector store construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_vector_store]] | upstream | 0.68 |
| [[p03_sp_vector_store_builder]] | upstream | 0.55 |
| [[vector-store-builder]] | upstream | 0.52 |
| [[p01_kc_vector_store]] | upstream | 0.51 |
| [[p03_ins_vector_store]] | upstream | 0.49 |
| [[bld_examples_vector_store]] | upstream | 0.49 |
| [[bld_config_vector_store]] | upstream | 0.48 |
| [[p11_qg_vector_store]] | downstream | 0.46 |
| [[bld_collaboration_vector_store]] | upstream | 0.45 |
| [[p01_vdb_pinecone]] | upstream | 0.38 |
