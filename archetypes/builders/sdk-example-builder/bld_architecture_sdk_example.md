---
kind: architecture
id: bld_architecture_sdk_example
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of sdk_example -- inventory, dependencies
quality: 9.0
title: "Architecture Sdk Example"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sdk_example, builder, architecture]
tldr: "Component map of sdk_example -- inventory, dependencies"
domain: "sdk_example construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name             | Role                          | Pillar | Status  |
|----------------------|-------------------------------|--------|---------|
| bld_manifest         | Defines structure             | P04    | Active  |
| bld_instruction      | Specifies execution logic     | P03    | Active  |
| bld_system_prompt    | Sets interaction guidelines   | P03    | Active  |
| bld_schema           | Enforces data format          | P06    | Active  |
| bld_quality_gate     | Validates output compliance   | P11    | Active  |
| bld_output_template  | Structures final output       | P05    | Active  |
| bld_examples         | Provides usage samples        | P07    | Active  |
| bld_knowledge_card   | Documents component purpose   | P01    | Active  |
| bld_architecture     | Defines system blueprint      | P08    | Active  |
| bld_collaboration    | Manages multi-agent workflows | P12    | Active  |
| bld_config           | Centralizes parameter storage | P09    | Active  |
| bld_memory           | Tracks session state          | P10    | Active  |
| bld_tools            | Integrates external utilities | P04    | Active  |

## Dependencies
| From          | To               | Type       |
|---------------|------------------|------------|
| bld_manifest  | bld_instruction  | Reference  |
| bld_schema    | bld_output_template | Validation |
| bld_config    | bld_memory       | Injection  |
| bld_quality_gate | bld_output_template | Validation |
| bld_tools     | external API     | Integration |

## Architectural Position
The sdk_example occupies a central role in P04 by providing a modular framework for constructing standardized SDKs. It ensures interoperability through structured components like manifests, schemas, and quality gates, while enabling customization via configuration and tool integrations, aligning with CEX's focus on extensible, reusable software building blocks.
