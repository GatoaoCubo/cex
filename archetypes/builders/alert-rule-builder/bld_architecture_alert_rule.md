---
id: bld_architecture_alert_rule
kind: component_map
pillar: P08
llm_function: CONSTRAIN
version: 1.0.0
quality: 6.8
tags: [alert_rule, architecture, observability]
title: "Architecture Alert Rule"
density_score: 1.0
updated: "2026-04-17"
---
# Architecture: alert_rule
## Position in CEX Kind Taxonomy
```
P09 Config
  alert_rule        <-- THIS KIND (threshold -> notification)
  env_config        (environment variables)
  rate_limit_config (API rate limits)
  feature_flag      (boolean toggles)

P11 Feedback
  guardrail         (LLM behavior constraint -- NOT alert_rule)
  quality_gate      (artifact scoring -- NOT alert_rule)
  signal            (telemetry data -- alert_rule fires on signal)
```

## Relationships
| Relation | Kind | Direction | Notes |
|----------|------|-----------|-------|
| fires on | signal | alert evaluates signal | Signal is what's measured |
| routes to | agent / webhook | one-to-many | PagerDuty, Slack, webhook |
| triggers | workflow | optional | Auto-remediation workflows |
| grouped by | rate_limit_config | optional | Alert routing rules |
| documented in | runbook | one-to-one | Remediation procedure |

## Prometheus Integration
alert_rule maps directly to Prometheus alerting rules:
```yaml
# Prometheus equivalent:
groups:
  - name: {alert_name}
    rules:
      - alert: {alert_name}
        expr: {metric_expression}
        for: {for_duration}
        labels:
          severity: {severity}
        annotations:
          summary: {title}
```

## When to Use alert_rule (vs. alternatives)
| Scenario | Use |
|----------|-----|
| System metric exceeds threshold | alert_rule |
| LLM output violates constraint | guardrail |
| Artifact scores below threshold | quality_gate |
| On-call schedule configuration | rate_limit_config or external tool |
