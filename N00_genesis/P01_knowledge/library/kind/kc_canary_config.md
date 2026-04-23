---
quality: null
id: kc_canary_config
kind: knowledge_card
title: "Canary Config: Progressive Traffic Rollout Strategy"
tldr: "Gradual traffic shifting with metric-gated stages, automatic rollback on threshold breach, and multi-platform deployment support"
version: 1.1.0
pillar: P01
nucleus: n00
domain: kind-taxonomy
tags: [kind, taxonomy, canary_config, P09, config, deployment]
density_score: 0.93
updated: "2026-04-22"
related:
  - p01_kc_experiment_config
  - experiment-config-builder
  - p01_kc_cicd_llm_pipeline
  - p11_qg_experiment_config
  - p03_sp_experiment_config_builder
  - ab-test-config-builder
  - bld_knowledge_card_experiment_config
  - bld_instruction_experiment_config
  - p10_lr_experiment_config_builder
  - p10_lr_e2e_eval_builder
---

# canary_config

## Spec
```yaml
kind: canary_config
pillar: P09
llm_function: GOVERN
max_bytes: 2048
naming: p09_cc_{{name}}.md + .yaml
core: false
```

## What It Is
A canary_config specifies a gradual traffic rollout strategy: the new version starts receiving a small percentage of traffic (e.g., 5%), observed against defined metrics, and either progresses to higher traffic percentages or rolls back to the stable version if metrics breach thresholds. Named after the "canary in a coal mine" safety practice.

Industry: Argo Rollouts (Kubernetes), Flagger (Kubernetes + service mesh), AWS CodeDeploy (Lambda/EC2), GCP Traffic Director.

It is NOT:
- `feature_flag` (boolean feature toggle -- on/off for specific users; not traffic split)
- `ab_test_config` (statistical experiment -- uses significance testing, hypothesis comparison)
- `deployment_manifest` (artifact specification -- defines what to deploy; canary_config defines how to shift traffic)

## When to Use
- Deploying a new service version to production with risk mitigation
- Progressive delivery where metrics gate advancement to higher traffic
- When automatic rollback on metric breach is required
- Any deployment where "blast radius" must be minimized

## When NOT to Use
- Toggling a feature for specific users -> use `feature_flag`
- Running a controlled A/B experiment with statistical analysis -> use `ab_test_config`
- Deploying to a test/ephemeral environment -> use `sandbox_spec`
- Simple blue-green (instant traffic swap) -> use `deployment_manifest` with swap strategy

## Structure
```yaml
# Required frontmatter fields
id: p09_cc_{name_slug}
kind: canary_config
pillar: P09
service_name: "..."
canary_version: "..."   # must be pinned
stable_version: "..."   # must be pinned
stages_count: N
rollback_trigger_metric: "..."
rollback_trigger_threshold: 0.01
provider: argo_rollouts | flagger | aws_codedeploy | custom
quality: null
```

```markdown
## Traffic Stages
Table: stage, traffic_percent, pause_duration_minutes, analysis_interval_minutes
(First stage < 50%, last stage = 100%)

## Rollback Triggers
Metric name, threshold, action

## Analysis Configuration
Provider, metric_provider, success_condition
```

## Standard Traffic Progression
| Stage | Canary % | Pause | Why |
|-------|---------|-------|-----|
| Initial | 5% | 10 min | Low blast radius; detect catastrophic failures |
| Phase 1 | 25% | 15 min | Broader validation; latency/error patterns |
| Phase 2 | 50% | 20 min | Equal split; final validation before full |
| Complete | 100% | - | Promotion complete |

## Rollback Trigger Metrics
| Metric | Typical Threshold | Platform |
|--------|-----------------|---------|
| error_rate | > 1% (0.01) | Prometheus, DataDog |
| latency_p99_ms | > 500 | Prometheus histogram |
| success_rate | < 0.99 | DataDog |
| slo_breach | any | Link to slo_definition |

## Relationships
```
[deployment_manifest] --> [canary_config] --> [slo_definition] (rollback signal)
                               |
                               +--> [trace_config] (metric source)
                               +--> [signal: canary_promoted | canary_rolled_back]
```

