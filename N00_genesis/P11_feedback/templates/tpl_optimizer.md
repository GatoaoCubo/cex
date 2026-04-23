---
# TEMPLATE: Optimizer (P11 Feedback)
# Valide contra P11_feedback/_schema.yaml (types.optimizer)
# Max 4096 bytes

id: p11_opt_{{TARGET_SLUG}}
kind: optimizer
pillar: P11
title: "Optimizer: {{TARGET_NAME}}"
version: 1.0.0
quality: 8.7
density_score: 1.0
related:
  - bld_collaboration_optimizer
  - p11_qg_optimizer
  - optimizer-builder
  - bld_output_template_user_journey
  - bld_architecture_optimizer
  - bld_knowledge_card_optimizer
  - p03_sp_optimizer_builder
  - p01_kc_optimizer
  - p03_ins_optimizer
  - bld_memory_optimizer
---

# Optimizer: {{TARGET_NAME}}

## Objective
{{ONE_SENTENCE_ON_THE_METRIC_TO_IMPROVE}}

## Signals
| Metric | Threshold | Action |
|--------|-----------|--------|
| {{METRIC_1}} | {{THRESHOLD_1}} | {{ACTION_1}} |
| {{METRIC_2}} | {{THRESHOLD_2}} | {{ACTION_2}} |
| {{METRIC_3}} | {{THRESHOLD_3}} | {{ACTION_3}} |

## Loop
1. {{MEASURE}}
2. {{CHOOSE_CHANGE}}
3. {{VERIFY_EFFECT}}

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_optimizer]] | related | 0.24 |
| [[p11_qg_optimizer]] | related | 0.22 |
| [[optimizer-builder]] | related | 0.21 |
| [[bld_output_template_user_journey]] | upstream | 0.21 |
| [[bld_architecture_optimizer]] | upstream | 0.20 |
| [[bld_knowledge_card_optimizer]] | upstream | 0.20 |
| [[p03_sp_optimizer_builder]] | upstream | 0.20 |
| [[p01_kc_optimizer]] | related | 0.19 |
| [[p03_ins_optimizer]] | upstream | 0.18 |
| [[bld_memory_optimizer]] | upstream | 0.17 |
