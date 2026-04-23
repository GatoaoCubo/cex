---
kind: schema
id: bld_schema_self_improvement_loop
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for self_improvement_loop
quality: 9.1
title: "Schema Self Improvement Loop"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [self_improvement_loop, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for self_improvement_loop"
domain: "self_improvement_loop construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_pitch_deck
  - bld_schema_quickstart_guide
  - bld_schema_integration_guide
  - bld_schema_playground_config
  - bld_schema_dataset_card
  - bld_schema_nps_survey
  - bld_schema_prompt_optimizer
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| id | string | yes |  | Must match ID Pattern |
| kind | string | yes | "self_improvement_loop" |  |
| pillar | string | yes | "P11" |  |
| title | string | yes |  | Descriptive name |
| version | string | yes | "1.0" |  |
| created | datetime | yes |  | ISO 8601 format |
| updated | datetime | yes |  | ISO 8601 format |
| author | string | yes |  |  |
| domain | string | yes | "self_improvement" |  |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | [] | Keywords for categorization |
| tldr | string | yes |  | Summary of purpose |
| loop_stages | list | yes | [] | Sequential steps in the loop |
| metrics | dict | yes | {} | Quantifiable outcomes |

### Recommended
| Field | Type | Notes |
|---|---|---|
| feedback_sources | list | External/peer inputs |
| review_cycle | string | Frequency of evaluation |

## ID Pattern
^p11_sil_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Overview**
   - Purpose of the self-improvement loop
   - Alignment with organizational goals

2. **Stages**
   - Detailed breakdown of `loop_stages` (e.g., assessment, planning, execution, review)

3. **Metrics**
   - Definition of `metrics` (e.g., KPIs, success criteria)

4. **Feedback Mechanisms**
   - Sources and integration of `feedback_sources`

5. **Review Process**
   - Frequency (`review_cycle`), responsible parties, and outcomes

## Constraints
- `loop_stages` must be sequential and actionable
- `metrics` must be quantifiable and time-bound
- `feedback_sources` must include at least two distinct channels
- `review_cycle` must be specified in ISO 8601 duration format
- All fields must adhere to ASCII encoding
- Total file size must not exceed 5120 bytes

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_benchmark_suite]] | sibling | 0.70 |
| [[bld_schema_reranker_config]] | sibling | 0.70 |
| [[bld_schema_usage_report]] | sibling | 0.70 |
| [[bld_schema_pitch_deck]] | sibling | 0.69 |
| [[bld_schema_quickstart_guide]] | sibling | 0.68 |
| [[bld_schema_integration_guide]] | sibling | 0.68 |
| [[bld_schema_playground_config]] | sibling | 0.65 |
| [[bld_schema_dataset_card]] | sibling | 0.65 |
| [[bld_schema_nps_survey]] | sibling | 0.65 |
| [[bld_schema_prompt_optimizer]] | sibling | 0.65 |
