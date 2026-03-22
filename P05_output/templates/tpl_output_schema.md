---
# TEMPLATE: Output Schema
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P05_output/_schema.yaml (types.output_schema)
# Max 1KB | density_min: 0.85 | quality_min: 8.0

id: p05_os_{{FORMAT_SLUG}}
type: output_schema
lp: P05
title: "Output Schema: {{AGENT_OR_SKILL_NAME}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{SATELLITE_NAME}}
format: {{json|yaml|markdown|table}}
quality: {{QUALITY_8_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, output]
tldr: "{{ONE_SENTENCE_WHAT_THIS_OUTPUT_DELIVERS}}"
max_bytes: {{MAX_BYTES_INT}}
density_score: {{0.85_TO_1.00}}
linked_artifacts:
  agent: {{p02_ag_name_OR_null}}
  schema: {{p06_is_name_OR_null}}
---

# Output Schema: {{AGENT_OR_SKILL_NAME}}

## Fields

| Field | Type | Required | Example |
|-------|------|----------|---------|
| {{FIELD_1}} | {{string|int|float|bool|list|object}} | {{yes|no}} | {{CONCRETE_EXAMPLE}} |
| {{FIELD_2}} | {{string|int|float|bool|list|object}} | {{yes|no}} | {{CONCRETE_EXAMPLE}} |
| {{FIELD_3}} | {{string|int|float|bool|list|object}} | {{yes|no}} | {{CONCRETE_EXAMPLE}} |

## Constraints

- max_bytes: {{MAX_BYTES_INT}}
- format: {{json|yaml|markdown}}
- encoding: utf-8
- {{CUSTOM_CONSTRAINT_1}}
- {{CUSTOM_CONSTRAINT_2}}

## Valid Example

```{{FORMAT}}
{{VALID_OUTPUT_EXAMPLE_CONCRETE}}
```

## Invalid Example

```{{FORMAT}}
{{INVALID_OUTPUT_EXAMPLE_WITH_COMMENT_WHY}}
```

## Error Handling

| Condition | Action | Return |
|-----------|--------|--------|
| {{ERROR_CONDITION_1}} | {{ACTION}} | {{FALLBACK_VALUE}} |
| {{ERROR_CONDITION_2}} | {{ACTION}} | {{FALLBACK_VALUE}} |
