---
kind: schema
id: bld_schema_faq_entry
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for faq_entry
quality: 9.1
title: "Schema Faq Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [faq_entry, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for faq_entry"
domain: "faq_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_schema_integration_guide
  - bld_schema_benchmark_suite
  - bld_schema_reranker_config
  - bld_schema_multimodal_prompt
  - bld_schema_eval_metric
  - bld_schema_app_directory_entry
  - bld_schema_audit_log
  - bld_schema_sandbox_spec
  - bld_schema_nps_survey
  - bld_schema_cohort_analysis
---

## Frontmatter Fields
### Required
| Field     | Type   | Required | Default | Notes                              |
|-----------|--------|----------|---------|------------------------------------|
| id        | string | yes      | null    | Unique identifier                  |
| kind      | string | yes      | null    | Must be `faq_entry`                |
| pillar    | string | yes      | null    | Must be `P01`                      |
| title     | string | yes      | null    | Concise question                   |
| version   | string | yes      | `1.0`   | Semantic versioning                |
| created   | string | yes      | null    | ISO 8601 date                      |
| updated   | string | yes      | null    | ISO 8601 date                      |
| author    | string | yes      | null    | Author name                        |
| domain    | string | yes      | null    | Contextual domain (e.g., `billing`, `account_management`, `product`) |
| quality   | null   | yes      | null    | Never self-score; peer review assigns |
| tags      | array  | yes      | `[]`    | Keywords for searchability         |
| tldr      | string | yes      | null    | Summary of answer                  |
| question  | string | yes      | null    | Full question text                 |
| answer    | string | yes      | null    | Detailed response                  |
| category  | string | yes      | null    | Classification (e.g., `security`)  |
| related_topics | array | yes | `[]`    | Linked FAQ entries                 |

### Recommended
| Field           | Type   | Notes                          |
|-----------------|--------|--------------------------------|
| difficulty_level | string | `beginner`, `intermediate`, `advanced` |
| last_reviewed  | string | ISO 8601 date                  |
| source_url     | string | Link to external reference     |

## ID Pattern
^p01_faq_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Question**
   Full text of the question.

2. **Answer**
   Detailed, structured response.

3. **Category**
   Contextual grouping (e.g., `getting_started`, `billing`, `troubleshooting`, `account`, `security`).

4. **Related Topics**
   List of linked FAQ entries.

5. **Difficulty Level**
   Audience-appropriate complexity rating.

6. **Source**
   External reference or internal documentation.

## Constraints
- ID must match `^p01_faq_[a-z][a-z0-9_]+.md$`
- `question` and `answer` fields must be non-empty
- `version` must follow semantic versioning (e.g., `1.0.0`)
- `quality` must be assigned by peer review, not self-scored
- `tags` must contain at least 2 keywords
- Total markdown body must be ≤ 3072 bytes (≈ 3000 characters)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_integration_guide]] | sibling | 0.74 |
| [[bld_schema_benchmark_suite]] | sibling | 0.71 |
| [[bld_schema_reranker_config]] | sibling | 0.70 |
| [[bld_schema_multimodal_prompt]] | sibling | 0.70 |
| [[bld_schema_eval_metric]] | sibling | 0.69 |
| [[bld_schema_app_directory_entry]] | sibling | 0.69 |
| [[bld_schema_audit_log]] | sibling | 0.69 |
| [[bld_schema_sandbox_spec]] | sibling | 0.67 |
| [[bld_schema_nps_survey]] | sibling | 0.67 |
| [[bld_schema_cohort_analysis]] | sibling | 0.67 |
