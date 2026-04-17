---
id: kc_canary_config
kind: knowledge_card
pillar: P01
nucleus: n00
domain: kind-taxonomy
quality: null
tags: [kind, taxonomy, canary_config, P09, config, deployment]
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

## Quality Criteria
- GOOD: stages with traffic_percent, rollback_trigger_metric, canary/stable versions pinned
- GREAT: analysis_interval_minutes per stage, pause_duration_minutes, success_condition explicit
- FAIL: Single stage at 100%, no rollback trigger, "latest" version
