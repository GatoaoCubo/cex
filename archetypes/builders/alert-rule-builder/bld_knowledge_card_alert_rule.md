---
id: bld_kc_alert_rule
kind: knowledge_card
pillar: P01
llm_function: INJECT
version: 1.0.0
quality: 6.5
tags: [alert_rule, prometheus, observability, knowledge]
title: "Knowledge: Alert Rule Pattern"
density_score: 1.0
updated: "2026-04-17"
---
# Domain Knowledge: alert_rule
## Core Facts
- Prometheus alerting rule format (Prometheus 2.x): expr + for + labels + annotations
- for duration: condition must hold for this long before alert fires (prevents flapping)
- Alertmanager routes alerts: severity label -> routing tree -> receiver (Slack/PD/email)
- PromQL alert expression: metric_name{label=value} > threshold
- Inhibition: critical alert suppresses warning alert for same system
- Silencing: temporary suppression during maintenance windows

## Severity Taxonomy (industry standard)
| Severity | MTTACK | Action | for_duration |
|----------|--------|--------|-------------|
| critical | < 5min | Page on-call immediately | 0s - 2m |
| warning | < 4h | Create ticket, monitor | 5m - 15m |
| info | days | Awareness, no urgency | 15m+ |

## PromQL Expression Patterns
| Pattern | Expression | Use Case |
|---------|------------|----------|
| Error rate | rate(errors_total[5m]) > 0.05 | 5% error rate over 5m window |
| Latency p99 | histogram_quantile(0.99, ...) > 0.5 | 99th percentile > 500ms |
| Disk usage | disk_used_bytes / disk_total_bytes > 0.85 | 85% disk capacity |
| Service down | up == 0 | Service unreachable |

## Anti-Patterns
| Anti-Pattern | Correct Approach |
|-------------|-----------------|
| Alert without for duration | Always set for_duration >= 1m for warning |
| Alert without runbook | Link runbook_url or add remediation_steps |
| Page for warning severity | critical = page; warning = ticket; info = log |
