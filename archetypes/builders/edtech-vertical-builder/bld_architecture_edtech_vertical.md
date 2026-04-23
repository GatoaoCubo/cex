---
kind: architecture
id: bld_architecture_edtech_vertical
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of edtech_vertical -- inventory, dependencies
quality: 9.0
title: "Architecture Edtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [edtech_vertical, builder, architecture]
tldr: "Component map of edtech_vertical -- inventory, dependencies"
domain: "edtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_app_directory_entry
  - bld_architecture_legal_vertical
  - bld_architecture_fintech_vertical
  - bld_architecture_roi_calculator
  - bld_architecture_api_reference
  - bld_architecture_healthcare_vertical
  - bld_architecture_benchmark_suite
  - bld_architecture_github_issue_template
  - bld_architecture_code_of_conduct
  - bld_architecture_sales_playbook
---

## Component Inventory
| ISO Name             | Role                                                   | Pillar | Status  |
|----------------------|--------------------------------------------------------|--------|---------|
| bld_manifest         | Builder identity and routing metadata                  | P05    | Active  |
| bld_instruction      | 3-phase production process (Research/Compose/Validate) | P03    | Active  |
| bld_system_prompt    | LLM persona: EdTech FERPA/LTI compliance builder       | P03    | Active  |
| bld_schema           | Edtech_vertical artifact data contract                 | P06    | Active  |
| bld_quality_gate     | HARD/SOFT validation (FERPA/COPPA/LTI 1.3 specificity) | P11    | Active  |
| bld_output_template  | Artifact template with frontmatter + 6 sections        | P05    | Active  |
| bld_examples         | Golden and anti-examples for edtech artifacts          | P07    | Active  |
| bld_knowledge_card   | FERPA/COPPA/LTI 1.3/1EdTech domain knowledge          | P01    | Active  |
| bld_architecture     | System blueprint (this file)                           | P08    | Active  |
| bld_collaboration    | Crew coordination: N01/N04/N06 hand-offs               | P12    | Active  |
| bld_config           | Naming conventions, paths, byte limits                 | P09    | Active  |
| bld_memory           | Learned EdTech compliance patterns and pitfalls        | P10    | Active  |
| bld_tools            | CEX production tools + EdTech external references      | P04    | Active  |

## Dependencies
| From              | To                  | Type       |
|-------------------|---------------------|------------|
| bld_config        | bld_schema          | Reference  |
| bld_instruction   | bld_system_prompt   | Dependency |
| bld_quality_gate  | bld_output_template | Validation |
| bld_memory        | bld_tools           | Utilization|
| bld_collaboration | bld_examples        | Reference  |

## Architectural Position
The edtech_vertical-builder operates as a specialized framework within the CEX P01 pillar, enabling the construction of domain-specific educational ecosystems. It focuses on modular knowledge assembly, ensuring alignment with pedagogical standards through structured ISO interactions, while maintaining isolation from cross-vertical infrastructure layers.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_app_directory_entry]] | sibling | 0.69 |
| [[bld_architecture_legal_vertical]] | sibling | 0.69 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.68 |
| [[bld_architecture_roi_calculator]] | sibling | 0.67 |
| [[bld_architecture_api_reference]] | sibling | 0.67 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.67 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.66 |
| [[bld_architecture_github_issue_template]] | sibling | 0.66 |
| [[bld_architecture_code_of_conduct]] | sibling | 0.65 |
| [[bld_architecture_sales_playbook]] | sibling | 0.65 |
