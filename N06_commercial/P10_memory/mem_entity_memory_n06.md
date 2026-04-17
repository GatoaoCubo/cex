---
id: mem_entity_memory_n06
kind: entity_memory
pillar: P10
nucleus: n06
title: Commercial Entity Memory
version: 1.0
quality: null
tags: [memory, entity_memory, accounts, offers, pricing, segments]
---
<!-- 8F: F1=P10/entity_memory F2=entity-memory-builder F3=nucleus_def_n06.md,kc_entity_memory.md,P10_memory/_schema.yaml,N06 commercial knowledge set F4=store_high_value_commercial_entities_with_update_policies F5=apply_patch;python _tools/cex_compile.py F6=author_dense_markdown_artifact F7=frontmatter_ascii_density_linecount_review F8=N06_commercial/P10_memory/mem_entity_memory_n06.md -->

# Commercial Entity Memory

## Purpose

| Field | Value |
|-------|-------|
| Goal | Define which commercial entities N06 remembers persistently and how facts about them are updated |
| Business Lens | Strategic Greed remembers entities in proportion to LTV, margin leverage, and decision reuse |
| Primary Use | keep stable facts about offers, customer segments, competitors, and high-value accounts |
| Failure Prevented | wasting memory on low-yield trivia while forgetting the entities that shape pricing and retention decisions |
| Memory Mode | current-state fact store with confidence and expiry |
| Update Style | overwrite volatile facts, preserve stable strategic attributes |

## Entity Classes

| Entity Type | Example | Why It Merits Memory |
|-------------|---------|----------------------|
| offer | annual_growth_plus | direct monetization surface |
| segment | scale_b2b_ops | controls pricing and proof selection |
| competitor | rival_usage_based_vendor | affects positioning and discount defense |
| account | expansion_candidate_001 | high-value live opportunity |
| service | stripe_checkout | operational dependency tied to revenue capture |

## Attribute Policy

| Attribute | Required | Example | Why |
|-----------|----------|---------|-----|
| entity_name | yes | `annual_growth_plus` | stable retrieval key |
| entity_type | yes | `offer` | drives update rules |
| current_value_band | yes | `high` | revenue priority |
| margin_profile | yes | `healthy` | greed cares about profit quality |
| stage_relevance | yes | `convert,expand` | retrieval routing |
| evidence_source | yes | `internal_offer_doc` | provenance |
| confidence | yes | `0.92` | distinguish fact from inference |
| review_window_days | yes | `14` | forces freshness discipline |

## Example Entities

| Entity | Type | Key Facts | Update Policy |
|--------|------|-----------|---------------|
| annual_growth_plus | offer | annual plan, margin-safe, best for scale buyers near quota | overwrite on pricing revision |
| scale_b2b_ops | segment | values ROI proof, needs procurement clarity, tolerates annual prepay | merge on new sales evidence |
| rival_usage_based_vendor | competitor | undercuts on entry tier, weak enterprise support proof | overwrite every market refresh |
| expansion_candidate_001 | account | current starter plan, usage above 85 percent, low discount tolerance | merge active signals, expire quickly |

## Relationship Map

| Entity | Relation | Target | Why It Matters |
|--------|----------|--------|----------------|
| annual_growth_plus | best_fit_for | scale_b2b_ops | supports offer recommendation |
| expansion_candidate_001 | fits_segment | scale_b2b_ops | enables segment-aware prompts |
| rival_usage_based_vendor | competes_with | annual_growth_plus | supports counter-positioning |
| stripe_checkout | enables | annual_growth_plus | ties ops dependency to revenue path |

## Freshness Policy

| Entity Type | TTL Days | Reason |
|-------------|----------|--------|
| offer | 14 | pricing and packaging shift frequently |
| segment | 45 | market pattern changes slower |
| competitor | 21 | pricing intel rots fast |
| account | 7 | live commercial state changes quickly |
| service | 30 | integration facts matter but churn less often |

## Update Rules

| Rule ID | Trigger | Action | Commercial Reason |
|---------|---------|--------|-------------------|
| EM01 | offer price or package changes | overwrite price, margin, and fit fields | stale pricing is dangerous |
| EM02 | account crosses usage threshold | merge new intent and stage facts | expansion prompts need live signals |
| EM03 | competitor launches new plan | overwrite comparison and risk notes | old competitive memory misprices value |
| EM04 | segment proof weakens | lower confidence, keep until reviewed | avoid overclaiming without deleting pattern |
| EM05 | entity misses TTL | demote from prompt injection | stale memory should not steer active deals |

## What Not to Store

| Exclusion | Why |
|-----------|-----|
| raw payment credentials | belongs in secret config, never memory |
| temporary task queues | belongs in runtime state |
| long narrative notes without structure | retrieval should operate on typed facts |
| vanity facts without revenue effect | greed forgets what does not move money |

## Rationale

| Design Choice | Why It Exists | Strategic Greed Impact |
|---------------|---------------|------------------------|
| value-band field | not all entities deserve equal prompt real estate | premium entities stay top of mind |
| short TTL for accounts | active revenue opportunities shift fast | reduces stale guidance |
| relationship mapping | offers convert better when fit and competition stay linked | improves recommendation quality |
| confidence scores | commercial systems should know what is inferred | supports safer automation |
| exclusions list | memory bloat dilutes retrieval and raises risk | protects operational focus |

## Example Structure

```yaml
name: annual_growth_plus
entity_type: offer
attributes:
  current_value_band: high
  margin_profile: healthy
  stage_relevance: convert,expand
  evidence_source: internal_offer_doc
  confidence: 0.92
relationships:
  - entity: scale_b2b_ops
    relation: best_fit_for
ttl_days: 14
```

## Properties

| Property | Value |
|----------|-------|
| Owner | N06 Commercial |
| Kind | `entity_memory` |
| Priority Bias | LTV and margin weighted |
| Main Entities | offers, segments, competitors, accounts, services |
| TTL Posture | short for volatile revenue facts |
| Update Mode | overwrite volatile, merge strategic |
| Related Artifacts | `mem_runtime_state_n06`, `mem_knowledge_index_n06`, `kno_retriever_config_n06` |
