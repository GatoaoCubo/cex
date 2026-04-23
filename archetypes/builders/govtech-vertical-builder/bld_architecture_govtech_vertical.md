---
kind: architecture
id: bld_architecture_govtech_vertical
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of govtech_vertical -- inventory, dependencies
quality: 9.0
title: "Architecture Govtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [govtech_vertical, builder, architecture]
tldr: "Component map of govtech_vertical -- inventory, dependencies"
domain: "govtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_app_directory_entry
  - bld_architecture_legal_vertical
  - bld_architecture_fintech_vertical
  - bld_architecture_roi_calculator
  - bld_architecture_api_reference
  - bld_architecture_quickstart_guide
  - bld_architecture_healthcare_vertical
  - bld_architecture_benchmark_suite
  - bld_architecture_github_issue_template
  - bld_architecture_sales_playbook
---

## Component Inventory
| ISO Name              | Role                                              | Pillar | Status  |
|-----------------------|---------------------------------------------------|--------|---------|
| bld_manifest          | Builder identity and routing metadata             | P05    | Active  |
| bld_instruction       | 3-phase production process (Research/Compose/Validate) | P03 | Active  |
| bld_system_prompt     | LLM persona: govtech compliance builder           | P03    | Active  |
| bld_schema            | Govtech_vertical artifact data contract           | P06    | Active  |
| bld_quality_gate      | HARD/SOFT validation (FedRAMP/FISMA/CJIS naming)  | P11    | Active  |
| bld_output_template   | Artifact template with frontmatter + 6 sections   | P05    | Active  |
| bld_examples          | Golden and anti-examples for govtech artifacts    | P07    | Active  |
| bld_knowledge_card    | FedRAMP/FISMA/CJIS/GSA domain knowledge           | P01    | Active  |
| bld_architecture      | System blueprint (this file)                      | P08    | Active  |
| bld_collaboration     | Crew coordination: N01/N04/N06 hand-offs          | P12    | Active  |
| bld_config            | Naming conventions, paths, byte limits            | P09    | Active  |
| bld_memory            | Learned govtech compliance patterns and pitfalls  | P10    | Active  |
| bld_tools             | CEX production tools + govtech external references| P04    | Active  |

## Dependencies
| From              | To                  | Type        |
|-------------------|---------------------|-------------|
| bld_manifest      | bld_config          | configuration|
| bld_instruction   | bld_system_prompt   | dependency  |
| bld_quality_gate  | bld_schema          | validation  |
| bld_output_template | bld_examples      | reference   |
| bld_tools         | bld_memory          | utility     |

## Architectural Position
govtech_vertical-builder operates as the foundational layer within CEX P01, enabling governance-specific solution orchestration through standardized ISOs that ensure compliance, interoperability, and domain-specific rigor across public sector workflows.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_app_directory_entry]] | sibling | 0.71 |
| [[bld_architecture_legal_vertical]] | sibling | 0.71 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.71 |
| [[bld_architecture_roi_calculator]] | sibling | 0.69 |
| [[bld_architecture_api_reference]] | sibling | 0.69 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.69 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.68 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.68 |
| [[bld_architecture_github_issue_template]] | sibling | 0.68 |
| [[bld_architecture_sales_playbook]] | sibling | 0.67 |
