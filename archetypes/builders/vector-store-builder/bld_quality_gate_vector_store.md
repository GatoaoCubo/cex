---
id: p11_qg_vector_store
kind: quality_gate
pillar: P11
title: "Gate: Vectordb Backend"
version: "1.0.0"
created: "2026-04-06"
updated: "2026-04-06"
author: builder_agent
domain: vector_store
quality: 9.0
tags: [quality-gate, vector-store, vector-database, P01, hnsw]
tldr: "Quality gate for vector_store artifacts: enforces dimensions, distance metric, index type, and persistence fields."
density_score: 0.87
llm_function: GOVERN
---
# Gate: Vectordb Backend
## Definition
A `vector_store` is a storage and indexing configuration for vector embeddings: backend type, dimensions, distance metric, index type, HNSW parameters, and persistence. Infrastructure artifact only — not a tutorial. Gates ensure dimension contract with upstream embedder, distance metric alignment with normalization, and complete index configuration.
## HARD Gates
All HARD gates must pass. Any single failure sets score to 0 and blocks publish.
| ID  | Check | Failure consequence |
|-----|-------|---------------------|
| H01 | YAML frontmatter parses without error | Artifact unparseable by tooling |
| H02 | `id` matches `^p01_vdb_[a-z][a-z0-9_]+$` | Namespace violation — not discoverable |
| H03 | `id` equals filename stem exactly | Brain search failure — id/file mismatch |
| H04 | `kind` == literal string `"vector_store"` | Type integrity failure |
| H05 | `quality` == `null` | Self-scoring violation — pool metric corruption |
| H06 | Required fields present: `id`, `kind`, `pillar`, `version`, `created`, `updated`, `author`, `backend`, `dimensions`, `distance_metric`, `index_type`, `persistence`, `tags`, `tldr` | Incomplete artifact |
| H07 | `backend` matches a known enum (pinecone, pgvector, chroma, faiss, qdrant, weaviate, milvus, other) | Prevents typos that break integration |
| H08 | `dimensions` is a positive integer matching upstream embedder | Dimension mismatch corrupts entire index |
| H09 | `distance_metric` is one of: cosine, l2, dot_product, inner_product | Invalid metric produces meaningless similarity |
| H10 | Body <= 4096 bytes | Exceeds artifact size contract |
## SOFT Scoring
Weights sum to 100%. Each dimension scores 0 or its full weight.
| ID  | Dimension | Weight | Criteria |
|-----|-----------|--------|----------|
| S01 | tldr quality | 1.0 | `tldr` <= 160 chars, names backend + index type + dimension count |
| S02 | HNSW parameters documented | 1.0 | M, ef_construction, ef_search present with tradeoff explanation |
| S03 | Persistence documented | 1.0 | `persistence` field present; FAISS = manual with save/load instructions |
| S04 | Namespace strategy defined | 1.0 | Body describes collection naming and domain isolation |
| S05 | Lifecycle operations documented | 1.0 | Create, reindex, backup procedures in body |
| S06 | Metadata filtering documented | 0.5 | `metadata_filtering` boolean; body describes supported operations |
| S07 | Connection config complete | 1.0 | Host, port, auth fields present |
| S08 | Anti-patterns documented | 1.0 | >= 4 specific anti-patterns with consequences |
| S09 | Scale guidance | 0.5 | Body notes when to use flat vs HNSW vs IVF based on vector count |
| S10 | Distance metric rationale | 0.5 | Body explains why chosen metric aligns with embedding normalization |
| S11 | `max_vectors` documented | 0.5 | Backend capacity limit or null with explanation |
| S12 | Density >= 0.85 | 1.0 | No filler: "powerful", "blazing-fast", "enterprise-grade" |
## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.5 | GOLDEN | Publish to pool + record in memory |
| >= 8.0 | PUBLISH | Commit to pool |
| >= 7.0 | REVIEW | Acceptable with documented improvement items |
| < 7.0 | REJECT | Revise and resubmit — do not publish |
| 0 (HARD fail) | REJECTED | Fix failing HARD gate(s) first |
## Bypass
Bypasses are logged and expire automatically.
| Field | Value |
|-------|-------|
