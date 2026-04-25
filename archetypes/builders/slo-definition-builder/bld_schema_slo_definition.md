---
quality: 8.3
quality: 7.9
id: bld_schema_slo_definition
kind: schema
pillar: P06
llm_function: CONSTRAIN
purpose: "Formal schema -- SINGLE SOURCE OF TRUTH for slo_definition"
title: "Schema: slo_definition"
version: "1.0.0"
author: builder
tags: [schema, slo_definition, P09]
domain: "reliability configuration"
created: "2026-04-17"
updated: "2026-04-17"
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for slo_definition"
density_score: null
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_quickstart_guide
  - bld_schema_pitch_deck
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_bugloop
  - bld_schema_action_paradigm
  - bld_schema_sandbox_config
---

# Schema: slo_definition

## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_slo_{name_slug}) | YES | - | Namespace compliance |
| kind | literal "slo_definition" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Version |
| service_name | string | YES | - | Service or agent governed by this SLO |
| sli_type | enum: availability, latency, error_rate, throughput, saturation | YES | - | What is measured |
| target_percent | float (50.0-100.0 exclusive) | YES | - | Target threshold |
| window_days | integer | YES | 30 | Rolling window |
| error_budget_minutes | float | YES | - | Derived: (1-target/100)*window*24*60 |
| error_budget_policy | enum: block_deploy, alert_only, auto_rollback | YES | alert_only | Budget exhaustion action |
| owner | string | YES | - | Team or nucleus responsible |
| domain | string | YES | - | Service domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "slo_definition" |
| tldr | string <= 160ch | YES | - | Dense summary |

## ID Pattern
Regex: `^p09_slo_[a-z][a-z0-9_]+$`

## Body Structure (required sections)
1. `## SLI Definition` -- metric, measurement method, denominator
2. `## Target` -- target_percent, window, derived error budget
3. `## Error Budget` -- budget math table, burn rate thresholds
4. `## Alerting Policy` -- alert conditions, owner escalation

## Constraints
- max_bytes: 3072
- naming: p09_slo_{name_slug}.md
- target_percent must be < 100.0 (100% SLO is unachievable)
- error_budget_minutes must be computed, not guessed
- quality: null always

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.67 |
| [[bld_schema_usage_report]] | sibling | 0.66 |
| [[bld_schema_dataset_card]] | sibling | 0.64 |
| [[bld_schema_quickstart_guide]] | sibling | 0.64 |
| [[bld_schema_pitch_deck]] | sibling | 0.64 |
| [[bld_schema_benchmark_suite]] | sibling | 0.63 |
| [[bld_schema_integration_guide]] | sibling | 0.63 |
| [[bld_schema_bugloop]] | sibling | 0.63 |
| [[bld_schema_action_paradigm]] | sibling | 0.62 |
| [[bld_schema_sandbox_config]] | sibling | 0.62 |
