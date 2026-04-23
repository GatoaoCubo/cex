---
id: bld_feedback_curriculum_config
kind: builder_default
pillar: P11
title: "Curriculum Config Builder - Feedback ISO"
domain: curriculum_config
version: 1.0.0
quality: null
tags: [feedback, anti-patterns, P11, curriculum_config]
related:
  - bld_eval_curriculum_config
tldr: "Anti-patterns and correction protocol for curriculum config builders."
author: builder_agent
llm_function: GOVERN
density_score: 0.85
created: "2026-04-23"
updated: "2026-04-23"
---

# Feedback: Curriculum Config

## Anti-Patterns (NEVER do)

| Rule | Violation | Gate |
|------|-----------|------|
| No self-score | Never assign quality score | H05 |
| No missing metric | Always define difficulty metric | H06 |
| No empty sources | Always list data sources | H07 |
| No missing strategy | Always specify curriculum strategy | H04 |
| No random-only | Curriculum without ordering is not curriculum | Best practice |

## Common Failure Modes

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| No difficulty metric | Cannot implement ordering | Define measurable metric |
| Fixed mixing ratios | Suboptimal throughout training | Add annealing schedule |
| No warmup | Training instability | Add 5-15% warmup phase |
| Missing checkpoints | Cannot detect training divergence | Add evaluation points |

## Correction Protocol

| Step | Action | Gate |
|------|--------|------|
| 1 | Identify failed gate | F7 |
| 2 | Return to F6 with fix | F6 |
| 3 | Re-run F7 | F7 |
| 4 | Max 2 retries | F8 |
