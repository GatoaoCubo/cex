---
kind: collaboration
id: bld_collaboration_faq_entry
pillar: P12
llm_function: COLLABORATE
purpose: How faq_entry-builder works in crews with other builders
quality: 8.9
title: "Collaboration Faq Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [faq_entry, builder, collaboration]
tldr: "How faq_entry-builder works in crews with other builders"
domain: "faq_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Curates and structures frequently asked questions (FAQs) into standardized entries, ensuring consistency and clarity for end-users.  

## Receives From  
| Builder       | What               | Format   |  
|---------------|--------------------|----------|  
| User Research | Raw user queries   | Text     |  
| Content Team  | Draft FAQ entries  | Markdown |  
| Analytics     | Usage statistics   | JSON     |  

## Produces For  
| Builder       | What               | Format   |  
|---------------|--------------------|----------|  
| Knowledge Base| Structured FAQ entry | Markdown |  
| Support Team  | Ready-to-use answers | JSON     |  
| Content Team  | Entry summary      | Text     |  

## Boundary  
Does NOT handle knowledge_card (broader conceptual explanations) or support_macro (agent-specific canned replies). Those are managed by dedicated builders.
