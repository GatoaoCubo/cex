---
kind: architecture
id: bld_architecture_api_reference
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of api_reference -- inventory, dependencies
quality: 9.0
title: "Architecture Api Reference"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [api_reference, builder, architecture]
tldr: "Component map of api_reference -- inventory, dependencies"
domain: "api_reference construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_roi_calculator
  - bld_architecture_sales_playbook
  - bld_architecture_app_directory_entry
  - bld_architecture_discovery_questions
  - bld_architecture_benchmark_suite
  - bld_architecture_quickstart_guide
  - bld_architecture_legal_vertical
  - bld_architecture_onboarding_flow
  - bld_architecture_sdk_example
  - bld_architecture_fintech_vertical
---

## Component Inventory
| ISO Name              | Role                          | Pillar | Status  |
|-----------------------|-------------------------------|--------|---------|
| bld_manifest          | Core reference structure      | P06    | Active  |
| bld_instruction       | Content generation rules      | P03    | Active  |
| bld_system_prompt     | LLM guidance framework        | P03    | Active  |
| bld_schema            | Data format validation        | P06    | Active  |
| bld_quality_gate      | Output verification           | P11    | Active  |
| bld_output_template   | Formatting standard           | P05    | Active  |
| bld_examples          | Sample implementation         | P07    | Active  |
| bld_knowledge_card    | Contextual metadata           | P01    | Active  |
| bld_architecture      | Structural documentation      | P08    | Active  |
| bld_collaboration     | Team coordination             | P12    | Active  |
| bld_config            | Configuration management      | P09    | Active  |
| bld_memory            | State retention               | P10    | Active  |
| bld_tools             | Utility functions             | P04    | Active  |

## Dependencies
| From          | To              | Type         |
|---------------|-----------------|--------------|
| bld_manifest  | bld_config      | Configuration|
| bld_instruction | bld_system_prompt | Dependency   |
| bld_quality_gate | bld_schema     | Validation   |
| bld_output_template | bld_examples | Formatting   |
| bld_tools     | JSON Schema Validator | External |
| bld_tools     | Markdown Renderer     | External |

## Architectural Position
api_reference serves as the central coordination hub for P06, enabling consistent API documentation generation through modular ISOs that enforce quality, structure, and collaboration standards across the CEX ecosystem.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_roi_calculator]] | sibling | 0.78 |
| [[bld_architecture_sales_playbook]] | sibling | 0.76 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.74 |
| [[bld_architecture_discovery_questions]] | sibling | 0.74 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.74 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.74 |
| [[bld_architecture_legal_vertical]] | sibling | 0.73 |
| [[bld_architecture_onboarding_flow]] | sibling | 0.71 |
| [[bld_architecture_sdk_example]] | sibling | 0.71 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.70 |
