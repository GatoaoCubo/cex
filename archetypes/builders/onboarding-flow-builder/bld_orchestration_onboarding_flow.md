---
kind: collaboration
id: bld_collaboration_onboarding_flow
pillar: P12
llm_function: COLLABORATE
purpose: How onboarding_flow-builder works in crews with other builders
quality: 8.9
title: "Collaboration Onboarding Flow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [onboarding_flow, builder, collaboration]
tldr: "How onboarding_flow-builder works in crews with other builders"
domain: "onboarding_flow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_onboarding_flow_builder
  - bld_knowledge_card_onboarding_flow
  - onboarding-flow-builder
  - quickstart-guide-builder
  - bld_architecture_agent_profile
  - bld_collaboration_agentic_rag
  - bld_instruction_onboarding_flow
  - bld_collaboration_product_tour
  - bld_collaboration_user_journey
  - bld_collaboration_sso_config
---

## Crew Role  
Orchestrates activation steps, validates prerequisites, and triggers system readiness checks for new users or entities.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| User Onboarding | Initial user data     | JSON        |  
| Config Service  | Activation rules      | YAML        |  
| Auth Service    | Authentication token  | JWT         |  

## Produces For  
| Builder         | What                    | Format      |  
|-----------------|-------------------------|-------------|  
| User Profile    | Activated user state    | JSON        |  
| Notification    | Onboarding confirmation | Email       |  
| Analytics       | Activation event        | Event       |  

## Boundary  
Does NOT handle long-term user data storage (User Profile Service), authentication (Auth Service), or post-activation workflows (Workflow Engine).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_onboarding_flow_builder]] | upstream | 0.27 |
| [[bld_knowledge_card_onboarding_flow]] | upstream | 0.27 |
| [[onboarding-flow-builder]] | upstream | 0.25 |
| [[quickstart-guide-builder]] | upstream | 0.24 |
| [[bld_architecture_agent_profile]] | upstream | 0.23 |
| [[bld_collaboration_agentic_rag]] | sibling | 0.22 |
| [[bld_instruction_onboarding_flow]] | upstream | 0.21 |
| [[bld_collaboration_product_tour]] | sibling | 0.21 |
| [[bld_collaboration_user_journey]] | sibling | 0.20 |
| [[bld_collaboration_sso_config]] | sibling | 0.20 |
