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
| Configuration Validity | 100% | equals | All reward model YAMLs |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML valid | Invalid YAML syntax |  
| H02 | ID matches pattern | ID does not match `^[a-zA-Z0-9_-]{3,20}$` |  
| H03 | kind matches | kind is not `reward_model` |  
| H04 | Reward scope defined | Missing `scope` field |  
| H05 | Thresholds set | Missing `threshold` values |  
| H06 | Operator valid | Operator not in `>=, >, <, <=, ==` |  
| H07 | Version number present | Missing `version` field |  
| H08 | Configuration non-empty | Empty configuration block |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | YAML structure | 0.15 | 1.0 if valid, 0.5 if partial, 0 otherwise |  
| D02 | Metric clarity | 0.12 | 1.0 if unambiguous, 0.7 if vague, 0 otherwise |  
| D03 | Threshold reasonableness | 0.10 | 1.0 if logical, 0.5 if questionable, 0 otherwise |  
| D04 | Operator validity | 0.10 | 1.0 if standard, 0.5 if non-standard, 0 otherwise |  
| D05 | Scope coverage | 0.15 | 1.0 if comprehensive, 0.7 if partial, 0 otherwise |  
| D06 | Versioning | 0.10 | 1.0 if semantic, 0.5 if missing, 0 otherwise |  
| D07 | Documentation | 0.10 | 1.0 if present, 0.5 if minimal, 0 otherwise |  
| D08 | Audit trail | 0.18 | 1.0 if complete, 0.7 if partial, 0 otherwise |  

## Actions  
| Score | Action |  
|---|---|  
| GOLDEN (>=9.5) | Automatically approve and deploy |  
| PUBLISH (>=8.0) | Publish with minimal review |  
| REVIEW (>=7.0) | Schedule review with technical lead |  
| REJECT (<7.0) | Reject and require rework |  

## Bypass  
| conditions | approver | audit trail |  
|---|---|---|  
| Critical bug fix | CTO | Signed-off by CTO on [date] |  
| Compliance exception | Compliance Officer | Approved by Compliance Officer on [date] |  
| Emergency deployment | CTO | Emergency deployment log [ID] |
