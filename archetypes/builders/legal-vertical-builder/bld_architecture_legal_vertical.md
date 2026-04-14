---
kind: architecture
id: bld_architecture_legal_vertical
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of legal_vertical -- inventory, dependencies
quality: null
title: "Architecture Legal Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [legal_vertical, builder, architecture]
tldr: "Component map of legal_vertical -- inventory, dependencies"
domain: "legal_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory  
| ISO Name             | Role                                      | Pillar | Status  |  
|----------------------|-------------------------------------------|--------|---------|  
| bld_manifest         | Defines legal document structure          | P01    | Active  |  
| bld_instruction      | Encodes procedural legal workflows        | P01    | Active  |  
| bld_system_prompt    | Sets AI behavior for legal tasks          | P01    | Active  |  
| bld_schema           | Standardizes legal data formats           | P01    | Active  |  
| bld_quality_gate     | Enforces legal compliance checks          | P01    | Active  |  
| bld_output_template  | Formats legal deliverables                | P01    | Active  |  
| bld_examples         | Provides legal case reference templates   | P01    | Active  |  
| bld_knowledge_card   | Stores legal domain-specific knowledge    | P01    | Active  |  
| bld_architecture     | Maps legal system integration points      | P01    | Active  |  
| bld_collaboration    | Manages multi-party legal workflows       | P01    | Active  |  
| bld_config           | Centralizes legal system parameters       | P01    | Active  |  
| bld_memory           | Tracks legal context and history          | P01    | Active  |  
| bld_tools            | Integrates legal-specific utilities       | P01    | Active  |  

## Dependencies  
| From           | To              | Type       |  
|----------------|-----------------|------------|  
| bld_instruction| bld_schema      | Data       |  
| bld_quality_gate| bld_config     | Configuration |  
| bld_output_template| bld_schema | Data       |  
| bld_tools      | legal_db        | External   |  
| bld_memory     | bld_config      | Configuration |  

## Architectural Position  
The legal_vertical-builder (P01) serves as the compliance and governance backbone of the CEX ecosystem, ensuring all legal workflows, standards, and enforcement mechanisms are rigorously encoded, validated, and integrated across the system.
