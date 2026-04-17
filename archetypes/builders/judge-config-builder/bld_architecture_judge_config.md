---
kind: architecture
id: bld_architecture_judge_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of judge_config -- inventory, dependencies
quality: 9.0
title: "Architecture Judge Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [judge_config, builder, architecture]
tldr: "Component map of judge_config -- inventory, dependencies"
domain: "judge_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory  
| ISO Name             | Role                                | Pillar | Status |  
|----------------------|-------------------------------------|--------|--------|  
| bld_manifest         | Defines configuration structure     | P07    | Active |  
| bld_instruction      | Specifies execution instructions    | P07    | Active |  
| bld_system_prompt    | Sets AI behavior guidelines         | P07    | Active |  
| bld_schema           | Defines data format and constraints | P07    | Active |  
| bld_quality_gate     | Enforces configuration standards    | P07    | Active |  
| bld_output_template  | Structures response formats         | P07    | Active |  
| bld_examples         | Provides sample configurations      | P07    | Active |  
| bld_knowledge_card   | Holds domain-specific knowledge     | P07    | Active |  
| bld_architecture     | Outlines system structure           | P07    | Active |  
| bld_collaboration    | Manages inter-component workflows   | P07    | Active |  
| bld_config           | Central configuration repository    | P07    | Active |  
| bld_memory           | Manages state persistence           | P07    | Active |  
| bld_tools            | Includes utility functions          | P07    | Active |  

## Dependencies  
| From           | To               | Type         |  
|----------------|------------------|--------------|  
| bld_config     | bld_schema       | definition   |  
| bld_instruction| bld_system_prompt| reference  |  
| bld_quality_gate| bld_output_template | validation |  
| bld_tools      | config_validator | external     |  
| bld_memory     | schema_parser    | external     |  

## Architectural Position  
judge_config acts as the central orchestrator in the CEX P07 ecosystem, ensuring consistency, quality, and alignment across configuration judgment processes. It integrates builder ISOs to define, validate, and execute configuration rules, while leveraging external tools for parsing and validation, positioning it as the backbone of structured decision-making in P07.
