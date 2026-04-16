---
kind: examples
id: bld_examples_experiment_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of experiment_config artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 9.2
title: "Examples Experiment Config"
version: "1.0.0"
author: n03_builder
tags: [experiment_config, builder, examples, P09]
tldr: "Golden and anti-examples for experiment_config: demonstrates correct variant structure, traffic splits, and metric definitions."
domain: "experiment config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Examples: experiment-config-builder
## Golden Example
INPUT: "A/B test two prompt styles for the code review agent -- current verbose prompt vs. concise prompt"
OUTPUT:
```yaml
id: p09_ec_code_review_prompt_style
kind: experiment_config
pillar: P09
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
author: "builder_agent"
hypothesis: "If code review prompt is made concise (<= 200 tokens) then review_acceptance_rate increases by >= 3pct vs verbose baseline"
variants:
  - control
  - concise_prompt
primary_metric: "review_acceptance_rate"
guardrail_metrics:
  - critical_issue_detection_rate
  - p99_latency_ms
traffic_split:
  control: 50
  concise_prompt: 50
status: draft
significance_threshold: 0.05
min_detectable_effect: "+3pct relative"
sample_size_target: 1200
duration_days: 14
segment: "all"
quality: null
tags: [experiment_config, code-review, prompt-experiment, P09]
tldr: "Prompt style A/B test: verbose vs concise for code review agent, primary metric review_acceptance_rate"
```
## Overview
Testing whether a concise code review prompt (under 200 tokens) improves review acceptance
rate compared to the current verbose prompt (avg 420 tokens).
Decision enabled: adopt concise prompt as default or retain verbose baseline.
## Variants
| Variant | Type | Description | Key Changes |
|---------|------|-------------|-------------|
| control | control | Current verbose prompt (avg 420 tokens) | Baseline -- no changes |
| concise_prompt | treatment | Compressed prompt (<= 200 tokens) | Removed preamble, inline examples replaced with references |
## Traffic Split
| Variant | Allocation | Segment |
|---------|-----------|---------|
| control | 50% | all |
| concise_prompt | 50% | all |
Allocation total: 100%. No hold-out; all traffic participates.
## Metrics
### Primary Metric
| Metric | Direction | Winning Threshold |
|--------|-----------|-------------------|
| review_acceptance_rate | higher is better | +3pct vs control |
### Guardrail Metrics
| Metric | Acceptable Limit | Action if Breached |
|--------|-----------------|-------------------|
| critical_issue_detection_rate | >= 95pct of baseline | pause experiment |
| p99_latency_ms | <= 120pct of baseline | pause experiment |
## Statistical Parameters
| Parameter | Value | Notes |
|-----------|-------|-------|
| Significance threshold | 0.05 | alpha = 5pct |
| Min detectable effect | +3pct relative | baseline ~68pct acceptance |
| Sample size (per variant) | 1,200 | 80pct power, two-tailed z-test |
| Duration | 14 days | ~170 reviews/day estimated |
## Lifecycle
| Field | Value |
|-------|-------|
| Status | draft |
| Created | 2026-04-13 |
| Launch target | 2026-04-20 |
| Conclusion criteria | p < 0.05 AND min 14 days runtime |
| Decision owner | N03 builder team |

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p09_ec_ pattern (H02 pass)
- kind: experiment_config (H04 pass)
- variants list starts with "control" (H06 pass)
- traffic_split sums to 100 (H07 pass)
- primary_metric defined as single value (H08 pass)
- guardrail_metrics present (S04 pass)
- significance_threshold and min_detectable_effect specified (S05 pass)
- hypothesis is falsifiable (S01 pass)
- all 6 required body sections present (H09 pass)
- tldr <= 160 chars (S02 pass)

## Anti-Example
INPUT: "Create experiment for new prompt"
BAD OUTPUT:
```yaml
id: prompt-experiment-v2
kind: experiment
pillar: config
variants: [new, old]
traffic: 50/50
quality: 8.5
tags: [test]
```
Testing new prompt vs old prompt. New is better.

FAILURES:
1. id: "prompt-experiment-v2" uses hyphens and no `p09_ec_` prefix -> H02 FAIL
2. kind: "experiment" not "experiment_config" -> H04 FAIL
3. pillar: "config" not "P09" -> H06 FAIL
4. quality: 8.5 (not null) -> H05 FAIL
5. variants: does not start with "control"; uses ambiguous "old"/"new" -> H06 FAIL
6. traffic: "50/50" is a string, not a structured split object -> H07 FAIL
7. Missing fields: hypothesis, primary_metric, status, significance_threshold, version, created, author -> H06 FAIL
8. tags: only 1 item, missing "experiment_config" -> S02 FAIL
9. Body missing all 6 required sections -> H09 FAIL
10. No guardrail_metrics defined -> S04 FAIL
11. No statistical parameters (MDE, sample size) -> S05 FAIL
12. "New is better" -- conclusion stated before experiment runs; not a hypothesis -> S01 FAIL
