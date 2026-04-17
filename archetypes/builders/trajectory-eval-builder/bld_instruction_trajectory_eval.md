---
kind: instruction
id: bld_instruction_trajectory_eval
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for trajectory_eval
quality: 8.9
title: "Instruction Trajectory Eval"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [trajectory_eval, builder, instruction]
tldr: "Step-by-step production process for trajectory_eval"
domain: "trajectory_eval construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Review existing agent trajectory evaluation frameworks (e.g., RL benchmarks, safety metrics).  
2. Define evaluation criteria: success rate, deviation from policy, resource usage, and ethical compliance.  
3. Analyze case studies of agent failures in real-world deployments.  
4. Collect annotated trajectory datasets for training and validation.  
5. Benchmark against P07 governance standards for AI system accountability.  
6. Interview domain experts to identify unmet evaluation needs.  

## Phase 2: COMPOSE
1. Set up artifact structure using bld_schema_trajectory_eval.md’s field definitions.
2. Write trajectory overview table aligned with bld_output_template_trajectory_eval.md’s structure.
3. Log each step: observation summary, reasoning summary, action taken, outcome.
4. Compute all evaluation metrics: task_success, path_efficiency, tool_call_accuracy, partial_credit.
5. Score each step using LLM-as-judge pattern from bld_quality_gate_trajectory_eval.md.
6. Reference bld_schema_trajectory_eval.md for ID pattern and required fields.
7. Identify first failure step and classify root cause (hallucination/grounding_error/tool_misuse/reasoning_drift).
8. Write targeted recommendations based on failure analysis.
9. Finalize frontmatter and compile: python _tools/cex_compile.py {path}  

## Phase 3: VALIDATE  
- [ ] Conduct peer review for clarity and governance alignment.  
- [ ] Verify data accuracy against Phase 1 datasets.  
- [ ] Ensure schema compliance (SCHEMA.md) and template adherence (OUTPUT_TEMPLATE.md).  
- [ ] Test artifact with sample trajectories for usability.  
- [ ] Obtain stakeholder approval for deployment.
