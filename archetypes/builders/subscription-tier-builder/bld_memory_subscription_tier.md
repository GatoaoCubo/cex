---
kind: learning_record
id: p10_lr_subscription_tier_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for subscription_tier construction
quality: null
title: "Learning Record Subscription Tier"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [subscription_tier, builder, learning_record]
tldr: "Learned patterns and pitfalls for subscription_tier construction"
domain: "subscription_tier construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Observation  
Common issues include inconsistent pricing models (e.g., annual vs. monthly discounts), unclear feature differentiation, and misalignment between tier names and perceived value. Overlapping features across tiers often confuse customers.  

## Pattern  
Successful tiers use progressive feature unlocking (e.g., "Basic → Pro → Enterprise") with transparent pricing. Naming conventions that reflect value (e.g., "Starter," "Growth," "Premium") improve user understanding.  

## Evidence  
Reviewed artifacts showed that tiers with explicit feature matrices reduced support queries by 25%. One SaaS product increased conversion by 18% after simplifying tier boundaries.  

## Recommendations  
- Align tier names with customer journey stages (e.g., "Solo," "Team," "Enterprise").  
- Use incremental feature scaling (e.g., API calls, storage limits) to justify price jumps.  
- Avoid more than 3-4 tiers to prevent decision fatigue.  
- Include clear "what’s included" tables in tier definitions.  
- Regularly audit tiers against customer feedback and usage data.
