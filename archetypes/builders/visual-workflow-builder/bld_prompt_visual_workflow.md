---
kind: instruction
id: bld_instruction_visual_workflow
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for visual_workflow
quality: 8.8
title: "Instruction Visual Workflow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [visual_workflow, builder, instruction]
tldr: "Step-by-step production process for visual_workflow"
domain: "visual_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - workflow-node-builder
  - bld_instruction_workflow_node
  - visual-workflow-builder
  - p03_sp_visual_workflow_builder
  - kc_visual_workflow
  - p03_sp_workflow_node_builder
  - bld_collaboration_workflow_node
  - bld_tools_visual_workflow
  - p10_mem_visual_workflow_builder
  - bld_examples_workflow_node
---

## Phase 1: RESEARCH  
1. Analyze existing GUI workflow tools for feature parity  
2. Identify user interaction patterns for drag-and-drop node placement  
3. Map workflow elements (tasks, triggers, conditions) to visual components  
4. Study UI/UX principles for hierarchical workflow visualization  
5. Evaluate technical constraints (browser compatibility, performance)  
6. Document requirements for real-time validation and error highlighting  

## Phase 2: COMPOSE  
1. Define node schema using bld_schema_visual_workflow.md for data model alignment  
2. Specify node types (trigger, action, condition, output) with input/output ports  
3. Define edge schema: connection type, data type, cardinality  
4. Map workflow DSL to visual representation (Mermaid-compatible node/edge schema)  
5. Apply bld_output_template_visual_workflow.md for final artifact structure  
6. Integrate validation rules from bld_schema_visual_workflow.md into workflow engine  
7. Add persistence layer: serialize/deserialize workflow as JSON  
8. Document visual layout conventions: left-to-right flow, color-coded node types  
9. Finalize artifact with versioning and export capabilities  

## Phase 3: VALIDATE  
[ ] Frontmatter complete and valid YAML  
[ ] Node schema complete with all required fields  
[ ] Edge connections validated (no orphaned nodes)  
[ ] Conforms to bld_output_template_visual_workflow.md structure  
[ ] Compatible with at least one DSL standard (Mermaid, LangGraph, n8n)


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[workflow-node-builder]] | downstream | 0.43 |
| [[bld_instruction_workflow_node]] | sibling | 0.39 |
| [[visual-workflow-builder]] | downstream | 0.35 |
| [[p03_sp_visual_workflow_builder]] | related | 0.34 |
| [[kc_visual_workflow]] | upstream | 0.33 |
| [[p03_sp_workflow_node_builder]] | related | 0.33 |
| [[bld_collaboration_workflow_node]] | downstream | 0.32 |
| [[bld_tools_visual_workflow]] | downstream | 0.29 |
| [[p10_mem_visual_workflow_builder]] | downstream | 0.26 |
| [[bld_examples_workflow_node]] | downstream | 0.24 |
