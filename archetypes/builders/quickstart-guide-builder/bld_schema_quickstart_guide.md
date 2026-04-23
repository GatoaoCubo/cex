---
kind: schema
id: bld_schema_quickstart_guide
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for quickstart_guide
quality: 9.1
title: "Schema Quickstart Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [quickstart_guide, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for quickstart_guide"
domain: "quickstart_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_usage_report
  - bld_schema_integration_guide
  - bld_schema_pitch_deck
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_search_strategy
  - bld_schema_contributor_guide
  - bld_schema_dataset_card
  - bld_schema_sandbox_config
  - bld_schema_onboarding_flow
---

## Frontmatter Fields
### Required
| Field     | Type   | Required | Default | Notes |
|-----------|--------|----------|---------|-------|
| id        | string | yes      |         |       |
| kind      | string | yes      |         |       |
| pillar    | string | yes      |         |       |
| title     | string | yes      |         |       |
| version   | string | yes      |         |       |
| created   | date   | yes      |         |       |
| updated   | date   | yes      |         |       |
| author    | string | yes      |         |       |
| domain    | string | yes      |         |       |
| quality   | null   | yes      | null    | Never self-score; peer review assigns |
| tags      | list   | yes      |         |       |
| tldr      | string | yes      |         |       |
| prerequisites | list | yes |         |       |
| steps     | list   | yes      |         |       |

### Recommended
| Field     | Type   | Notes |
|-----------|--------|-------|
| audience  | string |       |
| tools     | list   |       |

## ID Pattern
^p05_qs_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Introduction** – Purpose and scope of the guide
2. **Prerequisites** – Software, hardware, or knowledge required
3. **Steps** – Ordered actions to complete the task
4. **Troubleshooting** – Common issues and solutions
5. **Conclusion** – Summary and next steps

## Constraints
- File size must not exceed 8192 bytes
- ID must match ^p05_qs_[a-z][a-z0-9_]+.md$ exactly
- All required fields in frontmatter must be present and valid
- Content must use ASCII characters only
- Quality field must be assigned by peer review, not self-scored
- Steps must be numbered and ordered logically

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.75 |
| [[bld_schema_integration_guide]] | sibling | 0.74 |
| [[bld_schema_pitch_deck]] | sibling | 0.73 |
| [[bld_schema_reranker_config]] | sibling | 0.72 |
| [[bld_schema_benchmark_suite]] | sibling | 0.71 |
| [[bld_schema_search_strategy]] | sibling | 0.69 |
| [[bld_schema_contributor_guide]] | sibling | 0.68 |
| [[bld_schema_dataset_card]] | sibling | 0.68 |
| [[bld_schema_sandbox_config]] | sibling | 0.67 |
| [[bld_schema_onboarding_flow]] | sibling | 0.67 |
