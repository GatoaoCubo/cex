---
id: mem_knowledge_index_n02
kind: knowledge_index
pillar: P10
nucleus: N02
title: "N02 Marketing Knowledge Index"
version: "1.0.0"
quality: null
tags: [knowledge_index, marketing, hybrid_search, memory, creative_lust, n02]
---
<!-- 8F: F1=knowledge_index/P10 F2=knowledge-index-builder F3=nucleus_def_n02+con_path_config_n02+campaign_performance_memory+copy_optimization_insights+P10_schema F4=index_plan_for_n02_corpus_search F5=shell_command,apply_patch F6=approx_6kb F7=frontmatter+8F+80_lines+dense_tables+self_check_pass F8=N02_marketing/P10_memory/mem_knowledge_index_n02.md -->

# Purpose

| Property | Value |
|----------|-------|
| Kind | knowledge_index |
| Pillar | P10 |
| Nucleus | N02 |
| Index goal | searchable brain for campaign and copy decisions |
| Creative Lust lens | retrieve the exact mix of desire, proof, and action needed for the brief |
| Algorithm | hybrid BM25 plus vector search |

## Scope

| Include path | Why |
|--------------|-----|
| N02_marketing/P01_knowledge/ | core strategy and marketing knowledge |
| N02_marketing/P10_memory/ | performance and learning carry proof signals |
| N02_marketing/P09_config/ | runtime constraints and provider boundaries |
| N02_marketing/P06_schema/ | validation and contract cues |

| Exclude path | Why |
|--------------|-----|
| N02_marketing/compiled/ | derived artifacts, not source truth |
| N02_marketing/P05_output/ | campaign deliverables may be ephemeral |
| .cex/runtime/handoffs/ | instructions, not reusable knowledge corpus |

## Corpus Shape

| Corpus slice | Type | Search value |
|--------------|------|--------------|
| campaign KCs | text | reusable strategy |
| performance memory | text plus structured metrics | proof and winners |
| learning records | text plus pattern logs | optimization logic |
| config docs | structured markdown | runtime boundaries |

## Algorithm Configuration

| Layer | Choice | Reason |
|-------|--------|--------|
| lexical | BM25 | exact match on offer names, stats, and brand terms |
| semantic | Qdrant cosine vectors | recall adjacent persuasion patterns |
| fusion | weighted reciprocal rank | stable combination of both worlds |
| rerank | rule-guided marketing reranker | stage and proof matter beyond text similarity |

## BM25 Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| k1 | 1.4 | moderate term saturation |
| b | 0.72 | length normalization for markdown chunks |
| tokenizer | lowercase_wordpiece_plus_symbol_keep | preserve offer and CTA tokens |
| boost_exact_offer | 1.25 | named offers should surface fast |
| boost_recent_metrics | 1.15 | newer evidence matters more |

## Vector Parameters

| Parameter | Value | Notes |
|-----------|-------|-------|
| backend | qdrant | metadata filters required |
| metric | cosine | aligned with embedder |
| dimensions | 3072 primary | high-fidelity corpus |
| fallback_dimensions | 1536 | conservation mode |
| ef_search | 96 | recall-latency balance |

## Hybrid Weights

| Component | Weight | Notes |
|-----------|--------|-------|
| BM25 | 0.38 | precision on explicit language |
| semantic | 0.62 | nuance on tone, stage, and pain |
| rerank boosts | variable | stage, audience, offer, proof |

## Filters

| Filter | Type | Condition | Applied |
|--------|------|-----------|---------|
| funnel_stage | pre | exact when query names stage | always if present |
| audience_segment | post | prefer exact, allow close neighbors | when provided |
| channel | post | bias to same channel | when provided |
| artifact_kind | pre | memory and KCs weighted differently | always |
| recency | post | boost last 90d for performance docs | always on memory |

## Ranking Rules

| Factor | Weight | Description |
|--------|--------|-------------|
| stage_match | 0.14 | correct funnel positioning |
| audience_match | 0.12 | right emotional assumptions |
| offer_match | 0.10 | commercial relevance |
| proof_presence | 0.08 | avoids empty hype |
| recent_win | 0.06 | fresh success signal |
| validator_compatibility | 0.04 | keeps outputs compliant |

## Rebuild Schedule

| Trigger | Schedule | Duration | Impact |
|---------|----------|----------|--------|
| markdown source change | on_change | low | partial lexical refresh |
| batch campaign update | nightly | medium | partial vector upsert |
| embedder model change | manual | high | full vector rebuild |
| stale index over 7d | forced nightly | medium | restore freshness |

## Monitoring

| Metric | Threshold | Alert |
|--------|-----------|-------|
| empty_result_rate | > 8 percent | inspect filters and chunk quality |
| stale_hit_rate | > 20 percent | recency weighting too weak |
| proofless_hit_rate | > 15 percent | boost performance memory |
| average_latency | > 350 ms | tune candidate pool or cache |

## Creative Lust Search Contract

Every successful retrieval set should contain at least:

1. one desire or pain frame
2. one proof-bearing fragment
3. one action or CTA cue
4. one tone or brand guardrail

If the index returns only conceptual marketing notes, it has failed N02.

## Anti-Patterns

| Anti-pattern | Why it fails |
|--------------|--------------|
| index output files with source docs | noisy duplication |
| no recency weighting on memory | stale wins dominate |
| no lexical layer | exact offer names vanish |
| no proof-aware rerank | generic inspiration outranks tested guidance |
| one rebuild schedule for all layers | needless cost and drift |

## Properties

| Property | Value |
|----------|-------|
| Search mode | hybrid BM25 plus vectors |
| Primary corpus | N02 knowledge, memory, config, schemas |
| Rebuild style | event plus nightly |
| Main quality guard | proof-aware reranking |
| Main risk prevented | retrieval that sounds smart but sells weakly |
| Save path | N02_marketing/P10_memory/mem_knowledge_index_n02.md |
