---
kind: schema
id: bld_schema_trajectory_eval
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for trajectory_eval
quality: 9.1
title: "Schema Trajectory Eval"
version: "1.1.0"
author: n01_hybrid_review4
tags: [trajectory_eval, builder, schema]
tldr: "Formal schema for trajectory_eval artifacts: LLM agent step-level evaluation records."
domain: "trajectory_eval construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.86
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| id | string | yes | | Must match ID Pattern |
| kind | string | yes | | Fixed to 'trajectory_eval' |
| pillar | string | yes | | Fixed to 'P07' |
| title | string | yes | | Human-readable evaluation name |
| version | string | yes | | Semantic version (e.g., '1.0.0') |
| created | datetime | yes | | ISO 8601 format |
| updated | datetime | yes | | ISO 8601 format |
| author | string | yes | | Owner identifier |
| domain | string | yes | | Task domain (e.g., 'web_navigation', 'software_engineering') |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | | Keywords for categorization |
| tldr | string | yes | | Summary in 1-2 sentences |
| agent_id | string | yes | | Identifier of the evaluated agent |
| task_id | string | yes | | Benchmark task identifier (e.g., swe_bench_12, webArena_045) |
| step_count | integer | yes | | Total steps in trajectory |
| task_success | boolean | yes | | Did agent complete the final goal? |

### Recommended
| Field | Type | Notes |
|---|---|---|
| benchmark | string | Source benchmark (AgentBench, WebArena, SWE-bench, OSWorld) |
| path_efficiency | float | steps_taken / steps_optimal (1.0 = perfect) |
| tool_call_accuracy | float | Precision of tool invocations vs. ground truth |
| partial_credit | float | Fraction of sub-goals completed (0.0-1.0) |

## ID Pattern
^p07_te_[a-z][a-z0-9_]+$

## Body Structure
1. **Trajectory Overview**
   - Agent ID, task ID, benchmark, environment, total steps.
2. **Step Log**
   - Table: step_n | observation_summary | reasoning_summary | action | outcome
3. **Evaluation Metrics**
   - task_success, path_efficiency, tool_call_accuracy, partial_credit, backtrack_count.
4. **Step-level Scores**
   - Per-step score with judge rationale for flagged steps.
5. **Failure Analysis**
   - First failure point, root cause (hallucination / grounding error / tool misuse / reasoning drift).
6. **Recommendations**
   - Targeted improvements for the specific failure mode observed.

## Constraints
- ID must match ^p07_te_[a-z][a-z0-9_]+$ exactly.
- agent_id and task_id must be non-empty.
- step_count must be >= 1.
- task_success is boolean (not a percentage).
- Quality field must be assigned by peer review, not self-reported.
- Total file size must not exceed 5120 bytes.
