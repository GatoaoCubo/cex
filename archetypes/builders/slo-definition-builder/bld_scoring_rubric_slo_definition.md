---
id: bld_scoring_rubric_slo_definition
kind: knowledge_card
pillar: P07
title: "Scoring Rubric: slo_definition"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: slo_definition
quality: null
tags: [scoring_rubric, slo_definition, P09]
llm_function: GOVERN
tldr: "5-dimension scoring rubric for slo_definition artifacts."
density_score: null
---

# Scoring Rubric: slo_definition

## 5-Dimension Scoring

| Dimension | Weight | Score 10 | Score 5 | Score 0 |
|-----------|--------|----------|---------|---------|
| D1 Measurability | 0.30 | SLI metric query explicit + denominator documented | Metric type specified but no query | No SLI metric at all |
| D2 Math Correctness | 0.25 | error_budget_minutes verified from formula | Close but off by rounding | Missing or wrong |
| D3 Alerting Completeness | 0.20 | Both 1h fast + 6h slow burn thresholds present | One threshold only | No alerting defined |
| D4 Actionability | 0.15 | error_budget_policy + owner both set | Policy set, owner missing | Neither set |
| D5 Compliance | 0.10 | ID pattern, kind, target in range | Minor naming issue | HARD gate failure |

## Composite Score
`score = (D1*0.30 + D2*0.25 + D3*0.20 + D4*0.15 + D5*0.10) * 10`

## D1 Measurability is Critical
An SLO without a measurable SLI is meaningless. D1 failure = REJECT regardless of other scores.
