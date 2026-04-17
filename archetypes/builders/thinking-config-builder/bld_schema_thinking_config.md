---
kind: schema
id: bld_schema_thinking_config
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for thinking_config
quality: 9.2
title: "Schema Thinking Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [thinking_config, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for thinking_config"
domain: "thinking_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Frontmatter Fields  

This ISO configures a thinking budget: how many tokens the model may spend on internal reasoning before emitting.
### Required  
| Field       | Type   | Required | Default | Notes                              |  
|-------------|--------|----------|---------|------------------------------------|  
| id          | string | yes      | -       | Unique identifier                  |  
| kind        | string | yes      | "thinking_config" | CEX kind type           |  
| pillar      | string | yes      | "P09"    | Pillar classification              |  
| title       | string | yes      | -       | Configuration title                |  
| version     | string | yes      | "1.0"    | Schema version                     |  
| created     | date   | yes      | -       | ISO 8601 creation date             |  
| updated     | date   | yes      | -       | ISO 8601 last update date          |  
| author      | string | yes      | -       | Author/owner                       |  
| domain      | string | yes      | -       | Application domain                 |  
| quality     | null   | yes      | null     | Always null at authoring time; peer review assigns score |  
| tags        | list   | yes      | []       | Keywords for categorization        |  
| tldr        | string | yes      | -       | Summary of configuration purpose   |  
| thinking_model | string | yes | "default" | AI model used for reasoning       |  
| reasoning_depth | int | yes | 3 | Depth of logical steps (1-5)      |  

### Recommended  
| Field              | Type   | Notes                          |  
|--------------------|--------|--------------------------------|  
| validation_method  | string | Rule validation approach       |  
| example_use_case   | string | Sample application scenario   |  

## ID Pattern  
^p09_thk_[a-zA-Z0-9_]+\.yaml$  

## Body Structure  
1. **Overview**  
   - Purpose, scope, and intended use of the configuration.  
2. **Configuration Parameters**  
   - Detailed breakdown of all configurable fields and their constraints.  
3. **Validation Rules**  
   - Logic for validating input data and ensuring consistency.  
4. **Example Use Cases**  
   - Real-world scenarios demonstrating configuration application.  
5. **Optimization Guidelines**  
   - Recommendations for performance tuning and resource allocation.  

## Constraints  
- Max file size: 2048 bytes (UTF-8 encoded).  
- All required fields must be present and non-empty.  
- `thinking_model` must be a registered AI model name.  
- `reasoning_depth` must be an integer between 1 and 5.  
- `version` must follow semantic versioning (e.g., "1.2.3").  
- `created` and `updated` dates must be in ISO 8601 format (YYYY-MM-DD).

## Properties

| Property | Value |
|----------|-------|
| Kind | `schema` |
| Pillar | P06 |
| Domain | thinking_config construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |
