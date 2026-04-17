---
kind: collaboration
id: bld_collaboration_sales_playbook
pillar: P12
llm_function: COLLABORATE
purpose: How sales_playbook-builder works in crews with other builders
quality: 8.9
title: "Collaboration Sales Playbook"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sales_playbook, builder, collaboration]
tldr: "How sales_playbook-builder works in crews with other builders"
domain: "sales_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Coordinates creation and maintenance of sales playbooks, aligning strategies, customer insights, and templated content into actionable guides for sales teams.  

## Receives From  
| Builder       | What               | Format   |  
|---------------|--------------------|----------|  
| Strategist    | Strategy outline   | JSON     |  
| Researcher    | Customer data      | CSV      |  
| Content_Creator | Template assets  | Markdown |  

## Produces For  
| Builder       | What               | Format   |  
|---------------|--------------------|----------|  
| Sales_Playbook | Final playbook document | PDF      |  
| Strategist    | Summary report     | JSON     |  
| Manager       | Draft for approval | Markdown |  

## Boundary  
Does NOT design pitch decks (handled by `pitch_deck-builder`) or generate discovery questions (handled by `discovery_questions-builder`). Final approvals and legal reviews are managed by the Manager role.
