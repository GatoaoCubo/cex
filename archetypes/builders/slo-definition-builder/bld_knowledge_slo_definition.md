---
quality: 7.9
quality: 7.6
id: bld_knowledge_card_slo_definition
kind: knowledge_card
pillar: P01
title: "Knowledge Card: slo_definition"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: slo_definition
tags: [knowledge_card, slo_definition, P09]
llm_function: INJECT
tldr: "Domain knowledge for slo_definition: SLI types, error budget math, burn rate alerting."
density_score: null
related:
  - bld_knowledge_card_enterprise_sla
  - bld_collaboration_rate_limit_config
  - p11_qg_enterprise_sla
  - rate-limit-config-builder
  - bld_tools_enterprise_sla
  - p05_qg_onboarding_flow
  - bld_collaboration_cost_budget
  - bld_memory_model_provider
---

# Knowledge Card: slo_definition

## Error Budget Math
Given target T% over window W days:
- error_budget_seconds = (1 - T/100) * W * 86400
- error_budget_minutes = error_budget_seconds / 60
- Example: 99.9% over 30d = 0.001 * 30 * 1440 = 43.2 minutes of allowed downtime

## Burn Rate Alerting (Google SRE Standard)
| Alert | Window | Burn Rate | Error Budget Consumed |
|-------|--------|-----------|----------------------|
| Fast burn (page) | 1h | 14x | 2% in 1h |
| Fast burn (ticket) | 6h | 6x | 5% in 6h |
| Slow burn (ticket) | 3d | 3x | 10% in 3d |

## SLI Types
| Type | Measurement | Example Query |
|------|------------|---------------|
| availability | good_requests / total_requests | `sum(rate(http_requests_total{code!~"5.."}[5m])) / sum(rate(http_requests_total[5m]))` |
| latency | requests_under_threshold / total | `histogram_quantile(0.99, rate(http_request_duration_seconds_bucket[5m]))` |
| error_rate | 1 - availability | 1 - availability SLI |
| throughput | successful_requests / time | `sum(rate(http_requests_total{code=~"2.."}[5m]))` |
| saturation | resource_used / resource_capacity | `max(container_memory_usage_bytes) / max(container_spec_memory_limit_bytes)` |

## Anti-Patterns
| Anti-Pattern | Fix |
|-------------|-----|
| 100% SLO target | Unachievable; use 99.99% max |
| No error budget policy | Define block_deploy or auto_rollback |
| SLO = SLA | SLA is external contract; SLO must be stricter |
| Measuring output not outcome | Measure user-visible SLI, not internal queue depth |

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
| [[bld_knowledge_card_enterprise_sla]] | sibling | 0.34 |
| [[bld_collaboration_rate_limit_config]] | downstream | 0.22 |
| [[p11_qg_enterprise_sla]] | downstream | 0.20 |
| [[rate-limit-config-builder]] | downstream | 0.18 |
| [[bld_tools_enterprise_sla]] | downstream | 0.18 |
| [[p05_qg_onboarding_flow]] | downstream | 0.17 |
| [[bld_collaboration_cost_budget]] | downstream | 0.16 |
| [[bld_memory_model_provider]] | downstream | 0.15 |
