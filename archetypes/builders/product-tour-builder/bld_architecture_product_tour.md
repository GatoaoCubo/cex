---
kind: architecture
id: bld_architecture_product_tour
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of product_tour -- inventory, dependencies
quality: null
title: "Architecture Product Tour"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [product_tour, builder, architecture]
tldr: "Component map of product_tour -- inventory, dependencies"
domain: "product_tour construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name             | Role                          | Pillar | Status  |
|----------------------|-------------------------------|--------|---------|
| bld_manifest         | Tour definition               | P05    | Active  |
| bld_instruction      | Step-by-step guidance         | P05    | Active  |
| bld_system_prompt    | LLM interaction framework     | P05    | Active  |
| bld_schema           | Data structure validation     | P05    | Active  |
| bld_quality_gate     | Compliance checks             | P05    | Active  |
| bld_output_template  | UI rendering blueprint        | P05    | Active  |
| bld_examples         | Sample tour content           | P05    | Active  |
| bld_knowledge_card   | Contextual help integration   | P05    | Active  |
| bld_architecture     | System blueprint              | P05    | Active  |
| bld_collaboration    | Team workflow coordination    | P05    | Active  |
| bld_config           | Configuration management      | P05    | Active  |
| bld_memory           | Session state tracking        | P05    | Active  |
| bld_tools            | Utility functions             | P05    | Active  |

## Dependencies
| From              | To                  | Type       |
|-------------------|---------------------|------------|
| bld_manifest      | bld_config          | config     |
| bld_instruction   | bld_system_prompt   | runtime    |
| bld_quality_gate  | bld_schema          | validation |
| bld_output_template | bld_examples     | rendering  |
| bld_memory        | bld_tools           | utility    |
| bld_collaboration | bld_config          | config     |

## Architectural Position
product_tour occupies the user experience layer of CEX pillar P05, enabling interactive onboarding through structured, AI-assisted tour creation. It integrates with configuration, validation, and collaboration components to ensure consistent, high-quality product tours aligned with CEX's operational and compliance requirements.
