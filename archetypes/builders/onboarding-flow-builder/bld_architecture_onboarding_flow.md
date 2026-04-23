---
kind: architecture
id: bld_architecture_onboarding_flow
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of onboarding_flow -- inventory, dependencies
quality: 9.0
title: "Architecture Onboarding Flow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [onboarding_flow, builder, architecture]
tldr: "Component map of onboarding_flow -- inventory, dependencies"
domain: "onboarding_flow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_discovery_questions
  - bld_architecture_sdk_example
  - bld_architecture_roi_calculator
  - bld_architecture_api_reference
  - bld_architecture_quickstart_guide
  - bld_architecture_legal_vertical
  - bld_architecture_sales_playbook
  - bld_architecture_benchmark_suite
  - bld_architecture_app_directory_entry
  - bld_architecture_fintech_vertical
---

## Component Inventory
| ISO Name           | Role                          | Pillar | Status  |
|--------------------|-------------------------------|--------|---------|
| bld_manifest       | Defines flow structure        | P05    | Active  |
| bld_instruction    | Specifies user steps          | P03    | Active  |
| bld_system_prompt  | Sets AI behavior              | P03    | Active  |
| bld_schema         | Defines data structure        | P06    | Active  |
| bld_quality_gate   | Enforces compliance rules     | P11    | Active  |
| bld_output_template| Formats final output          | P05    | Active  |
| bld_examples       | Provides sample interactions  | P07    | Active  |
| bld_knowledge_card | Stores domain-specific info   | P01    | Active  |
| bld_architecture   | Outlines system blueprint     | P08    | Active  |
| bld_collaboration  | Manages user-AI interaction   | P12    | Active  |
| bld_config         | Centralizes configuration     | P09    | Active  |
| bld_memory         | Tracks session context        | P10    | Active  |
| bld_tools          | Integrates external functions | P04    | Active  |

## Dependencies
| From              | To                  | Type         |
|-------------------|---------------------|--------------|
| bld_manifest      | bld_schema          | Data         |
| bld_instruction   | bld_system_prompt   | Control      |
| bld_quality_gate  | bld_config          | Configuration|
| bld_output_template | bld_schema        | Data         |
| bld_tools         | External Auth       | Integration  |
| bld_memory        | bld_config          | Configuration|

## Architectural Position
The onboarding_flow is a foundational element in P05, enabling seamless user integration through structured, compliant, and personalized onboarding processes. It acts as a bridge between user expectations and system capabilities, ensuring alignment with CEX pillar goals of trust, efficiency, and scalability.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_discovery_questions]] | sibling | 0.75 |
| [[bld_architecture_sdk_example]] | sibling | 0.73 |
| [[bld_architecture_roi_calculator]] | sibling | 0.73 |
| [[bld_architecture_api_reference]] | sibling | 0.72 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.72 |
| [[bld_architecture_legal_vertical]] | sibling | 0.71 |
| [[bld_architecture_sales_playbook]] | sibling | 0.70 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.70 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.70 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.68 |
