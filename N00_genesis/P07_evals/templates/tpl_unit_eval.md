---
# TEMPLATE: Unit Eval
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P07_evals/_schema.yaml (types.unit_eval)
# Max 2KB | density_min: 0.80 | quality_min: 8.0

id: p07_ue_{{TARGET_SLUG}}
kind: unit_eval
8f: F7_govern
pillar: P07
title: "Unit Eval: {{AGENT_OR_PROMPT_NAME}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AGENT_GROUP_NAME}}
target: {{p02_ag_name|p03_pt_name|p04_sk_name}}
quality: {{QUALITY_8_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, eval, unit]
tldr: "{{ONE_SENTENCE_WHAT_THIS_TESTS}}"
pass_threshold: {{SCORE_FLOAT}}
baseline: {{BASELINE_SCORE_OR_null}}
density_score: {{0.80_TO_1.00}}
linked_artifacts:
  target: {{ARTIFACT_ID}}
  schema: {{p06_is_name_OR_null}}
---

# Unit Eval: {{AGENT_OR_PROMPT_NAME}}

## Setup

- Target: `{{PATH_TO_AGENT_OR_PROMPT}}`
- Model: {{MODEL_USED}}
- Temperature: {{TEMPERATURE}}
- Max tokens: {{MAX_TOKENS}}

## Test Cases

### Case 1: {{CASE_NAME_HAPPY_PATH}}

**Input:**
```{{FORMAT}}
{{FIXED_INPUT_CONCRETE}}
```

**Expected Output:**
```{{FORMAT}}
{{EXPECTED_OUTPUT_CONCRETE}}
```

**Assertions:**
| # | Type | Expression | Weight |
|---|------|------------|--------|
| 1 | {{exact|contains|regex|score_gte}} | `{{ASSERTION_EXPRESSION}}` | {{0.0_TO_1.0}} |
| 2 | {{exact|contains|regex|score_gte}} | `{{ASSERTION_EXPRESSION}}` | {{0.0_TO_1.0}} |

### Case 2: {{CASE_NAME_EDGE_CASE}}

**Input:**
```{{FORMAT}}
{{EDGE_CASE_INPUT}}
```

**Expected:** {{EXPECTED_BEHAVIOR_DESCRIPTION}}

**Assertions:**
| # | Type | Expression | Weight |
|---|------|------------|--------|
| 1 | {{exact|contains|regex|score_gte}} | `{{ASSERTION_EXPRESSION}}` | {{0.0_TO_1.0}} |

## Pass/Fail Criteria

- Pass: weighted score >= {{PASS_THRESHOLD}}
- Baseline: {{BASELINE_SCORE}} ({{BASELINE_DATE}})
- Regression: fail if score drops > {{REGRESSION_DELTA}} from baseline

## Run History

| Date | Score | Pass | Notes |
|------|-------|------|-------|
| {{ISO_DATE}} | {{SCORE}} | {{yes|no}} | {{FIRST_RUN_BASELINE}} |
