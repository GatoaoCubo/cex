---
id: kc_slo_definition
kind: knowledge_card
pillar: P01
nucleus: n00
domain: kind-taxonomy
quality: 7.9
tags: [kind, taxonomy, slo_definition, P09, reliability]
density_score: 1.0
updated: "2026-04-17"
---

# slo_definition

## Spec
```yaml
kind: slo_definition
pillar: P09
llm_function: GOVERN
max_bytes: 3072
naming: p09_slo_{{name}}.md + .yaml
core: false
```

## What It Is
A service level objective (SLO) is a measurable target for a system's reliability, expressed as a percentage over a rolling time window. The gap between 100% and the target is the **error budget** -- the amount of allowed unreliability. SLOs are the internal engineering commitment; SLAs are external contractual commitments.

Origin: Google SRE book (2016). Industry: Prometheus recording rules, DataDog SLO monitors, Honeycomb SLO widgets.

It is NOT:
- `enterprise_sla` (contractual SLA with external parties -- includes penalties, is legally binding)
- `quality_gate` (build-time artifact scoring -- governs CI/CD, not runtime reliability)
- `benchmark` (point-in-time performance measurement -- not an ongoing target)

## When to Use
- Defining reliability targets for a service, API, or agent
- Setting error budget policies that gate deployments
- Configuring burn-rate alerting for on-call teams
- Documenting service reliability commitments for internal stakeholders

## When NOT to Use
- Contractual commitments to customers -> use `enterprise_sla`
- Build-time quality gates -> use `quality_gate`
- One-time performance measurements -> use `benchmark`
- Availability tracking of a third-party dependency -> use `dependency_health` (future kind)

## Structure
```yaml
# Required frontmatter fields
id: p09_slo_{name_slug}
kind: slo_definition
pillar: P09
service_name: "..."
sli_type: availability | latency | error_rate | throughput | saturation
target_percent: 99.9     # must be < 100.0
window_days: 30
error_budget_minutes: 43.2  # = (1 - target/100) * window_days * 1440
error_budget_policy: block_deploy | alert_only | auto_rollback
owner: "..."
quality: null
```

```markdown
## SLI Definition
Metric query, denominator, measurement method

## Target
target_percent, window_days, derived error_budget_minutes

## Error Budget
Budget math table, fast-burn (1h, 14x) and slow-burn (6h, 6x) thresholds

## Alerting Policy
Page conditions, ticket conditions, owner escalation
```

## Error Budget Math
```
error_budget_seconds = (1 - target_percent/100) * window_days * 86400
error_budget_minutes = error_budget_seconds / 60

Example: 99.9% over 30 days
= 0.001 * 30 * 1440 = 43.2 minutes of allowed downtime
```

## Burn Rate Alerting (Google SRE Standard)
| Alert | Window | Burn Rate | Budget Consumed |
|-------|--------|-----------|----------------|
| Fast burn (page) | 1h | 14x | 2% in 1h |
| Slow burn (ticket) | 6h | 6x | 5% in 6h |

## SLI Types
| Type | What Is Measured | Example |
|------|-----------------|---------|
| availability | good_requests / total | HTTP 200s / all requests |
| latency | requests_under_threshold / total | p99 < 200ms |
| error_rate | bad_requests / total | 5xx / all requests |
| throughput | successful_ops / time | successful writes per second |
| saturation | used / capacity | CPU utilization |

## Relationships
```
[deployment_manifest] --> [slo_definition] --> [trace_config]
[canary_config] --------^  (rollback trigger signal)
[slo_definition] --> [signal: slo_breach]
```

## Decision Tree
- IF target_percent = 100 -> REJECT: 100% is unachievable; use 99.99% max
- IF no error_budget_policy -> BLOCK: require alert_only at minimum
- IF user conflates with SLA -> TEACH: SLA >= SLO; SLA has external penalties
- DEFAULT: 99.9% availability over 30d for new services; refine with actual data

## Quality Criteria
- GOOD: target_percent set, error_budget_minutes computed, sli_type specified
- GREAT: SLI metric query explicit, burn rate thresholds defined, owner set
- FAIL: target_percent = 100, error_budget_minutes missing, no error_budget_policy
