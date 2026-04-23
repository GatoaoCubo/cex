---
kind: collaboration
id: bld_collaboration_ecommerce_vertical
pillar: P12
llm_function: COLLABORATE
purpose: How ecommerce_vertical-builder works in crews with other builders
quality: 8.9
title: "Collaboration Ecommerce Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [ecommerce_vertical, builder, collaboration]
tldr: "How ecommerce_vertical-builder works in crews with other builders"
domain: "ecommerce_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_kind
  - kind-builder
  - bld_collaboration_builder
  - bld_collaboration_integration_guide
  - bld_collaboration_cohort_analysis
  - bld_collaboration_response_format
  - bld_collaboration_retriever
  - bld_collaboration_prompt_technique
  - bld_collaboration_rbac_policy
  - bld_collaboration_role_assignment
---

## Crew Role  
Assembles and maintains vertical-specific ecommerce capabilities (product catalogs, inventory, order processing), ensuring integration with frontend and backend systems.  

## Receives From  
| Builder | What | Format |  
|---|---|---|  
| Product Catalog Builder | Product data | JSON |  
| Inventory Management Builder | Stock updates | API |  
| Customer Data Builder | Customer info | CSV |  

## Produces For  
| Builder | What | Format |  
|---|---|---|  
| Frontend Builder | Product catalog | XML |  
| Notification Builder | Order confirmation | Webhook |  
| Analytics Builder | Inventory reports | CSV |  

## Boundary  
Does NOT handle payments (fintech_vertical), user authentication (security_builder), or shipping logistics (logistics_builder).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | upstream | 0.33 |
| [[kind-builder]] | upstream | 0.30 |
| [[bld_collaboration_builder]] | sibling | 0.28 |
| [[bld_collaboration_integration_guide]] | sibling | 0.27 |
| [[bld_collaboration_cohort_analysis]] | sibling | 0.26 |
| [[bld_collaboration_response_format]] | sibling | 0.26 |
| [[bld_collaboration_retriever]] | sibling | 0.25 |
| [[bld_collaboration_prompt_technique]] | sibling | 0.25 |
| [[bld_collaboration_rbac_policy]] | sibling | 0.25 |
| [[bld_collaboration_role_assignment]] | sibling | 0.24 |
