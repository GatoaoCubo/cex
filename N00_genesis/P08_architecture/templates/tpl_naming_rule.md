---
# TEMPLATE: Naming Rule (P05 Output)
# Valide contra P05_output/_schema.yaml (types.naming_rule)
# Max 4096 bytes

id: p05_nr_{{SCOPE_SLUG}}
kind: naming_rule
8f: F1_constrain
pillar: P05
title: "Naming Rule: {{SCOPE_NAME}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AGENT_GROUP_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [naming, convention, {{TAG1}}]
tldr: "{{ONE_SENTENCE_NAMING_PATTERN}}"
max_bytes: {{MAX_BYTES_INT}}
density_score: {{0.85_TO_1.00}}
---

# Naming Rule: {{SCOPE_NAME}}

## Pattern
```text
{{CANONICAL_FILENAME_OR_ID_PATTERN}}
```

## Segments
| Segment | Rule | Example |
|---------|------|---------|
| {{SEGMENT_1}} | {{REGRA_1}} | {{EXEMPLO_1}} |
| {{SEGMENT_2}} | {{REGRA_2}} | {{EXEMPLO_2}} |
| {{SEGMENT_3}} | {{REGRA_3}} | {{EXEMPLO_3}} |

## Constraints
- {{CONSTRAINT_1}}
- {{CONSTRAINT_2}}
- {{CONSTRAINT_3}}

## Invalid Examples
```text
{{EXEMPLO_INVALIDO_1}}  # FAILS: {{MOTIVO_1}}
{{EXEMPLO_INVALIDO_2}}  # FAILS: {{MOTIVO_2}}
```
