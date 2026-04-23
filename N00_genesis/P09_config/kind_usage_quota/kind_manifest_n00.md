---
id: n00_usage_quota_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Usage Quota -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, usage_quota, p09, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_usage_quota
  - bld_schema_rate_limit_config
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_sandbox_spec
  - bld_schema_sandbox_config
  - bld_schema_dataset_card
  - bld_schema_thinking_config
  - bld_schema_integration_guide
  - bld_schema_playground_config
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A usage_quota defines per-user or per-tenant fair-use enforcement limits: how many requests, artifacts, or tokens a given subject may consume within a period. It enables multi-tenant CEX deployments to prevent any single customer from monopolizing shared resources and provides the quota data that billing and upgrade prompts depend on.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `usage_quota` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable quota name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| subject | enum | yes | user \| tenant \| nucleus \| plan_tier |
| period | enum | yes | minute \| hour \| day \| month |
| limits | object | yes | Named limit definitions |
| limits.requests | integer | no | Max API requests per period |
| limits.tokens | integer | no | Max tokens per period |
| limits.artifacts | integer | no | Max artifacts created per period |
| on_exceed | enum | yes | block \| throttle \| alert |
| reset_at | string | no | When the quota resets (e.g. UTC midnight) |
| grace_pct | integer | no | Soft limit percentage before hard block (default 90) |

## When to use
- Enforcing fair-use across tenants in a multi-tenant SaaS deployment
- Setting usage limits for different pricing tiers (free vs. pro vs. enterprise)
- Preventing runaway automation from consuming all available capacity

## Builder
`archetypes/builders/usage_quota-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind usage_quota --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: usage_quota_free_tier
kind: usage_quota
pillar: P09
nucleus: n06
title: "Free Tier Monthly Usage Quota"
version: 1.0
quality: null
---
subject: plan_tier
period: month
limits:
  requests: 500
  tokens: 1000000
  artifacts: 50
on_exceed: throttle
reset_at: "UTC 00:00 first of month"
grace_pct: 90
```

## Related kinds
- `rate_limit_config` (P09) -- per-minute rate limits that complement monthly quotas
- `cost_budget` (P09) -- token budgets that overlap with token quotas
- `feature_flag` (P09) -- flags that enable quota upgrades for specific users

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_quota]] | upstream | 0.43 |
| [[bld_schema_rate_limit_config]] | upstream | 0.37 |
| [[bld_schema_reranker_config]] | upstream | 0.37 |
| [[bld_schema_usage_report]] | upstream | 0.37 |
| [[bld_schema_sandbox_spec]] | upstream | 0.37 |
| [[bld_schema_sandbox_config]] | upstream | 0.37 |
| [[bld_schema_dataset_card]] | upstream | 0.36 |
| [[bld_schema_thinking_config]] | upstream | 0.36 |
| [[bld_schema_integration_guide]] | upstream | 0.35 |
| [[bld_schema_playground_config]] | upstream | 0.35 |
