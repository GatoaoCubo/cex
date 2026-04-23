---
kind: architecture
id: bld_architecture_prompt_technique
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of prompt_technique -- inventory, dependencies
quality: 9.0
title: "Architecture Prompt Technique"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_technique, builder, architecture]
tldr: "Component map of prompt_technique -- inventory, dependencies"
domain: "prompt_technique construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_prompt_optimizer
  - bld_architecture_multimodal_prompt
  - bld_architecture_api_reference
  - bld_architecture_sales_playbook
  - bld_architecture_roi_calculator
  - bld_architecture_quickstart_guide
  - bld_architecture_churn_prevention_playbook
  - bld_architecture_discovery_questions
  - bld_architecture_app_directory_entry
  - bld_architecture_benchmark_suite
---

## Component Inventory
| ISO Name             | Role                          | Pillar | Status  |
|----------------------|-------------------------------|--------|---------|
| bld_manifest         | Core configuration            | P03    | Active  |
| bld_instruction      | Directive formulation         | P03    | Active  |
| bld_system_prompt    | LLM alignment framework       | P03    | Active  |
| bld_schema           | Output structure definition   | P03    | Active  |
| bld_quality_gate     | Validation enforcement        | P03    | Active  |
| bld_output_template  | Response formatting           | P03    | Active  |
| bld_examples         | Training data repository      | P03    | Active  |
| bld_knowledge_card   | Contextual information hub    | P03    | Active  |
| bld_architecture     | Technical blueprint           | P03    | Active  |
| bld_collaboration    | Stakeholder coordination      | P03    | Active  |
| bld_config           | Parameter management          | P03    | Active  |
| bld_memory           | Session state tracking        | P03    | Active  |
| bld_tools            | Utility integration           | P03    | Active  |

## Dependencies
| From              | To                  | Type         |
|-------------------|---------------------|--------------|
| bld_manifest      | bld_config          | Configuration|
| bld_instruction   | bld_tools           | Utilization  |
| bld_system_prompt | bld_knowledge_card  | Data Source  |
| bld_quality_gate  | bld_schema          | Validation   |
| bld_output_template | bld_examples     | Template     |
| bld_memory        | bld_instruction     | State Input  |

## Architectural Position
The prompt_technique-builder sits at the intersection of P03's CEX pillar, structuring and optimizing prompt generation workflows to ensure alignment with business objectives, technical constraints, and quality standards through modular, reusable ISO components that enable precise control over LLM behavior and output consistency.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_prompt_optimizer]] | sibling | 0.83 |
| [[bld_architecture_multimodal_prompt]] | sibling | 0.78 |
| [[bld_architecture_api_reference]] | sibling | 0.65 |
| [[bld_architecture_sales_playbook]] | sibling | 0.65 |
| [[bld_architecture_roi_calculator]] | sibling | 0.64 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.64 |
| [[bld_architecture_churn_prevention_playbook]] | sibling | 0.63 |
| [[bld_architecture_discovery_questions]] | sibling | 0.62 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.61 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.61 |
