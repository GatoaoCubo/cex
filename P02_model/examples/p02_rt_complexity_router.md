---
id: p02_rt_complexity_router
type: router
lp: P02
routes:
  - threshold: 0.45
    target: local
    label: simple
  - threshold: 0.70
    target: hybrid
    label: medium
  - threshold: 1.0
    target: cloud
    label: complex
fallback: cloud
version: 1.0.0
created: 2026-03-24
author: EDISON
quality: 9.0
tags: [router, complexity, local-cloud, scoring]
---

# Complexity Router

## Scoring (5 factors, 0.0-1.0 each)
| Factor | Weight | Local-Friendly | Cloud-Required |
|--------|--------|----------------|----------------|
| token_count | 0.25 | <1K tokens | >10K tokens |
| reasoning_depth | 0.30 | Lookup/format | Multi-step logic |
| tool_usage | 0.15 | None | 3+ tools |
| domain_expertise | 0.20 | General | Specialized |
| output_length | 0.10 | Short | Long-form |

## Routes
- **<0.45 LOCAL**: Simple tasks, Ollama/local LLM
- **0.45-0.70 HYBRID**: Start local, escalate if needed
- **>0.70 CLOUD**: Direct to Claude API

Source: `records/core/python/complexity_router.py`
