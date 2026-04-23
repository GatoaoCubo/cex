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
related:
  - bld_examples_usage_report
  - p03_qg_prompt_technique
  - p07_qg_eval_metric
  - p11_qg_audit_log
  - p01_qg_graph_rag_config
  - p05_qg_product_tour
  - p09_qg_marketplace_app_manifest
  - p07_qg_cohort_analysis
  - p05_qg_integration_guide
  - p05_qg_pricing_page
---

## Quality Gate

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

## Examples

## Golden Example
```yaml
kind: usage_report
name: monthly_usage_202310
spec:
  provider: aws
  service: bedrock
  model: Claude-3
  period: 2023-10
usage:
  total_invocations: 15234
  input_tokens: 4567890
  output_tokens: 1234567
  cost_usd: 1234.56
  peak_hour: "14:30"
  user_ids: ["user123", "user456"]
timestamp: "2023-11-01T08:00:00Z"
```

## Anti-Example 1: Missing required fields
```yaml
kind: usage_report
name: monthly_usage_202310
usage:
  total_invocations: 15234
```
## Why it fails
Lacks provider/service/model metadata required for billing attribution. Missing cost metrics and timestamp violate spec completeness.

## Anti-Example 2: Including budget data
```yaml
kind: usage_report
name: monthly_usage_202310
spec:
  provider: google
  service: aiplatform
  model: PaLM-2
  period: 2023-10
usage:
  total_invocations: 15234
  budget_limit: 2000
  actual_cost: 1234.56
```
## Why it fails
Mixes usage analytics with cost_budget spec data. The budget_limit field belongs to a different CEX kind and introduces scope contamination.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
