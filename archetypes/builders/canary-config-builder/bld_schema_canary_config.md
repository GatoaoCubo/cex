---
quality: 8.1
quality: 7.7
id: bld_schema_canary_config
kind: schema
pillar: P06
llm_function: CONSTRAIN
purpose: "Formal schema -- SINGLE SOURCE OF TRUTH for canary_config"
title: "Schema: canary_config"
version: "1.0.0"
author: builder
tags: [schema, canary_config, P09]
domain: "progressive delivery"
created: "2026-04-17"
updated: "2026-04-17"
density_score: null
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_pitch_deck
  - bld_schema_quickstart_guide
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
  - bld_schema_integration_guide
  - bld_schema_sandbox_config
  - bld_schema_sandbox_spec
  - bld_schema_search_strategy
---

# Schema: canary_config

## Frontmatter Fields
| Field | Type | Required | Default | Notes |
|-------|------|----------|---------|-------|
| id | string (p09_cc_{name_slug}) | YES | - | Namespace compliance |
| kind | literal "canary_config" | YES | - | Type integrity |
| pillar | literal "P09" | YES | - | Pillar assignment |
| version | semver string | YES | "1.0.0" | Version |
| service_name | string | YES | - | Service being canary deployed |
| canary_version | string | YES | - | New version being rolled out |
| stable_version | string | YES | - | Current stable version |
| stages_count | integer | YES | - | Must match stages list |
| rollback_trigger_metric | string | YES | - | Metric that triggers rollback |
| rollback_trigger_threshold | float | YES | - | Breach value |
| provider | enum: argo_rollouts, flagger, aws_codedeploy, custom | YES | argo_rollouts | Delivery platform |
| domain | string | YES | - | Service domain |
| quality | null | YES | null | Never self-score |
| tags | list[string], len >= 3 | YES | - | Must include "canary_config" |
| tldr | string <= 160ch | YES | - | Dense summary |

## ID Pattern
Regex: `^p09_cc_[a-z][a-z0-9_]+$`

## Body Structure
1. `## Traffic Stages` -- table: stage, traffic_percent, pause_duration_minutes, analysis_interval_minutes
2. `## Rollback Triggers` -- metric name, threshold, action
3. `## Analysis Configuration` -- provider, metric_provider, success_condition

## Constraints
- max_bytes: 2048
- naming: p09_cc_{name_slug}.md
- First stage traffic_percent MUST be < 50
- Last stage traffic_percent MUST be 100
- stages_count MUST match actual stages
- quality: null always

## Schema Validation Checklist

- Verify all required fields have type annotations
- Validate enum values against domain vocabulary
- Cross-reference with related schemas for consistency
- Test schema parsing with sample data before publishing

## Schema Pattern

```yaml
# Schema validation contract
types_annotated: true
enums_valid: true
cross_refs_checked: true
sample_data_tested: true
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_schema_hydrate.py --check
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.70 |
| [[bld_schema_usage_report]] | sibling | 0.70 |
| [[bld_schema_pitch_deck]] | sibling | 0.68 |
| [[bld_schema_quickstart_guide]] | sibling | 0.68 |
| [[bld_schema_benchmark_suite]] | sibling | 0.67 |
| [[bld_schema_dataset_card]] | sibling | 0.67 |
| [[bld_schema_integration_guide]] | sibling | 0.67 |
| [[bld_schema_sandbox_config]] | sibling | 0.66 |
| [[bld_schema_sandbox_spec]] | sibling | 0.65 |
| [[bld_schema_search_strategy]] | sibling | 0.65 |
