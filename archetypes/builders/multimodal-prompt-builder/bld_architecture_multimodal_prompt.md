---
kind: architecture
id: bld_architecture_multimodal_prompt
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of multimodal_prompt -- inventory, dependencies
quality: 9.0
title: "Architecture Multimodal Prompt"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [multimodal_prompt, builder, architecture]
tldr: "Component map of multimodal_prompt -- inventory, dependencies"
domain: "multimodal_prompt construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name             | Role                                      | Pillar | Status  |
|----------------------|-------------------------------------------|--------|---------|
| bld_manifest         | Defines structure and metadata            | P03    | Active  |
| bld_instruction      | Encodes task-specific directives          | P03    | Active  |
| bld_system_prompt    | Sets overarching behavior guidelines      | P03    | Active  |
| bld_schema           | Enforces data format consistency          | P03    | Active  |
| bld_quality_gate     | Validates output compliance               | P03    | Active  |
| bld_output_template  | Structures final response format          | P03    | Active  |
| bld_examples         | Provides reference outputs                | P03    | Active  |
| bld_knowledge_card   | Embeds domain-specific knowledge          | P03    | Active  |
| bld_architecture     | Maps component interactions              | P03    | Active  |
| bld_collaboration    | Coordinates multi-agent workflows         | P03    | Active  |
| bld_config           | Manages runtime parameters                | P03    | Active  |
| bld_memory           | Stores session-state data                 | P03    | Active  |
| bld_tools            | Integrates external APIs/functionalities  | P03    | Active  |

## Dependencies
| From         | To              | Type       |
|--------------|-----------------|------------|
| bld_manifest | bld_schema      | Definition |
| bld_instruction | bld_system_prompt | Inheritance |
| bld_quality_gate | bld_output_template | Validation |
| bld_knowledge_card | bld_examples | Reference |
| bld_tools    | llm_engine      | Integration |

## Architectural Position
The multimodal_prompt serves as the central orchestrator in P03, synthesizing heterogeneous modalities (text, data, logic) into coherent prompts. It acts as the nexus for quality assurance, collaboration, and schema enforcement, enabling CEX systems to generate robust, context-aware outputs while adhering to domain-specific constraints and interoperability standards.
