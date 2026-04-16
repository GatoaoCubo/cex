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
