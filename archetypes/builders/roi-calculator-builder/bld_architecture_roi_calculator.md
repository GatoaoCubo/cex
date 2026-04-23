---
kind: architecture
id: bld_architecture_roi_calculator
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of roi_calculator -- inventory, dependencies
quality: 9.0
title: "Architecture Roi Calculator"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [roi_calculator, builder, architecture]
tldr: "Component map of roi_calculator -- inventory, dependencies"
domain: "roi_calculator construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_api_reference
  - bld_architecture_quickstart_guide
  - bld_architecture_sales_playbook
  - bld_architecture_discovery_questions
  - bld_architecture_benchmark_suite
  - bld_architecture_legal_vertical
  - bld_architecture_onboarding_flow
  - bld_architecture_memory_benchmark
  - bld_architecture_app_directory_entry
  - bld_architecture_sdk_example
---

## Component Inventory
| ISO Name            | Role                          | Pillar | Status  |
|---------------------|-------------------------------|--------|---------|
| bld_manifest        | Builder configuration         | P11    | Active  |
| bld_instruction     | Task execution guidelines     | P03    | Active  |
| bld_system_prompt   | LLM interaction framework     | P03    | Active  |
| bld_schema          | Data structure definition     | P06    | Active  |
| bld_quality_gate    | Validation rules              | P11    | Active  |
| bld_output_template | Result formatting             | P05    | Active  |
| bld_examples        | Sample input/output           | P07    | Active  |
| bld_knowledge_card  | Domain-specific knowledge     | P01    | Active  |
| bld_architecture    | Builder system design         | P08    | Active  |
| bld_collaboration   | Multi-builder coordination    | P12    | Active  |
| bld_config          | Runtime parameter management  | P09    | Active  |
| bld_memory          | State retention mechanism     | P10    | Active  |
| bld_tools           | Utility functions             | P04    | Active  |

## Dependencies
| From              | To                  | Type         |
|-------------------|---------------------|--------------|
| bld_config        | bld_manifest        | Configuration|
| bld_instruction   | bld_system_prompt   | Execution    |
| bld_quality_gate  | bld_schema          | Validation   |
| bld_output_template | bld_examples      | Reference    |
| bld_tools         | external_calculator | Integration  |

## Architectural Position
The roi_calculator operates as a specialized tool within CEX Pillar P11, focusing on quantifying return-on-investment metrics through structured builder ISOs. It integrates with bld_instruction for task execution, bld_schema for data consistency, and bld_quality_gate for accuracy checks, positioning itself as a core analytics component in the pillar's ecosystem.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_api_reference]] | sibling | 0.76 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.75 |
| [[bld_architecture_sales_playbook]] | sibling | 0.73 |
| [[bld_architecture_discovery_questions]] | sibling | 0.73 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.72 |
| [[bld_architecture_legal_vertical]] | sibling | 0.71 |
| [[bld_architecture_onboarding_flow]] | sibling | 0.71 |
| [[bld_architecture_memory_benchmark]] | sibling | 0.71 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.70 |
| [[bld_architecture_sdk_example]] | sibling | 0.70 |
