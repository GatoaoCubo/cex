---
kind: memory
id: p10_mem_eval_metric_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for eval_metric construction
quality: 8.7
title: "Memory Eval Metric Builder"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_metric, builder, memory]
tldr: "Learned patterns and pitfalls for eval_metric construction"
domain: "eval_metric construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Observation
Common issues include ambiguous definitions leading to inconsistent scoring, lack of alignment with task objectives, and over-reliance on simplistic metrics that fail to capture nuanced performance aspects.

## Pattern
Effective metrics use precise, quantifiable criteria tied to specific task outcomes, often combining multiple dimensions (e.g., accuracy + fairness) while maintaining clarity.

## Evidence
Reviewed artifacts showed that metrics like "token_error_rate" (aligned with language modeling goals) performed better than vague terms like "quality."

## Recommendations
- Define metrics with explicit formulas and thresholds.
- Ensure alignment with downstream use cases (e.g., safety, efficiency).
- Avoid conflating evaluation with scoring rubrics; keep metrics objective.
- Document assumptions (e.g., data distribution, error types).
- Test metrics across edge cases to validate robustness.