## Decision Tree
- IF first stage >= 50% -> REJECT: start lower; explain blast radius
- IF no rollback_trigger_metric -> BLOCK: add metric threshold
- IF user wants boolean toggle -> redirect to feature_flag
- IF user wants statistical significance -> redirect to ab_test_config
- DEFAULT: 5->25->50->100% progression; error_rate > 1% rollback trigger

## Deployment Strategy Comparison

| Strategy | Traffic Shift | Rollback Speed | Risk Level | Infra Cost | Best For |
|----------|--------------|----------------|-----------|------------|----------|
| **Canary** | Gradual % | Fast (shift back) | Low | Medium (2 versions) | High-traffic services, metric-gated |
| **Blue-Green** | Instant 100% swap | Instant (swap back) | Medium | High (2x infra) | Stateless apps, fast validation |
| **Rolling Update** | Pod-by-pod replacement | Slow (re-roll) | Medium | Low (in-place) | Kubernetes default, stateless pods |
| **Recreate** | Kill all, start new | None (downtime) | High | Low | Dev/staging, batch jobs |
| **A/B Testing** | Segment-based split | Fast (remove segment) | Low | Medium | Feature experiments, hypothesis testing |
| **Shadow/Dark** | Duplicate traffic, discard responses | N/A (no user impact) | Very Low | High (2x compute) | Performance validation, data pipeline testing |

## Concrete Canary Configuration Example

```yaml
# p09_cc_api_gateway_v2.md frontmatter
id: p09_cc_api_gateway_v2
kind: canary_config
pillar: P09
service_name: "api-gateway"
canary_version: "2.4.1"
stable_version: "2.3.8"
stages_count: 4
rollback_trigger_metric: "error_rate"
rollback_trigger_threshold: 0.01
provider: argo_rollouts
quality: null

# Body: Traffic Stages
# | Stage | Canary % | Pause (min) | Analysis Interval |
# |-------|---------|-------------|-------------------|
# | 1     | 5       | 10          | 5                 |
# | 2     | 25      | 15          | 5                 |
# | 3     | 50      | 20          | 10                |
# | 4     | 100     | -           | -                 |

# Rollback Triggers
# | Metric     | Threshold | Action         |
# |------------|-----------|----------------|
# | error_rate | > 0.01    | auto_rollback  |
# | p99_ms     | > 500     | pause + alert  |
# | cpu_util   | > 85%     | pause + alert  |
```

## Argo Rollouts Manifest (Kubernetes)

```yaml
apiVersion: argoproj.io/v1alpha1
kind: Rollout
metadata:
  name: api-gateway
spec:
  replicas: 10
  strategy:
    canary:
      steps:
        - setWeight: 5
        - pause: {duration: 10m}
        - setWeight: 25
        - pause: {duration: 15m}
        - setWeight: 50
        - pause: {duration: 20m}
        - setWeight: 100
      analysis:
        templates:
          - templateName: error-rate-check
        startingStep: 1
      rollbackWindow:
        revisions: 2
```

## Quality Criteria
- GOOD: stages with traffic_percent, rollback_trigger_metric, canary/stable versions pinned
- GREAT: analysis_interval_minutes per stage, pause_duration_minutes, success_condition explicit
- FAIL: Single stage at 100%, no rollback trigger, "latest" version

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_experiment_config]] | sibling | 0.30 |
| [[experiment-config-builder]] | downstream | 0.28 |
| [[p01_kc_cicd_llm_pipeline]] | sibling | 0.26 |
| [[p11_qg_experiment_config]] | downstream | 0.26 |
| [[p03_sp_experiment_config_builder]] | downstream | 0.24 |
| [[ab-test-config-builder]] | downstream | 0.23 |
| [[bld_knowledge_card_experiment_config]] | sibling | 0.23 |
| [[bld_instruction_experiment_config]] | downstream | 0.21 |
| [[p10_lr_experiment_config_builder]] | downstream | 0.21 |
| [[p10_lr_e2e_eval_builder]] | downstream | 0.20 |
