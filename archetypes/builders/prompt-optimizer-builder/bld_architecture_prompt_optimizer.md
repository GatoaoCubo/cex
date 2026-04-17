---
kind: architecture
id: bld_architecture_prompt_optimizer
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of prompt_optimizer -- inventory, dependencies
quality: 9.0
title: "Architecture Prompt Optimizer"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_optimizer, builder, architecture]
tldr: "Component map of prompt_optimizer -- inventory, dependencies"
domain: "prompt_optimizer construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name             | Role                          | Pillar | Status   |
|----------------------|-------------------------------|--------|----------|
| bld_manifest         | Defines builder structure     | P03    | Active   |
| bld_instruction      | Encodes operational logic     | P03    | Active   |
| bld_system_prompt    | Sets LLM interaction rules    | P03    | Active   |
| bld_schema           | Enforces data format standards| P03    | Active   |
| bld_quality_gate     | Validates output compliance   | P03    | Active   |
| bld_output_template  | Structures final responses    | P03    | Active   |
| bld_examples         | Provides training samples     | P03    | Active   |
| bld_knowledge_card   | Embeds domain-specific facts  | P03    | Active   |
| bld_architecture     | Maps builder component layout | P03    | Active   |
| bld_collaboration    | Manages team coordination     | P03    | Active   |
| bld_config           | Stores runtime parameters     | P03    | Active   |
| bld_memory           | Maintains session context     | P03    | Active   |
| bld_tools            | Integrates external utilities | P03    | Active   |

## Dependencies
| From         | To             | Type       |
|--------------|----------------|------------|
| bld_config   | bld_memory     | data       |
| bld_instruction | bld_system_prompt | control  |
| bld_quality_gate | bld_schema     | validation |
| bld_output_template | bld_examples   | reference  |
| bld_tools    | LLM Engine     | integration|
| bld_architecture | bld_collaboration | design   |

## Architectural Position
The prompt_optimizer sits at the core of CEX pillar P03, ensuring consistent, high-quality prompt generation across all builder ISOs. It harmonizes instruction encoding, schema validation, and knowledge integration to maintain alignment with P03's operational and compliance objectives while enabling scalable collaboration.
