---
id: bld_examples_alert_rule
kind: few_shot_example
pillar: P03
llm_function: GOVERN
version: 1.0.0
quality: null
tags: [alert_rule, examples, few-shot]
title: "Examples: alert_rule"
---
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
