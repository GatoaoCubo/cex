---
kind: instruction
id: bld_instruction_dual_loop_architecture
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for dual_loop_architecture
quality: 8.9
title: "Instruction Dual Loop Architecture"
version: "1.0.0"
author: wave1_builder_gen
tags: [dual_loop_architecture, builder, instruction]
tldr: "Step-by-step production process for dual_loop_architecture"
domain: "dual_loop_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_collaboration_dual_loop_architecture
  - bld_knowledge_card_dual_loop_architecture
  - p03_sp_dual_loop_architecture_builder
  - dual-loop-architecture-builder
  - p10_lr_dual_loop_architecture_builder
  - kc_dual_loop_architecture
  - bld_examples_dual_loop_architecture
  - p08_qg_dual_loop_architecture
  - bld_tools_dual_loop_architecture
  - bld_architecture_dual_loop_architecture
---

## Phase 1: RESEARCH  

This ISO applies to the dual loop pattern, coordinating an outer orchestrator with one or more inner worker loops.
1. Define dual-loop architecture purpose: outer loop for long-term planning, inner loop for real-time execution.  
2. Analyze existing agent control frameworks for compatibility with P08 REASON function.  
3. Identify key components: outer loop (goals, policies), inner loop (sensors, actuators).  
4. Map interaction protocols between loops (e.g., feedback, error correction).  
5. Evaluate trade-offs between loop autonomy and coordination.  
6. Document research findings in schema-compatible format (SCHEMA.md).  

## Phase 2: COMPOSE  
1. Set up artifact directory with subfolders: `outer_loop`, `inner_loop`, `interface`.  
2. Define outer_loop schema: goal states, policy rules, and evaluation metrics.  
3. Define inner_loop schema: sensor inputs, actuator outputs, and error thresholds.  
4. Write outer_loop agent logic using SCHEMA.md-defined policies.  
5. Write inner_loop agent logic with real-time decision trees.  
6. Implement interface layer for bidirectional data flow between loops.  
7. Align artifact structure with OUTPUT_TEMPLATE.md section headers.  
8. Add metadata: version, author, and P08 REASON compliance notes.  
9. Finalize code with comments referencing SCHEMA.md and template sections.  

## Phase 3: VALIDATE  
- [ ] ✅ Verify outer/inner loop schemas match SCHEMA.md requirements.  
- [ ] ✅ Confirm interface layer supports all defined data types.  
- [ ] ✅ Test loop autonomy under simulated failure scenarios.  
- [ ] ✅ Validate performance against P08 REASON benchmarks.  
- [ ] ✅ Ensure documentation completeness in OUTPUT_TEMPLATE.md.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_dual_loop_architecture]] | downstream | 0.48 |
| [[bld_knowledge_card_dual_loop_architecture]] | upstream | 0.46 |
| [[p03_sp_dual_loop_architecture_builder]] | related | 0.45 |
| [[dual-loop-architecture-builder]] | downstream | 0.44 |
| [[p10_lr_dual_loop_architecture_builder]] | downstream | 0.42 |
| [[kc_dual_loop_architecture]] | upstream | 0.41 |
| [[bld_examples_dual_loop_architecture]] | downstream | 0.40 |
| [[p08_qg_dual_loop_architecture]] | downstream | 0.37 |
| [[bld_tools_dual_loop_architecture]] | downstream | 0.32 |
| [[bld_architecture_dual_loop_architecture]] | downstream | 0.30 |
