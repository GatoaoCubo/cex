---
# TEMPLATE: Formatter (P05 Output)
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P05_output/_schema.yaml (types.formatter)
# Max 4096 bytes

id: p05_fmt_{{FORMAT_SLUG}}
kind: formatter
pillar: P05
title: "Formatter: {{OUTPUT_NAME}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AGENT_GROUP_NAME}}
format: {{markdown|json|yaml|table}}
quality: {{QUALITY_8_TO_10}}
tags: [{{TAG1}}, formatter, output]
tldr: "{{ONE_SENTENCE_ON_FORMATTING_GOAL}}"
max_bytes: {{MAX_BYTES_INT}}
density_score: {{0.85_TO_1.00}}
linked_artifacts:
  schema: {{p06_is_name_OR_null}}
---

# Formatter: {{OUTPUT_NAME}}

## Purpose
{{COMO_ESTE_FORMATTER_PADRONIZA_A_SAIDA}}.

## Structure
```text
{{HEADER_SECTION}}
{{BODY_SECTION}}
{{FOOTER_SECTION}}
```

## Rules
| Rule | Why |
|------|-----|
| {{RULE_1}} | {{JUSTIFICATIVA_1}} |
| {{RULE_2}} | {{JUSTIFICATIVA_2}} |
| {{RULE_3}} | {{JUSTIFICATIVA_3}} |

## Valid Example
```{{FORMAT_LOWER}}
{{EXEMPLO_VALIDO_CONCRETO}}
```

## Invalid Example
```{{FORMAT_LOWER}}
{{EXEMPLO_INVALIDO_COM_FALHA_OBSERVAVEL}}
```
