---
kind: instruction
id: bld_instruction_judge_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for judge_config
quality: 8.8
title: "Instruction Judge Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [judge_config, builder, instruction]
tldr: "Step-by-step production process for judge_config"
domain: "judge_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_eval_framework
  - bld_instruction_playground_config
  - bld_instruction_reward_model
  - bld_instruction_eval_metric
  - bld_instruction_content_filter
  - bld_instruction_benchmark_suite
  - bld_instruction_edit_format
  - bld_instruction_safety_policy
  - bld_instruction_planning_strategy
  - bld_instruction_trajectory_eval
---

## Phase 1: RESEARCH  
1. Identify evaluation criteria (accuracy, fairness, compliance).  
2. Analyze existing judge_config templates for P07.  
3. Determine governance rules (scoring thresholds, escalation paths).  
4. Map LLM output types to evaluation metrics.  
5. Review schema constraints from SCHEMA.md.  
6. Document use cases for automated evaluation scenarios.  

## Phase 2: COMPOSE  
1. Define config structure: `judge_id`, `version`, `criteria`.  
2. Specify evaluation parameters (weightings, tolerances).  
3. Align with SCHEMA.md: ensure required fields are present.  
4. Populate `criteria` array with metric names and descriptions.  
5. Configure `governance` block: rules, thresholds, escalation.  
6. Integrate `output_template` from OUTPUT_TEMPLATE.md.  
7. Add `validation_rules` for schema compliance checks.  
8. Write `metadata` section: author, date, revision history.  
9. Finalize config with YAML/JSON syntax and comments.  

## Phase 3: VALIDATE  
- [ ] ✅ Validate schema compliance using SCHEMA.md  
- [ ] ✅ Check completeness of all required fields  
- [ ] ✅ Confirm governance rules align with P07 policies  
- [ ] ✅ Test config against sample LLM outputs  
- [ ] ✅ Obtain stakeholder approval for deployment


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_eval_framework]] | sibling | 0.39 |
| [[bld_instruction_playground_config]] | sibling | 0.33 |
| [[bld_instruction_reward_model]] | sibling | 0.32 |
| [[bld_instruction_eval_metric]] | sibling | 0.31 |
| [[bld_instruction_content_filter]] | sibling | 0.30 |
| [[bld_instruction_benchmark_suite]] | sibling | 0.29 |
| [[bld_instruction_edit_format]] | sibling | 0.26 |
| [[bld_instruction_safety_policy]] | sibling | 0.26 |
| [[bld_instruction_planning_strategy]] | sibling | 0.25 |
| [[bld_instruction_trajectory_eval]] | sibling | 0.24 |
