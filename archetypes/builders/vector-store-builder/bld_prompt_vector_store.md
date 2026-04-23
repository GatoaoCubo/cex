---
id: p03_ins_vector_store
kind: instruction
pillar: P03
version: 1.0.0
created: 2026-04-06
updated: 2026-04-06
author: instruction-builder
title: Vectordb Backend Builder Execution Protocol
target: vector-store-builder agent
phases_count: 4
prerequisites:
  - Vector database backend and deployment target are identified
  - Backend documentation is accessible (API reference, index types, limits)
  - Upstream embedder_provider dimensions are known
validation_method: checklist
domain: vector_store
quality: 9.1
tags: [instruction, vector-store, P01, vector-database, index, hnsw]
idempotent: true
atomic: false
rollback: "Discard generated artifact; no vector index is created or modified"
dependencies: []
logging: true
tldr: Configure a vector database backend's connection, index type, HNSW parameters, and namespace strategy from official sources into a complete vector_store artifact.
density_score: 0.91
llm_function: REASON
related:
  - p11_qg_vector_store
  - p03_sp_vector_store_builder
  - bld_output_template_vector_store
  - bld_knowledge_card_vector_store
  - bld_schema_vector_store
  - p03_ins_embedder_provider
  - bld_architecture_vector_store
  - bld_memory_vector_store
  - bld_config_vector_store
  - p01_kc_vector_store
---
## Context
The vector-store-builder produces `vector_store` artifacts (P01) — vector database storage configurations for RAG pipelines. Configs specify the backend type, connection details, collection naming, dimension contract, distance metric, index type and parameters, metadata filtering, and lifecycle operations. A vector_store is a storage config, not an embedder_provider (embedding model), not a model_provider (LLM routing), and not a retriever (query pipeline).
**Inputs:**
- `$backend (required) - string - "One of: pinecone, pgvector, chroma, faiss, qdrant, weaviate, milvus, other"`
- `$dimensions (required) - integer - "Must match upstream embedder_provider dimensions exactly"`
- `$scale (optional) - string - "Expected vector count: small (<100K), medium (100K-10M), large (>10M)"`
- `$deployment (optional) - string - "local, cloud, hybrid — affects connection and persistence config"`
**Output:** A single `vector_store` artifact with 22+ frontmatter fields and 6 body sections: Boundary, Backend Matrix, Index Configuration, Namespace Strategy, Lifecycle Operations, Anti-Patterns. Body <= 4096 bytes.
## Phases
### Phase 1: Research
**Action:** Gather all backend specifications from official documentation.
1. Identify the backend: name, version, deployment model (local, cloud, self-hosted).
2. Locate official documentation:
   - Backend API reference (collections, indexes, queries)
   - Index types supported (HNSW, IVF, flat, costm)
   - Distance metrics supported (cosine, L2, dot product, inner product)
   - Limits (max dimensions, max vectors per collection, max metadata size)
   - Pricing (if cloud-managed: per-vector, per-query, storage costs)
3. Extract all schema fields:
   - `connection`: host, port, api_key_env (or local path)
   - `collection`: naming convention for the collection/index
   - `dimensions`: integer matching upstream embedder
   - `distance_metric`: aligned with embedding normalization
   - `index_type`: hnsw, ivf, flat, or backend-specific
   - `hnsw`: M, ef_construction, ef_search (if applicable)
   - `metadata_filtering`: boolean, supported filter operations
   - `persistence`: auto, manual, or external (FAISS = manual)
4. Rule: if a parameter is unavailable, set to `null` — never guess.
5. Verify dimensions match the configured embedder_provider.
**Verification:** Dimensions match upstream exactly. Index type is supported by the backend. Distance metric aligns with normalization.
### Phase 2: Compose
**Action:** Write all frontmatter fields and body sections within the 4096-byte body limit.
1. Read SCHEMA — source of truth for all fields.
2. Read OUTPUT_TEMPLATE — fill every `{{var}}`.
3. Fill frontmatter: all required fields (`quality: null` mandatory).
4. Write `## Boundary` section — what a vector_store IS and IS NOT.
5. Write `## Backend Matrix` table:
   | Parameter | Value | Source |
   |-----------|-------|--------|
   Rows: backend, version, host, port, auth, dimensions, distance_metric, index_type, max_vectors, persistence.
6. Write `## Index Configuration` — HNSW parameters with recall/speed tradeoff table:
   | Parameter | Value | Effect |
   |-----------|-------|--------|
   Rows: M, ef_construction, ef_search, segment_size (if applicable).
7. Write `## Namespace Strategy` — collection/namespace naming and domain isolation.
8. Write `## Lifecycle Operations` — create, reindex, backup, restore procedures.
9. Write `## Anti-Patterns` — >= 4 common mistakes with this backend.
10. Write `## References` — >= 1 official URL.
**Verification:** Every Backend Matrix row has Source URL. Dimensions are integers. HNSW params documented. Body <= 4096 bytes.
### Phase 3: Validate
**Action:** Run all 10 HARD gates. Fix any failure before output.
| Gate | Check |
|------|-------|
| H01 | YAML frontmatter parses without error |
| H02 | `id` matches `^p01_vdb_[a-z][a-z0-9_]+$` |
| H03 | `id` equals filename stem exactly |
| H04 | `kind` == literal string `"vector_store"` |
| H05 | `quality` == `null` |
| H06 | Required fields present: `id`, `kind`, `pillar`, `backend`, `dimensions`, `distance_metric`, `index_type`, `tags`, `tldr` |
| H07 | `backend` matches a known enum value |
| H08 | `dimensions` is a positive integer |
| H09 | `distance_metric` is one of: cosine, l2, dot_product, inner_product |
| H10 | Body <= 4096 bytes |
Score all SOFT gates. If soft score < 8.0, revise in the same pass.
### Phase 4: Deliver
**Action:** Save, compile, commit, signal.
1. Save artifact to `P01_knowledge/examples/p01_vdb_{backend}.yaml`
2. Compile: `python _tools/cex_compile.py {path}`
3. Git commit with descriptive message
4. Signal: `write_signal('n03', 'complete', {score})`


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_vector_store]] | downstream | 0.53 |
| [[p03_sp_vector_store_builder]] | related | 0.50 |
| [[bld_output_template_vector_store]] | downstream | 0.49 |
| [[bld_knowledge_card_vector_store]] | upstream | 0.48 |
| [[bld_schema_vector_store]] | downstream | 0.47 |
| [[p03_ins_embedder_provider]] | sibling | 0.46 |
| [[bld_architecture_vector_store]] | downstream | 0.44 |
| [[bld_memory_vector_store]] | downstream | 0.43 |
| [[bld_config_vector_store]] | downstream | 0.42 |
| [[p01_kc_vector_store]] | upstream | 0.40 |
