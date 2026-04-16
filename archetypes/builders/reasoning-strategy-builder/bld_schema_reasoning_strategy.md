---
kind: schema
id: bld_schema_reasoning_strategy
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for reasoning_strategy
quality: 9.1
title: "Schema Reasoning Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [reasoning_strategy, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for reasoning_strategy"
domain: "reasoning_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Frontmatter Fields  

This ISO selects a reasoning strategy (e.g. chain-of-thought) and the conditions under which it applies.
### Required  
| Field        | Type       | Required | Default | Notes |  
|--------------|------------|----------|---------|-------|  
| id           | string     | yes      | -       | Unique identifier |  
| kind         | string     | yes      | "reasoning_strategy" | CEX type |  
| pillar       | string     | yes      | "P03"   | Pillar classification |  
| title        | string     | yes      | -       | Strategy name |  
| version      | string     | yes      | "1.0"   | Schema version |  
| created      | datetime   | yes      | -       | Timestamp |  
| updated      | datetime   | yes      | -       | Last modification |  
| author       | string     | yes      | -       | Creator |  
| domain       | string     | yes      | -       | Application domain |  
| quality      | null       | yes      | null    | Never self-score -- peer review only |  
| tags         | array      | yes      | []      | Keywords |  
| tldr         | string     | yes      | -       | Summary |  
| reasoning_type | enum     | yes      | ["deductive", "inductive", "abductive"] | Reasoning method |  
| strategy_depth | integer | yes      | 1-5     | Complexity level |  

### Recommended  
| Field              | Type   | Notes |  
|--------------------|--------|-------|  
| validation_method  | string | How strategy is validated |  
| application_scope  | string | Use case boundaries |  

## ID Pattern  
`^p03_rs_[a-zA-Z0-9]+$`  

## Body Structure  
1. **Overview**  
   - Description of the reasoning strategy's purpose and scope.  
2. **Core Components**  
   - Breakdown of logical steps, assumptions, and dependencies.  
3. **Validation Criteria**  
   - Metrics and tests to ensure strategy reliability.  
4. **Application Scope**  
   - Contexts where the strategy is applicable or restricted.  
5. **Quality Metrics**  
   - Evaluation framework for accuracy, robustness, and efficiency.  

## Constraints  
- **ID Uniqueness**: No duplicate `id` values across strategies.  
- **Versioning**: `version` must follow semantic versioning (e.g., "1.0.0").  
- **Domain Alignment**: `domain` must match predefined taxonomies.  
- **Validation Method**: Must be a recognized technique (e.g., "peer review", "empirical testing").  
- **Depth Range**: `strategy_depth` must be between 1 (basic) and 5 (highly complex).  
- **Quality**: `quality` must always be null -- never self-score, peer review assigns value.
