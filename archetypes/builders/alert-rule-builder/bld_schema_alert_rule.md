---
quality: 7.6
id: bld_schema_alert_rule
kind: input_schema
pillar: P06
llm_function: CONSTRAIN
version: 1.0.0
quality: 7.1
tags: [alert_rule, schema, prometheus]
title: "Schema Alert Rule"
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - bld_schema_usage_report
  - bld_schema_pitch_deck
  - bld_schema_reranker_config
  - bld_schema_sandbox_config
  - bld_schema_quickstart_guide
  - bld_schema_benchmark_suite
  - bld_schema_dataset_card
  - bld_schema_audit_log
  - bld_schema_safety_policy
  - bld_schema_action_paradigm
---
# Schema: alert_rule
## Frontmatter Fields (Required)
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| id | string (ar_{sys}_{metric}) | YES | snake_case |
| kind | literal "alert_rule" | YES | — |
| pillar | literal "P09" | YES | — |
| title | string | YES | Human-readable alert name |
| version | semver | YES | 1.0.0 start |
| quality | null | YES | Never self-score |
| alert_name | string (PascalCase) | YES | Prometheus alert name |
| severity | enum | YES | critical|warning|info |
| for_duration | ISO duration | YES | "0s", "1m", "5m", "15m", "1h" |
| metric_expression | string | YES | PromQL or logical expression |
| routing | string | YES | Team/channel/policy/webhook |
| tags | list[string] | YES | >= 3 tags |

## Optional Fields
| Field | Type | Notes |
|-------|------|-------|
| runbook_url | URL | Link to remediation procedure |
| automated_response | string | Auto-action: restart, scale, rollback |
| labels | map[string] | Prometheus labels for routing |
| annotations | map[string] | summary, description for Alertmanager |
| inhibit_rules | list | Suppress lower severity if critical fires |

## ID Pattern
`^ar_[a-z][a-z0-9_]+$`
Example: ar_api_error_rate_high, ar_db_latency_critical, ar_disk_usage_warning

## Severity Definitions
| Level | Meaning | for_duration recommendation |
|-------|---------|---------------------------|
| critical | Immediate action, page on-call | 0s - 2m |
| warning | Attention needed, create ticket | 5m - 15m |
| info | Log for awareness, no action needed | 15m+ |

## Constraints
- max_bytes: 2048
- metric_expression must contain a numeric threshold
- for_duration must be ISO 8601 duration (PT1M not 1min)

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
| [[bld_schema_usage_report]] | related | 0.65 |
| [[bld_schema_pitch_deck]] | related | 0.64 |
| [[bld_schema_reranker_config]] | related | 0.64 |
| [[bld_schema_sandbox_config]] | related | 0.63 |
| [[bld_schema_quickstart_guide]] | related | 0.63 |
| [[bld_schema_benchmark_suite]] | related | 0.63 |
| [[bld_schema_dataset_card]] | related | 0.62 |
| [[bld_schema_audit_log]] | related | 0.61 |
| [[bld_schema_safety_policy]] | related | 0.61 |
| [[bld_schema_action_paradigm]] | related | 0.60 |
