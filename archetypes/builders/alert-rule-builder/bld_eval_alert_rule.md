---
id: bld_qg_alert_rule
kind: quality_gate
pillar: P11
llm_function: GOVERN
version: 1.0.0
quality: 8.3
tags: [alert_rule, quality-gate, observability]
title: "Quality Gate: alert_rule"
tldr: "Alert Rule feedback: quality gate with scoring dimensions and pass/fail criteria"
density_score: 1.0
updated: "2026-04-17"
related:
  - p11_qg_validator
  - p11_qg_agent_computer_interface
  - p05_qg_github_issue_template
  - p11_qg_guardrail
  - p11_qg_citation
  - bld_examples_validator
  - p06_security_validation_schema
  - bld_examples_unit_eval
  - p11_qg_instruction
  - p11_qg_model_registry
---

## Quality Gate

# Quality Gate: alert_rule
## HARD Gates
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error |
| H02 | id matches `^ar_[a-z][a-z0-9_]+$` | Wrong prefix or format |
| H03 | kind == "alert_rule" | Wrong kind |
| H04 | quality == null | Non-null value |
| H05 | alert_name present (PascalCase) | Missing or wrong case |
| H06 | severity in {critical, warning, info} | Invalid severity |
| H07 | for_duration present (ISO format) | Missing or invalid format |
| H08 | metric_expression contains numeric threshold | No number in expression |
| H09 | routing target present and non-empty | Missing routing |
| H10 | Total file size <= 2048 bytes | Exceeds max_bytes |

## SOFT Scoring
| ID | Dimension | Weight | 10pts | 5pts | 0pts |
|----|-----------|--------|-------|------|------|
| S01 | Runbook presence | 1.0 | URL or inline steps | Steps vague | Absent |
| S02 | Automated response | 0.8 | Defined action | Mentioned | Absent |
| S03 | Prometheus labels | 0.7 | severity+team+service | Some labels | No labels |
| S04 | for_duration appropriate | 0.7 | Matches severity best practice | Present | Missing |
| S05 | Alert name PascalCase | 0.5 | PascalCase | Mixed | snake_case |

## Score Tiers
| Score | Action |
|-------|--------|
| >= 9.0 | Deploy to Prometheus; register in alert catalog |
| >= 7.0 | Use with monitoring; add runbook |
| < 7.0 | Return: add metric expression, routing, runbook |

## Examples

# Examples: alert_rule
## Example 1: API Error Rate Critical
```yaml
id: ar_api_error_rate_high
kind: alert_rule
pillar: P09
title: "API Error Rate High Alert"
alert_name: ApiErrorRateHigh
severity: critical
for_duration: "1m"
metric_expression: "rate(http_requests_total{status=~'5..'}[5m]) / rate(http_requests_total[5m]) > 0.05"
routing: "pagerduty-prod-api"
quality: null
tags: [api, error-rate, critical, alert-rule]
```
Runbook: restart api pods if OOM; check DB connections if timeout pattern
Automated: kubectl rollout restart deployment/api (if OOMKilled)

## Example 2: Disk Usage Warning
```yaml
id: ar_disk_usage_warning
kind: alert_rule
pillar: P09
title: "Disk Usage Warning Alert"
alert_name: DiskUsageWarning
severity: warning
for_duration: "15m"
metric_expression: "node_filesystem_avail_bytes / node_filesystem_size_bytes < 0.15"
routing: "slack-ops-channel"
quality: null
tags: [disk, storage, warning, alert-rule]
```
Runbook: clean logs older than 30d; expand PVC if needed

## Anti-example (WRONG)
```yaml
id: llm_response_guard      # WRONG: LLM behavior = guardrail, not alert_rule
kind: alert_rule            # WRONG kind for LLM constraint
metric_expression: "be polite"  # WRONG: not a numeric threshold expression
# Missing severity          # WRONG: required field
```

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
