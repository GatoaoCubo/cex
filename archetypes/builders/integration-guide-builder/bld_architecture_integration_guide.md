---
kind: architecture
id: bld_architecture_integration_guide
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of integration_guide -- inventory, dependencies
quality: 9.0
title: "Architecture Integration Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [integration_guide, builder, architecture]
tldr: "Component map of integration_guide -- inventory, dependencies"
domain: "integration_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_user_journey
  - bld_architecture_partner_listing
  - bld_architecture_course_module
  - bld_architecture_case_study
  - bld_architecture_onboarding_flow
  - bld_architecture_quickstart_guide
  - bld_architecture_app_directory_entry
  - bld_architecture_discovery_questions
  - bld_architecture_api_reference
  - bld_architecture_github_issue_template
---

## Component Inventory
| ISO Name              | Role                          | Pillar | Status |
|-----------------------|-------------------------------|--------|--------|
| bld_manifest          | Defines integration structure | P05    | Active |
| bld_instruction       | Specifies execution logic     | P05    | Active |
| bld_system_prompt     | Sets LLM interaction rules    | P05    | Active |
| bld_schema            | Defines data format standards | P05    | Active |
| bld_quality_gate      | Enforces quality criteria     | P05    | Active |
| bld_output_template   | Structures final deliverables | P05    | Active |
| bld_examples          | Provides sample implementations | P05    | Active |
| bld_knowledge_card    | Stores domain-specific info   | P05    | Active |
| bld_architecture      | Defines system topology       | P05    | Active |
| bld_collaboration     | Manages team coordination     | P05    | Active |
| bld_config            | Handles runtime parameters    | P05    | Active |
| bld_memory            | Maintains state context       | P05    | Active |
| bld_tools             | Integrates external utilities | P05    | Active |

## Dependencies
| From              | To                  | Type        |
|-------------------|---------------------|-------------|
| bld_manifest      | bld_config          | configuration|
| bld_instruction   | bld_system_prompt   | data        |
| bld_quality_gate  | bld_schema          | validation  |
| bld_output_template | bld_examples      | content     |
| bld_tools         | external_code_linter| tooling     |

## Architectural Position
The integration_guide serves as the central framework for standardizing integration processes within the CEX P05 ecosystem, ensuring consistent quality, reusable components, and aligned collaboration across technical and operational domains.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_user_journey]] | sibling | 0.85 |
| [[bld_architecture_partner_listing]] | sibling | 0.83 |
| [[bld_architecture_course_module]] | sibling | 0.82 |
| [[bld_architecture_case_study]] | sibling | 0.82 |
| [[bld_architecture_onboarding_flow]] | sibling | 0.67 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.64 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.63 |
| [[bld_architecture_discovery_questions]] | sibling | 0.62 |
| [[bld_architecture_api_reference]] | sibling | 0.61 |
| [[bld_architecture_github_issue_template]] | sibling | 0.61 |
