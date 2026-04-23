---
kind: quality_gate
id: p07_qg_cohort_analysis
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for cohort_analysis
quality: 9.0
title: "Quality Gate Cohort Analysis"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [cohort_analysis, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for cohort_analysis"
domain: "cohort_analysis construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_cohort_analysis
  - bld_instruction_cohort_analysis
  - kc_cohort_analysis
  - p09_qg_marketplace_app_manifest
  - cohort-analysis-builder
  - p01_qg_graph_rag_config
  - p01_qg_reranker_config
  - p07_qg_eval_metric
  - p11_qg_audit_log
  - p07_qg_benchmark_suite
---

## Quality Gate

## Definition
| metric         | threshold | operator | scope         |
|----------------|-----------|----------|---------------|
| retention_rate | 0.3       | >=       | per cohort    |
| ltv_model_r2   | 0.7       | >=       | per user segment |

## HARD Gates
| ID      | Check                     | Fail Condition                              |
|---------|---------------------------|---------------------------------------------|
| H01     | YAML frontmatter valid    | Missing or invalid frontmatter              |
| H02     | ID matches pattern        | ID does not match ^p07_ca_[a-z][a-z0-9_]+.yaml$ |
| H03     | kind field matches        | kind ≠ 'cohort_analysis'                   |
| H04     | cohort_key defined        | cohort_key missing or invalid               |
| H05     | retention_window defined  | retention_window missing or < 1 day        |
| H06     | ltv_window defined        | ltv_window missing or < 30 days            |
| H07     | metrics field valid       | metrics missing or not a list              |
| H08     | dimensions field valid    | dimensions missing or not a list           |

## SOFT Scoring
| Dim         | Dimension               | Weight | Scoring Guide                          |
|-------------|-------------------------|--------|----------------------------------------|
| D01         | Data completeness       | 0.15   | 1.0 if 100% data, 0.5 if 50%           |
| D02         | Metric accuracy         | 0.15   | 1.0 if metrics align with business KPIs|
| D03         | Cohort definition clarity | 0.10 | 1.0 if cohort_key is unambiguous       |
| D04         | Retention window validity | 0.10 | 1.0 if window ≥ 1 day                  |
| D05         | LTV model validity      | 0.15   | 1.0 if R² ≥ 0.7                        |
| D06         | Aggregation method      | 0.10   | 1.0 if method is documented and valid  |
| D07         | Analysis type           | 0.10   | 1.0 if 'retention' or 'ltv' specified  |
| D08         | Dimension relevance     | 0.15   | 1.0 if dimensions correlate with KPIs  |

## Actions
| Score     | Action         |
|-----------|----------------|
| GOLDEN    | Auto-publish   |
| PUBLISH   | Manual review  |
| REVIEW    | Flag for QA    |
| REJECT    | Block deployment |

## Bypass
| conditions                  | approver | audit trail              |
|-----------------------------|----------|--------------------------|
| Experimental schema         | CTO      | Note: "Bypassed for testing" |

## Examples

## Golden Example
```yaml
kind: cohort_analysis
name: monthly_retention_by_acquisition_channel
description: "Tracks user retention rates and LTV by acquisition channel over time"
vendor: Looker
data_source: Snowflake
parameters:
  cohort_definition: "Users acquired in the same calendar month"
  time_period: "2023-01-01 to 2023-12-31"
  metrics:
    - name: "30_day_retention_rate"
      description: "Percentage of users active 30 days post-acquisition"
    - name: "customer_lifetime_value"
      description: "Predicted LTV calculated using cohort spend patterns"
```

## Anti-Example 1: Mixed with Benchmarking
```yaml
kind: cohort_analysis
name: retention_vs_benchmark
description: "Compares cohort retention to industry benchmarks"
vendor: Google Analytics
data_source: BigQuery
parameters:
  cohort_definition: "Users from Q3 2023"
  benchmark_data: "Third-party retention benchmarks"
  metrics:
    - name: "Benchmark_rank"
      description: "Cohort performance relative to industry peers"
```
## Why it fails: Combines cohort analysis with benchmarking (model evaluation), violating the boundary.

## Anti-Example 2: Billing-focused
```yaml
kind: cohort_analysis
name: usage_by_subscription_type
description: "Tracks feature usage by subscription plan"
vendor: Stripe
data_source: PostgreSQL
parameters:
  cohort_definition: "Users with active subscriptions"
  metrics:
    - name: "Monthly_revenue_per_user"
      description: "Average revenue per user by subscription tier"
```
## Why it fails: Focuses on billing metrics rather than retention/LTV, confusing with usage_report kind.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
