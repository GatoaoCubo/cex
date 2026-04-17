---
id: kno_vector_store_n02
kind: vector_store
pillar: P01
nucleus: N02
title: "N02 Marketing Vector Store"
version: "1.0.0"
quality: null
tags: [vector_store, marketing, qdrant, retrieval, creative_lust, n02]
---
<!-- 8F: F1=vector_store/P01 F2=vector-store-builder F3=nucleus_def_n02+con_path_config_n02+con_permission_n02+con_secret_config_n02+P01_schema+P10_schema F4=vector_backend_for_marketing_similarity_search F5=shell_command,apply_patch F6=approx_6kb F7=frontmatter+8F+80_lines+dense_tables+self_check_pass F8=N02_marketing/P01_knowledge/kno_vector_store_n02.md -->

# Purpose

| Property | Value |
|----------|-------|
| Kind | vector_store |
| Pillar | P01 |
| Nucleus | N02 |
| Backend choice | Qdrant |
| Creative Lust lens | store must preserve fast recall of proven desire patterns |
| Deployment style | local-first with cloud-ready migration path |

## Backend Decision

N02 should use Qdrant as the primary vector store.
The corpus is medium-sized, metadata-rich, and retrieval must support fast filtered search across campaign stages, channels, offers, and A/B evidence.
Qdrant fits this shape better than a file-only FAISS setup and with less relational friction than forcing pgvector into the first version.

## Backend Matrix

| Parameter | Value | Why |
|-----------|-------|-----|
| backend | qdrant | metadata filtering plus HNSW support |
| collection | n02_marketing_memory | dedicated namespace for marketing knowledge |
| dimensions | 3072 primary / 1536 fallback collection | matches embedder tiers |
| distance_metric | cosine | stable for semantic text similarity |
| index_type | hnsw | good latency-recall tradeoff |
| metadata_filtering | yes | required for stage and audience filters |
| persistence | auto | avoids manual snapshot dependence |
| deployment | local_dev_then_cloud | aligned with current repo workflow |

## Connection Profile

```yaml
connection:
  host: localhost
  port: 6333
  api_key_env: QDRANT_API_KEY
  tls: false_local_true_cloud
  database: null
```

## Metadata Schema

| Field | Type | Purpose |
|-------|------|---------|
| nucleus | keyword | hard isolates N02 data |
| artifact_kind | keyword | boost by source type |
| funnel_stage | keyword | stage filtering |
| channel | keyword | channel-aware retrieval |
| audience_segment | keyword | persona fit |
| offer_family | keyword | commercial alignment |
| proof_type | keyword | proof-first reranking |
| cta_type | keyword | action compatibility |
| created_at | datetime | recency bias |
| performance_tier | keyword | winners vs experimental material |

## HNSW Configuration

| Parameter | Value | Effect |
|-----------|-------|--------|
| M | 32 | balanced graph connectivity |
| ef_construction | 256 | higher build quality |
| ef_search | 96 | strong recall without excessive latency |
| optimizer_flush | medium cadence | stable ingest during batch writes |

## Namespace Strategy

| Namespace rule | Decision |
|----------------|----------|
| per nucleus | yes |
| per embedding dimension family | yes |
| per environment | yes |
| per active mission | no, use metadata instead |
| per channel | no, channel stays filterable metadata |

## Why Qdrant Fits Creative Lust

N02 retrieval is not a plain library lookup.
It is a seduction support system.
The backend must therefore support:

1. fast approximate similarity
2. strict metadata filters
3. namespace isolation
4. reliable updates as campaigns learn
5. future rerank and hybrid integrations

Qdrant gives N02 a collection model where desire-rich fragments can be recalled with tactical precision.

## Ingest Lifecycle

| Step | Action |
|------|--------|
| 1 | chunk markdown by marketing-aware boundaries |
| 2 | serialize chunk plus metadata |
| 3 | embed with primary or fallback model |
| 4 | upsert into dimension-matched collection |
| 5 | verify metadata completeness |
| 6 | refresh lexical cache for hybrid search |

## Operational Guardrails

| Guardrail | Reason |
|-----------|--------|
| do not mix dimensions in one collection | query math and ranking drift |
| require metadata completeness on upsert | filters are core to N02 quality |
| prefer append and version fields over destructive rewrite | preserve learning history |
| snapshot before major rebuild | campaign memory is cumulative |
| deny secrets in markdown | credentials belong in env or vault |

## Comparison Snapshot

| Backend | Strength | Weakness vs Qdrant |
|---------|----------|--------------------|
| FAISS | fast local prototype | weak metadata filtering and persistence story |
| pgvector | SQL-friendly | more operational overhead for first pass |
| Chroma | simple startup | less robust filtering posture for long-term use |
| Qdrant | strong filter plus HNSW plus collections | extra service dependency |

## Failure Modes

| Failure | Mitigation |
|---------|------------|
| collection corruption | restore latest snapshot and replay ingest log |
| latency spike | raise cache use, tune ef_search, reduce top candidate pool |
| dimension mismatch | reject write at ingest validator |
| filter sparsity | backfill metadata before enabling hybrid retrieval |

## Example

```yaml
collection_profile:
  name: n02_marketing_memory_3072
  metric: cosine
  index: hnsw
  metadata_required:
    - funnel_stage
    - audience_segment
    - offer_family
    - cta_type
```

## Anti-Patterns

| Anti-pattern | Consequence |
|--------------|-------------|
| one giant cross-nucleus collection | noisy retrieval contamination |
| vectors without stage metadata | wrong-funnel prompts |
| rebuilding by delete-all each time | memory amnesia |
| mixing draft and production corpora | unstable quality |
| using vector store as source of truth | markdown source drift becomes invisible |

## Properties

| Property | Value |
|----------|-------|
| Backend | Qdrant |
| Index type | HNSW |
| Metric | cosine |
| Metadata stance | required and first-class |
| Main risk prevented | semantically close but tactically unusable recall |
| Save path | N02_marketing/P01_knowledge/kno_vector_store_n02.md |
