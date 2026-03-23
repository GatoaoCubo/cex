---
# TEMPLATE: Output Schema (P06 Schema)
# Valide contra P06_schema/_schema.yaml (types.output_schema)
# Max 3072 bytes

id: p06_os_{{SCOPE_SLUG}}
type: output_schema
lp: P06
title: "Output Schema: {{SCOPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Output Schema: {{SCOPE_NAME}}

## Envelope
```yaml
status: {{success|error}}
message: {{SHORT_MESSAGE}}
data:
  {{FIELD_1}}: {{TYPE_1}}
```

## Field Contract
| Field | Type | Required | Notes |
|-------|------|----------|-------|
| status | string | yes | {{STATUS_RULE}} |
| message | string | yes | {{MESSAGE_RULE}} |
| {{FIELD_1}} | {{TYPE_1}} | yes | {{NOTE_1}} |
| {{FIELD_2}} | {{TYPE_2}} | no | {{NOTE_2}} |

## Validation
1. {{VALIDATION_RULE_1}}
2. {{VALIDATION_RULE_2}}
3. {{VALIDATION_RULE_3}}
