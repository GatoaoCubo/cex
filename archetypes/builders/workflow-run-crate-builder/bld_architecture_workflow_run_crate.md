---
kind: architecture
id: bld_architecture_workflow_run_crate
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of workflow_run_crate -- inventory, dependencies
quality: 9.0
title: "Architecture Workflow Run Crate"
version: "1.0.0"
author: n04_wave7
tags: [workflow_run_crate, builder, architecture, RO-Crate, CreateAction, BioSchemas, FAIR]
tldr: "Component map of workflow_run_crate -- inventory, dependencies"
domain: "workflow_run_crate construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Component Inventory
| ISO Name            | Role                                     | Pillar | Status  |
|---------------------|------------------------------------------|--------|---------|
| bld_manifest        | Builder identity and routing             | P05    | Active  |
| bld_instruction     | RO-Crate assembly process                | P03    | Active  |
| bld_system_prompt   | LLM provenance crate persona             | P03    | Active  |
| bld_schema          | RO-Crate 1.2 Workflow Run schema         | P06    | Active  |
| bld_quality_gate    | FAIR + RO-Crate compliance gates         | P11    | Active  |
| bld_output_template | ro-crate-metadata.json template          | P05    | Active  |
| bld_examples        | Golden crate and anti-examples           | P07    | Active  |
| bld_knowledge_card  | RO-Crate + FAIR domain knowledge         | P01    | Active  |
| bld_architecture    | Component map                            | P08    | Active  |
| bld_collaboration   | Workflow with workflow-builder, dataset  | P12    | Active  |
| bld_config          | Naming, paths, limits                    | P09    | Active  |
| bld_memory          | Learned Workflow Run Crate patterns      | P10    | Active  |
| bld_tools           | RO-Crate validation, Galaxy export tools | P04    | Active  |

## Dependencies
| From                 | To                               | Type           |
|----------------------|----------------------------------|----------------|
| bld_schema           | RO-Crate 1.2 spec + BioSchemas   | normative      |
| bld_output_template  | bld_schema                       | constraint     |
| bld_quality_gate     | bld_schema + bld_examples        | validation     |
| bld_collaboration    | workflow-builder (P12)           | coordination   |
| bld_collaboration    | dataset-card-builder (P01)       | coordination   |
| bld_tools            | rocrate-py, ro-crate-validator   | integration    |

## Architectural Position
workflow_run_crate occupies the P10 scientific provenance sublayer. It is the execution-time complement to workflow-builder (P12 workflow definition). The data flow is: workflow-builder defines the workflow -> nucleus executes it -> workflow_run_crate packages the execution provenance. vc_credential can be linked from CreateAction.agent for cryptographic researcher identity. Downstream consumers: WorkflowHub.eu, Zenodo, institutional research data repositories, Galaxy History export format.
