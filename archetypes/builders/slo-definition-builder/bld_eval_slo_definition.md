---
id: bld_quality_gate_slo_definition
kind: quality_gate
pillar: P07
title: "Gate: slo_definition"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: slo_definition
quality: 8.7
tags: [quality_gate, slo_definition, P09]
llm_function: GOVERN
tldr: "Validates SLO definitions for measurability, error budget math, and alerting completeness."
density_score: null
related:
  - p11_qg_quality_gate
  - bld_knowledge_card_quality_gate
  - p11_qg_system_prompt
  - p11_qg_enterprise_sla
  - p11_qg_validator
  - p11_qg_thinking_config
  - p11_qg_creation_artifacts
  - p11_qg_input_schema
  - p11_qg_model_provider
  - p11_qg_response_format
---

## Quality Gate

## Definition
An slo_definition must be measurable, mathematically correct, and actionable. This gate ensures the SLO can be implemented in a monitoring system without ambiguity.

## HARD Gates
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML frontmatter valid |
| H02 | ID matches namespace | `^p09_slo_[a-z][a-z0-9_]+$` |
| H03 | Kind matches literal | `kind` is exactly `slo_definition` |
| H04 | Quality is null | `quality: null` |
| H05 | target_percent in range | 50.0 <= target_percent < 100.0 |
| H06 | error_budget_minutes present | Non-zero, computed from target and window |
| H07 | error_budget_policy set | One of: block_deploy, alert_only, auto_rollback |
| H08 | owner specified | Non-empty owner field |

## SOFT Scoring
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| SLI metric query explicit | 1.0 | Metric formula or query present |
| Both burn rate thresholds defined | 1.0 | 1h fast + 6h slow alerts both present |
| Error budget math verified | 1.0 | error_budget_minutes matches formula |
| Denominator documented | 0.5 | What "total" means for this SLI |
| Tags include slo_definition | 0.5 | tags contains "slo_definition" |

Sum of weights: 4.0. `soft_score = sum / 4.0 * 10`

## Actions
| Score | Action |
|-------|--------|
| >= 9.0 | PUBLISH |
| >= 7.0 | REVIEW |
| < 7.0 | REJECT |

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
