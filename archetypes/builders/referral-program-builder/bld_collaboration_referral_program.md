---
kind: collaboration
id: bld_collaboration_referral_program
pillar: P12
llm_function: COLLABORATE
purpose: How referral_program-builder works in crews with other builders
quality: null
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
| Builder         | What               | Format  |  
|-----------------|--------------------|---------|  
| Referral Designer | Program rules      | JSON    |  
| Data Engineer   | User data          | CSV     |  
| Marketing Team  | Campaign details   | YAML    |  

## Produces For  
| Builder             | What               | Format  |  
|---------------------|--------------------|---------|  
| Referral Program Manager | Program config   | JSON    |  
| Analytics Team      | Referral stats     | CSV     |  
| User Interface Team | UI components      | Figma   |  

## Boundary  
Does NOT handle A/B testing (ab_test_config) or pricing models (content_monetization). A/B testing is managed by Experiment Engineers; pricing is handled by Monetization Specialists.
