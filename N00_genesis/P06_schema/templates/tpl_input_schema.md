---
# TEMPLATE: Input Schema
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P06_schema/_schema.yaml (types.input_schema)
# Max 1KB | density_min: 0.85 | quality_min: 8.0

id: p06_is_{{SCOPE_SLUG}}
kind: input_schema
8f: F1_constrain
pillar: P06
title: "Input Schema: {{AGENT_OR_SKILL_NAME}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AGENT_GROUP_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, input, contract]
tldr: "{{ONE_SENTENCE_WHAT_INPUT_THIS_VALIDATES}}"
density_score: {{0.85_TO_1.00}}
linked_artifacts:
  agent: {{p02_ag_name_OR_null}}
  output: {{p05_os_name_OR_null}}
---

# Input Schema: {{AGENT_OR_SKILL_NAME}}

## Fields

| Field | Type | Required | Default | Constraints | Example |
|-------|------|----------|---------|-------------|---------|
| {{FIELD_1}} | {{string|int|float|bool|list|object}} | {{yes|no}} | {{DEFAULT_OR_none}} | {{MIN_MAX_ENUM_REGEX}} | {{CONCRETE_EXAMPLE}} |
| {{FIELD_2}} | {{string|int|float|bool|list|object}} | {{yes|no}} | {{DEFAULT_OR_none}} | {{MIN_MAX_ENUM_REGEX}} | {{CONCRETE_EXAMPLE}} |
| {{FIELD_3}} | {{string|int|float|bool|list|object}} | {{yes|no}} | {{DEFAULT_OR_none}} | {{MIN_MAX_ENUM_REGEX}} | {{CONCRETE_EXAMPLE}} |

## Validation Rules

1. {{RULE_1_IF_CONDITION_THEN_REJECT}}: `{{ERROR_MESSAGE_1}}`
2. {{RULE_2_IF_CONDITION_THEN_REJECT}}: `{{ERROR_MESSAGE_2}}`
3. {{RULE_3_IF_CONDITION_THEN_REJECT}}: `{{ERROR_MESSAGE_3}}`

## Valid Input Example

```yaml
{{FIELD_1}}: {{VALID_VALUE}}
{{FIELD_2}}: {{VALID_VALUE}}
{{FIELD_3}}: {{VALID_VALUE}}
```

## Invalid Input Example

```yaml
# FAILS: {{REASON_WHY_INVALID}}
{{FIELD_1}}: {{INVALID_VALUE}}
{{FIELD_2}}: {{INVALID_VALUE}}
```

## Upstream/Downstream

| Direction | Component | Protocol |
|-----------|-----------|----------|
| upstream | {{WHO_SENDS_THIS_INPUT}} | {{handoff|api|signal}} |
| downstream | {{WHO_RECEIVES_VALIDATED}} | {{handoff|api|signal}} |
