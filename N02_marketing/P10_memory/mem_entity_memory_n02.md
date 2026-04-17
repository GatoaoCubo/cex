---
id: mem_entity_memory_n02
kind: entity_memory
pillar: P10
nucleus: N02
title: "N02 Marketing Entity Memory"
version: "1.0.0"
quality: 9.1
tags: [entity_memory, marketing, entities, campaign_memory, creative_lust, n02]
density_score: 1.0
---
<!-- 8F: F1=entity_memory/P10 F2=entity-memory-builder F3=nucleus_def_n02+kc_campaign+campaign_performance_memory+copy_optimization_insights+P10_schema F4=entity_map_for_marketing_runtime_recall F5=shell_command,apply_patch F6=approx_6kb F7=frontmatter+8F+80_lines+dense_tables+self_check_pass F8=N02_marketing/P10_memory/mem_entity_memory_n02.md -->

# Purpose

| Property | Value |
|----------|-------|
| Kind | entity_memory |
| Pillar | P10 |
| Nucleus | N02 |
| Tracking goal | remember durable marketing entities across sessions |
| Creative Lust lens | seduction improves when the system remembers who desires what, where, and why |
| Update mode | merge with confidence-aware refresh |

## Scope

This memory is not for every passing campaign detail.
It stores durable entities that shape N02 behavior over time.
The main entity classes are:

1. audience segments
2. offer families
3. proof assets
4. channels
5. brand voice anchors

## Entity Catalog

| Entity | Type | Why it matters |
|--------|------|----------------|
| b2b_saas_founders | concept | recurring high-value audience |
| conversion_audit | project | repeated offer family used in copy |
| proof_metric_library | project | persistent store of trusted stats and wins |
| linkedin_paid | service | channel with specific tone and length constraints |
| n02_brand_voice | concept | tone guardrail for all generation |

## Canonical Attributes

| Attribute key | Meaning | Example |
|---------------|---------|---------|
| desire_vector | dominant aspiration or fear | more qualified demos without more spend |
| skepticism_level | expected resistance | high |
| proof_preference | evidence pattern that converts | metrics plus case evidence |
| CTA_preference | action style that performs | explicit, low-friction booking CTA |
| freshness_window | how long facts stay trusted | 90d for performance entities |

## Example Entity Payload

```yaml
entity_memory:
  name: b2b_saas_founders
  entity_type: concept
  attributes:
    desire_vector: "more pipeline from existing traffic"
    skepticism_level: "high"
    proof_preference: "metric_plus_diagnosis"
    CTA_preference: "book_audit"
    freshness_window: "90d"
  relationships:
    - entity: conversion_audit
      relation: responds_to
    - entity: linkedin_paid
      relation: reached_via
```

## Relationship Map

| Source entity | Relation | Target entity | Why it is stored |
|---------------|----------|---------------|------------------|
| b2b_saas_founders | responds_to | conversion_audit | maps offer fit |
| conversion_audit | validated_by | proof_metric_library | keeps proof tied to offer |
| linkedin_paid | constrained_by | n02_brand_voice | channel tone guardrail |
| n02_brand_voice | sharpens | b2b_saas_founders | audience-specific tone routing |

## Update Policy

| Policy area | Rule |
|-------------|------|
| strategy | merge |
| attribute overwrite | latest stronger evidence wins |
| confidence floor | below 0.65 stays provisional |
| expiry | performance-derived attributes reviewed every 90d |
| append-only fields | relationship history and evidence log |

## Confidence Model

| Confidence band | Meaning | Action |
|-----------------|---------|--------|
| 0.90-1.00 | direct observed win or official constraint | retrieve normally |
| 0.75-0.89 | repeated internal pattern | retrieve with minor caution |
| 0.65-0.74 | inferred from limited tests | label as tentative |
| below 0.65 | not memory-grade yet | keep out of main retrieval path |

## Creative Lust Memory Logic

N02 should remember not only facts, but conversion-relevant emotional structure.
For each audience or offer entity, store:

| Emotional field | Why |
|-----------------|-----|
| dominant desire | directs hook selection |
| dominant fear | shapes objection handling |
| acceptable urgency | prevents manipulative mismatch |
| trust trigger | aligns proof format |
| preferred invitation | improves CTA fit |

## Storage Rules

1. Do not store secrets, personal contact data, or irrelevant project noise.
2. Do store repeatable conversion traits that survive one campaign.
3. Separate entity facts from session guesses.
4. Link entities by verbs that influence generation behavior.
5. Keep slugs ASCII-safe and stable.

## Retrieval Use

| Runtime need | Entity memory contribution |
|--------------|---------------------------|
| write a new ad | recalls audience desire and skepticism |
| tune a CTA | recalls preferred invitation style |
| choose proof | recalls trusted evidence format |
| route a brief | recalls offer-to-channel fit |

## Anti-Patterns

| Anti-pattern | Result |
|--------------|--------|
| storing every campaign as an entity | memory bloat |
| storing raw metrics without interpretation | weak retrieval usefulness |
| mixing user identity data with audience archetypes | privacy and logic confusion |
| keeping stale proof forever | outdated persuasion guidance |
| relation names like "related_to" only | low-action graph |

## Maintenance Triggers

| Trigger | Action |
|---------|--------|
| new statistically significant test win | update relevant audience or offer entity |
| repeated CTA underperformance | revise CTA_preference attribute |
| brand voice change | update n02_brand_voice relations |
| quarterly review | decay stale performance-linked facts |

## Properties

| Property | Value |
|----------|-------|
| Main entity classes | audience, offer, proof, channel, brand voice |
| Update strategy | merge with confidence |
| Expiry stance | 90d review for performance facts |
| Main runtime value | better hook, proof, and CTA fit |
| Main risk prevented | forgetting durable audience and offer behavior |
| Save path | N02_marketing/P10_memory/mem_entity_memory_n02.md |
