---
quality: null
id: kc_slo_definition
kind: knowledge_card
8f: F3_inject
title: "SLO Definition: Service Level Objectives with Error Budgets"
tldr: "Measurable reliability targets expressed as percentages over rolling time windows, with error budget policies gating deployments"
version: 1.1.0
pillar: P01
nucleus: n00
domain: kind-taxonomy
tags: [kind, taxonomy, slo_definition, P09, reliability]
density_score: 0.93
updated: "2026-04-22"
related:
  - bld_knowledge_card_enterprise_sla
  - p03_sp_enterprise_sla_builder
  - enterprise-sla-builder
  - bld_tools_enterprise_sla
  - p11_qg_enterprise_sla
  - bld_examples_enterprise_sla
  - p10_mem_enterprise_sla_builder
  - bld_collaboration_cost_budget
  - cost-budget-builder
  - p03_sp_cost_budget_builder
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

## Error Budget Table by Target

| SLO Target | Allowed Downtime / 30d | Allowed Downtime / 90d | Allowed Downtime / 365d | Typical Use |
|------------|----------------------|----------------------|------------------------|-------------|
| 99.0% | 7h 12m | 21h 36m | 3d 15h 36m | Internal tools, batch jobs |
| 99.5% | 3h 36m | 10h 48m | 1d 19h 48m | Non-critical APIs |
| 99.9% | 43.2m | 2h 9.6m | 8h 45.6m | Production APIs, user-facing |
| 99.95% | 21.6m | 1h 4.8m | 4h 22.8m | High-traffic services |
| 99.99% | 4.32m | 12.96m | 52.56m | Payment processing, auth |
| 99.999% | 25.9s | 1.3m | 5.26m | Core infra (DNS, load balancer) |

## Concrete SLO/SLI Examples

### Example 1: API Availability SLO

```yaml
# p09_slo_api_gateway_availability.md
---
id: p09_slo_api_gateway_availability
kind: slo_definition
pillar: P09
service_name: "api-gateway"
sli_type: availability
target_percent: 99.9
window_days: 30
error_budget_minutes: 43.2
error_budget_policy: block_deploy
owner: "platform-team"
quality: null
---

## SLI Definition
metric: sum(rate(http_requests_total{code!~"5.."}[5m])) / sum(rate(http_requests_total[5m]))
denominator: all HTTP requests
measurement: ratio of non-5xx responses to total responses

## Error Budget Policy
- budget > 50% remaining: deploy freely
- budget 20-50% remaining: deploy with canary only
- budget < 20% remaining: block all deploys, page on-call
- budget exhausted: freeze deploys until budget replenishes at window rollover
```

### Example 2: Latency SLO

```yaml
# p09_slo_search_latency.md
---
id: p09_slo_search_latency
kind: slo_definition
pillar: P09
service_name: "search-service"
sli_type: latency
target_percent: 99.0
window_days: 30
error_budget_minutes: 432.0
error_budget_policy: alert_only
owner: "search-team"
quality: null
---

## SLI Definition
metric: histogram_quantile(0.99, rate(search_duration_seconds_bucket[5m]))
threshold: 200ms
measurement: proportion of requests completing under 200ms at p99
```

## SLO vs SLA vs SLI Hierarchy

| Concept | Definition | Owner | Consequence of Breach |
|---------|-----------|-------|-----------------------|
| **SLI** (Service Level Indicator) | The metric itself (e.g., error_rate, p99 latency) | Engineering | Signal for investigation |
| **SLO** (Service Level Objective) | Internal target for the SLI (e.g., 99.9% availability) | Engineering + Product | Error budget consumption, deploy gates |
| **SLA** (Service Level Agreement) | External contractual commitment (SLO + penalties) | Business + Legal | Financial penalties, credits, contract breach |

Relationship: SLA >= SLO (always set SLO tighter than SLA to have a safety margin).

## Quality Criteria
- GOOD: target_percent set, error_budget_minutes computed, sli_type specified
- GREAT: SLI metric query explicit, burn rate thresholds defined, owner set
- FAIL: target_percent = 100, error_budget_minutes missing, no error_budget_policy

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_enterprise_sla]] | sibling | 0.39 |
| [[p03_sp_enterprise_sla_builder]] | downstream | 0.24 |
| [[enterprise-sla-builder]] | downstream | 0.24 |
| [[bld_tools_enterprise_sla]] | downstream | 0.23 |
| [[p11_qg_enterprise_sla]] | downstream | 0.22 |
| [[bld_examples_enterprise_sla]] | downstream | 0.19 |
| [[p10_mem_enterprise_sla_builder]] | downstream | 0.17 |
| [[bld_collaboration_cost_budget]] | downstream | 0.17 |
| [[cost-budget-builder]] | downstream | 0.16 |
| [[p03_sp_cost_budget_builder]] | downstream | 0.16 |
