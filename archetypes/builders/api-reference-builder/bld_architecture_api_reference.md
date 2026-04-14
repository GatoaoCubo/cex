---
kind: architecture
id: bld_architecture_api_reference
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of api_reference -- inventory, dependencies
quality: null
title: "Architecture Api Reference"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [api_reference, builder, architecture]
tldr: "Component map of api_reference -- inventory, dependencies"
domain: "api_reference construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name              | Role                          | Pillar | Status  |
|-----------------------|-------------------------------|--------|---------|
| bld_manifest          | Core reference structure      | P06    | Active  |
| bld_instruction       | Content generation rules      | P06    | Active  |
| bld_system_prompt     | LLM guidance framework        | P06    | Active  |
| bld_schema            | Data format validation        | P06    | Active  |
| bld_quality_gate      | Output verification           | P06    | Active  |
| bld_output_template   | Formatting standard           | P06    | Active  |
| bld_examples          | Sample implementation         | P06    | Active  |
| bld_knowledge_card    | Contextual metadata           | P06    | Active  |
| bld_architecture      | Structural documentation      | P06    | Active  |
| bld_collaboration     | Team coordination             | P06    | Active  |
| bld_config            | Configuration management      | P06    | Active  |
| bld_memory            | State retention              | P06    | Active  |
| bld_tools             | Utility functions             | P06    | Active  |

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
