---
kind: instruction
id: bld_instruction_workflow_node
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for workflow_node
quality: 8.8
title: "Instruction Workflow Node"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [workflow_node, builder, instruction]
tldr: "Step-by-step production process for workflow_node"
domain: "workflow_node construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_visual_workflow
  - workflow-node-builder
  - p03_sp_workflow_node_builder
  - bld_collaboration_workflow_node
  - bld_instruction_benchmark_suite
  - bld_instruction_eval_framework
  - p03_sp_visual_workflow_builder
  - bld_instruction_tts_provider
  - bld_instruction_search_strategy
  - bld_instruction_content_filter
---

## Phase 1: RESEARCH  
1. Analyze schema requirements from SCHEMA.md for node typing rules  
2. Identify required input/output ports and their data types  
3. Review existing workflow_node implementations in P12 pillar  
4. Document visual representation standards (colors, icons, connectors)  
5. Study error handling patterns in workflow_node lifecycle methods  
6. Map node behavior to programmatic execution flow diagrams  

## Phase 2: COMPOSE  
1. Create node class with typed identifier per SCHEMA.md  
2. Implement port definitions using OUTPUT_TEMPLATE.md structure  
3. Write initialization method for visual configuration  
4. Code execution logic with input/output validation  
5. Add error propagation handlers for failure states  
6. Implement serialization methods for workflow storage  
7. Integrate with UI framework for drag-and-drop placement  
8. Write unit tests for edge case scenarios  
9. Finalize documentation in node's metadata block  

## Phase 3: VALIDATE  
[ ] [ ] Verify schema compliance with SCHEMA.md  
[ ] [ ] Test port type mismatches in execution  
[ ] [ ] Confirm visual rendering matches design specs  
[ ] [ ] Validate error handling in all lifecycle stages  
[ ] [ ] Ensure compatibility with P12 workflow engine


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_visual_workflow]] | sibling | 0.37 |
| [[workflow-node-builder]] | downstream | 0.37 |
| [[p03_sp_workflow_node_builder]] | related | 0.37 |
| [[bld_collaboration_workflow_node]] | downstream | 0.28 |
| [[bld_instruction_benchmark_suite]] | sibling | 0.25 |
| [[bld_instruction_eval_framework]] | sibling | 0.25 |
| [[p03_sp_visual_workflow_builder]] | related | 0.25 |
| [[bld_instruction_tts_provider]] | sibling | 0.24 |
| [[bld_instruction_search_strategy]] | sibling | 0.23 |
| [[bld_instruction_content_filter]] | sibling | 0.22 |
