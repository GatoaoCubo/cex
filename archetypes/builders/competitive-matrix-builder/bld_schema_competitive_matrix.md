---
kind: schema
id: bld_schema_competitive_matrix
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for competitive_matrix
quality: null
title: "Schema Competitive Matrix"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [competitive_matrix, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for competitive_matrix"
domain: "competitive_matrix construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields (competitive matrix schema)
### Required fields for competitive matrix artifacts  
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
| competitors | list | yes      |         |       |  
| metrics   | list   | yes      |         |       |  
| analysis_date | date | yes      |         |       |  
| key_insights | string | yes      |         |       |  

### Recommended  
| Field         | Type   | Notes |  
|---------------|--------|-------|  
| source        | string |       |  
| methodology   | string |       |  
| reviewers     | list   |       |  

## ID Pattern  
^p01_cm_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview**  
2. **Competitor Analysis**  
3. **Key Metrics**  
4. **Strategic Insights**  
5. **Recommendations**  

## Constraints  
- ID must match ^p01_cm_[a-z][a-z0-9_]+.md$  
- `analysis_date` must be ISO 8601 format  
- `quality` field must be assigned by peer review  
- Tags must follow domain-specific conventions  
- File size must not exceed 5120 bytes
