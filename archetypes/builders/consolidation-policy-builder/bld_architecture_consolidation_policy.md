---
kind: architecture
id: bld_architecture_consolidation_policy
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of consolidation_policy -- inventory, dependencies
quality: null
title: "Architecture Consolidation Policy"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [consolidation_policy, builder, architecture]
tldr: "Component map of consolidation_policy -- inventory, dependencies"
domain: "consolidation_policy construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory  
| ISO Name              | Role                          | Pillar | Status  |  
|-----------------------|-------------------------------|--------|---------|  
| bld_manifest          | Policy structure definition   | P10    | Active  |  
| bld_instruction       | Directive formulation         | P10    | Active  |  
| bld_system_prompt     | AI behavior guidance          | P10    | Active  |  
| bld_schema            | Data format specification     | P10    | Active  |  
| bld_quality_gate      | Compliance validation         | P10    | Active  |  
| bld_output_template   | Policy rendering blueprint    | P10    | Active  |  
| bld_examples          | Use case references           | P10    | Active  |  
| bld_knowledge_card    | Contextual information        | P10    | Active  |  
| bld_architecture      | Structural policy mapping     | P10    | Active  |  
| bld_collaboration     | Stakeholder alignment         | P10    | Active  |  
| bld_config            | Configuration management      | P10    | Active  |  
| bld_memory            | Historical policy tracking    | P10    | Active  |  
| bld_tools             | Policy execution utilities    | P10    | Active  |  

## Dependencies  
| From              | To              | Type           |  
|-------------------|-----------------|----------------|  
| bld_manifest      | bld_config      | Configuration  |  
| bld_instruction   | bld_system_prompt | Input      |  
| bld_quality_gate  | bld_schema      | Validation     |  
| bld_output_template | bld_examples  | Reference      |  
| bld_tools         | Policy Engine   | External       |  
| bld_memory        | bld_config      | Storage        |  

## Architectural Position  
consolidation_policy acts as the central orchestrator within the CEX P10 pillar, integrating builder ISOs to standardize policy creation, enforce quality gates, and ensure alignment with architectural principles across execution environments. It bridges domain-specific logic with system-wide governance, enabling consistent policy deployment and auditability.
