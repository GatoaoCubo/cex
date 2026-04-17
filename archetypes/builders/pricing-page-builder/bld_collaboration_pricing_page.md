---
kind: collaboration
id: bld_collaboration_pricing_page
pillar: P12
llm_function: COLLABORATE
purpose: How pricing_page-builder works in crews with other builders
quality: 8.9
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
| Builder                      | What                              | Format  |  
|------------------------------|-----------------------------------|---------|  
| content_monetization-builder | Tier pricing data, feature gating spec | YAML |  
| landing_page-builder         | Hero section copy + brand context | YAML    |  
| referral_program-builder     | Upgrade CTA copy variants (A/B)   | YAML    |  

## Produces For  
| Builder                      | What                              | Format  |  
|------------------------------|-----------------------------------|---------|  
| landing_page-builder         | Pricing section embed (tier table + CTAs) | YAML |  
| content_monetization-builder | Tier comparison UI spec + most-popular badge logic | YAML |  
| onboarding_flow-builder      | Post-sign-up upgrade nudge copy   | YAML    |  

## Boundary  
Does NOT handle subscription billing logic (content_monetization-builder), landing_page hero content (landing_page-builder), or payment gateway integration. Pricing page is UI + copy only; business logic lives in monetization layer.
