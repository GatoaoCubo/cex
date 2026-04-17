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
