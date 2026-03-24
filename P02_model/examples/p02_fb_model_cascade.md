---
id: p02_fb_model_cascade
type: fallback_chain
lp: P02
chain:
  - model: opus
    timeout: 30
    cost_pct: 100
  - model: sonnet
    timeout: 15
    cost_pct: 25
  - model: haiku
    timeout: 5
    cost_pct: 5
timeout_per_step: varies
version: 1.0.0
created: 2026-03-24
author: STELLA
quality: 9.0
tags: [fallback, cascade, cost-optimization]
---

# Model Fallback Chain
Complex=opus(30s, 100%) > Medium=sonnet(15s, 25%) > Simple=haiku(5s, 5%).
