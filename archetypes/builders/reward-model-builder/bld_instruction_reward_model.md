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
