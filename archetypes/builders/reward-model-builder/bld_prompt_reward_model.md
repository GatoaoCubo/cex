---
kind: instruction
id: bld_instruction_reward_model
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for reward_model
quality: 8.9
title: "Instruction Reward Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [reward_model, builder, instruction]
tldr: "Step-by-step production process for reward_model"
domain: "reward_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_instruction_judge_config
  - bld_instruction_eval_framework
  - bld_instruction_benchmark_suite
  - bld_instruction_eval_metric
  - bld_instruction_content_filter
  - bld_instruction_playground_config
  - bld_instruction_planning_strategy
  - bld_instruction_edit_format
  - bld_instruction_sandbox_spec
  - bld_architecture_reward_model
---

## Phase 1: RESEARCH  
1. Define reward_model objectives: align with P07 governance metrics.  
2. Gather stakeholder input: identify process/outcome prioritization weights.  
3. Analyze historical data: extract reward triggers and scaling factors.  
4. Review existing schemas: map to SCHEMA.md’s reward_model structure.  
5. Identify edge cases: e.g., conflicting outcomes, zero-impact scenarios.  
6. Validate assumptions: confirm alignment with domain-specific governance rules.  

## Phase 2: COMPOSE  
1. Set up environment: install dependencies from SCHEMA.md’s toolchain.  
2. Define reward_model schema: use SCHEMA.md’s `reward_config` structure.  
3. Map variables: assign process/outcome keys to `metrics` array in OUTPUT_TEMPLATE.md.  
4. Write configuration: populate `weights`, `thresholds`, and `scaling_functions`.  
5. Align with template: ensure `version` and `governance_rules` match OUTPUT_TEMPLATE.md.  
6. Integrate validation: add `preconditions` and `postconditions` per SCHEMA.md.  
7. Document parameters: describe each metric’s purpose in `metadata` section.  
8. Test with sample data: simulate outcomes using OUTPUT_TEMPLATE.md’s examples.  
9. Finalize model: export as YAML/JSON per SCHEMA.md’s format specifications.  

## Phase 3: VALIDATE  
- [ ] ✅ Check schema compliance: validate against SCHEMA.md’s `reward_model` spec.  
- [ ] ✅ Verify data alignment: ensure metrics match stakeholder-defined priorities.  
- [ ] ✅ Test edge cases: confirm zero-impact and conflicting-outcome handling.  
- [ ] ✅ Audit governance rules: ensure `governance_rules` align with P07 pillars.  
- [ ] ✅ Peer review: cross-check with domain experts for logic consistency.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_judge_config]] | sibling | 0.40 |
| [[bld_instruction_eval_framework]] | sibling | 0.35 |
| [[bld_instruction_benchmark_suite]] | sibling | 0.33 |
| [[bld_instruction_eval_metric]] | sibling | 0.32 |
| [[bld_instruction_content_filter]] | sibling | 0.30 |
| [[bld_instruction_playground_config]] | sibling | 0.28 |
| [[bld_instruction_planning_strategy]] | sibling | 0.28 |
| [[bld_instruction_edit_format]] | sibling | 0.27 |
| [[bld_instruction_sandbox_spec]] | sibling | 0.27 |
| [[bld_architecture_reward_model]] | downstream | 0.26 |
