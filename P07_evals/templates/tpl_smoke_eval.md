---
# TEMPLATE: Smoke Eval (P07 Evals)
# Valide contra P07_evals/_schema.yaml (types.smoke_eval)
# Max 3072 bytes

id: p07_se_{{SCOPE_SLUG}}
type: smoke_eval
lp: P07
title: "Smoke Eval: {{SCOPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Smoke Eval: {{SCOPE_NAME}}

## Goal
{{FAST_SANITY_CHECK_FOR_THE_CRITICAL_PATH}}

## Setup
- Target: {{TARGET_UNDER_TEST}}
- Max duration: {{UNDER_30_SECONDS}}
- Preconditions: {{PRECONDITION}}

## Execute
1. {{STEP_1}}
2. {{STEP_2}}
3. {{STEP_3}}

## Assert
- {{ASSERTION_1}}
- {{ASSERTION_2}}
- {{ASSERTION_3}}
