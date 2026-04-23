---
kind: instruction
id: bld_instruction_eval_framework
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for eval_framework
quality: 8.8
title: "Instruction Eval Framework"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_framework, builder, instruction]
tldr: "Step-by-step production process for eval_framework"
domain: "eval_framework construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_judge_config
  - bld_instruction_eval_metric
  - bld_instruction_reward_model
  - eval-framework-builder
  - bld_instruction_playground_config
  - bld_instruction_benchmark_suite
  - bld_instruction_compliance_framework
  - bld_instruction_content_filter
  - bld_instruction_trajectory_eval
  - bld_instruction_prompt_optimizer
---

## Phase 1: RESEARCH  
1. Define evaluation criteria aligned with P07 governance metrics  
2. Identify required data sources and integration points  
3. Survey existing evaluation tools and frameworks  
4. Document success/failure scenarios for edge cases  
5. Map stakeholder requirements to evaluation phases  
6. Assess regulatory and compliance constraints  

## Phase 2: COMPOSE  
1. Set up dev environment with SCHEMA.md as reference  
2. Implement evaluation pipeline using OUTPUT_TEMPLATE.md structure  
3. Write data ingestion module for heterogeneous sources  
4. Develop scoring engine with weighted metric calculations  
5. Integrate visualization layer for result interpretation  
6. Add audit logging for traceability per P07 standards  
7. Implement validation rules from SCHEMA.md  
8. Write unit tests for each evaluation component  
9. Finalize artifact with governance metadata tags  

## Phase 3: VALIDATE  
- [ ] Verify schema alignment with SCHEMA.md  
- [ ] Confirm data integrity across all integration points  
- [ ] Test tool compatibility with P07-compliant systems  
- [ ] Validate stakeholder requirements coverage  
- [ ] Ensure compliance with governance and regulatory rules


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_judge_config]] | sibling | 0.41 |
| [[bld_instruction_eval_metric]] | sibling | 0.36 |
| [[bld_instruction_reward_model]] | sibling | 0.29 |
| [[eval-framework-builder]] | downstream | 0.29 |
| [[bld_instruction_playground_config]] | sibling | 0.28 |
| [[bld_instruction_benchmark_suite]] | sibling | 0.28 |
| [[bld_instruction_compliance_framework]] | sibling | 0.27 |
| [[bld_instruction_content_filter]] | sibling | 0.26 |
| [[bld_instruction_trajectory_eval]] | sibling | 0.25 |
| [[bld_instruction_prompt_optimizer]] | sibling | 0.25 |
