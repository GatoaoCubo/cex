---
quality: 8.0
quality: 7.8
id: bld_rules_canary_config
kind: knowledge_card
pillar: P08
title: "Rules: canary_config Builder Constraints"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: canary_config
tags: [rules, canary_config, P09]
llm_function: COLLABORATE
tldr: "Hard constraints and edge cases for canary_config builder."
density_score: null
related:
  - p10_lr_e2e_eval_builder
  - p11_qg_experiment_config
  - p01_kc_cicd_llm_pipeline
  - p11_qg_e2e_eval
  - p03_sp_ab_test_config_builder
  - bld_norms
  - bld_instruction_e2e_eval
  - p10_lr_golden_test_builder
  - bld_quality_gate_memory_type
  - p03_ins_quality_gate
---

# Rules: canary_config Builder

## Hard Constraints
1. First traffic stage MUST be < 50% (gate H09)
2. Last traffic stage MUST be 100% (gate H08)
3. rollback_trigger_metric MUST be set (gate H07)
4. canary_version and stable_version MUST be different
5. stages_count MUST equal len(stages list)
6. max_bytes: 2048 body
7. quality MUST be null
8. id pattern: `^p09_cc_[a-z][a-z0-9_]+$`

## Edge Cases
| Situation | Resolution |
|-----------|-----------|
| User wants to start at 50% | Reject: start at 5-10%; explain risk proportionality |
| No monitoring/metrics | Use synthetic health check as rollback trigger; note as limited |
| User conflates with feature_flag | Teach: feature_flag is boolean; canary_config is traffic % |
| User wants A/B statistical test | Redirect to ab_test_config |
| Single-stage "canary" (direct to 100%) | Reject: that is deployment_manifest, not canary |
| Partial rollout frozen (never 100%) | Use stages_count reflecting actual stages; mark as dark_launch variant |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_e2e_eval_builder]] | downstream | 0.22 |
| [[p11_qg_experiment_config]] | downstream | 0.19 |
| [[p01_kc_cicd_llm_pipeline]] | sibling | 0.18 |
| [[p11_qg_e2e_eval]] | downstream | 0.18 |
| [[p03_sp_ab_test_config_builder]] | upstream | 0.18 |
| [[bld_norms]] | related | 0.18 |
| [[bld_instruction_e2e_eval]] | upstream | 0.18 |
| [[p10_lr_golden_test_builder]] | downstream | 0.17 |
| [[bld_quality_gate_memory_type]] | downstream | 0.17 |
| [[p03_ins_quality_gate]] | downstream | 0.17 |
