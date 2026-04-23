---
kind: instruction
id: bld_instruction_benchmark_suite
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for benchmark_suite
quality: 8.9
title: "Instruction Benchmark Suite"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [benchmark_suite, builder, instruction]
tldr: "Step-by-step production process for benchmark_suite"
domain: "benchmark_suite construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_judge_config
  - kc_workflow_run_crate
  - bld_instruction_playground_config
  - bld_instruction_reward_model
  - bld_instruction_eval_framework
  - p10_mem_benchmark_suite_builder
  - p10_lr_builder-builder
  - p03_sp_benchmark_suite_builder
  - bld_instruction_content_filter
  - bld_instruction_search_strategy
---

## Phase 1: RESEARCH  
1. Identify benchmark objectives and scope (e.g., performance, scalability).  
2. Gather candidate tasks from existing benchmarks and domain experts.  
3. Analyze task dependencies and resource requirements (CPU, memory, I/O).  
4. Define success criteria and metrics for each task (e.g., latency, throughput).  
5. Prioritize tasks based on relevance to governance goals (P07).  
6. Document research findings in a structured requirements matrix.  

## Phase 2: COMPOSE  
1. Create artifact root directory with `schema.yaml` and `tasks/` subdirectory.  
2. Define benchmark_suite schema in `schema.yaml` (reference SCHEMA.md).  
3. Write individual task definitions in YAML format under `tasks/`.  
4. Integrate metrics configuration into each task (use OUTPUT_TEMPLATE.md).  
5. Ensure all tasks comply with schema constraints (validate against SCHEMA.md).  
6. Add metadata to benchmark_suite (author, version, license).  
7. Implement task execution order and dependencies in `workflow.yaml`.  
8. Include validation rules for input/output formats in `schema.yaml`.  
9. Finalize artifact with checksums and version control tags.  

## Phase 3: VALIDATE  
- [ ] ✅ Validate schema compliance using `schema.yaml` and SCHEMA.md  
- [ ] ✅ Confirm all tasks have defined metrics and success criteria  
- [ ] ✅ Execute benchmark_suite in test environment (dry-run)  
- [ ] ✅ Verify output matches OUTPUT_TEMPLATE.md structure  
- [ ] ✅ Review documentation for clarity and completeness


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_judge_config]] | sibling | 0.27 |
| [[kc_workflow_run_crate]] | related | 0.26 |
| [[bld_instruction_playground_config]] | sibling | 0.26 |
| [[bld_instruction_reward_model]] | sibling | 0.25 |
| [[bld_instruction_eval_framework]] | sibling | 0.25 |
| [[p10_mem_benchmark_suite_builder]] | downstream | 0.25 |
| [[p10_lr_builder-builder]] | downstream | 0.24 |
| [[p03_sp_benchmark_suite_builder]] | related | 0.23 |
| [[bld_instruction_content_filter]] | sibling | 0.23 |
| [[bld_instruction_search_strategy]] | sibling | 0.22 |
