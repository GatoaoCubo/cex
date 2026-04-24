---
# TEMPLATE: Feature Flag
# Preencha todas as {{VARIAVEIS}} antes de usar
# Valide contra P09_config/_schema.yaml (types.feature_flag)
# Max 256 bytes | density_min: 0.80 | quality_min: 8.0

id: p09_ff_{{FEATURE_SLUG}}
kind: feature_flag
8f: F1_constrain
pillar: P09
title: "Flag: {{FLAG_NAME}}"
version: 1.0.0
created: {{ISO_DATE}}
updated: {{ISO_DATE}}
author: {{AGENT_GROUP_NAME}}
quality: {{QUALITY_8_TO_10}}
tags: [{{TAG1}}, {{TAG2}}, feature-flag, config]
tldr: "{{ONE_SENTENCE_WHAT_FLAG_CONTROLS}}"
density_score: {{0.80_TO_1.00}}
---

# Flag: {{FLAG_NAME}}

## Definition

| Property | Value |
|----------|-------|
| Flag | `{{FLAG_NAME}}` |
| State | {{on / off}} |
| Rollout | {{100% / gradual_N%}} |
| Owner | {{TEAM_OR_PERSON}} |
| Expires | {{ISO_DATE_OR_never}} |

## Behavior

| State | Effect |
|-------|--------|
| `on` | {{WHAT_HAPPENS_WHEN_ENABLED}} |
| `off` | {{WHAT_HAPPENS_WHEN_DISABLED}} |

## Guard

- Enable condition: {{WHEN_TO_TURN_ON}}
- Disable condition: {{WHEN_TO_TURN_OFF}}
- Rollback: {{HOW_TO_EMERGENCY_DISABLE}}
