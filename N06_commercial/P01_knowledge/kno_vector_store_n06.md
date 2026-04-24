---
id: kno_vector_store_n06
kind: vector_store
8f: F3_inject
pillar: P02
nucleus: n06
title: Commercial Vector Store
version: 1.0
quality: 9.0
tags: [knowledge, vector_store, pgvector, search, pricing, monetization]
density_score: 1.0
related:
  - p01_kc_vector_store
  - bld_knowledge_card_vector_store
  - bld_schema_vector_store
  - bld_memory_vector_store
  - vector-store-builder
  - p03_ins_vector_store
  - bld_collaboration_vector_store
  - p01_vdb_pinecone
  - p03_sp_vector_store_builder
  - bld_schema_memory_architecture
---
<!-- 8F: F1=P01/vector_store F2=vector-store-builder F3=nucleus_def_n06.md,kc_vector_store.md,P01_knowledge/_schema.yaml,N06 W1 config/schema F4=pgvector_backed_storage_for_revenue_scoped_similarity_search F5=apply_patch;python _tools/cex_compile.py F6=author_dense_markdown_artifact F7=frontmatter_ascii_density_linecount_review F8=N06_commercial/P01_knowledge/kno_vector_store_n06.md -->

# Commercial Vector Store

## Purpose

| Field | Value |
|-------|-------|
| Goal | Persist and query commercial embeddings with strong metadata filtering and predictable operational cost |
| Business Lens | Strategic Greed prefers infrastructure that compounds into repeatable monetization over flashy infra sprawl |
| Primary Use | storage for offer, pricing, segment, proof, objection, and retention vectors |
| Failure Prevented | vector stores that are cheap to start but weak on filtering, governance, or reindex discipline |
| Backend Choice | `pgvector` on Postgres |
| Secondary Mode | local FAISS mirror for offline testing only |

## Backend Contract

| Setting | Value | Reason |
|---------|-------|--------|
| backend | `pgvector` | metadata filters and transactional discipline matter for commercial ops |
| connection_profile | `shared_postgres_commercial` | keeps N06 close to existing app infra |
| collection | `n06_commercial_knowledge` | explicit namespace avoids cross-domain contamination |
| dimensions | `1024` | aligned to commercial embedder profile |
| distance_metric | `cosine` | stable for normalized embeddings |
| index_type | `hnsw` | low-latency recall for mixed query loads |
| ef_construction | `128` | better recall for nuanced pricing language |
| ef_search | `64` | good balance between speed and quality |

## Collection Design

| Namespace | Contents | Why |
|-----------|----------|-----|
| `offers` | tiers, bundles, annual plans, add-ons | highest-frequency monetization retrieval |
| `proof` | case studies, metrics, testimonials, benchmarks | persuasion support |
| `competitive` | rival pricing and positioning | strategic response |
| `retention` | renewal saves, churn triggers, downgrade defenses | protects existing revenue |
| `icp` | segment patterns and qualification logic | keeps premium relevance high |

## Metadata Indexing

| Field | Indexed | Purpose |
|-------|---------|---------|
| revenue_stage | yes | stage-aware filtering |
| segment_value | yes | premium and enterprise retrieval precision |
| offer_type | yes | plan-specific lookup |
| margin_sensitivity | yes | protect high-margin motions |
| source_class | yes | separate internal proof from competitor intel |
| freshness_date | yes | demote stale evidence |

## Operational Rules

| Rule ID | Trigger | Action | Commercial Reason |
|---------|---------|--------|-------------------|
| VS01 | dimension mismatch detected | reject write | corrupted search is worse than no search |
| VS02 | stale competitor corpus | reindex namespace only | spend should target changed value surfaces |
| VS03 | enterprise proposal run | warm cache for `offers` and `proof` | faster premium-path generation |
| VS04 | local dev session | allow FAISS mirror reads only | cheap testing without polluting prod |
| VS05 | metadata missing | write to quarantine queue, not main collection | untyped vectors reduce commercial trust |

## Why pgvector Wins

| Factor | pgvector | Why N06 Prefers It |
|--------|----------|--------------------|
| metadata filters | strong | commercial search is filter-heavy |
| operational simplicity | high | one fewer separate system to babysit |
| transactional writes | native | index updates can align with content publishing |
| local parity | moderate | dev and prod can share SQL idioms |
| cost profile | efficient at current scale | greed likes boring infra with good unit economics |

## Rationale

| Design Choice | Why It Exists | Strategic Greed Impact |
|---------------|---------------|------------------------|
| pgvector over managed niche store | N06 does not need premium infra tax before premium scale exists | better margin discipline |
| namespace split | retrieval quality collapses if every surface shares one pile | keeps decisions crisp |
| metadata mandatory | semantic similarity alone cannot reason about business stage | preserves cash relevance |
| HNSW index | enough speed for interactive use | supports commercial workflows without overpaying |
| FAISS mirror only for dev | local speed is useful, but prod truth should stay governed | limits ops drift |

## Example

| Scenario | Result |
|----------|--------|
| N06 adds new annual bundle proof and updates competitor pricing notes | only `offers`, `proof`, and `competitive` namespaces reindex, while retention corpus stays untouched |

```yaml
backend: pgvector
collection: n06_commercial_knowledge
dimensions: 1024
distance_metric: cosine
index_type: hnsw
ef_construction: 128
ef_search: 64
```

## Risk Controls

| Risk | Guard |
|------|-------|
| mixed namespaces in one query | require namespace filter in retriever profile |
| silent vector drift | pin dimension and model tuple in index metadata |
| stale proof claims | freshness filter and scheduled demotion |
| operational sprawl | keep FAISS out of production write path |

## Properties

| Property | Value |
|----------|-------|
| Owner | N06 Commercial |
| Kind | `vector_store` |
| Primary Backend | `pgvector` |
| Index Type | `hnsw` |
| Dimensions | 1024 |
| Metadata Posture | mandatory and indexed |
| Cost Bias | compound value before infra expansion |
| Related Artifacts | `kno_embedder_provider_n06`, `kno_retriever_config_n06`, `mem_knowledge_index_n06` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_vector_store]] | upstream | 0.27 |
| [[bld_knowledge_card_vector_store]] | upstream | 0.26 |
| [[bld_schema_vector_store]] | downstream | 0.26 |
| [[bld_memory_vector_store]] | downstream | 0.26 |
| [[vector-store-builder]] | related | 0.25 |
| [[p03_ins_vector_store]] | downstream | 0.25 |
| [[bld_collaboration_vector_store]] | related | 0.24 |
| [[p01_vdb_pinecone]] | sibling | 0.24 |
| [[p03_sp_vector_store_builder]] | downstream | 0.23 |
| [[bld_schema_memory_architecture]] | downstream | 0.23 |
