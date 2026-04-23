---
id: bld_kc_alert_rule
kind: knowledge_card
pillar: P01
llm_function: INJECT
version: 1.0.0
quality: 7.6
tags: [alert_rule, prometheus, observability, knowledge]
title: "Knowledge: Alert Rule Pattern"
author: builder
density_score: 0.88
created: "2026-04-17"
updated: "2026-04-17"
related:
  - p06_security_validation_schema
  - bld_knowledge_card_guardrail
  - extraction_gate_severity
  - p10_lr_guardrail_builder
  - bld_memory_validator
  - p04_notifier_NAME
  - p11_qg_validator
  - p03_sp_validator-builder
  - p03_ins_validator
  - p10_lr_cost_budget_builder
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

## Knowledge Injection Checklist

- Verify domain facts are sourced and citable
- Validate density_score >= 0.85 (no filler content)
- Cross-reference with related KCs for consistency
- Check for outdated facts that need refresh

## Injection Pattern

```yaml
# KC injection at F3
source: verified
density: 0.85+
cross_refs: checked
freshness: current
```

```bash
python _tools/cex_compile.py {FILE}
python _tools/cex_retriever.py --query "{DOMAIN}"
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_security_validation_schema]] | downstream | 0.23 |
| [[bld_knowledge_card_guardrail]] | sibling | 0.22 |
| [[extraction_gate_severity]] | sibling | 0.20 |
| [[p10_lr_guardrail_builder]] | downstream | 0.20 |
| [[bld_memory_validator]] | downstream | 0.19 |
| [[p04_notifier_NAME]] | downstream | 0.19 |
| [[p11_qg_validator]] | downstream | 0.18 |
| [[p03_sp_validator-builder]] | downstream | 0.18 |
| [[p03_ins_validator]] | downstream | 0.16 |
| [[p10_lr_cost_budget_builder]] | downstream | 0.16 |
