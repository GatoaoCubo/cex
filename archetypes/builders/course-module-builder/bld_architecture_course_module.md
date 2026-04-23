---
kind: architecture
id: bld_architecture_course_module
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of course_module -- inventory, dependencies
quality: 9.0
title: "Architecture Course Module"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [course_module, builder, architecture]
tldr: "Component map of course_module -- inventory, dependencies"
domain: "course_module construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_user_journey
  - bld_architecture_partner_listing
  - bld_architecture_case_study
  - bld_architecture_integration_guide
  - bld_architecture_app_directory_entry
  - bld_architecture_quickstart_guide
  - bld_architecture_api_reference
  - bld_architecture_onboarding_flow
  - bld_architecture_github_issue_template
  - bld_architecture_roi_calculator
---

## Component Inventory
| ISO Name             | Role                          | Pillar | Status |
|----------------------|-------------------------------|--------|--------|
| bld_manifest         | Core definition               | P05    | Active |
| bld_instruction      | Content creation rules        | P05    | Active |
| bld_system_prompt    | AI interaction guidance       | P05    | Active |
| bld_schema           | Structural validation         | P05    | Active |
| bld_quality_gate     | Output verification           | P05    | Active |
| bld_output_template  | Formatting standard           | P05    | Active |
| bld_examples         | Sample content repository     | P05    | Active |
| bld_knowledge_card   | Knowledge encapsulation       | P05    | Active |
| bld_architecture     | Module blueprint              | P05    | Active |
| bld_collaboration    | Team coordination             | P05    | Active |
| bld_config           | Parameter management          | P05    | Active |
| bld_memory           | State retention              | P05    | Active |
| bld_tools            | External tool integration     | P05    | Active |

## Dependencies
| From          | To              | Type       |
|---------------|-----------------|------------|
| bld_manifest  | bld_config      | Configuration |
| bld_instruction | bld_system_prompt | Data Flow |
| bld_quality_gate | bld_schema     | Validation |
| bld_output_template | bld_examples | Template |
| bld_memory    | bld_knowledge_card | Reference |
| bld_tools     | LMS API         | External |

## Architectural Position
The course_module-builder sits at the intersection of P05's knowledge structuring and collaborative learning goals, enabling modular course construction through ISO-driven standardization, quality assurance, and cross-component coordination.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_user_journey]] | sibling | 0.88 |
| [[bld_architecture_partner_listing]] | sibling | 0.85 |
| [[bld_architecture_case_study]] | sibling | 0.85 |
| [[bld_architecture_integration_guide]] | sibling | 0.84 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.66 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.66 |
| [[bld_architecture_api_reference]] | sibling | 0.65 |
| [[bld_architecture_onboarding_flow]] | sibling | 0.64 |
| [[bld_architecture_github_issue_template]] | sibling | 0.63 |
| [[bld_architecture_roi_calculator]] | sibling | 0.62 |
