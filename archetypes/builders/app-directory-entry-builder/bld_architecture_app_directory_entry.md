---
kind: architecture
id: bld_architecture_app_directory_entry
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of app_directory_entry -- inventory, dependencies
quality: 9.0
title: "Architecture App Directory Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [app_directory_entry, builder, architecture]
tldr: "Component map of app_directory_entry -- inventory, dependencies"
domain: "app_directory_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_github_issue_template
  - bld_architecture_code_of_conduct
  - bld_architecture_benchmark_suite
  - bld_architecture_legal_vertical
  - bld_architecture_api_reference
  - bld_architecture_fintech_vertical
  - bld_architecture_roi_calculator
  - bld_architecture_healthcare_vertical
  - bld_architecture_sdk_example
  - bld_architecture_sales_playbook
---

## Component Inventory
| ISO Name             | Role                                                      | Pillar | Status  |
|----------------------|-----------------------------------------------------------|--------|---------|
| bld_manifest         | Builder identity, capabilities, routing                   | P05    | Active  |
| bld_instruction      | 3-phase production process (Research, Compose, Validate)  | P03    | Active  |
| bld_system_prompt    | LLM persona and ALWAYS/NEVER rules                        | P03    | Active  |
| bld_schema           | Frontmatter fields + body structure (SSOT)                | P06    | Active  |
| bld_quality_gate     | HARD gates (H01-H08) + SOFT scoring (D01-D08)             | P11    | Active  |
| bld_output_template  | Production template with var guidance                     | P05    | Active  |
| bld_examples         | Golden + anti-examples with failure analysis              | P07    | Active  |
| bld_knowledge_card   | Domain knowledge: app directory standards + pitfalls      | P01    | Active  |
| bld_architecture     | This document: ISO map + dependencies                     | P08    | Active  |
| bld_collaboration    | Cross-builder workflow coordination                       | P12    | Active  |
| bld_config           | Naming, paths, limits, hooks                              | P09    | Active  |
| bld_memory           | Learned patterns and pitfalls (memory)                    | P10    | Active  |
| bld_tools            | Production + validation tools (CEX-native)                | P04    | Active  |

## Dependencies
| From               | To                   | Type         |
|--------------------|----------------------|--------------|
| bld_manifest       | bld_instruction      | Control Flow |
| bld_schema         | bld_output_template  | Data Flow    |
| bld_quality_gate   | bld_examples         | Validation   |
| bld_config         | bld_memory           | Configuration|
| bld_tools          | external API         | Integration  |

## Architectural Position
app_directory_entry serves as the central registry and coordination hub for P05's builder ISOs, enabling structured application development through standardized manifests, quality gates, and cross-component dependencies, aligning with CEX's focus on modular, reusable, and auditable software constructs.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_github_issue_template]] | sibling | 0.76 |
| [[bld_architecture_code_of_conduct]] | sibling | 0.74 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.74 |
| [[bld_architecture_legal_vertical]] | sibling | 0.73 |
| [[bld_architecture_api_reference]] | sibling | 0.73 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.72 |
| [[bld_architecture_roi_calculator]] | sibling | 0.71 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.70 |
| [[bld_architecture_sdk_example]] | sibling | 0.69 |
| [[bld_architecture_sales_playbook]] | sibling | 0.69 |
