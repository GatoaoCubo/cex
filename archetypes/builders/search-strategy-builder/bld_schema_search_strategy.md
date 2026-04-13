---
kind: schema
id: bld_schema_search_strategy
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for search_strategy
quality: null
title: "Schema Search Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [search_strategy, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for search_strategy"
domain: "search_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field             | Type       | Required | Default      | Notes                                      |  
|-------------------|------------|----------|--------------|--------------------------------------------|  
| id                | string     | yes      |              | Unique identifier                          |  
| kind              | string     | yes      | "search_strategy" | CEX kind                                 |  
| pillar            | string     | yes      | "P04"        | Pillar number                              |  
| title             | string     | yes      |              | Descriptive title                          |  
| version           | string     | yes      | "1.0.0"      | Semantic version                           |  
| created           | datetime   | yes      |              | ISO 8601 date                              |  
| updated           | datetime   | yes      |              | ISO 8601 date                              |  
| author            | string     | yes      |              | Responsible party                          |  
| domain            | string     | yes      |              | Application area                           |  
| quality           | string     | yes      | "draft"      | Quality level (draft, reviewed, approved)  |  
| tags              | array      | yes      |              | Keywords                                   |  
| tldr              | string     | yes      |              | Summary (≤255 chars)                       |  
| algorithm_type    | string     | yes      |              | e.g., Boolean, Vector                      |  
| data_sources      | array      | yes      |              | Sources used (e.g., SQL, NoSQL)            |  
| optimization_goal | string     | yes      |              | e.g., speed, accuracy                      |  
| query_language    | string     | yes      |              | e.g., SQL, Lucene                          |  

### Recommended  
| Field              | Type
