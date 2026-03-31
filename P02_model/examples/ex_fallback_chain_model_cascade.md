---
id: p02_fb_model_cascade
kind: fallback_chain
pillar: P02
chain:
  - {model: opus, timeout: 30}
  - {model: sonnet, timeout: 15}
  - {model: haiku, timeout: 5}
timeout_per_step: varies
quality: 9.0
tags: [fallback, cascade]
---
tldr: "Model cascade: opus for complex, sonnet for standard, haiku for simple. Cost-optimized fallback."
quality: null
tldr: "Model cascade: opus for complex, sonnet for standard, haiku for simple. Cost-optimized fallback."
quality: null
---

# Fallback: model_cascade

## Chain
opus > sonnet > haiku. Never skip. Trigger: timeout or error.

## Timing
| Step | Timeout | Cost |
|------|---------|------|
| opus | 30s | 100% |
| sonnet | 15s | 25% |
| haiku | 5s | 5% |
