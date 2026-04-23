---
kind: schema
id: bld_schema_rl_algorithm
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for rl_algorithm
quality: 9.1
title: "Schema Rl Algorithm"
version: "1.0.0"
author: wave1_builder_gen
tags: [rl_algorithm, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for rl_algorithm"
domain: "rl_algorithm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_schema_usage_report
  - bld_schema_search_strategy
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_quickstart_guide
  - bld_schema_sandbox_config
  - bld_schema_dataset_card
  - bld_schema_pitch_deck
  - bld_schema_diff_strategy
  - bld_schema_voice_pipeline
---

## Frontmatter Fields  
### Required  
| Field      | Type   | Required | Default | Notes |  
|------------|--------|----------|---------|-------|  
| id         | string | yes      | -       | Unique identifier |  
| kind       | string | yes      | "rl_algorithm" | CEX kind |  
| pillar     | string | yes      | "P02"    | Pillar classification |  
| title      | string | yes      | -       | Algorithm name |  
| version    | string | yes      | "1.0"    | Version number |  
| created    | date   | yes      | -       | Creation date |  
| updated    | date   | yes      | -       | Last update date |  
| author     | string | yes      | -       | Author name |  
| domain     | string | yes      | -       | Application domain |  
| quality    | null   | yes      | null     | Never self-score -- peer review only |  
| tags       | list   | yes      | []      | Keywords |  
| tldr       | string | yes      | -       | Summary |  
| algorithm_type | string | yes | - | RL variant (e.g., DQN, PPO) |  
| hyperparameters | map | yes | {} | Key-value parameter settings |  

### Recommended  
| Field              | Type   | Notes |  
|--------------------|--------|-------|  
| environment        | string | Training environment |  
| reward_function    | string | Reward definition |  

## ID Pattern  
^p02_rla_[a-zA-Z0-9_]+\.md$  

## Body Structure  
1. **Overview**  
   - Description of the algorithm's purpose and scope.  
2. **Algorithm Components**  
   - Key modules (e.g., policy, value function, exploration strategy).  
3. **Training Process**  
   - Steps for initialization, iteration, and convergence.  
4. **Evaluation Metrics**  
   - Performance indicators (e.g., reward, episode length).  
5. **Use Cases**  
   - Scenarios where the algorithm is applicable.  
6. **Constraints**  
   - Limitations or assumptions (e.g., computational requirements).  

## Constraints  
- All required fields must be present and valid.  
- ID must match the regex pattern.  
- File size must not exceed 5120 bytes.  
- Domain-specific fields must align with RL terminology.  
- No markdown formatting in body sections.  
- Version must follow semantic versioning (e.g., "1.2.3").

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_usage_report]] | sibling | 0.73 |
| [[bld_schema_search_strategy]] | sibling | 0.73 |
| [[bld_schema_reranker_config]] | sibling | 0.70 |
| [[bld_schema_benchmark_suite]] | sibling | 0.70 |
| [[bld_schema_quickstart_guide]] | sibling | 0.69 |
| [[bld_schema_sandbox_config]] | sibling | 0.69 |
| [[bld_schema_dataset_card]] | sibling | 0.69 |
| [[bld_schema_pitch_deck]] | sibling | 0.69 |
| [[bld_schema_diff_strategy]] | sibling | 0.68 |
| [[bld_schema_voice_pipeline]] | sibling | 0.68 |
