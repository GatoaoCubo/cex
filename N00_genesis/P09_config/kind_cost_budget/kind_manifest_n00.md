---
id: n00_cost_budget_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Cost Budget -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, cost_budget, p09, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A cost_budget defines token budget allocations, spend tracking thresholds, and cost alert rules for LLM operations. It governs how much compute each nucleus or mission may consume, enforces hard caps to prevent runaway costs, and triggers alerts when spending approaches configured limits.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `cost_budget` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable budget name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| scope | string | yes | What this budget covers (nucleus, mission, global) |
| max_tokens_per_call | integer | yes | Hard cap on tokens per individual LLM call |
| max_tokens_per_day | integer | yes | Daily token spend ceiling |
| alert_threshold_pct | integer | yes | Alert when usage reaches this % of max (0-100) |
| hard_cap | boolean | no | If true, block calls that exceed budget (default false) |
| model_costs | object | no | Per-model cost per million tokens (input/output) |
| track_by | enum | no | nucleus \| mission \| kind \| global |

## When to use
- Setting spend guardrails for an overnight autonomous mission
- Allocating token budgets per nucleus to prevent one nucleus from starving others
- Enforcing cost discipline during high-volume batch or evolve operations

## Builder
`archetypes/builders/cost_budget-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind cost_budget --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: cost_budget_mission_default
kind: cost_budget
pillar: P09
nucleus: n07
title: "Default Mission Cost Budget"
version: 1.0
quality: null
---
scope: mission
max_tokens_per_call: 100000
max_tokens_per_day: 5000000
alert_threshold_pct: 80
hard_cap: false
track_by: nucleus
```

## Related kinds
- `usage_quota` (P09) -- quota enforcement that pairs with cost_budget alerts
- `rate_limit_config` (P09) -- rate limits that naturally constrain spend
- `thinking_config` (P09) -- extended thinking budget tokens that contribute to cost
