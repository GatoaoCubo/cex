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
related:
  - bld_architecture_app_directory_entry
  - bld_architecture_code_of_conduct
  - bld_architecture_legal_vertical
  - bld_architecture_benchmark_suite
  - bld_architecture_fintech_vertical
  - bld_architecture_api_reference
  - bld_architecture_roi_calculator
  - bld_architecture_healthcare_vertical
  - bld_architecture_quickstart_guide
  - bld_architecture_discovery_questions
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_app_directory_entry]] | sibling | 0.78 |
| [[bld_architecture_code_of_conduct]] | sibling | 0.74 |
| [[bld_architecture_legal_vertical]] | sibling | 0.71 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.71 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.70 |
| [[bld_architecture_api_reference]] | sibling | 0.70 |
| [[bld_architecture_roi_calculator]] | sibling | 0.68 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.67 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.67 |
| [[bld_architecture_discovery_questions]] | sibling | 0.66 |
