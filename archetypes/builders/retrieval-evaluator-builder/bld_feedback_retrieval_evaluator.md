---
id: bld_feedback_retrieval_evaluator
kind: builder_default
pillar: P11
title: "Retrieval Evaluator Builder - Feedback ISO"
domain: retrieval_evaluator
version: 1.0.0
quality: null
tags: [feedback, anti-patterns, P11, retrieval_evaluator]
related:
  - bld_eval_retrieval_evaluator
  - bld_model_retrieval_evaluator
tldr: "Anti-patterns and correction protocol for retrieval evaluator builders. 6 NEVER rules + 4 failure modes + 3-step correction."
author: builder_agent
llm_function: GOVERN
density_score: 0.85
created: "2026-04-23"
updated: "2026-04-23"
---

# Feedback: Retrieval Evaluator

## Anti-Patterns (NEVER do)

| Rule | Violation | Gate |
|------|-----------|------|
| No self-score | Never assign quality score to own output | H01 |
| No vague metrics | Never use qualitative terms like "good results" as metrics | H04 |
| No missing baseline | Never produce evaluator without baseline comparison | H06 |
| No tiny query sets | Never accept query set size < 30 | Schema constraint |
| No frontmatter omission | Every artifact starts with valid YAML frontmatter | H01 |
| No single metric | Always define at least 2 complementary metrics | D1 |

## Common Failure Modes

| Failure Mode | Signal | Fix |
|-------------|--------|-----|
| Vague metric definition | No formula, just name | Add mathematical formula for each metric |
| Missing judgment protocol | No annotator guidelines | Add relevance scale and agreement threshold |
| No regression criteria | No numeric thresholds | Add pass/fail/alert thresholds |
| Output schema mismatch | Output does not match template | Re-read bld_output ISO |

## Correction Protocol

| Step | Action | Gate |
|------|--------|------|
| 1 | Identify which H01-H07 gate failed | F7 |
| 2 | Return to F6 PRODUCE with explicit fix | F6 |
| 3 | Re-run F7 GOVERN | F7 |
| 4 | Max 2 retries before escalating to N07 | F8 |
