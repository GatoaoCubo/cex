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
related:
  - bld_collaboration_discovery_questions
  - bld_collaboration_analyst_briefing
  - bld_collaboration_case_study
  - bld_collaboration_customer_segment
  - bld_collaboration_prompt_technique
  - bld_collaboration_app_directory_entry
  - bld_collaboration_agent_computer_interface
  - bld_collaboration_agent_profile
  - sales-playbook-builder
  - bld_collaboration_dataset_card
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_discovery_questions]] | sibling | 0.33 |
| [[bld_collaboration_analyst_briefing]] | sibling | 0.28 |
| [[bld_collaboration_case_study]] | sibling | 0.27 |
| [[bld_collaboration_customer_segment]] | sibling | 0.27 |
| [[bld_collaboration_prompt_technique]] | sibling | 0.26 |
| [[bld_collaboration_app_directory_entry]] | sibling | 0.26 |
| [[bld_collaboration_agent_computer_interface]] | sibling | 0.26 |
| [[bld_collaboration_agent_profile]] | sibling | 0.26 |
| [[sales-playbook-builder]] | upstream | 0.25 |
| [[bld_collaboration_dataset_card]] | sibling | 0.25 |
