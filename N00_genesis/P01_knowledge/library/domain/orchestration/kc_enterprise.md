---
id: p01_kc_enterprise_orchestration
kind: knowledge_card
type: domain
pillar: P01
title: "Enterprise Orchestration — Scaling Agent Systems"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: orchestration
quality: 9.1
tags: [enterprise, scaling, orchestration, governance, compliance]
tldr: "Patterns for scaling agent systems: RBAC, audit trails, rate limiting, cost controls, compliance gates. From solo to team to enterprise."
when_to_use: "Scaling an agent system beyond single-user to team or enterprise deployment"
keywords: [enterprise, scaling, rbac, audit-trail, cost-control, governance]
density_score: 0.91
updated: "2026-04-07"
---

# Enterprise Orchestration

## Scaling Levels

| Level | Users | Agents | Governance |
|-------|-------|--------|------------|
| Solo | 1 | 1-7 | Informal (trust the user) |
| Team | 2-10 | 7-20 | Shared brand + review gates |
| Enterprise | 10+ | 20+ | RBAC + audit + compliance + cost |

## Enterprise Patterns

| Pattern | Purpose |
|---------|---------|
| RBAC | Who can dispatch which nuclei |
| Audit trail | git log + signals = full traceability |
| Rate limiting | Max dispatches per hour/day |
| Cost controls | Token budget per mission |
| Compliance gates | Regulatory checks (ANVISA, GDPR) before publish |
| Multi-tenant | Separate brand_config per client |

## CEX Enterprise Readiness
- Audit: git log (every action committed)
- Signals: full event trail in `.cex/runtime/signals/`
- Brand isolation: `brand_config.yaml` per instance
- Quality gates: automated enforcement
- Missing: RBAC, rate limiting, cost tracking (future work)

## Cross-References

- **Pillar**: P01 (Knowledge)
- **Kind**: `knowledge card`
- **Artifact ID**: `p01_kc_enterprise_orchestration`
- **Tags**: [enterprise, scaling, orchestration, governance, compliance]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P01 | Knowledge domain |
| Kind `knowledge card` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Retrieval Example

```yaml
# Query this card via cex_retriever.py
query: "Enterprise Orchestration — Scaling Agent Systems"
kind_filter: knowledge_card
threshold: 0.7
```

```bash
# CLI retrieval
python _tools/cex_retriever.py "Enterprise Orchestration — Scaling Agent Systems" --top 5
```
