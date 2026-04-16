---
id: kno_retriever_config_n06
kind: retriever_config
pillar: P01
nucleus: n06
title: Commercial Retriever Config
version: 1.0
quality: null
tags: [knowledge, retriever_config, rag, pricing, search, revenue]
---
<!-- 8F: F1=P01/retriever_config F2=retriever-config-builder F3=nucleus_def_n06.md,kc_retriever_config.md,P01_knowledge/_schema.yaml,N06 W1 config/schema F4=hybrid_retrieval_tuned_for_margin_safe_conversion_decisions F5=apply_patch;python _tools/cex_compile.py F6=author_dense_markdown_artifact F7=frontmatter_ascii_density_linecount_review F8=N06_commercial/knowledge/kno_retriever_config_n06.md -->

# Commercial Retriever Config

## Purpose

| Field | Value |
|-------|-------|
| Goal | Retrieve the highest-value commercial evidence fast enough to support pricing and funnel decisions in-session |
| Business Lens | Strategic Greed retrieves by expected cash impact, not by semantic curiosity |
| Primary Use | commercial prompt hydration for pricing, offer selection, renewal save, upsell, and competitor response |
| Failure Prevented | broad retrieval that surfaces nice-to-know context while hiding revenue-critical evidence |
| Search Mode | hybrid with metadata filters and lightweight rerank |
| Default Output | top ranked commercial passages plus rationale tags |

## Core Settings

| Setting | Value | Reason |
|---------|-------|--------|
| name | `commercial_hybrid_priority` | stable retrieval profile for N06 |
| store_type | `hybrid_pgvector_bm25` | combines lexical precision with dense recall |
| top_k | `8` | enough breadth without flooding prompts |
| search_type | `hybrid` | pricing language benefits from exact terms and semantic match |
| reranker | `metadata_first_then_cosine` | buying-stage metadata should influence ranking before prose style |
| min_score | `0.63` | cuts weak semantic matches that add noise |
| timeout_ms | `1800` | commercial flow should stay responsive |

## Ranking Policy

| Rank Signal | Weight | Why It Matters |
|-------------|--------|----------------|
| intent proximity | 0.28 | active checkout and renewal risk deserve priority |
| segment match | 0.18 | enterprise guidance should not hydrate starter prompts |
| offer match | 0.16 | keeps plan-specific evidence near the top |
| lexical overlap | 0.14 | exact tier names and metrics remain important |
| semantic similarity | 0.14 | captures alternate phrasing and proof |
| margin safety | 0.10 | low-margin suggestions should fall behind safer options |

## Query Profiles

| Profile | top_k | Filters | Use Case |
|---------|-------|---------|----------|
| pricing_refresh | 8 | stage=`convert` or `expand` | build or revise plan positioning |
| renewal_rescue | 6 | stage=`retain` and intent=`renewal_risk` | pull save motions fast |
| competitor_counter | 10 | source=`competitive` | prepare response to rival pricing |
| bundle_design | 8 | offer_type=`bundle` or `add_on` | assemble monetizable package |
| icp_match | 7 | segment exact match preferred | choose proof for target buyer |

## Filter Contract

| Filter | Allowed Values | Commercial Purpose |
|--------|----------------|-------------------|
| revenue_stage | acquire, convert, expand, retain | keeps retrieval aligned with buyer journey |
| segment_value | starter, growth, scale, enterprise | defends premium relevance |
| offer_type | trial, monthly, annual, bundle, enterprise | binds evidence to monetization motion |
| margin_sensitivity | high, medium, low | avoids recommending weak-profit options too early |
| source_class | internal, competitive, proof, playbook | controls trust and persuasion mix |

## Rerank Logic

| Step | Action | Result |
|------|--------|--------|
| 1 | execute BM25 and vector search in parallel | candidate pool |
| 2 | deduplicate by chunk id | clean pool |
| 3 | apply hard metadata filters | commercially relevant set |
| 4 | boost exact offer and stage match | rank stability |
| 5 | penalize stale competitor sources and low-margin advice | safer decisions |
| 6 | return top 8 with tags | prompt-ready evidence |

## Freshness Rules

| Content Class | Max Age | Action if Stale |
|---------------|---------|-----------------|
| competitor pricing | 30 days | demote unless explicitly requested |
| internal offer docs | 14 days | request refresh if newer version exists |
| retention playbooks | 45 days | keep if policy unchanged |
| proof metrics | 21 days | demote if outdated performance claims |
| ICP notes | 60 days | retain with lower confidence |

## Rationale

| Design Choice | Why It Exists | Strategic Greed Impact |
|---------------|---------------|------------------------|
| top_k of 8 | commercial prompts need focused evidence, not archive dumps | better action density |
| hybrid mode | exact pricing labels and semantic objections both matter | stronger retrieval across sales language |
| metadata-first rerank | business stage often matters more than verbal similarity | aligns search with cash timing |
| stale demotion | old pricing evidence can trigger margin damage | reduces costly mistakes |
| margin safety factor | not every convertible move is worth the discount | protects profit quality |

## Example

| Scenario | Result |
|----------|--------|
| User asks for the best upgrade path for a scale account near quota limit | retriever prioritizes expansion-stage annual offer chunks, proof for scale teams, and margin-safe upgrade plays |

```yaml
name: commercial_hybrid_priority
store_type: hybrid_pgvector_bm25
top_k: 8
search_type: hybrid
reranker: metadata_first_then_cosine
filters:
  - revenue_stage
  - segment_value
  - offer_type
  - margin_sensitivity
```

## Operating Notes

| Topic | Rule |
|-------|------|
| null results | relax segment filter before relaxing stage filter |
| noisy results | raise min_score before lowering top_k |
| enterprise prompts | boost proof and policy chunks over generic copy |
| experimentation | log winning result sets into memory for later tuning |

## Properties

| Property | Value |
|----------|-------|
| Owner | N06 Commercial |
| Kind | `retriever_config` |
| Search Type | hybrid |
| Default top_k | 8 |
| Primary Bias | cash-proximate evidence first |
| Rerank Style | metadata-first then cosine |
| Freshness Guard | stale pricing evidence demoted |
| Related Artifacts | `kno_chunk_strategy_n06`, `kno_vector_store_n06`, `mem_knowledge_index_n06` |
