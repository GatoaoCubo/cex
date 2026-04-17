---
id: bld_examples_slo_definition
kind: knowledge_card
pillar: P01
title: "Examples: slo_definition"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: slo_definition
quality: 7.0
tags: [examples, slo_definition, P09]
llm_function: GOVERN
tldr: "Golden and anti-examples for slo_definition construction."
density_score: null
---

# Examples: slo_definition

## Golden Example
```yaml
---
id: p09_slo_cex_api_availability
kind: slo_definition
pillar: P09
version: 1.0.0
service_name: "CEX API"
sli_type: availability
target_percent: 99.9
window_days: 30
error_budget_minutes: 43.2
error_budget_policy: block_deploy
owner: "N05 Operations"
domain: cex-api
quality: null
tags: [slo_definition, cex-api, availability]
tldr: "CEX API availability SLO: 99.9% over 30d rolling window; blocks deploys on budget exhaustion"
---
## SLI Definition
- Type: availability
- Metric: `sum(rate(http_requests_total{code!~"5.."}[5m])) / sum(rate(http_requests_total[5m]))`
- Denominator: total HTTP requests
- Measurement: Prometheus recording rule, 5m evaluation interval

## Target
- Target: 99.9% over 30-day rolling window
- Error Budget: 43.2 minutes

## Error Budget
| Period | Allowed Downtime | Burn Rate Trigger |
|--------|-----------------|-------------------|
| 1h fast burn | 3.1m | 14x |
| 6h slow burn | 18.9m | 6x |

## Alerting Policy
- Page on: burn rate >= 14 over 1h
- Ticket on: burn rate >= 6 over 6h
- Budget exhaustion: block_deploy
- Owner: N05 Operations
```

## Anti-Example (REJECTED)
```yaml
target_percent: 100.0   # FAIL: 100% is unachievable
error_budget_minutes: 0 # FAIL: derived from 100%, meaningless
error_budget_policy: null # FAIL: policy required
```
