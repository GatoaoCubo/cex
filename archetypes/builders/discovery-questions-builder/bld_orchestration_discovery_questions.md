---
kind: collaboration
id: bld_collaboration_discovery_questions
pillar: P12
llm_function: COLLABORATE
purpose: How discovery_questions-builder works in crews with other builders
quality: 8.9
title: "Collaboration Discovery Questions"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [discovery_questions, builder, collaboration]
tldr: "How discovery_questions-builder works in crews with other builders"
domain: "discovery_questions construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_sales_playbook
  - bld_collaboration_compliance_framework
  - bld_collaboration_customer_segment
  - bld_collaboration_action_paradigm
  - bld_collaboration_prompt_technique
  - bld_collaboration_agent_profile
  - bld_collaboration_self_improvement_loop
  - bld_collaboration_eval_framework
  - bld_collaboration_dataset_card
  - discovery-questions-builder
---

## Crew Role  
Facilitates structured discovery by generating targeted questions to uncover customer needs, challenges, and priorities for specific use cases.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Use Case Def  | Use case details      | Document    |  
| Industry Spec | Industry-specific info| JSON        |  
| Customer Feed | Existing feedback     | CSV         |  

## Produces For  
| Builder           | What                    | Format        |  
|-------------------|-------------------------|---------------|  
| Discovery Qs      | Question set            | JSON          |  
| Prioritization    | Question prioritization | Spreadsheet   |  
| Follow-up Guide   | Next steps framework    | Document      |  

## Boundary  
Does NOT generate broad sales strategies (handled by `sales_playbook_builder`) or define ICPs (handled by `customer_segment_builder`). Avoids data analysis or reporting (handled by `data_analysis_builder` and `reporting_builder`).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_sales_playbook]] | sibling | 0.27 |
| [[bld_collaboration_compliance_framework]] | sibling | 0.27 |
| [[bld_collaboration_customer_segment]] | sibling | 0.26 |
| [[bld_collaboration_action_paradigm]] | sibling | 0.24 |
| [[bld_collaboration_prompt_technique]] | sibling | 0.24 |
| [[bld_collaboration_agent_profile]] | sibling | 0.23 |
| [[bld_collaboration_self_improvement_loop]] | sibling | 0.23 |
| [[bld_collaboration_eval_framework]] | sibling | 0.23 |
| [[bld_collaboration_dataset_card]] | sibling | 0.22 |
| [[discovery-questions-builder]] | upstream | 0.22 |
