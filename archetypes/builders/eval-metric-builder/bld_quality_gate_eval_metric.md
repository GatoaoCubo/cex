---
kind: quality_gate
id: p07_qg_eval_metric
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for eval_metric
quality: 9.1
title: "Quality Gate Eval Metric"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_metric, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for eval_metric"
domain: "eval_metric construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| metric          | threshold | operator | scope        |
|-----------------|-----------|----------|--------------|
| frontmatter     | valid     | ==       | artifact     |
| section_count   | >=4       | >=       | body         |
| metric_type     | defined   | ==       | frontmatter  |
| id_pattern      | matches   | ==       | frontmatter  |

## HARD Gates
(Table: ID | Check | Fail Condition)
| ID       | Check                  | Fail Condition                                      |
|----------|------------------------|-----------------------------------------------------|
| H01      | YAML frontmatter valid | Invalid YAML syntax or missing fields               |
| H02      | ID matches pattern     | ID does not match ^p07_em_[a-z][a-z0-9_]+.md$      |
| H03      | kind field matches     | kind is not 'eval_metric'                           |
| H04      | metric defined         | metric field is missing or empty                    |
| H05      | threshold numeric      | threshold is not a number                           |
| H06      | operator valid         | operator is not in [<=, >=, ==, !=]                |
| H07      | scope defined          | scope field is missing or empty                     |

## SOFT Scoring
| Dim | Dimension     | Weight | Scoring Guide                                      |
|-----|---------------|--------|----------------------------------------------------|
| D1  | Clarity       | 0.15   | Clear definition (1.0) vs ambiguous (0.0)          |
| D2  | Relevance     | 0.20   | Directly tied to task goal (1.0) vs irrelevant     |
| D3  | Precision     | 0.15   | Measurable with formula (1.0) vs vague (0.0)       |
| D4  | Consistency   | 0.10   | Aligns with existing metrics (1.0) vs conflicting  |
| D5  | Documentation | 0.10   | Full context provided (1.0) vs incomplete          |
| D6  | Uniqueness    | 0.10   | No duplication (1.0) vs redundant (0.0)            |
| D7  | Scope         | 0.10   | Covers critical use case (1.0) vs limited          |
| D8  | Alignment     | 0.10   | Supports evaluation goals (1.0) vs misaligned      |

## Actions
(Table: Score | Action)
| Score     | Action         |
|-----------|----------------|
| >=9.5     | GOLDEN         |
| >=8.0     | PUBLISH        |
| >=7.0     | REVIEW         |
| <7.0      | REJECT         |

## Bypass
(Table: conditions, approver, audit trail)
| conditions                  | approver       | audit trail              |
|-----------------------------|----------------|--------------------------|
| Critical business exception | CTO            | Signed waiver, timestamp |
