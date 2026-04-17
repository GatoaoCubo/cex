---
id: bld_quality_gate_saga
kind: quality_gate
pillar: P07
title: "Gate: saga"
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: saga
quality: null
tags: [quality_gate, saga, P12]
llm_function: GOVERN
tldr: "Validates saga for compensation completeness, rollback sequence, and topology definition."
density_score: null
---

## Definition
A saga must be fully compensable: every step that executes a side effect must have a compensating action that undoes it. This gate ensures no saga enters production with uncompensable steps.

## HARD Gates
| ID  | Check | Rule |
|-----|-------|------|
| H01 | Frontmatter parses | YAML valid |
| H02 | ID matches namespace | `^p12_saga_[a-z][a-z0-9_]+$` |
| H03 | Kind matches literal | `kind` is exactly `saga` |
| H04 | Quality is null | `quality: null` |
| H05 | Topology specified | topology is choreography or orchestration |
| H06 | All steps have compensating_action | No null or empty compensating_action in any step |
| H07 | steps_count matches list | frontmatter count = actual step count |
| H08 | on_failure at saga level | on_failure is non-null |

## SOFT Scoring
| Dimension | Weight | Pass Condition |
|-----------|--------|----------------|
| Rollback sequence explicit | 1.0 | Rollback Sequence section present with ordered list |
| Compensating actions are idempotent | 1.0 | Actions described as retry-safe |
| Goal statement present | 0.5 | ## Goal section has one-sentence description |
| Participant identified per step | 0.5 | Each step has participant field |
| Tags include saga | 0.5 | tags contains "saga" |

Sum of weights: 3.5. `soft_score = sum / 3.5 * 10`

## Actions
| Score | Action |
|-------|--------|
| >= 9.0 | PUBLISH |
| >= 7.0 | REVIEW |
| < 7.0 | REJECT -- do not deploy without compensation completeness |
