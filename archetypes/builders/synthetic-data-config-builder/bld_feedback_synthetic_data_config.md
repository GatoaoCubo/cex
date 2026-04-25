---
id: bld_feedback_synthetic_data_config
kind: builder_default
pillar: P11
title: "Synthetic Data Config Builder - Feedback ISO"
domain: synthetic_data_config
version: 1.0.0
quality: null
tags: [feedback, anti-patterns, P11, synthetic_data_config]
related:
  - bld_eval_synthetic_data_config
tldr: "Anti-patterns and correction protocol for synthetic data config builders."
author: builder_agent
llm_function: GOVERN
density_score: 0.85
created: "2026-04-23"
updated: "2026-04-23"
---

# Feedback: Synthetic Data Config

## Anti-Patterns (NEVER do)

| Rule | Violation | Gate |
|------|-----------|------|
| No self-score | Never assign quality score to own output | H05 |
| No missing filters | Never produce config without quality filters | D2 |
| No skipped decontamination | Never omit decontamination section | D3 |
| No vague methods | Always specify method with parameters | D1 |
| No frontmatter omission | Every artifact starts with valid YAML | H01 |

## Common Failure Modes

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| Missing source model | No teacher model specified | Add specific model identifier |
| No filter thresholds | Qualitative filter descriptions | Add numeric thresholds |
| Missing output format | No schema for generated data | Specify JSONL/Alpaca/etc with fields |
| No seed requirements | No diversity or count specified | Add minimum seed count and diversity |

## Correction Protocol

| Step | Action | Gate |
|------|--------|------|
| 1 | Identify which gate failed | F7 |
| 2 | Return to F6 with explicit fix | F6 |
| 3 | Re-run F7 GOVERN | F7 |
| 4 | Max 2 retries before escalation | F8 |

## Quality Dimensions

| Dimension | Weight | Criteria |
|-----------|--------|----------|
| D1 Structural completeness | 20%% | All required sections present |
| D2 Domain accuracy | 25% | Content matches synthetic data config domain |
| D3 Density | 20%% | >= 0.85 information density |
| D4 Cross-references | 15%% | Valid links to related artifacts |
| D5 Actionability | 20%% | Builder can produce from this alone |

## Common Failures

| Failure | Frequency | Fix |
|---------|-----------|-----|
| Generic content | High | Add domain-specific examples |
| Missing boundary adherence | Medium | Check kinds_meta.json boundary |
| Low density score | Medium | Replace prose with tables |

## Properties

| Property | Value |
|----------|-------|
| Kind | `feedback` |
| Pillar | P11 |
| Domain | synthetic data config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
