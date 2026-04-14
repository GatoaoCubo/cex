---
kind: schema
id: bld_schema_subscription_tier
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for subscription_tier
quality: null
title: "Schema Subscription Tier"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [subscription_tier, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for subscription_tier"
domain: "subscription_tier construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field      | Type       | Required | Default | Notes                              |  
|------------|------------|----------|---------|------------------------------------|  
| id         | string     | yes      | null    | Must match ID Pattern              |  
| kind       | string     | yes      | null    | Always "subscription_tier"         |  
| pillar     | string     | yes      | null    | Always "P11"                       |  
| title      | string     | yes      | null    | Human-readable name                |  
| version    | integer    | yes      | 1       | Schema version                     |  
| created    | datetime   | yes      | null    | ISO 8601                           |  
| updated    | datetime   | yes      | null    | ISO 8601                           |  
| author     | string     | yes      | null    | Creator identifier                 |  
| domain     | string     | yes      | null    | "subscription_tier"                |  
| quality    | null       | yes      | null    | Never self-score; peer review assigns |  
| tags       | list       | yes      | []      | Keywords for categorization        |  
| tldr       | string     | yes      | null    | Summary of tier benefits           |  
| tier_level | string     | yes      | null    | "bronze", "silver", "gold", etc.   |  
| benefits   | list       | yes      | []      | Perks included in tier             |  
| price      | object     | yes      | {}      | { "currency": "USD", "amount": 9.99 } |  
| exclusive_content | bool | yes      | false   | Access to premium materials        |  

### Recommended  
| Field          | Type   | Notes                          |  
|----------------|--------|--------------------------------|  
| currency       | string | ISO 4217 code (e.g., "USD")    |  
| max_users      | integer| Limit for concurrent users     |  
| trial_period   | integer| Days before charge             |  
| renewal_policy | string | "monthly", "yearly", "one-time" |  

## ID Pattern  
^p11_st_[a-z][a-z0-9_]+.yaml$  

## Body Structure  
1. **Tier Level**: Define the subscription level (e.g., "gold").  
2. **Benefits**: List features or services included.  
3. **Pricing**: Specify cost structure and currency.  
4. **Exclusive Content**: Boolean flag for premium access.  
5. **Trial Period**: Duration of free trial (if applicable).  
6. **Renewal Policy**: Frequency of billing cycles.  

## Constraints  
- Tier_level must be one of: "bronze", "silver", "gold", "platinum".  
- Price must include "currency" and "amount" fields.  
- Benefits must be a non-empty list of strings.  
- Exclusive_content must be a boolean.  
- Trial_period must be ≥ 0 if specified.  
- Renewal_policy must be "monthly", "yearly", or "one-time".
