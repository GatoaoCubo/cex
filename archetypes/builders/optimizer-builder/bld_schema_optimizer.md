---
kind: schema
id: bld_schema_optimizer
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema — SINGLE SOURCE OF TRUTH for optimizer
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Optimizer"
version: "1.0.0"
author: n03_builder
tags: [optimizer, builder, examples]
tldr: "Golden and anti-examples for optimizer construction, demonstrating ideal structure and common pitfalls."
domain: "optimizer construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_usage_report
  - bld_schema_bugloop
  - bld_schema_dataset_card
  - bld_schema_reranker_config
  - bld_schema_unit_eval
  - bld_schema_quickstart_guide
  - bld_schema_safety_policy
  - bld_schema_search_strategy
  - bld_schema_input_schema
  - bld_schema_pitch_deck
---

# Schema: optimizer
## Frontmatter Fields
| Field | Type | Required | Default |
|-------|------|----------|---------|
| id | string (p11_opt_{slug}) | YES | — |
| kind | literal "optimizer" | YES | — |
| pillar | literal "P11" | YES | — |
| version | semver string | YES | "1.0.0" |
| created | date YYYY-MM-DD | YES | — |
| updated | date YYYY-MM-DD | YES | — |
| author | string | YES | — |
| domain | string (process domain being optimized) | YES | — |
| quality | null | YES | null |
| tags | list[string], len >= 3, includes "optimizer" | YES | — |
| tldr | string < 160ch | YES | — |
| density_score | float 0.80-1.00 | REC | — |
## Type-Specific Fields
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| target | string | YES | what process is being optimized |
| metric | object | YES | {name: string, unit: string, direction: enum[minimize,maximize]} |
| action | object | YES | {type: enum[tune,prune,scale,replace,restructure], description: string, automated: boolean} |
| threshold | object | YES | {trigger: float, target: float, critical: float} |
| frequency | string enum | YES | continuous / hourly / daily / weekly / monthly |
| baseline | object | YES | {value: float, measured_at: date, conditions: string} |
| improvement | object | YES | {current: float, target: float, history: list} |
| cost | object | YES | {compute: float, time: float, risk: string} |
| risk | object | YES | {level: enum[low,medium,high], mitigation: string} |
| monitoring | object | YES | {dashboard: string, alerts: list, reporting: string} |
## Body Structure (required sections)
1. ## Target Process — scope, boundaries, what is being optimized
2. ## Metrics — primary metric, secondary metrics, thresholds
3. ## Actions — triggers, strategies, automation level
4. ## Risk Assessment — cost, side effects, rollback plan
5. ## Monitoring — dashboards, alerts, reporting cadence
## Constraints
- max_bytes: 4096 (body only)
- naming: p11_opt_{target_slug}.md
- id == filename stem
- threshold.trigger < threshold.target < threshold.critical (direction: minimize) OR reversed (maximize)
- improvement.history is list of {date, value} entries
- quality: null always
- metric.direction determines threshold ordering

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.64 |
| [[bld_schema_bugloop]] | sibling | 0.64 |
| [[bld_schema_dataset_card]] | sibling | 0.63 |
| [[bld_schema_reranker_config]] | sibling | 0.62 |
| [[bld_schema_unit_eval]] | sibling | 0.62 |
| [[bld_schema_quickstart_guide]] | sibling | 0.61 |
| [[bld_schema_safety_policy]] | sibling | 0.61 |
| [[bld_schema_search_strategy]] | sibling | 0.61 |
| [[bld_schema_input_schema]] | sibling | 0.61 |
| [[bld_schema_pitch_deck]] | sibling | 0.61 |
