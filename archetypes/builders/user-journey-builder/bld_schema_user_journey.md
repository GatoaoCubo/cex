---
kind: schema
id: bld_schema_user_journey
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for user_journey
quality: 9.1
title: "Schema User Journey"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [user_journey, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for user_journey"
domain: "user_journey construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_pitch_deck
  - bld_schema_usage_report
  - bld_schema_benchmark_suite
  - bld_schema_quickstart_guide
  - bld_schema_reranker_config
  - bld_schema_onboarding_flow
  - bld_schema_integration_guide
  - bld_schema_dataset_card
  - bld_schema_playground_config
  - bld_schema_customer_segment
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| id | string | yes |  | Must match ID Pattern |
| kind | string | yes | "user_journey" |  |
| pillar | string | yes | "P05" |  |
| title | string | yes |  | Descriptive name |
| version | string | yes | "1.0" |  |
| created | datetime | yes |  | ISO 8601 format |
| updated | datetime | yes |  | ISO 8601 format |
| author | string | yes |  |  |
| domain | string | yes | "CEX" |  |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | [] | Keywords for search |
| tldr | string | yes |  | Summary in 1 sentence |
| journey_stages | list | yes | [] | Ordered steps in journey |
| user_segment | string | yes |  | Target audience |

### Recommended
| Field | Type | Notes |
|---|---|---|
| research_method | string | e.g., "interviews", "analytics" |
| validation_status | string | "draft", "review", "approved" |

## ID Pattern
^p05_uj_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Overview**
   Brief description of the user journey's purpose and scope.

2. **Key Stages**
   Detailed breakdown of each stage, including touchpoints and goals.

3. **User Segment**
   Demographic, behavioral, or psychographic profile of the target audience.

4. **Success Metrics**
   Quantitative and qualitative indicators of journey effectiveness.

5. **Validation**
   Summary of research methods, data sources, and peer review outcomes.

## Constraints
- Journey stages must be ordered chronologically.
- Use domain-specific terminology consistently.
- All metrics must include both quantitative and qualitative data.
- Quality field must be assigned by peer review, not self-assessed.
- File size must not exceed 5120 bytes.
- Tags must use lowercase, hyphen-separated keywords.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_pitch_deck]] | sibling | 0.74 |
| [[bld_schema_usage_report]] | sibling | 0.73 |
| [[bld_schema_benchmark_suite]] | sibling | 0.72 |
| [[bld_schema_quickstart_guide]] | sibling | 0.71 |
| [[bld_schema_reranker_config]] | sibling | 0.71 |
| [[bld_schema_onboarding_flow]] | sibling | 0.68 |
| [[bld_schema_integration_guide]] | sibling | 0.68 |
| [[bld_schema_dataset_card]] | sibling | 0.68 |
| [[bld_schema_playground_config]] | sibling | 0.67 |
| [[bld_schema_customer_segment]] | sibling | 0.67 |
