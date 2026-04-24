---
# TEMPLATE: Type Definition (P06 Schema)
# Valide contra P06_schema/_schema.yaml (types.type_def)
# Max 3072 bytes

id: p06_td_{{TYPE_SLUG}}
kind: type_def
8f: F1_constrain
pillar: P06
title: "Type Def: {{TYPE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Type Def: {{TYPE_NAME}}

## Definition
```yaml
name: {{TYPE_NAME}}
base: {{string|integer|object|array}}
nullable: {{true|false}}
```

## Fields
| Field | Type | Required | Example |
|-------|------|----------|---------|
| {{FIELD_1}} | {{TYPE_1}} | yes | {{EXAMPLE_1}} |
| {{FIELD_2}} | {{TYPE_2}} | no | {{EXAMPLE_2}} |

## Constraints
- {{CONSTRAINT_1}}
- {{CONSTRAINT_2}}
- {{CONSTRAINT_3}}
