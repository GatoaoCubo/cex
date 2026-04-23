---
kind: schema
id: bld_schema_search_strategy
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for search_strategy
quality: 9.1
title: "Schema Search Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [search_strategy, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for search_strategy"
domain: "search_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_schema_usage_report
  - bld_schema_action_paradigm
  - bld_schema_diff_strategy
  - bld_schema_rl_algorithm
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_quickstart_guide
  - bld_schema_benchmark_suite
  - bld_schema_voice_pipeline
  - bld_schema_thinking_config
---

## Frontmatter Fields  
### Required  
| Field        | Type   | Required | Default | Notes |  
|--------------|--------|----------|---------|-------|  
| id           | string | yes      | -       | Unique identifier |  
| kind         | string | yes      | "search_strategy" | CEX kind |  
| pillar       | string | yes      | "P04"    | Pillar classification |  
| title        | string | yes      | -       | Strategy name |  
| version      | string | yes      | "1.0"   | Version number |  
| created      | date   | yes      | -       | Creation date |  
| updated      | date   | yes      | -       | Last update date |  
| author       | string | yes      | -       | Author name |  
| domain       | string | yes      | -       | Application domain |  
| quality      | null   | yes      | null    | Never self-score -- peer review only |  
| tags         | list   | yes      | []      | Keywords |  
| tldr         | string | yes      | -       | Summary |  
| strategy_type| string | yes      | -       | Strategy category |  
| target_entity| string | yes      | -       | Target entity |  

### Recommended  
| Field           | Type   | Notes |  
|------------------|--------|-------|  
| last_reviewed  | date   | Last review date |  
| related_strategies | list | Linked strategies |  

## ID Pattern  
^p04_ss_[a-zA-Z0-9_-]+\.md$  

## Body Structure  
1. **Overview**  
   - Purpose and scope of the strategy.  
2. **Objectives**  
   - Specific goals and success criteria.  
3. **Methodology**  
   - Step-by-step approach and algorithms.  
4. **Parameters**  
   - Configurable variables and their ranges.  
5. **Constraints**  
   - Limitations and edge cases.  
6. **Evaluation Metrics**  
   - KPIs and validation methods.  

## Constraints  
- Strategy must align with domain-specific requirements.  
- Parameters must be validated for type and range.  
- No duplicate strategy IDs within the same pillar.  
- Versioning required for all updates.  
- Quality must be null -- never self-score; peer review assigns the score before deployment.  
- Tags must include at least one domain-related keyword.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.70 |
| [[bld_schema_action_paradigm]] | sibling | 0.69 |
| [[bld_schema_diff_strategy]] | sibling | 0.68 |
| [[bld_schema_rl_algorithm]] | sibling | 0.68 |
| [[bld_schema_integration_guide]] | sibling | 0.68 |
| [[bld_schema_reranker_config]] | sibling | 0.67 |
| [[bld_schema_quickstart_guide]] | sibling | 0.67 |
| [[bld_schema_benchmark_suite]] | sibling | 0.67 |
| [[bld_schema_voice_pipeline]] | sibling | 0.66 |
| [[bld_schema_thinking_config]] | sibling | 0.66 |
