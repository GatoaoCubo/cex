---
kind: schema
id: bld_schema_cost_budget
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for cost_budget
pattern: TEMPLATE derives from this. CONFIG restricts this.
quality: 9.0
title: "Schema Cost Budget"
version: "1.0.0"
author: n03_builder
tags: [cost_budget, builder, schema, P09, spend-tracking]
tldr: "Formal schema for cost_budget: budget limits, alert thresholds, reset policy, and provider/model scope."
domain: "cost budget construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Schema: cost_budget
## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_cb_{name_slug}) | YES | - | Namespace compliance |
| kind | literal "cost_budget" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Artifact versioning |
| created | date YYYY-MM-DD | YES | - | Creation date |
| updated | date YYYY-MM-DD | YES | - | Last update |
| author | string | YES | - | Producer identity |
| scope | string | YES | - | Budget scope: global, provider name, or model slug |
| providers | list[string], len >= 1 | YES | - | Providers covered by this budget |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "cost_budget" |
| tldr | string <= 160ch | YES | - | Dense summary |
| description | string <= 200ch | REC | - | What this budget governs |
| currency | enum: USD, token_units | REC | USD | Budget unit |
| reset_policy | enum: daily, weekly, monthly, rolling_7d, rolling_30d, none | REC | monthly | When counters reset |
| alert_enabled | boolean | REC | true | Whether alerts fire |
| total_budget | number | REC | - | Top-level budget cap |
| overage_action | enum: block, warn, log | REC | warn | What happens on breach |
## ID Pattern
Regex: `^p09_cb_[a-z][a-z0-9_]+$`
Rule: id MUST equal filename stem.
## Body Structure (required sections)
1. `## Overview` -- what scope, why these limits, who enforces them
2. `## Budget Catalog` -- table: provider, model, token_limit, usd_limit, alert_threshold, reset_policy
3. `## Alert Policy` -- thresholds, channels, escalation path
4. `## Overage Rules` -- what happens when limit is hit (block/warn/log), grace period
## Constraints
- max_bytes: 3072 (body only)
- naming: p09_cb_{name_slug}.yaml
- machine_format: yaml (compiled artifact)
- id == filename stem
- providers list MUST match provider entries in Budget Catalog
- quality: null always
- NEVER include actual API keys or billing credentials
