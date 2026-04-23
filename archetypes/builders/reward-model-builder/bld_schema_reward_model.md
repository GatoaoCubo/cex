---
kind: schema
id: bld_schema_reward_model
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for reward_model
quality: 9.1
title: "Schema Reward Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [reward_model, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for reward_model"
domain: "reward_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_schema_reranker_config
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_dataset_card
  - bld_schema_benchmark_suite
  - bld_schema_sandbox_config
  - bld_schema_quickstart_guide
  - bld_schema_rl_algorithm
  - bld_schema_integration_guide
  - bld_schema_action_paradigm
---

## Frontmatter Fields  
### Required  
| Field         | Type   | Required | Default | Notes                              |  
|---------------|--------|----------|---------|------------------------------------|  
| id            | string | yes      | -       | Unique identifier                  |  
| kind          | string | yes      | "reward_model" | CEX kind type              |  
| pillar        | string | yes      | "P07"    | Pillar reference                   |  
| title         | string | yes      | -       | Model name                         |  
| version       | string | yes      | "1.0"    | Schema version                     |  
| created       | date   | yes      | -       | Creation timestamp                 |  
| updated       | date   | yes      | -       | Last update timestamp              |  
| author        | string | yes      | -       | Author/owner                       |  
| domain        | string | yes      | -       | Application domain (e.g., trading) |  
| quality       | null   | yes      | null     | Never self-score -- peer review only |  
| tags          | list   | yes      | []       | Keywords                           |  
| tldr          | string | yes      | -       | Summary                            |  
| reward_type   | string | yes      | -       | Type of reward (e.g., token, fiat) |  
| calculation_method | string | yes | -       | Formula or logic                   |  
| max_reward_amount | number | yes | 0       | Cap limit                          |  

### Recommended  
| Field         | Type   | Notes                              |  
|---------------|--------|------------------------------------|  
| description   | string | Detailed model explanation         |  
| example       | object | Sample input/output                |  
| references    | list   | External documentation links       |  

## ID Pattern  
^p07_rwm_[a-zA-Z0-9]+\.md$  

## Body Structure  
1. **Overview**  
   - Purpose, scope, and use case.  
2. **Calculation Method**  
   - Formula, variables, and logic.  
3. **Reward Parameters**  
   - Thresholds, multipliers, and caps.  
4. **Eligibility Criteria**  
   - User conditions and restrictions.  
5. **Distribution Schedule**  
   - Timing and frequency of payouts.  
6. **Compliance and Auditing**  
   - Regulatory checks and validation.  

## Constraints  
- `reward_type` must be one of: "token", "fiat", "utility".  
- `calculation_method` must include a valid mathematical expression.  
- `max_reward_amount` must be ≥ 0.  
- `domain` must align with CEX operational areas.  
- All timestamps must use ISO 8601 format.  
- `version` must follow semantic versioning (e.g., "1.2.3").

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_reranker_config]] | sibling | 0.72 |
| [[bld_schema_usage_report]] | sibling | 0.71 |
| [[bld_schema_search_strategy]] | sibling | 0.70 |
| [[bld_schema_dataset_card]] | sibling | 0.69 |
| [[bld_schema_benchmark_suite]] | sibling | 0.69 |
| [[bld_schema_sandbox_config]] | sibling | 0.68 |
| [[bld_schema_quickstart_guide]] | sibling | 0.68 |
| [[bld_schema_rl_algorithm]] | sibling | 0.68 |
| [[bld_schema_integration_guide]] | sibling | 0.68 |
| [[bld_schema_action_paradigm]] | sibling | 0.68 |
