---
pillar: P05
llm_function: PRODUCE
purpose: Template with variables that the LLM fills to produce a validator
pattern: every field here exists in SCHEMA.md
---

# Output Template: validator

```yaml
---
id: p06_val_{{rule_slug}}
kind: validator
pillar: P06
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{producer}}"
title: "Validator: {{what_it_validates}}"
trigger: {{pre_commit|post_generate|pre_pool|on_signal}}
severity: {{block|warn|info}}
quality: null
tags: [validator, {{domain_tag}}, {{scope_tag}}]
tldr: "{{one_sentence_rejection_rule}}"
threshold: {{number_or_null}}
target: "{{file_glob_or_field_path}}"
action_on_fail: {{reject|warn|log}}
density_score: {{0.80_to_1.00}}
linked_artifacts:
  source: {{schema_or_law_ref}}
  related: {{related_artifact_or_null}}
---
```

## Rule

```yaml
condition: {{expression_that_must_be_true}}
```

## Checks

| # | Check | Expression | On Fail |
|---|-------|------------|---------|
| 1 | {{check_name_1}} | `{{expression_1}}` | {{reject|warn|log}} |
| 2 | {{check_name_2}} | `{{expression_2}}` | {{reject|warn|log}} |
| 3 | {{check_name_3}} | `{{expression_3}}` | {{reject|warn|log}} |

## Error Messages

| Check | Message | Fix Hint |
|-------|---------|----------|
| {{check_name_1}} | `{{clear_error_message}}` | {{how_to_fix}} |
| {{check_name_2}} | `{{clear_error_message}}` | {{how_to_fix}} |

## Pass Example
```text
Input: {{passing_input}}
Result: PASS
```

## Fail Example
```text
Input: {{failing_input}}
Result: FAIL - {{error_message}}
```
