---
id: mem_knowledge_index_n06
kind: knowledge_index
8f: F3_inject
pillar: P10
nucleus: n06
title: Commercial Knowledge Index
version: 1.0
quality: 9.0
tags: [memory, knowledge_index, hybrid, bm25, pgvector, retrieval]
density_score: 1.0
updated: "2026-04-17"
related:
  - p01_kc_knowledge_index
  - knowledge-index-builder
  - bld_knowledge_card_knowledge_index
  - bld_collaboration_knowledge_index
  - bld_examples_knowledge_index
  - p03_sp_knowledge_index_builder
  - n04_knowledge_memory_index
  - p10_lr_knowledge-index-builder
  - p10_bi_bm25_knowledge
  - agent_card_n06
---
<!-- 8F: F1=P10/knowledge_index F2=knowledge-index-builder F3=nucleus_def_n06.md,kc_knowledge_index.md,P10_memory/_schema.yaml,N06 commercial knowledge set F4=hybrid_index_topology_for_revenue_weighted_search F5=apply_patch;python _tools/cex_compile.py F6=author_dense_markdown_artifact F7=frontmatter_ascii_density_linecount_review F8=N06_commercial/P10_memory/mem_knowledge_index_n06.md -->

# Commercial Knowledge Index

## Purpose

| Field | Value |
|-------|-------|
| Goal | Define the persistent search index strategy for N06 commercial knowledge and memory |
| Business Lens | Strategic Greed builds indexes that surface monetization leverage first and archive trivia second |
| Primary Use | hybrid retrieval across pricing, offers, proof, objections, competitors, and retention memory |
| Failure Prevented | one flat index where premium deal evidence competes with low-value noise |
| Backend Mode | BM25 plus pgvector hybrid |
| Scope | N06 knowledge and selected memory only |

## Index Topology

| Index Name | Backend | Contents | Why |
|------------|---------|----------|-----|
| `idx_n06_offers` | hybrid | offer docs, tier matrices, bundle notes | highest monetization frequency |
| `idx_n06_proof` | hybrid | proof claims, case studies, ROI snippets | persuasion support |
| `idx_n06_competitive` | hybrid | competitor pricing and positioning | pricing defense |
| `idx_n06_retention` | hybrid | save motions, churn triggers, renewal notes | retained revenue protection |
| `idx_n06_icp` | bm25_heavy_hybrid | segments, pains, objections, qualification logic | exact vocabulary matters strongly |

## Core Settings

| Setting | Value | Reason |
|---------|-------|--------|
| backend | `hybrid` | commercial search benefits from lexical and semantic layers |
| dense_backend | `pgvector_hnsw` | scalable enough and metadata-friendly |
| sparse_backend | `bm25` | exact tier labels and metrics still matter |
| dimensions | `1024` | aligned to embedder and vector store |
| hybrid_alpha | `0.62` | slight semantic lean without losing keyword sharpness |
| rebuild_on_stale_h | `24` | daily refresh keeps pricing and proof current |
| namespace_isolation | `strict` | each revenue surface stays searchable without contamination |

## Ranking Intent

| Surface | Alpha | Why |
|---------|-------|-----|
| offers | 0.68 | semantics matter for package and upsell similarity |
| proof | 0.64 | claims and proof vary in wording |
| competitive | 0.55 | exact competitor terms matter more |
| retention | 0.60 | semantic similarity helps on churn phrasing |
| icp | 0.48 | exact role, segment, and pain language matter heavily |

## Inclusion Rules

| Include | Decision |
|---------|----------|
| N06 knowledge cards tied to pricing, segments, proof, offers | yes |
| N06 memory entities with active TTL and confidence >= 0.70 | yes |
| stale account memory | no |
| raw config files | no |
| generic brand theory with no monetization tie | no unless referenced by offer docs |

## Rebuild Triggers

| Trigger | Action | Commercial Reason |
|---------|--------|-------------------|
| pricing artifact updated | rebuild `idx_n06_offers` | active plan changes must search correctly immediately |
| competitor knowledge updated | rebuild `idx_n06_competitive` | stale rival intel erodes pricing power |
| proof metrics changed | rebuild `idx_n06_proof` | outdated claims hurt trust |
| chunk strategy revised | full dense rebuild | vector shape and boundaries changed |
| embedder dimensions changed | full dense rebuild and validation | mixed dimensions break retrieval |

## Validation Rules

| Check | Pass Condition |
|-------|----------------|
| dimension integrity | every dense index entry is 1024d |
| alpha sanity | index alpha stays within 0.40 to 0.75 |
| stale window | no namespace exceeds rebuild threshold without flag |
| namespace purity | each index contains only allowed content classes |
| retrieval smoke test | known pricing query returns expected namespace in top hits |

## Rationale

| Design Choice | Why It Exists | Strategic Greed Impact |
|---------------|---------------|------------------------|
| multiple indexes | revenue tasks differ too much for one global ranking recipe | cleaner monetization retrieval |
| alpha by surface | one weighting scheme is too blunt | profit-critical surfaces get tuned separately |
| strict inclusion rules | not everything worth storing is worth indexing | keeps prompt context high-signal |
| daily stale rebuild | commercial truth changes often enough to punish lazy indexing | preserves pricing accuracy |
| memory inclusion threshold | weak facts should not masquerade as knowledge | safer automation |

## Example

```yaml
backend: hybrid
dense_backend: pgvector_hnsw
sparse_backend: bm25
dimensions: 1024
hybrid_alpha: 0.62
rebuild_on_stale_h: 24
indexes:
  - idx_n06_offers
  - idx_n06_proof
  - idx_n06_competitive
```

## Properties

| Property | Value |
|----------|-------|
| Owner | N06 Commercial |
| Kind | `knowledge_index` |
| Dense Backend | `pgvector_hnsw` |
| Sparse Backend | `bm25` |
| Hybrid Alpha | 0.62 |
| Index Count | 5 |
| Freshness Policy | daily surface rebuilds |
| Related Artifacts | `kno_vector_store_n06`, `kno_embedder_provider_n06`, `kno_retriever_config_n06` |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_knowledge_index]] | related | 0.38 |
| [[knowledge-index-builder]] | related | 0.36 |
| [[bld_knowledge_card_knowledge_index]] | upstream | 0.33 |
| [[bld_collaboration_knowledge_index]] | downstream | 0.32 |
| [[bld_examples_knowledge_index]] | upstream | 0.30 |
| [[p03_sp_knowledge_index_builder]] | upstream | 0.27 |
| [[n04_knowledge_memory_index]] | related | 0.27 |
| [[p10_lr_knowledge-index-builder]] | related | 0.26 |
| [[p10_bi_bm25_knowledge]] | sibling | 0.25 |
| [[agent_card_n06]] | upstream | 0.25 |
