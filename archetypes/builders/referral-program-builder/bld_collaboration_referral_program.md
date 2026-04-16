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
