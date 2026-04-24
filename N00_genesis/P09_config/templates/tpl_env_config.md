---
# TEMPLATE: Environment Config
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P09_config/_schema.yaml (types.env_config)
# Max 512 bytes | density_min: 0.80 | quality_min: 8.0

id: p09_env_{{SCOPE}}
kind: env_config
8f: F1_constrain
pillar: P09
title: "Env: {{VAR_NAME}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AGENT_GROUP_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, env, config]
tldr: "{{ONE_SENTENCE_WHAT_THIS_VAR_CONTROLS}}"
density_score: {{0.80_TO_1.00}}
---

# Env: {{VAR_NAME}}

## Variable

| Property | Value |
|----------|-------|
| Name | `{{VAR_NAME}}` |
| Value | `{{DEFAULT_VALUE}}` |
| Scope | {{dev / staging / prod / all}} |
| Required | {{true / false}} |
| Format | {{string / int / bool / url / path}} |

## Source

- Where defined: {{FILE_OR_SERVICE_WHERE_SET}}
- How to obtain: {{INSTRUCTIONS_TO_GET_VALUE}}

## Fallback

| Condition | Behavior |
|-----------|----------|
| Absent | {{WHAT_HAPPENS_IF_MISSING}} |
| Default | `{{FALLBACK_VALUE}}` |

## Consumers

- {{SERVICE_1}}: {{HOW_IT_USES_THIS_VAR}}
- {{SERVICE_2}}: {{HOW_IT_USES_THIS_VAR}}

## Dependencies

- Requires: {{OTHER_VARS_OR_SERVICES_NEEDED}}
- Conflicts: {{VARS_THAT_CONFLICT}}
