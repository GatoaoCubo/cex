---
kind: architecture
id: bld_architecture_onboarding_flow
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of onboarding_flow -- inventory, dependencies
quality: null
title: "Architecture Onboarding Flow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [onboarding_flow, builder, architecture]
tldr: "Component map of onboarding_flow -- inventory, dependencies"
domain: "onboarding_flow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory  
| ISO Name           | Role                          | Pillar | Status  |  
|--------------------|-------------------------------|--------|---------|  
| bld_manifest       | Defines flow structure        | P05    | Active  |  
| bld_instruction    | Specifies user steps          | P05    | Active  |  
| bld_system_prompt  | Sets AI behavior              | P05    | Active  |  
| bld_schema         | Defines data structure        | P05    | Active  |  
| bld_quality_gate   | Enforces compliance rules     | P05    | Active  |  
| bld_output_template| Formats final output          | P05    | Active  |  
| bld_examples       | Provides sample interactions  | P05    | Active  |  
| bld_knowledge_card | Stores domain-specific info   | P05    | Active  |  
| bld_architecture   | Outlines system blueprint     | P05    | Active  |  
| bld_collaboration  | Manages user-AI interaction   | P05    | Active  |  
| bld_config         | Centralizes configuration     | P05    | Active  |  
| bld_memory         | Tracks session context        | P05    | Active  |  
| bld_tools          | Integrates external functions | P05    | Active  |  

## Dependencies  
| From              | To                  | Type         |  
|-------------------|---------------------|--------------|  
| bld_manifest      | bld_schema          | Data         |  
| bld_instruction   | bld_system_prompt   | Control      |  
| bld_quality_gate  | bld_config          | Configuration|  
| bld_output_template | bld_schema        | Data         |  
| bld_tools         | External Auth       | Integration  |  
| bld_memory        | bld_config          | Configuration|  

## Architectural Position  
The onboarding_flow is a foundational element in P05, enabling seamless user integration through structured, compliant, and personalized onboarding processes. It acts as a bridge between user expectations and system capabilities, ensuring alignment with CEX pillar goals of trust, efficiency, and scalability.
