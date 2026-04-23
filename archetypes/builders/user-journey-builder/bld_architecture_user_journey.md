---
kind: architecture
id: bld_architecture_user_journey
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of user_journey -- inventory, dependencies
quality: 9.0
title: "Architecture User Journey"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [user_journey, builder, architecture]
tldr: "Component map of user_journey -- inventory, dependencies"
domain: "user_journey construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_course_module
  - bld_architecture_partner_listing
  - bld_architecture_integration_guide
  - bld_architecture_case_study
  - bld_architecture_quickstart_guide
  - bld_architecture_onboarding_flow
  - bld_architecture_app_directory_entry
  - bld_architecture_api_reference
  - bld_architecture_github_issue_template
  - bld_architecture_roi_calculator
---

## Component Inventory
| ISO Name             | Role                     | Pillar | Status  |
|----------------------|--------------------------|--------|---------|
| bld_manifest         | Core configuration       | P05    | Active  |
| bld_instruction      | Task definition          | P05    | Active  |
| bld_system_prompt    | LLM guidance             | P05    | Active  |
| bld_schema           | Data structure           | P05    | Active  |
| bld_quality_gate     | Validation rules         | P05    | Active  |
| bld_output_template  | Formatting rules         | P05    | Active  |
| bld_examples         | Sample content           | P05    | Active  |
| bld_knowledge_card   | Context repository       | P05    | Active  |
| bld_architecture     | Structural blueprint     | P05    | Active  |
| bld_collaboration    | Multi-agent coordination | P05    | Active  |
| bld_config           | Runtime parameters       | P05    | Active  |
| bld_memory           | State persistence        | P05    | Active  |
| bld_tools            | External integration     | P05    | Active  |

## Dependencies
| From              | To                  | Type       |
|-------------------|---------------------|------------|
| bld_manifest      | bld_config          | Config     |
| bld_instruction   | bld_system_prompt   | Dependency |
| bld_quality_gate  | bld_schema          | Validation |
| bld_output_template | bld_examples     | Template   |
| bld_memory        | external DB         | External   |

## Architectural Position
User_journey is the central orchestrator in P05, translating abstract user needs into executable workflows via ISOs like bld_instruction and bld_schema, while ensuring consistency through bld_quality_gate and bld_config, and integrating external systems via bld_tools.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_course_module]] | sibling | 0.86 |
| [[bld_architecture_partner_listing]] | sibling | 0.86 |
| [[bld_architecture_integration_guide]] | sibling | 0.85 |
| [[bld_architecture_case_study]] | sibling | 0.85 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.66 |
| [[bld_architecture_onboarding_flow]] | sibling | 0.66 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.65 |
| [[bld_architecture_api_reference]] | sibling | 0.64 |
| [[bld_architecture_github_issue_template]] | sibling | 0.63 |
| [[bld_architecture_roi_calculator]] | sibling | 0.63 |
