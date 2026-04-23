---
kind: quality_gate
id: p11_qg_vector_store
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of vector_store artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: Vectordb Backend"
version: "1.0.0"
author: builder_agent
tags: [quality-gate, vector-store, vector-database, P01, hnsw]
tldr: "Quality gate for vector_store artifacts: enforces dimensions, distance metric, index type, and persistence fields."
domain: vector_store
created: "2026-04-06"
updated: "2026-04-06"
density_score: 0.87
related:
  - p03_ins_vector_store
  - p11_qg_embedder_provider
  - bld_knowledge_card_vector_store
  - p03_sp_vector_store_builder
  - p11_qg_model_provider
  - bld_output_template_vector_store
  - bld_memory_vector_store
  - bld_schema_vector_store
  - p11_qg_model_card
  - bld_config_vector_store
---

## Quality Gate

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

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
