---
kind: architecture
id: bld_architecture_quickstart_guide
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of quickstart_guide -- inventory, dependencies
quality: null
title: "Architecture Quickstart Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [quickstart_guide, builder, architecture]
tldr: "Component map of quickstart_guide -- inventory, dependencies"
domain: "quickstart_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory  
| ISO Name             | Role                          | Pillar | Status |  
|----------------------|-------------------------------|--------|--------|  
| bld_manifest         | Core structure definition     | P05    | Active |  
| bld_instruction      | User task definition          | P05    | Active |  
| bld_system_prompt    | LLM interaction framework     | P05    | Active |  
| bld_schema           | Data format validation        | P05    | Active |  
| bld_quality_gate     | Output verification logic     | P05    | Active |  
| bld_output_template  | Standardized response format  | P05    | Active |  
| bld_examples         | Training data repository      | P05    | Active |  
| bld_knowledge_card   | Domain-specific knowledge     | P05    | Active |  
| bld_architecture     | System design blueprint       | P05    | Active |  
| bld_collaboration    | Multi-agent coordination      | P05    | Active |  
| bld_config           | Runtime parameter store       | P05    | Active |  
| bld_memory           | Session state management      | P05    | Active |  
| bld_tools            | Utility functions             | P05    | Active |  

## Dependencies  
| From              | To                  | Type       |  
|-------------------|---------------------|------------|  
| bld_manifest      | bld_schema          | validation |  
| bld_instruction   | bld_system_prompt   | execution  |  
| bld_quality_gate  | bld_config          | parameter  |  
| bld_output_template | bld_examples     | reference  |  
| bld_collaboration | bld_memory          | state      |  
| bld_tools         | bld_instruction     | utility    |  

## Architectural Position  
The quickstart_guide serves as the foundational framework for P05, enabling rapid deployment of standardized, reusable components. It orchestrates knowledge encoding, quality assurance, and system interoperability, acting as the bridge between domain-specific logic (e.g., bld_knowledge_card) and executable workflows (e.g., bld_instruction). Its role is critical in ensuring consistency and scalability across CEX operations.
