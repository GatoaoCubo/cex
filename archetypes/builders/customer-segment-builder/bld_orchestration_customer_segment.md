---
kind: collaboration
id: bld_collaboration_customer_segment
pillar: P12
llm_function: COLLABORATE
purpose: How customer_segment-builder works in crews with other builders
quality: 8.9
title: "Collaboration Customer Segment"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [customer_segment, builder, collaboration]
tldr: "How customer_segment-builder works in crews with other builders"
domain: "customer_segment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - customer-segment-builder
  - kc_customer_segment
  - bld_collaboration_competitive_matrix
  - p02_qg_customer_segment
  - p03_sp_customer_segment_builder
  - bld_collaboration_discovery_questions
  - bld_knowledge_card_customer_segment
  - bld_collaboration_sales_playbook
  - bld_collaboration_action_paradigm
  - bld_collaboration_cohort_analysis
---

## Crew Role  
Defines and refines customer segments based on ICP (Ideal Customer Profile) data, ensuring alignment with business goals and market realities. Collaborates with product, marketing, and sales to validate segment relevance.  

## Receives From  
| Builder       | What                  | Format  |  
|---------------|-----------------------|---------|  
| ICP_Definer   | ICP criteria          | JSON    |  
| Support_Team  | Customer feedback     | CSV     |  
| Marketing_Team| Market research       | PDF     |  

## Produces For  
| Builder       | What                  | Format  |  
|---------------|-----------------------|---------|  
| Product_Team  | Refined segments      | JSON    |  
| Sales_Team    | Segment reports       | PDF     |  
| Persona_Builder| Segment inputs      | CSV     |  

## Boundary  
Does NOT collect raw data (handled by Data_Engineers), validate ICP criteria (handled by ICP_Validation_Team), or execute campaigns (handled by Marketing_Team).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[customer-segment-builder]] | upstream | 0.42 |
| [[kc_customer_segment]] | upstream | 0.38 |
| [[bld_collaboration_competitive_matrix]] | sibling | 0.36 |
| [[p02_qg_customer_segment]] | upstream | 0.30 |
| [[p03_sp_customer_segment_builder]] | upstream | 0.30 |
| [[bld_collaboration_discovery_questions]] | sibling | 0.28 |
| [[bld_knowledge_card_customer_segment]] | upstream | 0.27 |
| [[bld_collaboration_sales_playbook]] | sibling | 0.27 |
| [[bld_collaboration_action_paradigm]] | sibling | 0.26 |
| [[bld_collaboration_cohort_analysis]] | sibling | 0.26 |
