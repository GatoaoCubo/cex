---
kind: architecture
id: bld_architecture_referral_program
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of referral_program -- inventory, dependencies
quality: 9.0
title: "Architecture Referral Program"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [referral_program, builder, architecture]
tldr: "Component map of referral_program -- inventory, dependencies"
domain: "referral_program construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_onboarding_flow
  - bld_architecture_discovery_questions
  - bld_architecture_roi_calculator
  - bld_architecture_api_reference
  - bld_architecture_sdk_example
  - bld_architecture_quickstart_guide
  - bld_architecture_sales_playbook
  - bld_architecture_legal_vertical
  - bld_architecture_benchmark_suite
  - bld_architecture_app_directory_entry
---

## Component Inventory
| ISO Name             | Role                                      | Pillar | Status |
|----------------------|-------------------------------------------|--------|--------|
| bld_manifest         | Defines program structure and metadata    | P05    | Active |
| bld_instruction      | Encodes referral logic and rules        | P03    | Active |
| bld_system_prompt    | Sets AI behavior for program execution  | P03    | Active |
| bld_schema           | Validates data formats and structures   | P06    | Active |
| bld_quality_gate     | Enforces compliance and accuracy checks | P11    | Active |
| bld_output_template  | Formats referral program outputs        | P05    | Active |
| bld_examples         | Provides sample referral scenarios      | P07    | Active |
| bld_knowledge_card   | Stores domain-specific referral knowledge | P01    | Active |
| bld_architecture     | Documents system design and components  | P08    | Active |
| bld_collaboration    | Manages stakeholder coordination        | P12    | Active |
| bld_config           | Centralizes program configuration       | P09    | Active |
| bld_memory           | Tracks referral program state           | P10    | Active |
| bld_tools            | Integrates external referral utilities  | P04    | Active |

## Dependencies
| From              | To                  | Type       |
|-------------------|---------------------|------------|
| bld_manifest      | bld_config          | Configuration |
| bld_instruction   | bld_system_prompt   | Data       |
| bld_quality_gate  | bld_schema          | Validation |
| bld_output_template | bld_examples     | Data       |
| bld_tools         | bld_memory          | Storage    |
| bld_collaboration | bld_knowledge_card  | Reference  |

## Architectural Position
The referral_program serves as a collaborative framework within the CEX P11 pillar, enabling structured configuration, knowledge sharing, and quality assurance through integrated components like bld_config, bld_knowledge_card, and bld_quality_gate, ensuring alignment with ecosystem standards and user expectations.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_onboarding_flow]] | sibling | 0.73 |
| [[bld_architecture_discovery_questions]] | sibling | 0.72 |
| [[bld_architecture_roi_calculator]] | sibling | 0.72 |
| [[bld_architecture_api_reference]] | sibling | 0.71 |
| [[bld_architecture_sdk_example]] | sibling | 0.70 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.70 |
| [[bld_architecture_sales_playbook]] | sibling | 0.69 |
| [[bld_architecture_legal_vertical]] | sibling | 0.69 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.68 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.67 |
