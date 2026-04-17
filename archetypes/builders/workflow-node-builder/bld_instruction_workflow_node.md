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
