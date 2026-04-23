---
id: bld_feedback_distillation_config
kind: builder_default
pillar: P11
title: "Distillation Config Builder - Feedback ISO"
domain: distillation_config
version: 1.0.0
quality: null
tags: [feedback, anti-patterns, P11, distillation_config]
related:
  - bld_eval_distillation_config
tldr: "Anti-patterns and correction protocol for distillation config builders."
author: builder_agent
llm_function: GOVERN
density_score: 0.85
created: "2026-04-23"
updated: "2026-04-23"
---

# Feedback: Distillation Config

## Anti-Patterns (NEVER do)

| Rule | Violation | Gate |
|------|-----------|------|
| No self-score | Never assign quality score | H05 |
| No T=1 | Temperature 1.0 defeats distillation | H07 |
| No missing teacher | Always specify teacher model | H04 |
| No missing student | Always specify student model | H06 |
| No unbalanced loss | Alpha must be between 0 and 1 | Schema |

## Common Failure Modes

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| Temperature too low | No soft knowledge transfer | Increase to 3-10 range |
| Alpha = 1.0 | Student drifts from ground truth | Balance at 0.3-0.7 |
| No eval checkpoints | Cannot detect training divergence | Add checkpoint schedule |
| Student too small | Quality loss exceeds budget | Use progressive distillation |

## Correction Protocol

| Step | Action | Gate |
|------|--------|------|
| 1 | Identify failed gate | F7 |
| 2 | Return to F6 with fix | F6 |
| 3 | Re-run F7 | F7 |
| 4 | Max 2 retries | F8 |
