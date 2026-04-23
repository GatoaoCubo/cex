---
kind: schema
id: bld_schema_nps_survey
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for nps_survey
quality: 9.1
title: "Schema Nps Survey"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [nps_survey, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for nps_survey"
domain: "nps_survey construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_multimodal_prompt
  - bld_schema_prompt_technique
  - bld_schema_usage_report
  - bld_schema_app_directory_entry
  - bld_schema_sandbox_spec
  - bld_schema_pitch_deck
  - bld_schema_oauth_app_config
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|------|------|----------|---------|-------|
| id | string | yes | null | Must match ID Pattern |
| kind | string | yes | "nps_survey" | Fixed value |
| pillar | string | yes | "P11" | Fixed value |
| title | string | yes | null | Human-readable name |
| version | string | yes | "1.0" | Semantic versioning |
| created | datetime | yes | null | ISO 8601 format |
| updated | datetime | yes | null | ISO 8601 format |
| author | string | yes | null | Creator's identifier |
| domain | string | yes | "customer_experience" | Fixed value |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | array | yes | [] | List of strings |
| tldr | string | yes | null | Summary of purpose |
| survey_questions | array | yes | [] | List of question strings |
| response_rate | number | yes | null | Percentage (0-100) |

### Recommended
| Field | Type | Notes |
|------|------|-------|
| survey_duration | string | "30 days" |
| target_demographic | string | "active users" |
| incentive_offered | boolean | false |
| analysis_method | string | "quantitative" |

## ID Pattern
^p11_nps_[a-z][a-z0-9_]+.yaml$

## Body Structure
1. **Survey Design**: Define question phrasing, scoring logic (0-10), and response options
2. **Distribution Plan**: Channels (email, app, website), frequency, and targeting rules
3. **Data Collection**: Integration endpoints, storage schema, and anonymization rules
4. **Analysis Framework**: Calculation of NPS, segment breakdowns, and trend tracking
5. **Reporting**: Output formats (CSV, JSON), visualization rules, and delivery cadence

## Constraints
- File size must not exceed 3072 bytes
- All required fields must be present and valid
- ID must match exact regex pattern
- Quality field must be assigned by peer review only
- Response_rate must be numeric between 0-100
- Survey_questions must contain at least 3 items

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.76 |
| [[bld_schema_benchmark_suite]] | sibling | 0.74 |
| [[bld_schema_integration_guide]] | sibling | 0.73 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.70 |
| [[bld_schema_prompt_technique]] | sibling | 0.69 |
| [[bld_schema_usage_report]] | sibling | 0.69 |
| [[bld_schema_app_directory_entry]] | sibling | 0.68 |
| [[bld_schema_sandbox_spec]] | sibling | 0.68 |
| [[bld_schema_pitch_deck]] | sibling | 0.68 |
| [[bld_schema_oauth_app_config]] | sibling | 0.68 |
