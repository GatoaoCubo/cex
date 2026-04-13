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
| Field        | Type     | Required | Default | Notes |  
|--------------|----------|----------|---------|-------|  
| id           | string   | yes      | -       | Unique identifier |  
| kind         | string   | yes      | "reward_model" | CEX kind |  
| pillar       | string   | yes      | "P07"    | Pillar classification |  
| title        | string   | yes      | -       | Model name |  
| version      | string   | yes      | "1.0"    | Version number |  
| created      | datetime | yes      | -       | Creation timestamp |  
| updated      | datetime | yes      | -       | Last update timestamp |  
| author       | string   | yes      | -       | Author/owner |  
| domain       | string   | yes      | -       | Application domain (e.g., DeFi) |  
| quality      | string   | yes      | "draft"  | Quality status |  
| tags         | list     | yes      | []      | Keywords |  
| tldr         | string   | yes      | -       | Summary |  
| reward_type  | string   | yes      | -       | "token", "fiat", etc. |  
| distribution_mechanism | string | yes | - | "staking", "airdrop", etc. |  

### Recommended  
| Field              | Type   | Notes |  
|--------------------|--------|-------|  
| minimum_stake      | number | Minimum stake requirement |  
| apy_range          | string | Annual percentage yield range |  
| vesting_period     | string | Token vesting duration |  

## ID Pattern  
`^p07_rwm_[a-zA-Z0-9]+\.md$`  

## Body Structure  
1. **Overview**  
   - Description of the reward model's purpose and scope.  
2. **Reward Structure**  
   - Details of token/fiat rewards, calculation methods, and tiers.  
3. **Eligibility Criteria**  
   - Requirements for participation (e.g., stake thresholds, KYC).  
4. **Distribution Mechanism**  
   - How rewards are distributed (e.g., periodic, on-chain).  
5. **Performance Metrics**  
   - KPIs for evaluating model effectiveness (e.g., user growth, APY).  
6. **Compliance**  
   - Regulatory adherence and audit status.  

## Constraints  
- ID must follow `p07_rwm_{{name}}.md` format.  
- `reward_type` must be one of: "token", "fiat", "utility".  
- `apy_range` must be a valid percentage range (e.g., "5%-10%").  
- `distribution_mechanism` must be one of: "staking", "airdrop", "referral".  
- Minimum stake must be ≥ 0.  
- All timestamps must be ISO 8601 compliant.
