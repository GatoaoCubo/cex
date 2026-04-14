---
kind: architecture
id: bld_architecture_github_issue_template
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of github_issue_template -- inventory, dependencies
quality: null
title: "Architecture Github Issue Template"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [github_issue_template, builder, architecture]
tldr: "Component map of github_issue_template -- inventory, dependencies"
domain: "github_issue_template construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory  
| ISO Name              | Role                          | Pillar | Status  |  
|-----------------------|-------------------------------|--------|---------|  
| bld_manifest          | Template structure definition | P05    | Active  |  
| bld_instruction       | User guidance logic           | P05    | Active  |  
| bld_system_prompt     | LLM interaction framework     | P05    | Active  |  
| bld_schema            | Data validation rules         | P05    | Active  |  
| bld_quality_gate      | Compliance verification       | P05    | Active  |  
| bld_output_template   | Response formatting           | P05    | Active  |  
| bld_examples          | Sample issue patterns         | P05    | Active  |  
| bld_knowledge_card    | Contextual information hub    | P05    | Active  |  
| bld_architecture      | System blueprint              | P05    | Active  |  
| bld_collaboration     | Multi-stakeholder workflow    | P05    | Active  |  
| bld_config            | Parameter management          | P05    | Active  |  
| bld_memory            | Session state tracking        | P05    | Active  |  
| bld_tools             | External integration hub      | P05    | Active  |  

## Dependencies  
| From              | To                  | Type         |  
|-------------------|---------------------|--------------|  
| bld_manifest      | bld_schema          | validation   |  
| bld_instruction   | bld_system_prompt   | input        |  
| bld_quality_gate  | bld_output_template | validation   |  
| bld_tools         | GitHub API          | integration  |  
| bld_memory        | bld_collaboration   | state        |  

## Architectural Position  
github_issue_template sits at the intersection of user experience and operational rigor in P05, standardizing issue creation workflows to ensure consistency, traceability, and alignment with CEX quality standards. It acts as a central orchestrator, integrating schema validation, collaboration logic, and external tools to maintain a unified interface for issue management across the ecosystem.
