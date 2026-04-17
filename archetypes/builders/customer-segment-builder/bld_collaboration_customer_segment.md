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
