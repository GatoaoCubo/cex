---
kind: collaboration
id: bld_collaboration_subscription_tier
pillar: P12
llm_function: COLLABORATE
purpose: How subscription_tier-builder works in crews with other builders
quality: 8.9
title: "Collaboration Subscription Tier"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [subscription_tier, builder, collaboration]
tldr: "How subscription_tier-builder works in crews with other builders"
domain: "subscription_tier construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_integration_guide
  - bld_collaboration_white_label_config
  - bld_collaboration_cohort_analysis
  - bld_collaboration_reward_model
  - bld_collaboration_ab_test_config
  - subscription-tier-builder
  - bld_collaboration_sandbox_spec
  - bld_collaboration_pricing_page
  - bld_collaboration_reranker_config
  - pricing-page-builder
---

## Crew Role  
Defines subscription pricing structures, benefits, and access levels. Collaborates with product, billing, and analytics teams to align tiers with business goals and user needs.  

## Receives From  
| Builder        | What                  | Format  |  
|----------------|-----------------------|---------|  
| Pricing Strategy | Tier configuration inputs | JSON    |  
| Product Team   | Feature access mappings | YAML    |  
| Billing Team   | Payment plan details  | CSV     |  

## Produces For  
| Builder        | What                  | Format  |  
|----------------|-----------------------|---------|  
| Pricing Page   | Tier definitions      | JSON    |  
| Analytics Team | Tier performance data | CSV     |  
| Customer Support | Tier documentation  | Markdown|  

## Boundary  
Does NOT handle content monetization strategies (Content Team) or pricing page UI (UI Team). Billing integration is handled by Billing Team.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_integration_guide]] | sibling | 0.39 |
| [[bld_collaboration_white_label_config]] | sibling | 0.37 |
| [[bld_collaboration_cohort_analysis]] | sibling | 0.36 |
| [[bld_collaboration_reward_model]] | sibling | 0.36 |
| [[bld_collaboration_ab_test_config]] | sibling | 0.35 |
| [[subscription-tier-builder]] | upstream | 0.35 |
| [[bld_collaboration_sandbox_spec]] | sibling | 0.33 |
| [[bld_collaboration_pricing_page]] | sibling | 0.32 |
| [[bld_collaboration_reranker_config]] | sibling | 0.31 |
| [[pricing-page-builder]] | upstream | 0.30 |
