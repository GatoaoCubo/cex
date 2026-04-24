---
# TEMPLATE: Validator
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P06_schema/_schema.yaml (types.validator)
# Max 512B | density_min: 0.90 | quality_min: 8.0

id: p06_val_{{RULE_SLUG}}
kind: validator
8f: F7_govern
pillar: P06
title: "Validator: {{WHAT_IT_VALIDATES}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AGENT_GROUP_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [{{TAG1}}, validation, gate]
tldr: "{{ONE_SENTENCE_WHAT_THIS_REJECTS}}"
trigger: {{pre_commit|post_generate|pre_pool|on_signal}}
severity: {{block|warn|info}}
density_score: {{0.90_TO_1.00}}
---

# Validator: {{WHAT_IT_VALIDATES}}

## Rule

```yaml
target: {{FILE_GLOB_OR_FIELD_PATH}}
condition: {{EXPRESSION_THAT_MUST_BE_TRUE}}
threshold: {{NUMERIC_THRESHOLD_OR_null}}
action_on_fail: {{reject|warn|log}}
```

## Checks

| # | Check | Expression | On Fail |
|---|-------|------------|---------|
| 1 | {{CHECK_NAME_1}} | `{{FIELD}} {{>=|<=|==|!=|matches}} {{VALUE}}` | {{reject|warn}} |
| 2 | {{CHECK_NAME_2}} | `{{FIELD}} {{>=|<=|==|!=|matches}} {{VALUE}}` | {{reject|warn}} |
| 3 | {{CHECK_NAME_3}} | `{{FIELD}} {{>=|<=|==|!=|matches}} {{VALUE}}` | {{reject|warn}} |

## Error Messages

| Check | Message | Fix Hint |
|-------|---------|----------|
| {{CHECK_1}} | `{{CLEAR_ERROR_MESSAGE}}` | {{HOW_TO_FIX}} |
| {{CHECK_2}} | `{{CLEAR_ERROR_MESSAGE}}` | {{HOW_TO_FIX}} |

## Pass Example

```
Input: {{PASSING_INPUT_CONCRETE}}
Result: PASS
```

## Fail Example

```
Input: {{FAILING_INPUT_CONCRETE}}
Result: FAIL - {{ERROR_MESSAGE}}
```
