---
# TEMPLATE: Parser (P05 Output)
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P05_output/_schema.yaml (types.parser)
# Max 4096 bytes

id: p05_parser_{{TARGET_SLUG}}
kind: parser
pillar: P05
title: "Parser: {{TARGET_NAME}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AGENT_GROUP_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [parser, output, {{TAG1}}]
tldr: "{{ONE_SENTENCE_ON_EXTRACTION_GOAL}}"
density_score: {{0.80_TO_1.00}}
---

# Parser: {{TARGET_NAME}}

## Input Format
```text
{{RAW_INPUT_EXAMPLE}}
```

## Extraction Rules
| Field | Pattern | Transform |
|-------|---------|-----------|
| {{FIELD_1}} | {{REGEX_OR_RULE_1}} | {{CAST_OR_NORMALIZE_1}} |
| {{FIELD_2}} | {{REGEX_OR_RULE_2}} | {{CAST_OR_NORMALIZE_2}} |
| {{FIELD_3}} | {{REGEX_OR_RULE_3}} | {{CAST_OR_NORMALIZE_3}} |

## Parsed Output
```yaml
{{FIELD_1}}: {{EXAMPLE_VALUE_1}}
{{FIELD_2}}: {{EXAMPLE_VALUE_2}}
{{FIELD_3}}: {{EXAMPLE_VALUE_3}}
```

## Validation
- Reject when: {{BROKEN_PATTERN}}
- Accept when: {{MINIMUM_COMPLETE_SHAPE}}
