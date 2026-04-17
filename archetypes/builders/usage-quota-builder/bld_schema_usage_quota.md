---
kind: schema
id: bld_schema_usage_quota
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for usage_quota
quality: 9.1
title: "Schema Usage Quota"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [usage_quota, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for usage_quota"
domain: "usage_quota construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field | Type | Required | Default | Notes |
|------|------|----------|---------|-------|
| id | string | yes | null | Must match ID Pattern |
| kind | string | yes | null | Must be "usage_quota" |
| pillar | string | yes | null | Must be "P09" |
| title | string | yes | null | Human-readable name |
| version | string | yes | "1.0.0" | Semantic versioning |
| created | datetime | yes | null | ISO 8601 format |
| updated | datetime | yes | null | ISO 8601 format |
| author | string | yes | null | Responsible party |
| domain | string | yes | null | Usage context (e.g., "API", "storage") |
| quality | null | yes | null | Never self-score; peer review assigns |
| tags | array | yes | [] | Categorization |
| tldr | string | yes | null | Summary of quota rules |
| quota_limit | number | yes | null | Maximum allowed usage |
| usage_metric | string | yes | null | Unit of measurement (e.g., "requests/day") |
| reset_interval | string | yes | null | Timeframe for reset (e.g., "24h") |
| enforcement_policy | string | yes | null | "hard" or "soft" enforcement |

### Recommended
| Field | Type | Notes |
|------|------|-------|
| description | string | Detailed explanation |
| example | string | Sample usage scenario |
| related_entities | array | Linked resources |
| deprecated | boolean | Mark if obsolete |

## ID Pattern
^p09_uq_[a-z][a-z0-9_]+.yaml$

## Body Structure
1. **Quota Limit Definition**
   Specify numerical limit and unit of measurement.

2. **Usage Metric**
   Define what usage is measured (e.g., API calls, data transfer).

3. **Reset Interval**
   Define timeframe for quota reset (e.g., daily, monthly).

4. **Enforcement Policy**
   Specify enforcement type (hard: block, soft: warn).

5. **Quota Allocation**
   Describe how quotas are distributed across users/roles.

## Constraints
- All required fields must be present and valid
- `quota_limit` must be a positive number
- `reset_interval` must use ISO 8601 duration format
- `enforcement_policy` must be "hard" or "soft"
- `id` must match exact regex pattern
- File size must not exceed 3072 bytes
