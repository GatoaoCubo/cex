---
kind: architecture
id: bld_architecture_github_issue_template
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of github_issue_template -- inventory, dependencies
quality: 9.0
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
| ISO Name              | Role                                                        | Pillar | Status  |  
|-----------------------|-------------------------------------------------------------|--------|---------|  
| bld_manifest          | Builder identity, capabilities, routing                     | P05    | Active  |  
| bld_instruction       | 3-phase production process (Research, Compose, Validate)    | P03    | Active  |  
| bld_system_prompt     | LLM persona and ALWAYS/NEVER rules                          | P03    | Active  |  
| bld_schema            | Frontmatter fields + body structure (SSOT)                  | P06    | Active  |  
| bld_quality_gate      | HARD gates (H01-H09) + SOFT scoring (D01-D05)               | P11    | Active  |  
| bld_output_template   | Production template with var guidance                       | P05    | Active  |  
| bld_examples          | Golden + anti-examples with failure analysis                | P07    | Active  |  
| bld_knowledge_card    | Domain knowledge: GitHub issue template standards           | P01    | Active  |  
| bld_architecture      | This document: ISO map + dependencies                       | P08    | Active  |  
| bld_collaboration     | Cross-builder workflow coordination                         | P12    | Active  |  
| bld_config            | Naming, paths, limits, hooks                                | P09    | Active  |  
| bld_memory            | Learned patterns and pitfalls (memory)                      | P10    | Active  |  
| bld_tools             | Production + validation tools (CEX-native)                  | P04    | Active  |  

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
