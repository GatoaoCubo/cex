---
kind: schema
id: bld_schema_pricing_page
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for pricing_page
quality: 9.1
title: "Schema Pricing Page"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [pricing_page, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for pricing_page"
domain: "pricing_page construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field      | Type   | Required | Default | Notes                              |  
|------------|--------|----------|---------|------------------------------------|  
| id         | string | yes      | null    | Unique identifier                  |  
| kind       | string | yes      | null    | Always "pricing_page"              |  
| pillar     | string | yes      | null    | Always "P05"                       |  
| title      | string | yes      | null    | Page title                         |  
| version    | string | yes      | null    | Version control (e.g., "v1.0")     |  
| created    | date   | yes      | null    | ISO 8601 format                    |  
| updated    | date   | yes      | null    | ISO 8601 format                    |  
| author     | string | yes      | null    | Author name                        |  
| domain     | string | yes      | null    | "pricing"                          |  
| quality    | null   | yes      | null    | Never self-score; peer review assigns |  
| tags       | array  | yes      | null    | Keywords (e.g., "saas", "freemium", "b2b") |  
| tldr       | string | yes      | null    | Summary of pricing structure       |  
| pricing_model | string | yes | null | "flat", "tiered", "dynamic"        |  
| currency   | string | yes      | null    | ISO 4217 code (e.g., "USD")        |  
| tiers      | array  | yes      | null    | Tiered pricing details             |  

### Recommended  
| Field         | Type   | Notes                          |  
|---------------|--------|--------------------------------|  
| last_reviewed | date   | Last peer review date          |  
| source_url    | string | Link to pricing source         |  
| notes         | string | Additional context or comments |  

## ID Pattern  
^p05_pp_[a-z][a-z0-9_]+.md$  

## Body Structure  
1. **Overview**  
   - Description of pricing page purpose and scope.  
2. **Pricing Tiers**  
   - Detailed breakdown of pricing levels, features, and limits.  
3. **Currency & Fees**  
   - Supported currencies, conversion rates, and transaction fees.  
4. **Subscription Models**  
   - Billing cycles, discounts, and recurring charges.  
5. **Terms & Conditions**  
   - Legal terms, validity periods, and disclaimers.  

## Constraints  
- All pricing data must be sourced from verified, up-to-date records.  
- Tiers must be ordered by ascending value and clearly labeled.  
- Currency codes must adhere to ISO 4217 standards.  
- Subscription models must specify renewal intervals and cancellation policies.  
- Terms must include compliance with local financial regulations.  
- File size must not exceed 6144 bytes.
