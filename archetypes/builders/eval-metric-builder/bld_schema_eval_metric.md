---
kind: schema
id: bld_schema_eval_metric
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for eval_metric
quality: 9.1
title: "Schema Eval Metric"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_metric, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for eval_metric"
domain: "eval_metric construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_multimodal_prompt
  - bld_schema_app_directory_entry
  - bld_schema_audit_log
  - bld_schema_sandbox_spec
  - bld_schema_faq_entry
  - bld_schema_cohort_analysis
  - bld_schema_usage_report
---

## Frontmatter Fields
### Required
| Field      | Type   | Required | Default | Notes                              |
|------------|--------|----------|---------|------------------------------------|
| id         | string | yes      | null    | Unique identifier                  |
| kind       | string | yes      | null    | Always "eval_metric"               |
| pillar     | string | yes      | null    | "P07"                              |
| title      | string | yes      | null    | Descriptive name                   |
| version    | string | yes      | "1.0"   | Schema version                     |
| created    | date   | yes      | null    | ISO 8601                           |
| updated    | date   | yes      | null    | ISO 8601                           |
| author     | string | yes      | null    | Owner                              |
| domain     | string | yes      | null    | Application area                   |
| quality    | null   | yes      | null    | Never self-score; peer review assigns |
| tags       | list   | yes      | []      | Keywords                           |
| tldr       | string | yes      | null    | Summary                            |
| metric_type| string | yes      | null    | e.g., "accuracy", "precision"      |
| evaluation_context | string | yes | null | e.g., "training", "testing" |

### Recommended
| Field         | Type   | Notes                          |
|---------------|--------|--------------------------------|
| description   | string | Detailed explanation           |
| example       | string | Sample usage                   |
| reference     | string | Source or standard             |

## ID Pattern
^p07_em_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Definition**
   Clear description of the metric's purpose and scope.

2. **Context**
   Use case, data sources, and evaluation phase (e.g., training, inference).

3. **Calculation**
   Formula, thresholds, and implementation details.

4. **Interpretation**
   Meaning of values, benchmarks, and success criteria.

5. **Thresholds**
   Critical values for performance evaluation.

6. **Sources**
   Origin of the metric (e.g., internal, external standards).

## Constraints
- ID must match ^p07_em_[a-z][a-z0-9_]+.md$ exactly.
- `metric_type` must be a valid evaluation metric (predefined list).
- `evaluation_context` must be one of: "training", "testing", "validation".
- All required fields must be present and non-null.
- Version must follow semantic versioning (e.g., "1.0.0").
- Quality must be assigned by peer review, not self-assigned.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_benchmark_suite]] | sibling | 0.74 |
| [[bld_schema_integration_guide]] | sibling | 0.74 |
| [[bld_schema_reranker_config]] | sibling | 0.72 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.70 |
| [[bld_schema_app_directory_entry]] | sibling | 0.69 |
| [[bld_schema_audit_log]] | sibling | 0.69 |
| [[bld_schema_sandbox_spec]] | sibling | 0.68 |
| [[bld_schema_faq_entry]] | sibling | 0.67 |
| [[bld_schema_cohort_analysis]] | sibling | 0.67 |
| [[bld_schema_usage_report]] | sibling | 0.67 |
