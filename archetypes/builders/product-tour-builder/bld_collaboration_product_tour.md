---
kind: collaboration
id: bld_collaboration_product_tour
pillar: P12
llm_function: COLLABORATE
purpose: How product_tour-builder works in crews with other builders
quality: 8.9
title: "Collaboration Product Tour"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [product_tour, builder, collaboration]
tldr: "How product_tour-builder works in crews with other builders"
domain: "product_tour construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Designs and manages non-interactive product tours to educate users on key features without sales or activation focus.  

## Receives From  
| Builder     | What                  | Format      |  
|-------------|-----------------------|-------------|  
| Content Team| Feature descriptions  | Markdown    |  
| Design Team | Visual assets         | PNG/SVG     |  
| Engineering | Technical constraints | JSON spec   |  

## Produces For  
| Builder     | What                  | Format      |  
|-------------|-----------------------|-------------|  
| Engineering | Tour implementation   | JSON        |  
| Design Team | Storyboard            | Figma       |  
| Support Team| User guide            | PDF         |  

## Boundary  
Does NOT handle interactive demos (sales) or onboarding flows (activation). Interactive demos are managed by `interactive_demo-builder`; onboarding flows by `onboarding_flow-builder`. Technical implementation is handled by Engineering, not this builder.
