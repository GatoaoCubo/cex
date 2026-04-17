---
id: p01_kc_alert_rule
kind: knowledge_card
type: kind
pillar: P01
title: "Alert Rule -- Deep Knowledge for alert_rule"
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
domain: alert_rule
quality: null
tags: [alert_rule, p09, GOVERN, kind-kc, prometheus, observability]
tldr: "Observable threshold condition triggering notification or automated response; Prometheus alerting rule format; NOT guardrail (LLM) nor quality_gate (artifact scoring)."
when_to_use: "Defining system conditions that should trigger on-call notification, ticket creation, or automated remediation"
keywords: [alert-rule, prometheus, threshold, observability, alerting]
feeds_kinds: [alert_rule]
density_score: null
aliases: ["alerting rule", "threshold rule", "monitoring alert", "alert condition"]
user_says: ["create alert for X", "notify when Y exceeds Z", "set up monitoring for", "page when"]
long_tails: ["define a threshold condition that triggers a notification when a metric exceeds a value", "configure an alert that fires when error rate is above 5%", "set up PagerDuty alert for disk usage"]
---

# Alert Rule

## Spec
```yaml
kind: alert_rule
pillar: P09
llm_function: GOVERN
max_bytes: 2048
naming: ar_{system}_{metric}.md
```

## What It Is
An alert_rule defines an observable threshold condition that triggers a notification or automated response. The Prometheus alerting rule format is the industry standard: a PromQL metric expression, a for-duration (how long the condition must hold before firing), a severity label (critical/warning/info), and routing to an Alertmanager receiver (PagerDuty, Slack, email, webhook). An alert_rule is CONFIGURATION for the observability stack -- it lives in P09 Config, not P11 Feedback.

Boundary: alert_rule is for SYSTEM METRICS crossing a threshold. NOT guardrail (LLM behavior constraints in P11 Feedback) and NOT quality_gate (artifact scoring in P11 Feedback).

## Severity Taxonomy (Prometheus / SRE Standard)
| Severity | MTTACK Target | Action | for_duration | Routing |
|----------|--------------|--------|-------------|---------|
| critical | < 5 minutes | Page on-call immediately, halt deployment | 0s - 2m | PagerDuty/OpsGenie |
| warning | < 4 hours | Create Jira/Linear ticket, investigate | 5m - 15m | Slack ops channel |
| info | days | Awareness log, no immediate action | 15m+ | Log aggregator |

## for_duration (Anti-Flapping Mechanism)
- critical: 0s (immediate) to 2m (confirm it's real, not a spike)
- warning: 5m to 15m (sustained condition indicates real problem)
- info: 15m+ (trend awareness, not individual spikes)
- Rule: for_duration >= 1m prevents >90% of false-positive pages

## PromQL Expression Patterns
| Pattern | Expression | Condition |
|---------|------------|-----------|
| Error rate | `rate(errors_total[5m]) / rate(requests_total[5m]) > 0.05` | > 5% error rate |
| Latency p99 | `histogram_quantile(0.99, sum(rate(latency_bucket[5m])) by (le)) > 0.5` | p99 > 500ms |
| Disk capacity | `node_filesystem_avail_bytes / node_filesystem_size_bytes < 0.15` | < 15% free |
| Service down | `up{job="api"} == 0` | Service unreachable |
| Memory pressure | `container_memory_usage_bytes / container_spec_memory_limit_bytes > 0.90` | > 90% memory |

## Prometheus Alertmanager Integration
```yaml
# CEX alert_rule frontmatter maps to Prometheus groups:
groups:
  - name: {alert_name}
    rules:
      - alert: {alert_name}          # from alert_name field
        expr: {metric_expression}    # from metric_expression field
        for: {for_duration}          # from for_duration field
        labels:
          severity: {severity}       # from severity field
        annotations:
          summary: {title}           # from title field
          runbook_url: {runbook_url} # from runbook_url field
```

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No for_duration (instant fire) | False positives from transient spikes | Set for_duration >= 1m for warning |
| Vague expression ("when slow") | Not measurable; Prometheus can't evaluate | PromQL with numeric threshold |
| Page on warning | Alert fatigue; engineers stop responding | critical=page, warning=ticket |
| No runbook for critical | On-call wastes time figuring out response | Every critical needs runbook_url |
| Alert without routing | Fires into void | Always set routing target |

## Decision Tree
- IF system metric exceeds numeric threshold -> alert_rule
- IF LLM output violates behavioral constraint -> guardrail
- IF artifact quality score below threshold -> quality_gate
- IF SLO error budget burn rate exceeded -> alert_rule (burn rate expression)
- IF scheduled maintenance suppression needed -> silence (Alertmanager config, not alert_rule)
- DEFAULT: alert_rule for any observable system condition needing notification

## Quality Criteria
- GOOD: metric_expression with numeric threshold, severity, for_duration, routing
- GREAT: runbook_url + automated_response + Prometheus labels + annotations
- FAIL: vague expression OR missing routing OR paging on warning severity
