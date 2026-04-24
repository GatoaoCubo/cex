---
id: p06_is_api_contract
kind: input_schema
8f: F1_constrain
pillar: P06
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "n05_operations"
scope: "CEX infrastructure operations API: deploy, monitor, scale, health-check, rollback"
fields:
  - name: "endpoint"
    type: "string"
    required: true
    default: null
    description: "Target operation: deploy | monitor | scale | health_check"
    error_message: "endpoint is required -- must be deploy|monitor|scale|health_check"
  - name: "nucleus_id"
    type: "string"
    required: true
    default: null
    description: "Nucleus identifier: n01..n07"
    error_message: "nucleus_id is required -- must be n01..n07"
  - name: "environment"
    type: "string"
    required: false
    default: "staging"
    description: "Deploy target environment: staging | prod"
    error_message: "environment must be staging or prod"
  - name: "artifact_paths"
    type: "list"
    required: false
    default: null
    description: "List of artifact file paths to deploy (deploy endpoint only)"
    error_message: "artifact_paths must be a list of strings"
  - name: "rollback_on_fail"
    type: "boolean"
    required: false
    default: true
    description: "Auto-rollback if deploy gate fails (deploy endpoint only)"
    error_message: null
  - name: "metric_type"
    type: "string"
    required: false
    default: "health"
    description: "Metric to collect: health | latency | error_rate (monitor endpoint only)"
    error_message: "metric_type must be health|latency|error_rate"
  - name: "interval_seconds"
    type: "integer"
    required: false
    default: 60
    description: "Polling interval in seconds (monitor endpoint only, min 10)"
    error_message: "interval_seconds must be integer >= 10"
  - name: "target_replicas"
    type: "integer"
    required: false
    default: null
    description: "Desired replica count (scale endpoint only, min 1)"
    error_message: "target_replicas is required for scale endpoint -- must be integer >= 1"
  - name: "max_budget_usd"
    type: "float"
    required: false
    default: null
    description: "Spend ceiling in USD (scale endpoint only)"
    error_message: "max_budget_usd must be a positive float"
  - name: "target"
    type: "string"
    required: false
    default: null
    description: "Check target: nucleus | tool | pipeline (health_check endpoint only)"
    error_message: "target must be nucleus|tool|pipeline"
  - name: "depth"
    type: "string"
    required: false
    default: "shallow"
    description: "Check depth: shallow | deep (health_check endpoint only)"
    error_message: "depth must be shallow or deep"
coercion:
  - from: "string"
    to: "integer"
    rule: "Parse interval_seconds and target_replicas from string if numeric, reject if non-numeric"
  - from: "string"
    to: "float"
    rule: "Parse max_budget_usd from string if numeric, reject if non-numeric"
  - from: "string"
    to: "boolean"
    rule: "Parse rollback_on_fail: 'true'/'1' -> true, 'false'/'0' -> false, reject all other strings"
examples:
  - {endpoint: "deploy", nucleus_id: "n03", environment: "staging", artifact_paths: ["N03_engineering/P06_schema/p06_is_agent.md"], rollback_on_fail: true}
  - {endpoint: "monitor", nucleus_id: "n05", metric_type: "error_rate", interval_seconds: 30}
  - {endpoint: "scale", nucleus_id: "n01", target_replicas: 3, max_budget_usd: 5.00}
  - {endpoint: "health_check", target: "pipeline", depth: "deep"}
domain: "infrastructure"
quality: 9.2
tags: [input-schema, infrastructure, cicd, deploy, monitor, scale, health-check, N05, operations]
tldr: "Input contract for CEX ops API: deploy/monitor/scale/health-check endpoints. Enforces nucleus_id, environment, metric, replica, and depth gates."
keywords: [deploy, monitor, scale, health_check, nucleus_id, rollback, replica, budget, pipeline, cicd]
density_score: 0.92
related:
  - bld_schema_input_schema
  - bld_schema_validation_schema
  - bld_schema_api_reference
  - bld_schema_sandbox_config
  - bld_schema_nucleus_def
  - bld_schema_smoke_eval
  - bld_schema_usage_report
  - bld_schema_research_pipeline
  - bld_schema_reranker_config
  - bld_schema_dataset_card
