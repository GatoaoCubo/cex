---
kind: quality_gate
id: p07_qg_trajectory_eval
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for trajectory_eval
quality: 9.0
title: "Quality Gate Trajectory Eval"
version: "1.1.0"
author: n01_hybrid_review4
tags: [trajectory_eval, builder, quality_gate]
tldr: "Quality gate for trajectory_eval artifacts: HARD structural checks + SOFT 5D scoring."
domain: "trajectory_eval construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.86
---

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| required_fields_present | 100% | == | frontmatter |
| id_pattern_match | true | == | artifact id |
| step_log_rows | >=1 | >= | body |
| evaluation_metrics_present | true | == | body |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Syntax errors or missing required fields |
| H02 | ID matches ^p07_te_[a-z][a-z0-9_]+$ | ID does not match pattern |
| H03 | kind field equals 'trajectory_eval' | kind is absent or mismatched |
| H04 | agent_id is non-empty | agent_id missing or blank |
| H05 | task_id is non-empty | task_id missing or blank |
| H06 | step_count >= 1 | step_count is zero or absent |
| H07 | Step Log section present with at least one row | Body has no step log table |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D1 | Step coverage | 0.20 | 1.0 = all steps logged with observation+action+outcome |
| D2 | Metric completeness | 0.20 | 1.0 = task_success + path_efficiency + tool_call_accuracy present |
| D3 | Failure analysis depth | 0.20 | 1.0 = first failure step identified with root cause |
| D4 | Benchmark alignment | 0.20 | 1.0 = task_id matches a known benchmark (AgentBench/WebArena/SWE-bench) |
| D5 | Actionability | 0.20 | 1.0 = recommendations target specific step failures |

## Actions
| Score | Action |
|---|---|
| >=9.5 | GOLDEN |
| >=8.0 | PUBLISH |
| >=7.0 | REVIEW |
| <7.0 | REJECT |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Experimental agent under active development | Research lead | Issue tracker link |
| Incomplete benchmark environment | QA lead | Environment config hash |
