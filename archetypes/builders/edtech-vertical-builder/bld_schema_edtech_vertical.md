---
kind: schema
id: bld_schema_edtech_vertical
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for edtech_vertical
quality: 9.1
title: "Schema Edtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [edtech_vertical, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for edtech_vertical"
domain: "edtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_prompt_technique
  - bld_schema_nps_survey
  - bld_schema_onboarding_flow
  - bld_schema_usage_report
  - bld_schema_app_directory_entry
  - bld_schema_sandbox_spec
  - bld_schema_eval_metric
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| id | string | yes | null | Must match ID Pattern |
| kind | string | yes | "edtech_vertical" | Fixed value |
| pillar | string | yes | "P01" | Fixed value |
| title | string | yes | null | Human-readable name |
| version | string | yes | "1.0" | Semantic versioning |
| created | datetime | yes | null | ISO 8601 format |
| updated | datetime | yes | null | ISO 8601 format |
| author | string | yes | null | Owner/creator |
| domain | string | yes | "edtech" | Fixed value |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | [] | Keywords for categorization |
| tldr | string | yes | null | Summary in 1–2 sentences |
| focus_area | string | yes | null | E.g., "K-12", "Higher Ed" |
| target_demographic | string | yes | null | E.g., "students", "instructors" |

### Recommended
| Field | Type | Notes |
|---|---|---|
| certifications | list | E.g., "ISO 27001", "GDPR" |
| partnerships | list | Key collaborators |

## ID Pattern
^p01_etv_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Overview**
   Brief description of the vertical’s purpose and scope.

2. **Focus Areas**
   Detailed breakdown of educational domains (e.g., STEM, language learning).

3. **Target Demographics**
   Specific user groups (e.g., age ranges, roles, geographic regions).

4. **Technology Stack**
   Tools, platforms, and integrations used (e.g., LMS, AI tutors).

5. **Compliance**
   Regulatory and data privacy requirements (e.g., COPPA, FERPA).

6. **Partnerships**
   Collaborations with institutions, developers, or content providers.

## Constraints
- ID must match ^p01_etv_[a-z][a-z0-9_]+.md$ exactly.
- All required fields must be present and valid.
- Version must follow semantic versioning (e.g., "1.0.0").
- Domain-specific fields (focus_area, target_demographic) must be non-empty.
- Quality must be assigned by peer review, not self-reported.
- File size must not exceed 6144 bytes.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.76 |
| [[bld_schema_benchmark_suite]] | sibling | 0.75 |
| [[bld_schema_integration_guide]] | sibling | 0.74 |
| [[bld_schema_prompt_technique]] | sibling | 0.71 |
| [[bld_schema_nps_survey]] | sibling | 0.70 |
| [[bld_schema_onboarding_flow]] | sibling | 0.69 |
| [[bld_schema_usage_report]] | sibling | 0.68 |
| [[bld_schema_app_directory_entry]] | sibling | 0.68 |
| [[bld_schema_sandbox_spec]] | sibling | 0.68 |
| [[bld_schema_eval_metric]] | sibling | 0.67 |
