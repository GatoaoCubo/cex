---
kind: quality_gate
id: p07_qg_reward_model
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for reward_model
quality: null
title: "Quality Gate Reward Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [reward_model, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for reward_model"
domain: "reward_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  
| metric | threshold | operator | scope |  
|---|---|---|---|  
| Reward model configuration | Valid and complete | equals | All reward models |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML valid | Syntax errors or parsing failures |  
| H02 | ID matches pattern | ID does not conform to `^[A-Z]{3}-[0-9]{4}$` |  
| H03 | kind matches | `kind` field ≠ `reward_model` |  
| H04 | Process defined | Missing process description |  
| H05 | Outcome metrics | <3 outcome metrics specified |  
| H06 | Thresholds set | Any metric lacks a numerical threshold |  
| H07 | Configuration non-empty | Empty or placeholder configuration |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | YAML structure | 0.10 | 1.0 if valid, 0.5 if minor issues |  
| D02 | Process clarity | 0.15 | 1.0 if unambiguous, 0.25 if vague |  
| D03 | Policy alignment | 0.10 | 1.0 if aligned, 0.5 if partial |  
| D04 | Metric completeness | 0.15 | 1.0 if ≥5 metrics, 0.5 if <3 |  
| D05 | Threshold reasonableness | 0.10 | 1.0 if logical, 0.25 if arbitrary |  
| D06 | Auditability | 0.10 | 1.0 if traceable, 0.5 if unclear |  
| D07 | Scalability | 0.10 | 1.0 if adaptable, 0.25 if rigid |  
| D08 | User feedback | 0.10 | 1.0 if documented, 0.5 if absent |  

## Actions  
| Score | Action |  
|---|---|  
| GOLDEN (≥9.5) | Auto-approve and deploy |  
| PUBLISH (≥8.0) | Require peer review before deployment |  
| REVIEW (≥7.0) | Flag for manual inspection |  
| REJECT (<7.0) | Reject and request revisions |  

## Bypass  
| conditions | approver | audit trail |  
|---|---|---|  
| Urgent business need | CTO | Documented justification + CTO signature |
