---
quality: 8.4
quality: 7.9
kind: instruction
id: bld_instruction_pipeline_template
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for pipeline_template
title: "Instruction Pipeline Template"
version: "1.0.0"
author: n03_hermes_w1_5
tags: [pipeline_template, builder, instruction, hermes, scenario_indexed]
tldr: "Step-by-step production process for pipeline_template"
domain: "pipeline_template construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.87
related:
  - bld_instruction_e2e_eval
  - p10_lr_e2e_eval_builder
  - bld_collaboration_llm_evaluation_scenario
  - llm-evaluation-scenario-builder
  - bld_instruction_nucleus_def
  - bld_instruction_input_schema
  - bld_instruction_playground_config
  - p03_sp_llm_evaluation_scenario_builder
  - bld_instruction_enum_def
  - p11_qg_e2e_eval
---

## Phase 1: RESEARCH
1. Identify target scenario from the 7 canonical values: new_feature, new_feature_security, bug_fix_unknown, bug_fix_known, refactoring, perf_opt, infra.
2. Load the canonical stage sequence for the scenario from bld_knowledge_card_pipeline_template.md.
3. Identify optional stages (e.g., researcher for new_feature_security, security for new_feature_security).
4. Determine model_tier per stage: xhigh for architect/planner; high for analyst/coder/optimizer/refactorer/devops; medium for finder/debugger/fixer/documenter/security; low for reviewer/tester.
5. Confirm revision_loop target (user for interactive, nucleus for autonomous).

## Phase 2: COMPOSE
1. Reference SCHEMA (bld_schema_pipeline_template.md) for required fields.
2. Set scenario to one of the 7 canonical values.
3. Populate stages array in execution order; mark optional stages.
4. Set model_tier for each stage per the tier mapping from Phase 1.
5. Configure revision_loop: max_iterations (default 3), escalation_target.
6. Set quality_gates: mandatory MUST include reviewer and tester; set priority_order.
7. Apply naming: `p12_pt_{{scenario}}.yaml` (yaml extension, not .md).
8. Set tags: [hermes_origin, pipeline, scenario_indexed] plus scenario-specific tags.
9. Proofread: stages in correct order, no missing mandatory gates, revision_loop valid.

## Phase 3: VALIDATE
- [ ] scenario is one of the 7 canonical values.
- [ ] stages array has >= 2 entries, all in execution order.
- [ ] every stage has role and model_tier set.
- [ ] quality_gates.mandatory includes reviewer and tester.
- [ ] revision_loop.max_iterations between 1 and 5.
- [ ] priority_order includes security for new_feature_security scenario.
- [ ] File size <= 4096 bytes.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_e2e_eval]] | sibling | 0.26 |
| [[p10_lr_e2e_eval_builder]] | downstream | 0.23 |
| [[bld_collaboration_llm_evaluation_scenario]] | downstream | 0.21 |
| [[llm-evaluation-scenario-builder]] | downstream | 0.20 |
| [[bld_instruction_nucleus_def]] | sibling | 0.20 |
| [[bld_instruction_input_schema]] | sibling | 0.20 |
| [[bld_instruction_playground_config]] | sibling | 0.19 |
| [[p03_sp_llm_evaluation_scenario_builder]] | related | 0.19 |
| [[bld_instruction_enum_def]] | sibling | 0.19 |
| [[p11_qg_e2e_eval]] | downstream | 0.18 |
