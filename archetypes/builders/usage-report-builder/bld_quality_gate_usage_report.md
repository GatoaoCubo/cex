---
kind: quality_gate
id: p11_qg_usage_report
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for usage_report
quality: 9.1
title: "Quality Gate Usage Report"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [usage_report, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for usage_report"
domain: "usage_report construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
(Table: metric, threshold, operator, scope)
| metric       | threshold                          | operator | scope              |
|--------------|------------------------------------|----------|--------------------|
| schema_id    | ^p07_ur_[a-z][a-z0-9_]+.yaml$     | matches  | all usage reports  |

## HARD Gates
(Table: ID | Check | Fail Condition)
| ID  | Check                          | Fail Condition                                      |
|-----|--------------------------------|-----------------------------------------------------|
| H01 | YAML frontmatter valid       | Missing or invalid YAML frontmatter                 |
| H02 | ID matches pattern ^p07_ur_[a-z][a-z0-9_]+.yaml$ | ID does not match required schema pattern         |
| H03 | kind field matches 'usage_report' | kind field is not 'usage_report'                  |
| H04 | report_date field exists       | report_date field missing                           |
| H05 | user_count metric is numeric   | user_count is not a number                          |
| H06 | time_range is valid (YYYY-MM)  | time_range format invalid or missing                |
| H07 | ID is unique per report        | Duplicate ID detected                               |

## SOFT Scoring
(Table: Dim | Dimension | Weight | Scoring Guide)
| Dim | Dimension             | Weight | Scoring Guide                                      |
|-----|------------------------|--------|----------------------------------------------------|
| D01 | Completeness           | 0.15   | 100% complete = 1.0; missing fields = 0.5           |
| D02 | Accuracy               | 0.15   | 100% accurate data = 1.0; errors = 0.5              |
| D03 | Timeliness             | 0.10   | Delivered within 24h = 1.0; delayed = 0.5           |
| D04 | Clarity                | 0.10   | Clear metrics = 1.0; ambiguous = 0.5                |
| D05 | Consistency            | 0.10   | Consistent across reports = 1.0; inconsistent = 0.5 |
| D06 | Data integrity         | 0.10   | No duplicates = 1.0; duplicates = 0.5               |
| D07 | Alignment with billing | 0.15   | Fully aligned = 1.0; partial = 0.5                  |
| D08 | User-friendliness      | 0.15   | Easy to interpret = 1.0; complex = 0.5              |

## Actions
(Table: Score | Action)
| Score       | Action                  |
|-------------|-------------------------|
| GOLDEN >=9.5 | Auto-publish            |
| PUBLISH >=8.0| Manual review required  |
| REVIEW >=7.0 | Escalate to CFO         |
| REJECT <7.0 | Reject and rework       |

## Bypass
(Table: conditions, approver, audit trail)
| conditions                          | approver | audit trail                          |
|-----------------------------------|----------|--------------------------------------|
| Urgent business need confirmed    | CFO      | Documented in system audit logs      |
