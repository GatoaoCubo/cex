---
id: kno_retriever_config_n02
kind: retriever_config
8f: F3_inject
pillar: P01
nucleus: N02
title: "N02 Marketing Retriever Config"
version: "1.0.0"
quality: 9.1
tags: [retriever_config, marketing, hybrid_search, retrieval, creative_lust, n02]
density_score: 1.0
related:
  - p01_retriever_config
  - p08_ac_n02
  - n02_kc_campaign
  - bld_knowledge_card_retriever_config
  - n02_self_review_2026-04-02
  - n04_rc_knowledge
  - p01_kc_retriever
  - p11_qg_marketing_artifacts
  - p10_lr_retriever_config_builder
  - p01_kc_brand_voice_consistency_channels
---
<!-- 8F: F1=retriever_config/P01 F2=retriever-config-builder F3=nucleus_def_n02+kc_campaign+ab_testing_framework+campaign_performance_memory+P01_schema+P10_schema F4=hybrid_ranker_for_marketing_generation F5=shell_command,apply_patch F6=approx_6kb F7=frontmatter+8F+80_lines+dense_tables+self_check_pass F8=N02_marketing/P01_knowledge/kno_retriever_config_n02.md -->

# Purpose

| Property | Value |
|----------|-------|
| Kind | retriever_config |
| Pillar | P01 |
| Nucleus | N02 |
| Search objective | fetch the most behaviorally useful campaign context |
| Creative Lust lens | rank what can persuade now, not what merely shares vocabulary |
| Search mode | hybrid with rerank |

## Core Configuration

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| name | marketing_hybrid_retriever_n02 | scoped identity |
| store_type | qdrant_plus_bm25_cache | vector plus lexical blend |
| top_k | 8 | enough diversity without flooding prompt budget |
| fetch_k | 24 | broad candidate pool for reranking |
| search_type | hybrid_semantic_lexical | best fit for copy plus metrics |
| hybrid_ratio | 0.62 semantic / 0.38 lexical | semantic leads, exact terms still matter |
| reranker | rule_weighted_cross_encoder | desire-proof-stage refinement |
| score_threshold | 0.43 | filters weak contextual hits |
| filters | stage, channel, audience, offer, artifact_kind | keeps retrieval tactically aligned |

## Why Hybrid Beats Single-Mode Search

| Mode | Win | Loss |
|------|-----|------|
| dense only | captures tonal similarity | misses exact offer terms and brand phrases |
| lexical only | finds exact named offers and metrics | misses adjacent persuasive patterns |
| hybrid | joins language precision with behavioral similarity | slightly more pipeline complexity |

## Ranking Priorities

1. funnel stage match
2. audience segment match
3. offer family match
4. proof relevance
5. channel match
6. recency of performance learning
7. brand voice compatibility

## Scoring Formula

```yaml
ranking_formula:
  hybrid_score: 0.62 * semantic + 0.38 * lexical
  rerank_boosts:
    stage_match: 0.14
    audience_match: 0.12
    offer_match: 0.10
    proof_match: 0.08
    recent_win: 0.06
  penalties:
    stale_performance_claim: -0.10
    wrong_channel: -0.07
    conflicting_cta: -0.09
```

## Filter Policy

| Filter | Default | Why |
|--------|---------|-----|
| funnel_stage | hard filter | stage drift is expensive |
| audience_segment | soft filter | adjacent segments can still teach |
| channel | soft filter | some cross-channel transfer is useful |
| offer_family | hard filter when closing, soft otherwise | BOFU needs stricter precision |
| artifact_kind | weighted | A/B memory often outranks generic brand docs |

## Corpus Weighting

| Source type | Weight | Use case |
|-------------|--------|----------|
| campaign performance memory | high | proof and tested outcomes |
| copy optimization insights | high | learned persuasion patterns |
| current campaign brief chunks | very high | mission-specific constraints |
| brand voice docs | medium | tone guardrails |
| generic marketing KC | medium | fallback reasoning |

## Creative Lust Retrieval Rules

N02 should retrieve the smallest set of sources that can produce:

| Needed output quality | Retrieval requirement |
|----------------------|-----------------------|
| desire | at least one high-tension or high-aspiration chunk |
| proof | at least one metric, testimonial, or outcome chunk |
| fit | at least one audience or channel-matched chunk |
| action | at least one CTA-pattern chunk |

If any one of these is missing, generation should either re-query or ask for missing data.

## Query Rewrite Policy

| Trigger | Rewrite action |
|---------|----------------|
| vague user intent | expand with stage, channel, and offer placeholders |
| no proof terms supplied | append proof-seeking terms like stat, case, testimonial |
| too many brand docs returned | add performance and campaign filters |
| too many stale results | add recency bias |

## Default Retrieval Packs

| Task type | Retrieval pack |
|-----------|----------------|
| ad variants | 3 performance chunks, 2 audience chunks, 2 offer chunks, 1 brand chunk |
| landing page hero | 2 positioning chunks, 3 proof chunks, 2 objection chunks, 1 CTA chunk |
| email sequence | 2 segment chunks, 2 prior winners, 2 offer chunks, 2 stage-transition chunks |

## Failure Handling

| Failure | Response |
|---------|----------|
| fewer than 3 valid hits | lower audience strictness, keep stage strict |
| no proof hit found | inject explicit proof gap into generation prompt |
| stale results dominate | promote learning_record and campaign memory |
| conflicting CTA hits | prefer current campaign brief over historical memory |

## Anti-Patterns

| Anti-pattern | Why it harms N02 |
|--------------|------------------|
| top_k too high | prompt pollution and style blending |
| no reranker | lexical noise outranks persuasive fit |
| equal source weights | old generic docs drown out recent wins |
| hard-filter channel always | useful transfer learning gets blocked |
| semantic-only ranking of metrics | exact numbers and named offers disappear |

## Example

```yaml
retrieval_example:
  task: write_mofu_linkedin_ad
  query: "b2b saas conversion audit qualified demos friction"
  top_k: 8
  fetch_k: 24
  filters:
    funnel_stage: mofu
    channel: linkedin
    audience_segment: b2b_saas_founders
  must_have:
    - proof
    - cta
```

## Properties

| Property | Value |
|----------|-------|
| Retrieval mode | hybrid plus rerank |
| Default top_k | 8 |
| Candidate pool | 24 |
| Strongest bias | stage and audience fit |
| Main risk prevented | generic recall that weakens conversion quality |
| Save path | N02_marketing/P01_knowledge/kno_retriever_config_n02.md |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_retriever_config]] | sibling | 0.24 |
| [[p08_ac_n02]] | downstream | 0.23 |
| [[n02_kc_campaign]] | related | 0.23 |
| [[bld_knowledge_card_retriever_config]] | related | 0.23 |
| [[n02_self_review_2026-04-02]] | downstream | 0.22 |
| [[n04_rc_knowledge]] | sibling | 0.22 |
| [[p01_kc_retriever]] | related | 0.21 |
| [[p11_qg_marketing_artifacts]] | downstream | 0.21 |
| [[p10_lr_retriever_config_builder]] | downstream | 0.21 |
| [[p01_kc_brand_voice_consistency_channels]] | related | 0.21 |
