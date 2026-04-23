---
kind: instruction
id: bld_instruction_eval_metric
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for eval_metric
quality: 8.8
title: "Instruction Eval Metric"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_metric, builder, instruction]
tldr: "Step-by-step production process for eval_metric"
domain: "eval_metric construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_eval_framework
  - bld_instruction_judge_config
  - bld_instruction_reward_model
  - bld_instruction_content_filter
  - bld_instruction_benchmark_suite
  - bld_instruction_search_strategy
  - bld_instruction_playground_config
  - bld_instruction_prompt_optimizer
  - bld_instruction_planning_strategy
  - bld_instruction_edit_format
---

## Phase 1: RESEARCH  
1. Identify domain-specific KPIs aligned with P07 governance goals.  
2. Analyze historical data to determine baseline metric thresholds.  
3. Define success criteria (e.g., accuracy, fairness, scalability).  
4. Survey stakeholders for metric prioritization and weighting.  
5. Review existing evaluation frameworks for compatibility.  
6. Document data sources and quality requirements.  

## Phase 2: COMPOSE  
1. Set up environment with SCHEMA.md dependencies.  
2. Name metric using `P07_<DOMAIN>_<MEASURE>` convention.  
3. Map metric to SCHEMA.md fields: `id`, `description`, `formula`.  
4. Write calculation logic in Python (reference OUTPUT_TEMPLATE.md).  
5. Implement edge case handling (e.g., null values, outliers).  
6. Embed metadata: governance owner, data lineage, version.  
7. Validate against OUTPUT_TEMPLATE.md structure.  
8. Add unit tests for formula and edge cases.  
9. Finalize artifact with governance approval.  

## Phase 3: VALIDATE  
- [ ] ✅ Schema compliance (SCHEMA.md)  
- [ ] ✅ Formula passes unit tests  
- [ ] ✅ Edge cases handled (nulls, outliers)  
- [ ] ✅ Metric aligns with P07 governance goals  
- [ ] ✅ Stakeholder approval for definition and weights


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_eval_framework]] | sibling | 0.40 |
| [[bld_instruction_judge_config]] | sibling | 0.36 |
| [[bld_instruction_reward_model]] | sibling | 0.30 |
| [[bld_instruction_content_filter]] | sibling | 0.26 |
| [[bld_instruction_benchmark_suite]] | sibling | 0.26 |
| [[bld_instruction_search_strategy]] | sibling | 0.26 |
| [[bld_instruction_playground_config]] | sibling | 0.24 |
| [[bld_instruction_prompt_optimizer]] | sibling | 0.23 |
| [[bld_instruction_planning_strategy]] | sibling | 0.22 |
| [[bld_instruction_edit_format]] | sibling | 0.22 |
