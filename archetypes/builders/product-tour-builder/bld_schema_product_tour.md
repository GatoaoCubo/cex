---
kind: schema
id: bld_schema_product_tour
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for product_tour
quality: 9.1
title: "Schema Product Tour"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [product_tour, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for product_tour"
domain: "product_tour construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields
### Required
| Field      | Type   | Required | Default | Notes                              |
|------------|--------|----------|---------|------------------------------------|
| id         | string | yes      | null    | Must match ID Pattern              |
| kind       | string | yes      | null    | Always "product_tour"              |
| pillar     | string | yes      | null    | Always "P05"                       |
| title      | string | yes      | null    | Descriptive name                   |
| version    | string | yes      | "1.0"   | Semantic versioning                |
| created    | date   | yes      | null    | ISO 8601                           |
| updated    | date   | yes      | null    | ISO 8601                           |
| author     | string | yes      | null    | Owner email                        |
| domain     | string | yes      | null    | Product area (e.g., "onboarding")  |
| quality    | null   | yes      | null    | Never self-score; peer review assigns |
| tags       | array  | yes      | []      | Keywords for search                |
| tldr       | string | yes      | null    | One-sentence summary               |
| tour_steps | array  | yes      | []      | Ordered list of tour steps         |
| target_audience | string | yes | null | User segment (e.g., "new users") |
| completion_criteria | string | yes | null | Metric for tour success |

### Recommended
| Field             | Type   | Notes                          |
|-------------------|--------|--------------------------------|
| feature_highlight | string | Key feature emphasized         |
| related_content   | array  | Links to related resources     |

## ID Pattern
^p05_pt_[a-z][a-z0-9_]+.md$

## Body Structure
1. **Introduction**
   - Purpose of the product tour
   - Target audience and use case

2. **Key Features**
   - Highlight 3–5 core features demonstrated in the tour

3. **User Journey**
   - Step-by-step flow and interaction points

4. **Completion Metrics**
   - Success criteria (e.g., completion rate, engagement time)

5. **Next Steps**
   - Post-tour actions (e.g., onboarding, support links)

## Constraints
- ID must match ^p05_pt_[a-z][a-z0-9_]+.md$
- All required fields must be present and valid
- Version must follow semantic versioning (e.g., "1.0.0")
- Tags must be lowercase, alphanumeric, and underscore-separated
- Quality must be assigned by peer review before publication
- Tour steps must be ordered and actionable
