---
id: bld_scoring_rubric_constitutional_rule
kind: knowledge_card
pillar: P11
title: "Constitutional Rule Builder -- Scoring Rubric"
version: 1.0.0
quality: null
tags: [builder, constitutional_rule, scoring]
llm_function: GOVERN
---
# Scoring Rubric: constitutional_rule
## 5D Dimensions
| Dim | Name | Weight | Description |
|-----|------|--------|-------------|
| D1 | Principle Strength | 0.35 | Is the principle concrete, singular, and testable? |
| D2 | Absoluteness | 0.25 | Is bypass_policy truly none with documented rationale? |
| D3 | Violation Coverage | 0.20 | Are violation examples specific and diverse? |
| D4 | Detection Feasibility | 0.15 | Is the detection method practical and specified? |
| D5 | Constitutional Grounding | 0.05 | Is the basis classified and cited? |
## D1 Scoring Guide: Principle Strength
| Score | Criteria |
|-------|----------|
| 1.0 | Principle: single prohibition, concrete (named action/content), testable by reviewer, begins with Never/Always |
| 0.7 | Mostly concrete but slightly abstract in one area |
| 0.3 | Principle contains multiple prohibitions or is aspirational |
| 0.0 | Principle is a general value ("be honest") not a rule |
## D2 Scoring Guide: Absoluteness
| Score | Criteria |
|-------|----------|
| 1.0 | bypass_policy: none + rationale explains why no exception exists + all edge cases addressed |
| 0.7 | bypass_policy: none but rationale is thin (one sentence) |
| 0.0 | Any bypass condition present (automatic HARD gate failure) |
