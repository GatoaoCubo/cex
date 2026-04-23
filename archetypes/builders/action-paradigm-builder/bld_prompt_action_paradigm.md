---
kind: instruction
id: bld_instruction_action_paradigm
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for action_paradigm
quality: 9.0
title: "Instruction Action Paradigm"
version: "1.0.0"
author: wave1_builder_gen
tags: [action_paradigm, builder, instruction]
tldr: "Step-by-step production process for action_paradigm"
domain: "action_paradigm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - p03_sp_action_paradigm_builder
  - action-paradigm-builder
  - bld_memory_action_paradigm
  - bld_instruction_action_prompt
  - bld_examples_action_paradigm
  - bld_knowledge_card_action_paradigm
  - bld_tools_action_paradigm
  - action-prompt-builder
  - p11_qg_action_paradigm
  - bld_instruction_function_def
---

## Phase 1: RESEARCH  
1. Analyze existing action paradigms (e.g., reactive, deliberative, hybrid).  
2. Map agent-environment interaction models (e.g., state-action spaces, reward functions).  
3. Study action representation formats (e.g., discrete, continuous, symbolic).  
4. Investigate execution mechanisms (e.g., rule-based, learning-based, hybrid).  
5. Review validation criteria for action reliability and adaptability.  
6. Document case studies of successful action paradigm implementations.  

## Phase 2: COMPOSE  
1. Define schema structure per SCHEMA.md (action types, parameters, outcomes).  
2. Specify function CALL interface (input: environment state; output: action).  
3. Map action types to environment-specific APIs (e.g., robotics, simulation).  
4. Write execution logic for each action type (e.g., planning, reacting, learning).  
5. Integrate validation hooks (e.g., pre/post-condition checks, error handling).  
6. Use OUTPUT_TEMPLATE.md to format artifact (e.g., YAML, JSON, code blocks).  
7. Add examples for each action type with environment-specific parameters.  
8. Embed references to research findings (Phase 1) in artifact metadata.  
9. Finalize artifact with versioning, authorship, and usage guidelines.  

## Phase 3: VALIDATE  
1. [ ] Verify schema compliance with SCHEMA.md (all required fields present).  
2. [ ] Confirm action_type is classified (reactive/deliberative/hierarchical/hybrid).  
3. [ ] Verify preconditions and postconditions are defined for all actions.  
4. [ ] Confirm failure recovery is documented for each action class.  
5. [ ] Validate id matches pattern: p04_act_[a-z0-9_]+  
6. [ ] Run H01-H08 quality gate checks before delivering.  

## Properties

| Property | Value |
|----------|-------|
| Kind | `instruction` |
| Pillar | P03 |
| Domain | action_paradigm construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_action_paradigm_builder]] | related | 0.35 |
| [[action-paradigm-builder]] | downstream | 0.33 |
| [[bld_memory_action_paradigm]] | downstream | 0.33 |
| [[bld_instruction_action_prompt]] | sibling | 0.32 |
| [[bld_examples_action_paradigm]] | downstream | 0.31 |
| [[bld_knowledge_card_action_paradigm]] | upstream | 0.28 |
| [[bld_tools_action_paradigm]] | downstream | 0.28 |
| [[action-prompt-builder]] | related | 0.28 |
| [[p11_qg_action_paradigm]] | downstream | 0.27 |
| [[bld_instruction_function_def]] | sibling | 0.25 |
