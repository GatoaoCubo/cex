---
kind: instruction
id: bld_instruction_subscription_tier
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for subscription_tier
quality: 8.9
title: "Instruction Subscription Tier"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [subscription_tier, builder, instruction]
tldr: "Step-by-step production process for subscription_tier"
domain: "subscription_tier construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Analyze market trends for SaaS pricing models (e.g., freemium, tiered).  
2. Benchmark competitors’ subscription tiers for feature parity and pricing.  
3. Identify core features to include in each tier (e.g., API calls, storage limits).  
4. Prioritize features based on customer value and technical feasibility.  
5. Segment target users by usage patterns (light, medium, enterprise).  
6. Review legal requirements for pricing (e.g., tax compliance, refund policies).  

## Phase 2: COMPOSE  
1. Define tier name using SCHEMA.md’s `name` field (e.g., “Basic”, “Pro”).  
2. Set pricing structure with `price_id`, `currency`, and `recurring_interval`.  
3. Map features to tiers in `feature_matrix` (e.g., “unlimited users” → “Pro”).  
4. Specify constraints via `constraints` (e.g., “max 100 API calls/month”).  
5. Link to payment gateway configurations in `external_ids`.  
6. Add tier description using OUTPUT_TEMPLATE.md’s `summary` section.  
7. Validate feature dependencies (e.g., “Pro” requires “Basic” features).  
8. Document onboarding workflows for each tier in `user_journey`.  
9. Finalize artifact with metadata from SCHEMA.md’s `created_at` and `updated_at`.  

## Phase 3: VALIDATE  
- [ ] ✅ Check schema compliance via JSON schema validator.  
- [ ] ✅ Confirm pricing consistency across all tiers and currencies.  
- [ ] ✅ Ensure feature matrix aligns with technical implementation.  
- [ ] ✅ Verify constraint enforcement logic in backend systems.  
- [ ] ✅ Conduct user testing with sample tier configurations.
