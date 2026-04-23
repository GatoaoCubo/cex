---
id: bld_feedback_query_optimizer
kind: builder_default
pillar: P11
title: "Query Optimizer Builder - Feedback ISO"
domain: query_optimizer
version: 1.0.0
quality: null
tags: [feedback, anti-patterns, P11, query_optimizer]
related:
  - bld_eval_query_optimizer
tldr: "Anti-patterns and correction protocol for query optimizer builders."
author: builder_agent
llm_function: GOVERN
density_score: 0.85
created: "2026-04-23"
updated: "2026-04-23"
---

# Feedback: Query Optimizer

## Anti-Patterns (NEVER do)

| Rule | Violation | Gate |
|------|-----------|------|
| No self-score | Never assign quality score | H05 |
| No empty techniques | Always specify at least one technique | H04 |
| No unbounded latency | Always set latency budget | D3 |
| No missing fallback | Always define failure behavior | D5 |
| No over-engineering | Do not add techniques without justification | Best practice |

## Common Failure Modes

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| No latency budget | Pipeline too slow for interactive use | Add per-step time allocation |
| Over-expansion | Precision drops due to term dilution | Limit expansion terms |
| No query classification | Same pipeline for all query types | Add query routing |
| Missing fallback | Optimization error blocks retrieval | Fall back to raw query |

## Correction Protocol

| Step | Action | Gate |
|------|--------|------|
| 1 | Identify failed gate | F7 |
| 2 | Return to F6 with fix | F6 |
| 3 | Re-run F7 | F7 |
| 4 | Max 2 retries | F8 |
