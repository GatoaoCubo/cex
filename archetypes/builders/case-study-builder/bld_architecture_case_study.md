---
kind: architecture
id: bld_architecture_case_study
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of case_study -- inventory, dependencies
quality: 9.0
title: "Architecture Case Study"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [case_study, builder, architecture]
tldr: "Component map of case_study -- inventory, dependencies"
domain: "case_study construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_user_journey
  - bld_architecture_course_module
  - bld_architecture_integration_guide
  - bld_architecture_partner_listing
  - bld_architecture_quickstart_guide
  - bld_architecture_onboarding_flow
  - bld_architecture_app_directory_entry
  - bld_architecture_roi_calculator
  - bld_architecture_api_reference
  - bld_architecture_github_issue_template
---

## Component Inventory
| ISO Name             | Role                          | Pillar | Status  |
|----------------------|-------------------------------|--------|---------|
| bld_manifest         | Case study structure definition | P05    | Active  |
| bld_instruction      | User guidance specification   | P05    | Active  |
| bld_system_prompt    | LLM interaction framework     | P05    | Active  |
| bld_schema           | Data format validation        | P05    | Active  |
| bld_quality_gate     | Output verification logic     | P05    | Active  |
| bld_output_template  | Result formatting rules       | P05    | Active  |
| bld_examples         | Sample case study repository  | P05    | Active  |
| bld_knowledge_card   | Domain-specific knowledge base| P05    | Active  |
| bld_architecture     | System design documentation   | P05    | Active  |
| bld_collaboration    | Multi-stakeholder workflow    | P05    | Active  |
| bld_config           | Builder parameter management  | P05    | Active  |
| bld_memory           | Session state persistence     | P05    | Active  |
| bld_tools            | External utility integration  | P05    | Active  |

## Dependencies
| From              | To                  | Type         |
|-------------------|---------------------|--------------|
| bld_config        | bld_instruction     | Configuration|
| bld_schema        | bld_quality_gate    | Validation   |
| bld_knowledge_card| bld_examples        | Data source  |
| bld_memory        | bld_collaboration   | State sharing|
| bld_tools         | bld_output_template | External API |

## Architectural Position
case_study acts as a P05 CEX pillar enabler, orchestrating structured knowledge creation through ISO-driven modularity. It bridges domain expertise (via bld_knowledge_card) and technical execution (via bld_tools), ensuring alignment with CEX standards through bld_quality_gate and bld_schema.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_user_journey]] | sibling | 0.86 |
| [[bld_architecture_course_module]] | sibling | 0.84 |
| [[bld_architecture_integration_guide]] | sibling | 0.83 |
| [[bld_architecture_partner_listing]] | sibling | 0.82 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.67 |
| [[bld_architecture_onboarding_flow]] | sibling | 0.65 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.63 |
| [[bld_architecture_roi_calculator]] | sibling | 0.63 |
| [[bld_architecture_api_reference]] | sibling | 0.62 |
| [[bld_architecture_github_issue_template]] | sibling | 0.62 |
