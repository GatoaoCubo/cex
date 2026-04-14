---
kind: architecture
id: bld_architecture_govtech_vertical
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of govtech_vertical -- inventory, dependencies
quality: null
title: "Architecture Govtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [govtech_vertical, builder, architecture]
tldr: "Component map of govtech_vertical -- inventory, dependencies"
domain: "govtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name              | Role                          | Pillar | Status  |
|-----------------------|-------------------------------|--------|---------|
| bld_manifest          | Core configuration            | P01    | Active  |
| bld_instruction       | Workflow definition           | P01    | Active  |
| bld_system_prompt     | AI behavior guidance          | P01    | Active  |
| bld_schema            | Data structure validation     | P01    | Active  |
| bld_quality_gate      | Compliance verification       | P01    | Active  |
| bld_output_template   | Standardized response format  | P01    | Active  |
| bld_examples          | Training data repository      | P01    | Active  |
| bld_knowledge_card    | Domain-specific knowledge     | P01    | Active  |
| bld_architecture      | System blueprint              | P01    | Active  |
| bld_collaboration     | Multi-stakeholder coordination| P01    | Active  |
| bld_config            | Runtime parameter management  | P01    | Active  |
| bld_memory            | Session state retention       | P01    | Active  |
| bld_tools             | Utility functions             | P01    | Active  |

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
