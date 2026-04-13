---
kind: schema
id: bld_schema_reward_model
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for reward_model
quality: null
title: "Schema Reward Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [reward_model, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for reward_model"
domain: "reward_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field | Type | Required | Default | Notes |  
|-------|------|----------|---------|-------|  
| id | string | yes | - | Regex: ^p07_rwm_[a-zA-Z0-9]+\.md$ |  
| kind | string | yes | "reward_model" | - |  
| pillar | string | yes | "P07" | - |  
| title | string | yes | - | Human-readable name |  
| version | string | yes | "1.0.0" | Semantic versioning |  
| created | datetime | yes | - | ISO 8601 format |  
| updated | datetime | yes | - | ISO 8601 format |  
| author | string | yes | - | Responsible party |  
| domain | string | yes | - | Application context (e.g., "staking") |  
| quality | string | yes | "draft" | Status: draft/provisional/final |  
| tags | list | yes | [] | Keywords for categorization |  
| tldr | string | yes | - | One-sentence summary |  
| reward_type | string | yes | - | "token", "fee", "staking" |  
| distribution_mechanism | string | yes | - | "linear", "tiered", "time-locked" |  

### Recommended  
| Field | Type | Notes |  
|-------|------|-------|  
| reference_url | string | Link to spec or code |  
| implementation_status | string | "concept", "prototype", "live" |  

## ID Pattern  
^p07_rwm_[a-zA-Z0-9]+\.md$  

## Body Structure  
1. **Overview**  
   - Purpose, scope, and context of the reward model.  

2. **Mechanics**  
   - Rules for reward calculation, distribution, and eligibility.  

3. **Parameters**  
   - Key variables (e.g., `activation_threshold`, `decay_rate`).  

4. **Validation**  
   - Constraints, edge cases, and error handling.  

5. **Use Cases**  
   - Scenarios where the model is applied (e.g., user retention, governance).  

## Constraints  
- ID must match regex pattern.  
- `reward_type` must be one of: "token", "fee", "staking".  
- `distribution_mechanism` must be one of: "linear", "tiered", "time-locked".  
- `activation_threshold` ≥ 0.  
- `decay_rate` ∈ [0, 1].  
- Parameters must align with mechanics section.
