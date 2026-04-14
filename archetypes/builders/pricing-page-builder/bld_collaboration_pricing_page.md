---
kind: collaboration
id: bld_collaboration_pricing_page
pillar: P12
llm_function: COLLABORATE
purpose: How pricing_page-builder works in crews with other builders
quality: null
title: "Collaboration Pricing Page"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [pricing_page, builder, collaboration]
tldr: "How pricing_page-builder works in crews with other builders"
domain: "pricing_page construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Designs and builds interactive pricing page UI components, ensuring alignment with brand guidelines and user experience standards. Coordinates with data and marketing teams for integration.  

## Receives From  
| Builder              | What                  | Format      |  
|---------------------|-----------------------|-------------|  
| subscription_tier   | Tier data             | JSON        |  
| design_system       | UI component specs    | Figma       |  
| analytics           | Usage statistics      | CSV         |  

## Produces For  
| Builder              | What                  | Format      |  
|---------------------|-----------------------|-------------|  
| subscription_tier   | Configurable tier UI  | React       |  
| marketing           | Embeddable pricing UI | HTML/CSS    |  
| analytics           | Event tracking code   | JavaScript  |  

## Boundary  
Does NOT handle subscription_tier data modeling (subscription_tier_builder), landing_page content (landing_page_builder), or payment processing (payment_gateway_builder).
