---
# TEMPLATE: Spawn Config (P12 Orchestration)
# Valide contra P12_orchestration/_schema.yaml (types.spawn_config)
# Max 3072 bytes

id: p12_spawn_{{MODE_SLUG}}
type: spawn_config
lp: P12
title: "Spawn Config: {{MODE_NAME}}"
quality: {{QUALITY_8_TO_10}}
---

# Spawn Config: {{MODE_NAME}}

## Strategy
```yaml
mode: {{solo|grid|continuous}}
max_agents: {{MAX_AGENTS}}
ownership: {{HOW_WORK_IS_SPLIT}}
```

## Dispatch Rules
- Spawn when: {{SPAWN_TRIGGER}}
- Reuse when: {{REUSE_TRIGGER}}
- Wait when: {{WAIT_TRIGGER}}

## Limits
- Cost budget: {{BUDGET_RULE}}
- Timeout: {{TIMEOUT_RULE}}
