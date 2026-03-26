---
# TEMPLATE: Hook (P04 Tools)
# Valide contra P04_tools/_schema.yaml (types.hook)
# Max 1024 bytes

id: p04_hook_{{HOOK_SLUG}}
kind: {{pre|post|stop}}
trigger_event: {{EVENT_NAME}}
script_path: {{RELATIVE_SCRIPT_PATH}}
---

# Hook: {{HOOK_SLUG}}

## Trigger
<!-- INSTRUCAO: evento observavel que dispara o hook. -->
- Type: {{pre|post|stop}}
- Event: {{EVENT_NAME}}
- Script: {{RELATIVE_SCRIPT_PATH}}

## Behavior
1. {{O_QUE_LE_OU_RECEBE}}
2. {{O_QUE_TRANSFORMA_OU_VALIDA}}
3. {{O_QUE_EMITE_OU_BLOQUEIA}}

## Safety
- Fail mode: {{warn|block|noop}}
- Idempotent: {{yes|no}}
- Timeout: {{SECONDS_INT}}s
