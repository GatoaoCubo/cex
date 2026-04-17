---
kind: schema
id: bld_schema_usage_report
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for usage_report
quality: 9.1
title: "Schema Usage Report"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [usage_report, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for usage_report"
domain: "usage_report construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
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
| report_period | string | yes |         |       |
| user_count | integer | yes |         |       |

### Recommended
| Field         | Type   | Notes |
|---------------|--------|-------|
| data_source   | string |       |
| metrics       | list   |       |
| methodology   | string |       |

## ID Pattern
^p07_ur_[a-z][a-z0-9_]+.yaml$

## Body Structure
1. **Overview**: Summary of report scope and purpose.
2. **Key Metrics**: Core usage statistics (e.g., active users, session counts).
3. **User Activity**: Breakdown by time, feature, or cohort.
4. **Data Sources**: Description of systems or tools used to collect data.
5. **Constraints**: Limitations or assumptions in data collection.

## Constraints
- File size must not exceed 3072 bytes.
- All required fields must be present and valid.
- ID must match ^p07_ur_[a-z][a-z0-9_]+.yaml$ exactly.
- Version must follow semantic versioning (e.g., 1.0.0).
- Quality field must be assigned by peer review, not self-assigned.
