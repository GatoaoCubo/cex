---
kind: schema
id: bld_schema_referral_program
pillar: P06
llm_function: CONSTRAIN
purpose: Formal schema -- SINGLE SOURCE OF TRUTH for referral_program
quality: 9.1
title: "Schema Referral Program"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [referral_program, builder, schema]
tldr: "Formal schema -- SINGLE SOURCE OF TRUTH for referral_program"
domain: "referral_program construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Frontmatter Fields  
### Required  
| Field      | Type   | Required | Default | Notes                              |  
|------------|--------|----------|---------|------------------------------------|  
| id         | string | yes      | null    | Must match ID Pattern              |  
| kind       | string | yes      | null    | Always "referral_program"          |  
| pillar     | string | yes      | null    | Always "P11"                       |  
| title      | string | yes      | null    | Program name                       |  
| version    | string | yes      | "1.0"   | Schema version                     |  
| created    | date   | yes      | null    | ISO 8601                           |  
| updated    | date   | yes      | null    | ISO 8601                           |  
| author     | string | yes      | null    | Owner                              |  
| domain     | string | yes      | null    | "referral_program"                 |  
| quality    | null   | yes      | null    | Never self-score; peer review assigns |  
| tags       | list   | yes      | []      | Keywords                           |  
| tldr       | string | yes      | null    | One-sentence summary               |  
| referral_rate | float | yes | 0.0 | Percentage of referral earnings |  
| commission_structure | string | yes | null | E.g., "flat", "percentage" |  

### Recommended  
| Field              | Type   | Notes                          |  
|--------------------|--------|--------------------------------|  
| referral_expiry    | date   | Expiration date for referrals  |  
| max_referrals_per_user | int | Limit per user                 |  
| tracking_method    | string | E.g., "UTM", "custom_code"     |  

## ID Pattern  
^p11_rp_[a-z][a-z0-9_]+.yaml$  

## Body Structure  
1. **Program Overview**  
   - Description, objectives, and scope.  
2. **Referral Mechanics**  
   - Eligibility, referral code generation, and usage rules.  
3. **Rewards Structure**  
   - Payout terms, tiers, and commission rates.  
4. **Compliance & Terms**  
   - Legal requirements, anti-fraud policies, and termination clauses.  
5. **Tracking & Analytics**  
   - Metrics, reporting tools, and data privacy considerations.  

## Constraints  
- Referral codes must be unique and non-reusable.  
- Commission rates must not exceed 20% of transaction value.  
- All users must agree to terms before participating.  
- Program data must be auditable and transparent.  
- Referral expiry dates must be at least 30 days from creation.  
- YAML file size must not exceed 4096 bytes.
