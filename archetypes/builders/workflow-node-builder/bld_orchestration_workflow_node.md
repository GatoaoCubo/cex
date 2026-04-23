---
kind: collaboration
id: bld_collaboration_workflow_node
pillar: P12
llm_function: COLLABORATE
purpose: How workflow_node-builder works in crews with other builders
quality: 8.9
title: "Collaboration Workflow Node"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [workflow_node, builder, collaboration]
tldr: "How workflow_node-builder works in crews with other builders"
domain: "workflow_node construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - workflow-node-builder
  - p03_sp_workflow_node_builder
  - bld_collaboration_workflow
  - visual-workflow-builder
  - bld_collaboration_visual_workflow
  - workflow-builder
  - kc_visual_workflow
  - p03_sp_visual_workflow_builder
  - bld_instruction_visual_workflow
  - bld_architecture_kind
---

## Crew Role  
Defines individual workflow nodes, their behavior, and integration points. Ensures nodes adhere to contract standards for execution and data passing.  

## Receives From  
| Builder       | What               | Format     |  
|---------------|--------------------|------------|  
| Config Builder | Node configuration | JSON       |  
| DependencyMgr | Required libraries | YAML       |  
| ValidationMgr | Schema rules       | SchemaDef  |  

## Produces For  
| Builder       | What               | Format     |  
|---------------|--------------------|------------|  
| Orchestrator  | Node definition    | JSON       |  
| RuntimeEngine | Execution plan     | Protobuf   |  
| Registry      | Metadata           | YAML       |  

## Boundary  
Does NOT handle full workflow orchestration (Orchestrator), UI configuration (Visual Workflow Builder), or cross-node dependency resolution (DependencyMgr).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[workflow-node-builder]] | related | 0.44 |
| [[p03_sp_workflow_node_builder]] | upstream | 0.37 |
| [[bld_collaboration_workflow]] | sibling | 0.32 |
| [[visual-workflow-builder]] | related | 0.32 |
| [[bld_collaboration_visual_workflow]] | sibling | 0.29 |
| [[workflow-builder]] | related | 0.29 |
| [[kc_visual_workflow]] | upstream | 0.28 |
| [[p03_sp_visual_workflow_builder]] | upstream | 0.28 |
| [[bld_instruction_visual_workflow]] | upstream | 0.27 |
| [[bld_architecture_kind]] | upstream | 0.27 |
