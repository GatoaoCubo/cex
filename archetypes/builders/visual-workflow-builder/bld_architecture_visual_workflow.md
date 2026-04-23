---
kind: architecture
id: bld_architecture_visual_workflow
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of visual_workflow -- inventory, dependencies
quality: 9.0
title: "Architecture Visual Workflow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [visual_workflow, builder, architecture]
tldr: "Component map of visual_workflow -- inventory, dependencies"
domain: "visual_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_workflow_node
  - bld_architecture_roi_calculator
  - bld_architecture_quickstart_guide
  - bld_architecture_api_reference
  - bld_architecture_sales_playbook
  - bld_architecture_discovery_questions
  - bld_architecture_churn_prevention_playbook
  - bld_architecture_onboarding_flow
  - bld_architecture_sdk_example
  - bld_architecture_benchmark_suite
---

## Component Inventory
| ISO Name             | Role                          | Pillar | Status |
|----------------------|-------------------------------|--------|--------|
| bld_manifest         | Core workflow definition      | P12    | Active |
| bld_instruction      | Step-level task specification | P12    | Active |
| bld_system_prompt    | LLM interaction framework     | P12    | Active |
| bld_schema           | Data structure validation     | P12    | Active |
| bld_quality_gate     | Compliance verification       | P12    | Active |
| bld_output_template  | Result formatting             | P12    | Active |
| bld_examples         | Sample workflow repository    | P12    | Active |
| bld_knowledge_card   | Domain-specific guidance      | P12    | Active |
| bld_architecture     | System-level design blueprint   | P12    | Active |
| bld_collaboration    | Multi-user editing            | P12    | Active |
| bld_config           | Runtime parameter management  | P12    | Active |
| bld_memory           | Session state retention       | P12    | Active |
| bld_tools            | External integration hub      | P12    | Active |

## Dependencies
| From              | To                  | Type         |
|-------------------|---------------------|--------------|
| bld_manifest      | bld_schema          | validation   |
| bld_instruction   | bld_tools           | execution    |
| bld_quality_gate  | bld_output_template | validation   |
| bld_collaboration | bld_memory          | state sync   |
| bld_config        | bld_system_prompt   | parameter    |

## Architectural Position
Visual_workflow sits at the intersection of P12's workflow orchestration and knowledge management, enabling collaborative, configurable, and compliant workflow design through ISO-driven modularity, with explicit integration points for external systems and quality assurance.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_workflow_node]] | sibling | 0.85 |
| [[bld_architecture_roi_calculator]] | sibling | 0.61 |
| [[bld_architecture_quickstart_guide]] | sibling | 0.60 |
| [[bld_architecture_api_reference]] | sibling | 0.60 |
| [[bld_architecture_sales_playbook]] | sibling | 0.58 |
| [[bld_architecture_discovery_questions]] | sibling | 0.57 |
| [[bld_architecture_churn_prevention_playbook]] | sibling | 0.57 |
| [[bld_architecture_onboarding_flow]] | sibling | 0.56 |
| [[bld_architecture_sdk_example]] | sibling | 0.56 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.56 |
