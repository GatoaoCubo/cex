---
kind: architecture
id: bld_architecture_contributor_guide
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of contributor_guide -- inventory, dependencies
quality: null
title: "Architecture Contributor Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [contributor_guide, builder, architecture]
tldr: "Component map of contributor_guide -- inventory, dependencies"
domain: "contributor_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory  
| ISO Name             | Role                          | Pillar | Status  |  
|----------------------|-------------------------------|--------|---------|  
| bld_manifest         | Defines structure             | P05    | Active  |  
| bld_instruction      | Specifies guidelines          | P05    | Active  |  
| bld_system_prompt    | Sets interaction rules        | P05    | Active  |  
| bld_schema           | Enforces data format          | P05    | Active  |  
| bld_quality_gate     | Validates output standards    | P05    | Active  |  
| bld_output_template  | Structures final deliverables | P05    | Active  |  
| bld_examples         | Provides reference cases      | P05    | Active  |  
| bld_knowledge_card   | Documents domain specifics    | P05    | Active  |  
| bld_architecture     | Maps system components        | P05    | Active  |  
| bld_collaboration    | Enables team coordination     | P05    | Active  |  
| bld_config           | Manages runtime parameters    | P05    | Active  |  
| bld_memory           | Tracks state and history      | P05    | Active  |  
| bld_tools            | Integrates external utilities | P05    | Active  |  

## Dependencies  
| From              | To                  | Type         |  
|-------------------|---------------------|--------------|  
| bld_instruction   | bld_schema          | Validation   |  
| bld_quality_gate  | bld_config          | Configuration|  
| bld_output_template | bld_examples     | Formatting   |  
| bld_tools         | Code linter         | External     |  
| bld_memory        | bld_config          | Configuration|  

## Architectural Position  
The contributor_guide serves as the foundational framework for P05, standardizing collaboration, knowledge sharing, and output quality across the CEX ecosystem. It ensures alignment between technical execution and community expectations, acting as a bridge between builder tools and governance protocols.
