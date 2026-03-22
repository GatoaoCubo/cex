---
# TEMPLATE: Satellite Specification
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P08_architecture/_schema.yaml (types.satellite_spec)
# Max 2KB | density_min: 0.80 | quality_min: 8.0

id: p08_sat_{{NAME_LOWER}}
type: satellite_spec
lp: P08
title: "Satellite: {{SAT_NAME_UPPER}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{SATELLITE_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [{{TAG1}}, satellite, spec]
tldr: "{{ONE_SENTENCE_SATELLITE_ROLE}}"
density_score: {{0.80_TO_1.00}}
linked_artifacts:
  prime: {{records/satellites/NAME/PRIME_NAME.md}}
  mental_model: {{records/satellites/NAME/mental_model.yaml}}
---

# Satellite: {{SAT_NAME_UPPER}}

## Identity

| Property | Value |
|----------|-------|
| Name | {{SAT_NAME_UPPER}} |
| Domain | {{DOMAIN_PHRASE}} |
| Model | {{opus|sonnet|haiku}} |
| Runtime | {{claude|codex}} |
| Boot time | {{SECONDS}}s |
| MCPs | {{MCP_1}}, {{MCP_2}} |

## Role

{{2_3_SENTENCES_WHAT_THIS_SATELLITE_DOES_AND_DOESNT}}

## Capabilities

| Capability | Description | Quality |
|------------|-------------|---------|
| {{CAP_1}} | {{WHAT_IT_CAN_DO}} | {{8.0_TO_10}} |
| {{CAP_2}} | {{WHAT_IT_CAN_DO}} | {{8.0_TO_10}} |
| {{CAP_3}} | {{WHAT_IT_CAN_DO}} | {{8.0_TO_10}} |

## Routing Keywords

`{{keyword1}}, {{keyword2}}, {{keyword3}}, {{keyword4}}, {{keyword5}}`

## Constraints

- Max concurrent: {{N_INSTANCES}}
- Token budget: {{TOKENS_PER_TASK}}
- Scope fence: ONLY `{{ALLOWED_PATHS}}`
- Never: {{WHAT_IT_MUST_NOT_DO}}

## Spawn

```bash
powershell -NoProfile -ExecutionPolicy Bypass -File records/framework/powershell/spawn_solo.ps1 -sat {{SAT_LOWER}} -task "{{TASK}}" -interactive
```

## Diagram

```
[User/STELLA] --handoff--> [{{SAT_NAME}}]
                                |
                           [{{MCP_1}}] + [{{MCP_2}}]
                                |
                           [output] --signal--> [STELLA]
```

## Failure Modes

| Failure | Detection | Recovery |
|---------|-----------|----------|
| {{FAILURE_1}} | {{HOW_DETECTED}} | {{HOW_TO_RECOVER}} |
| {{FAILURE_2}} | {{HOW_DETECTED}} | {{HOW_TO_RECOVER}} |