---

## Contract Definition

CEX infrastructure operations API. Callers (N07, CI/CD hooks, cex_mission_runner.py) POST
to one of four endpoints. The `endpoint` field routes to the correct handler. Fields are
partitioned by endpoint -- each endpoint ignores fields outside its partition.

| Endpoint | Caller | Gate Enforcer |
|----------|--------|---------------|
| deploy | N07, dispatch.sh | N05 CI/CD gate: compile + doctor + quality >= 8.0 |
| monitor | N07, cex_signal_watch.py | N05 metrics collector: latency, error rate, health |
| scale | N07 (budget-aware dispatch) | N05 budget gate: max_budget_usd hard ceiling |
| health_check | any nucleus, cex_doctor.py | N05 Gating Wrath: shallow=ping, deep=full pipeline trace |

## Fields by Endpoint

### Common (all endpoints)

| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 1 | endpoint | `string` | YES | - | deploy\|monitor\|scale\|health_check |
| 2 | nucleus_id | `string` | YES* | - | n01..n07 (*not required for health_check) |

### deploy

| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 3 | environment | `string` | NO | staging | staging\|prod |
| 4 | artifact_paths | `list` | NO | null | Paths to artifacts being deployed |
| 5 | rollback_on_fail | `boolean` | NO | true | Auto-rollback if gate fails |

### monitor

| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 6 | metric_type | `string` | NO | health | health\|latency\|error_rate |
| 7 | interval_seconds | `integer` | NO | 60 | Poll interval, min 10 |

### scale

| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 8 | target_replicas | `integer` | YES | - | Replica count, min 1 |
| 9 | max_budget_usd | `float` | YES | - | Spend ceiling USD |

### health_check

| # | Name | Type | Required | Default | Description |
|---|------|------|----------|---------|-------------|
| 10 | target | `string` | YES | - | nucleus\|tool\|pipeline |
| 11 | depth | `string` | NO | shallow | shallow\|deep |

## Coercion Rules

| From | To | Rule |
|------|----|------|
| `string` | `integer` | Parse interval_seconds, target_replicas -- reject if non-numeric |
| `string` | `float` | Parse max_budget_usd -- reject if non-numeric |
| `string` | `boolean` | rollback_on_fail: true/1 -> true, false/0 -> false, else reject |

## Examples

```json
{"endpoint": "deploy", "nucleus_id": "n03", "environment": "staging",
 "artifact_paths": ["N03_engineering/P06_schema/p06_is_agent.md"],
 "rollback_on_fail": true}
```

```json
{"endpoint": "monitor", "nucleus_id": "n05", "metric_type": "error_rate", "interval_seconds": 30}
```

```json
{"endpoint": "scale", "nucleus_id": "n01", "target_replicas": 3, "max_budget_usd": 5.00}
```

```json
{"endpoint": "health_check", "target": "pipeline", "depth": "deep"}
```

## References

1. `N05_operations/P06_schema/health_check_schema.md` -- health response shape
2. `N05_operations/P06_schema/api_response_contract.md` -- response envelope format
3. `.cex/config/nucleus_models.yaml` -- nucleus_id registry

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_input_schema]] | related | 0.35 |
| [[bld_schema_validation_schema]] | related | 0.33 |
| [[bld_schema_api_reference]] | related | 0.33 |
| [[bld_schema_sandbox_config]] | related | 0.31 |
| [[bld_schema_nucleus_def]] | related | 0.30 |
| [[bld_schema_smoke_eval]] | related | 0.30 |
| [[bld_schema_usage_report]] | related | 0.30 |
| [[bld_schema_research_pipeline]] | related | 0.30 |
| [[bld_schema_reranker_config]] | related | 0.30 |
| [[bld_schema_dataset_card]] | related | 0.29 |
