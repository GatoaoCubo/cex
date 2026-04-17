---
id: kno_retriever_config_n01
kind: retriever_config
pillar: P01
nucleus: N01
title: "N01 Retriever Config"
version: "1.0.0"
quality: 9.0
tags: [retriever_config, n01, p01, analytical_envy, hybrid_search]
density_score: 0.99
---
<!-- 8F: F1=retriever_config/P01 F2=kc_retriever_config+tpl_retriever_config F3=nucleus_def_n01+kc_retriever_config+ex_retriever_config_hybrid_rag+search_config_intelligence F4=hybrid retrieval for competitive evidence
     F5=rg+Get-Content+apply_patch F6=target dense markdown artifact F7=self-check properties+8F+ascii+80lines F8=N01_intelligence/P01_knowledge/kno_retriever_config_n01.md -->

# N01 Retriever Config

## Purpose
The retriever config decides which evidence gets the first chance to shape synthesis.
For N01, that makes it a strategic artifact, not a tuning file.
Analytical Envy means retrieval must favor the strongest comparative evidence, not just the most semantically nearby text.

## Properties

| Property | Value |
|----------|-------|
| Kind | `retriever_config` |
| Pillar | `P01` |
| Nucleus | `N01` |
| Lens | `Analytical Envy` |
| Default mode | hybrid |
| Candidate set | over-fetch then rerank |
| top_k final | 6 |
| top_k initial | 24 |
| Core filters | source tier, date, entity, axis |
| Main mission | retrieve evidence fit for comparison, not just mention overlap |

## Retrieval Thesis
N01 queries often ask:
- who is better and why
- what changed recently
- what is true according to the strongest source
- how one competitor differs from another on a specific axis

That means the retriever must combine:
- exact term recall
- semantic similarity
- metadata filtering
- citation-aware reranking

## Recommended Defaults

| Setting | Value | Reason |
|---------|-------|--------|
| search_type | `hybrid` | balances semantic and exact lookup |
| dense_weight | `0.65` | semantic relation matters |
| sparse_weight | `0.35` | exact competitor names and plans still matter |
| top_k_initial | `24` | enough headroom for reranking |
| top_k_final | `6` | fits synthesis budgets |
| similarity_floor | `0.62` | rejects weak semantic drift |
| reranker | `cross_encoder_or_llm` | stronger final ordering |
| freshness_bias | `on_for_volatile_axes` | pricing and specs decay quickly |

## Metadata Filters

| Filter | Why it matters |
|--------|----------------|
| source_type | official docs versus commentary |
| reliability_tier | keep weak evidence from dominating |
| entity_primary | row or vendor targeting |
| comparison_axis | price, feature, performance, trust |
| date_claim | freshness-sensitive retrieval |
| region | prevent invalid market mixing |
| contradiction_flag | surface conflict when needed |

## Retrieval Pipeline
1. Parse the query into entity, axis, date, region, and intent.
2. Run dense search and sparse search in parallel.
3. Merge candidates with weighted fusion.
4. Apply hard metadata filters.
5. Rerank with a model that can read evidence quality cues.
6. Return final chunks with citation metadata attached.

## Query Modes

| Mode | Trigger | Retrieval behavior |
|------|---------|--------------------|
| compare | query includes two or more entities | promote chunks with direct contrast |
| verify | user asks if a claim is true | prioritize tier_1 and freshest citations |
| scan | broad market lookup | widen topic coverage, keep proof quality visible |
| gap_find | user asks what is missing | surface unresolved or low-confidence areas |

## Reranking Logic
Reranking in N01 should not score text on relevance alone.
It should weigh:
- claim specificity
- citation presence
- reliability tier
- freshness
- comparative usefulness

A chunk that says less but proves more should beat a chunk that says more but proves little.

## Fallback Chain

| Failure mode | Fallback |
|--------------|----------|
| no results above floor | lower threshold slightly and keep filters |
| still sparse | widen date window |
| still sparse | drop to hybrid without region filter |
| still sparse | return explicit evidence gap |

The system should not hallucinate completeness when the corpus does not support it.

## Anti-Patterns
- dense-only retrieval for pricing queries
- sparse-only retrieval for conceptual method questions
- fixed top_k without query intent awareness
- reranking that ignores freshness and source quality
- no way to surface contradiction cases

## Evaluation Set Expectations
N01 should maintain test queries for:
- direct competitor battles
- pricing changes
- plan naming edge cases
- benchmark metric retrieval
- conflict and contradiction detection

## N01 Decision
The N01 retriever config exists to maximize decision-grade evidence per token.
If retrieval returns generic context instead of decisive comparative proof, the rest of the pipeline is already compromised.
