---
quality: 8.0
quality: 7.7
id: bld_instruction_canary_config
kind: instruction
pillar: P09
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
title: "Canary Config Builder Instructions"
target: "canary-config-builder agent"
phases_count: 4
prerequisites:
  - "Deployment target and service name are identified"
  - "Traffic stages are defined or can be derived"
  - "Rollback metric and threshold are known"
tags: [instruction, canary_config, P09, rollout]
llm_function: REASON
tldr: "Build a canary_config with traffic stages, analysis intervals, and rollback trigger configuration."
density_score: null
related:
  - p01_kc_cicd_llm_pipeline
  - bld_schema_e2e_eval
  - p06_is_creation_data
  - bld_schema_model_registry
  - bld_schema_experiment_tracker
  - bld_instruction_instruction
  - bld_schema_instruction
  - bld_instruction_kind
  - p06_is_quality_audit
  - bld_schema_eval_metric
---
## Context
The canary-config-builder produces a `canary_config` -- a progressive delivery specification that shifts traffic incrementally from stable to canary version with automatic rollback if metrics breach thresholds. NOT feature_flag (boolean toggle), NOT ab_test_config (statistical experiment), NOT deployment_manifest (artifact list).

**Input contract**:
- `service_name`: string -- service being deployed
- `canary_version`: string -- the new version being rolled out
- `stable_version`: string -- the currently running version
- `stages`: list -- each with traffic_percent, pause_duration_minutes
- `rollback_trigger_metric`: string -- metric name
- `rollback_trigger_threshold`: float -- breach value that triggers rollback

## Phases

### Phase 1: Define Traffic Stages
Standard canary progression: 5% -> 25% -> 50% -> 100%.
Each stage:
- `traffic_percent`: int (canary receives this %)
- `pause_duration_minutes`: how long to hold before advancing
- `analysis_interval_minutes`: how often to evaluate metrics during this stage

### Phase 2: Define Rollback Triggers
Conditions that cause automatic rollback to stable_version:
- `error_rate_threshold`: if canary error rate > X%
- `latency_p99_threshold_ms`: if canary p99 latency > X ms
- `slo_breach`: reference to slo_definition id

### Phase 3: Define Analysis Method
- `provider`: Argo Rollouts | Flagger | custom
- `metric_provider`: Prometheus | DataDog | CloudWatch
- `success_condition`: formula to evaluate metric (e.g. `result < 0.05`)

### Phase 4: Compose Artifact
Required frontmatter: id, kind, pillar, service_name, canary_version, stable_version, stages_count, quality: null.
Required body: Traffic Stages, Rollback Triggers, Analysis Configuration.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cicd_llm_pipeline]] | upstream | 0.21 |
| [[bld_schema_e2e_eval]] | upstream | 0.20 |
| [[p06_is_creation_data]] | upstream | 0.19 |
| [[bld_schema_model_registry]] | upstream | 0.19 |
| [[bld_schema_experiment_tracker]] | upstream | 0.18 |
| [[bld_instruction_instruction]] | sibling | 0.18 |
| [[bld_schema_instruction]] | upstream | 0.18 |
| [[bld_instruction_kind]] | sibling | 0.18 |
| [[p06_is_quality_audit]] | upstream | 0.17 |
| [[bld_schema_eval_metric]] | upstream | 0.17 |
