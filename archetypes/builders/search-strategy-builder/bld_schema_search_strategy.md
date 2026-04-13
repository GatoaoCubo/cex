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
| Field        | Type   | Required | Default | Notes |  
|--------------|--------|----------|---------|-------|  
| id           | string | yes      | -       | Unique identifier |  
| kind         | string | yes      | "search_strategy" | CEX kind |  
| pillar       | string | yes      | "P04"    | Pillar classification |  
| title        | string | yes      | -       | Strategy name |  
| version      | string | yes      | "1.0"    | Schema version |  
| created      | date   | yes      | -       | ISO 8601 format |  
| updated      | date   | yes      | -       | ISO 8601 format |  
| author       | string | yes      | -       | Creator |  
| domain       | string | yes      | -       | Application domain |  
| quality      | string | yes      | "draft"  | Review status |  
| tags         | list   | yes      | []      | Keywords |  
| tldr         | string | yes      | -       | Summary |  
| strategy_type| string | yes      | -       | "keyword", "semantic", etc. |  
| target_entity| string | yes      | -       | "data", "documents", etc. |  

### Recommended  
| Field              | Type   | Notes |  
|--------------------|--------|-------|  
| coverage_criteria  | string | Scope details |  
| efficiency_metric  | string | Performance metric |  

## ID Pattern  
^p04_ss_[a-zA-Z0-9_]+\.md$  

## Body Structure  
1. **Overview**  
   - Purpose, scope, and use case.  
2. **Methodology**  
   - Algorithm, heuristics, or rules applied.  
3. **Parameters**  
   - Configurable inputs (e.g., depth, filters).  
4. **Evaluation**  
   - Metrics, validation, and success criteria.  
5. **Constraints**  
   - Limitations or edge cases.  
6. **Examples**  
   - Use cases or sample queries.  

## Constraints  
- ID must follow regex pattern.  
- Required fields must be present and non-empty.  
- Dates must use ISO 8601 format.  
- strategy_type must be from predefined enum.  
- Body sections must be non-empty and ordered.  
- Total markdown size must not exceed 4096 bytes.
