---
kind: instruction
id: bld_instruction_visual_workflow
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for visual_workflow
quality: null
title: "Instruction Visual Workflow"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [visual_workflow, builder, instruction]
tldr: "Step-by-step production process for visual_workflow"
domain: "visual_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Analyze existing GUI workflow tools for feature parity  
2. Identify user interaction patterns for drag-and-drop node placement  
3. Map workflow elements (tasks, triggers, conditions) to visual components  
4. Study UI/UX principles for hierarchical workflow visualization  
5. Evaluate technical constraints (browser compatibility, performance)  
6. Document requirements for real-time validation and error highlighting  

## Phase 2: COMPOSE  
1. Set up project structure using SCHEMA.md for data model alignment  
2. Define node types in `config/nodes.yaml` per SCHEMA.md specifications  
3. Implement canvas rendering with SVG for scalable workflow diagrams  
4. Code drag-and-drop handlers using OUTPUT_TEMPLATE.md event hooks  
5. Create property panels for node configuration (inputs/outputs)  
6. Integrate validation rules from SCHEMA.md into workflow engine  
7. Add persistence layer for saving/load workflows as JSON  
8. Implement zoom/pan controls for complex workflow layouts  
9. Finalize artifact with versioning and export capabilities  

## Phase 3: VALIDATE  
[ ] ✅ Verify schema compliance for all node types  
[ ] ✅ Test drag-and-drop with 100+ node load scenarios  
[ ] ✅ Confirm error highlighting for invalid connections  
[ ] ✅ Validate export/import roundtrip integrity  
[ ] ✅ Ensure documentation matches OUTPUT_TEMPLATE.md specs
