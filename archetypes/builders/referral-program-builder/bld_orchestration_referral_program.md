---
kind: collaboration
id: bld_collaboration_referral_program
pillar: P12
llm_function: COLLABORATE
purpose: How referral_program-builder works in crews with other builders
quality: 8.9
title: "Collaboration Referral Program"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [referral_program, builder, collaboration]
tldr: "How referral_program-builder works in crews with other builders"
domain: "referral_program construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_pricing_page
  - bld_architecture_kind
  - kind-builder
  - bld_collaboration_builder
  - bld_collaboration_rbac_policy
  - p03_sp_referral_program_builder
  - bld_collaboration_model_card
  - bld_collaboration_reward_signal
  - bld_collaboration_retriever
  - bld_collaboration_response_format
---

## Crew Role  
Designs and manages referral program logic, tracking, and integration with external systems.  

## Receives From  
| Builder                   | What                              | Format  |  
|---------------------------|-----------------------------------|---------|  
| content_monetization-builder | Pricing tier data (LTV, CAC ratios) | YAML  |  
| landing_page-builder      | Campaign landing page spec        | YAML    |  
| onboarding_flow-builder   | Aha-moment trigger points for invite hooks | YAML |  

## Produces For  
| Builder                   | What                              | Format  |  
|---------------------------|-----------------------------------|---------|  
| landing_page-builder      | Referral CTA copy and reward spec | YAML    |  
| onboarding_flow-builder   | Invite hook config (step, trigger, reward) | YAML |  
| content_monetization-builder | Viral k-factor input for revenue model | YAML |  

## Boundary  
Does NOT handle A/B test configurations (experiment_config-builder) or pricing models (content_monetization-builder). Referral program produces the reward spec; monetization determines whether the CAC is sustainable.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_pricing_page]] | sibling | 0.44 |
| [[bld_architecture_kind]] | upstream | 0.32 |
| [[kind-builder]] | upstream | 0.28 |
| [[bld_collaboration_builder]] | sibling | 0.27 |
| [[bld_collaboration_rbac_policy]] | sibling | 0.27 |
| [[p03_sp_referral_program_builder]] | upstream | 0.27 |
| [[bld_collaboration_model_card]] | sibling | 0.26 |
| [[bld_collaboration_reward_signal]] | sibling | 0.26 |
| [[bld_collaboration_retriever]] | sibling | 0.25 |
| [[bld_collaboration_response_format]] | sibling | 0.25 |
