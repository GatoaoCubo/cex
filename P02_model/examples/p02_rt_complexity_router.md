---
id: p02_rt_complexity_router
type: router
lp: P02
routes:
  - {threshold: 0.45, target: local}
  - {threshold: 0.70, target: hybrid}
  - {threshold: 1.0, target: cloud}
fallback: cloud
quality: 9.0
tags: [router, complexity, scoring]
---

# Router: complexity

## Routes
| Score | Target | Use Case |
|-------|--------|----------|
| <0.45 | local (Ollama) | Lookup, format, simple |
| 0.45-0.70 | hybrid | Start local, escalate |
| >0.70 | cloud (Claude) | Multi-step, specialized |

Factors: token_est(0.20), reasoning(0.25), tools(0.15), domain(0.20), output(0.10), multi_step(0.10).

## Fallback
Cloud (Claude API). Source: `records/core/python/complexity_router.py`
