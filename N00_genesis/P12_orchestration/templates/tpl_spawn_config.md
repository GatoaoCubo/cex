---
# TEMPLATE: Spawn Config (P12 Orchestration)
# Valide contra P12_orchestration/_schema.yaml (types.spawn_config)
# Max 3072 bytes

id: p12_spawn_{{MODE_SLUG}}
kind: spawn_config
8f: F1_constrain
pillar: P12
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

## Autonomy Mode
```yaml
autonomy_mode: {{interactive|yolo}}
# interactive: pause at every checkpoint for human approval
# yolo: auto-approve human-verify + auto-select-first for human-decision
```

## Checkpoint Types
<!-- Define how each checkpoint behaves per autonomy_mode -->

| Type | Frequency | interactive | yolo |
|------|-----------|-------------|------|
| `human-verify` | ~90% of checkpoints | Pause for approval | Auto-approve |
| `human-decision` | ~9% of checkpoints | Pause for selection | Auto-select first option |
| `human-action` | ~1% of checkpoints | Always stop | Always stop (cannot automate) |

## Guardrails
```yaml
guardrails:
  max_fix_attempts: 3          # After 3 retries, defer/escalate
  paralysis_guard: 5           # 5+ reads without a write → STOP and report
  analysis_paralysis_action: stop_and_report
```

## Worktree Isolation
```yaml
worktree:
  enabled: {{true|false}}
  strategy: {{per_agent_group|per_mission}}
  # per_agent_group: each sat gets own branch (sat/mission-name)
  # per_mission: one branch per mission, all sats share
  lifecycle:
    setup: "git worktree add .worktrees/{{sat}} -b {{branch}}"
    finish: {{merge_local|push_pr|keep|discard}}
    precondition: "baseline tests must pass before starting"
```

## Dispatch Rules
- Spawn when: {{SPAWN_TRIGGER}}
- Reuse when: {{REUSE_TRIGGER}}
- Wait when: {{WAIT_TRIGGER}}

## Limits
- Cost budget: {{BUDGET_RULE}}
- Timeout: {{TIMEOUT_RULE}}
