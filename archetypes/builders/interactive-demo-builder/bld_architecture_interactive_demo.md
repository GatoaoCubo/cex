---
kind: architecture
id: bld_architecture_interactive_demo
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of interactive_demo -- inventory, dependencies
quality: null
title: "Architecture Interactive Demo"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [interactive_demo, builder, architecture]
tldr: "Component map of interactive_demo -- inventory, dependencies"
domain: "interactive_demo construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory  
| ISO Name             | Role                          | Pillar | Status  |  
|----------------------|-------------------------------|--------|---------|  
| bld_manifest         | Demo structure definition     | P05    | Active  |  
| bld_instruction      | User interaction logic        | P05    | Active  |  
| bld_system_prompt    | LLM behavior guidance        | P05    | Active  |  
| bld_schema           | Data format specification     | P05    | Active  |  
| bld_quality_gate     | Output validation rules       | P05    | Active  |  
| bld_output_template  | Response formatting           | P05    | Active  |  
| bld_examples         | Sample interaction scenarios  | P05    | Active  |  
| bld_knowledge_card   | Contextual information hub    | P05    | Active  |  
| bld_architecture     | System blueprint              | P05    | Active  |  
| bld_collaboration    | Multi-agent coordination      | P05    | Active  |  
| bld_config           | Runtime parameter management  | P05    | Active  |  
| bld_memory           | Session state tracking        | P05    | Active  |  
| bld_tools            | External API integration      | P05    | Active  |  

## Dependencies  
| From               | To                  | Type       |  
|--------------------|---------------------|------------|  
| bld_manifest       | bld_instruction     | Reference  |  
| bld_system_prompt  | bld_output_template | Dependency |  
| bld_quality_gate   | bld_schema          | Validation |  
| bld_memory         | bld_collaboration   | Data Flow  |  
| bld_tools          | external LLM        | Integration|  

## Architectural Position  
interactive_demo serves as the user-facing execution layer of P05, translating abstract CEX requirements into interactive, validated experiences through coordinated ISOs, ensuring alignment with domain-specific workflows and quality constraints.
