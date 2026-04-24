---
# TEMPLATE: Scoring Rubric (P07 Evals)
# Valide contra P07_evals/_schema.yaml (types.scoring_rubric)
# Max 3072 bytes

id: p07_sr_{{FRAMEWORK_SLUG}}
kind: scoring_rubric
8f: F7_govern
pillar: P07
title: "Scoring Rubric: {{FRAMEWORK_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Scoring Rubric: {{FRAMEWORK_NAME}}

## Dimensions
| Dimension | Weight | 5 Score | 1 Score |
|-----------|--------|---------|---------|
| {{DIMENSION_1}} | {{WEIGHT_1}} | {{BEST_CASE_1}} | {{WORST_CASE_1}} |
| {{DIMENSION_2}} | {{WEIGHT_2}} | {{BEST_CASE_2}} | {{WORST_CASE_2}} |
| {{DIMENSION_3}} | {{WEIGHT_3}} | {{BEST_CASE_3}} | {{WORST_CASE_3}} |

## Scoring Rule
1. {{HOW_TO_SCORE_1}}
2. {{HOW_TO_SCORE_2}}
3. {{HOW_TO_SCORE_3}}

## Pass Threshold
- Minimum total: {{MIN_SCORE}}
- Auto-fail condition: {{BLOCKING_FAILURE}}
