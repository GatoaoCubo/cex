---
kind: schema
id: bld_schema_onboarding_flow
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for onboarding_flow
quality: 9.1
title: "Schema Onboarding Flow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [onboarding_flow, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for onboarding_flow"
domain: "onboarding_flow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_schema_app_directory_entry
  - bld_schema_prompt_technique
  - bld_schema_audit_log
  - bld_schema_oauth_app_config
  - bld_schema_sandbox_spec
  - bld_schema_eval_metric
  - bld_schema_quickstart_guide
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|---|---|---|---|---|
| id | string | yes | null | Must match ID Pattern |
| kind | string | yes | null | Always "onboarding_flow" |
| pillar | string | yes | null | Always "P05" |
| title | string | yes | null | Descriptive name |
| version | string | yes | "1.0" | Semantic versioning |
| created | datetime | yes | null | ISO 8601 format |
| updated | datetime | yes | null | ISO 8601 format |
| author | string | yes | null | Owner's name |
| domain | string | yes | null | CEX subsystem (e.g., "KYC") |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | list | yes | [] | Keywords for categorization |
| tldr | string | yes | null | Summary of flow purpose |
| steps | list | yes | [] | Ordered onboarding steps |
| user_journey | string | yes | null | High-level user path |

### Recommended
| Field | Type | Notes |
|---|---|---|
| estimated_time | string | Approximate duration (e.g., "10 mins") |
| completion_rate | float | Target percentage (e.g., 95.0) |
| risk_assessment | string | Security/privacy impact summary |

## ID Pattern
^p05_of_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Purpose and Objectives**
   Define the flow's goal, target audience, and alignment with CEX policies.

2. **Key Components and Requirements**
   List mandatory fields, integrations, and technical dependencies.

3. **User Journey Mapping**
   Detail step-by-step interactions, UI/UX considerations, and friction points.

4. **Success Metrics and KPIs**
   Define measurable outcomes (e.g., conversion rates, error rates).

5. **Compliance and Security Requirements**
   Outline regulatory checks, data handling, and audit trails.

## Constraints
- All required fields must be present and valid.
- ID must match ^p05_of_[a-z][a-z0-9_]+.md$ exactly.
- File size must not exceed 5120 bytes.
- Quality field must be assigned by peer review, not self-scored.
- Steps must be ordered and numbered sequentially.
- Versioning must follow semantic versioning (e.g., 1.0.0).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | sibling | 0.75 |
| [[bld_schema_benchmark_suite]] | sibling | 0.73 |
| [[bld_schema_reranker_config]] | sibling | 0.72 |
| [[bld_schema_app_directory_entry]] | sibling | 0.68 |
| [[bld_schema_prompt_technique]] | sibling | 0.68 |
| [[bld_schema_audit_log]] | sibling | 0.68 |
| [[bld_schema_oauth_app_config]] | sibling | 0.67 |
| [[bld_schema_sandbox_spec]] | sibling | 0.67 |
| [[bld_schema_eval_metric]] | sibling | 0.67 |
| [[bld_schema_quickstart_guide]] | sibling | 0.67 |
