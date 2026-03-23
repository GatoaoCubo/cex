---
# TEMPLATE: Daemon (P04 Tools)
# Valide contra P04_tools/_schema.yaml (types.daemon)
# Max 1024 bytes

id: p04_daemon_{{NAME_SLUG}}
type: daemon
lp: P04
title: "Daemon: {{DAEMON_NAME}}"
quality: {{QUALITY_7_TO_10}}
---

# Daemon: {{DAEMON_NAME}}

## Runtime
- Trigger: {{cron|queue|watcher}}
- Interval: {{INTERVAL}}
- Owner: {{OWNER}}

## Loop
1. {{READ_INPUT}}
2. {{PROCESS_WORK}}
3. {{EMIT_STATE}}

## Safety
- Healthcheck: {{HEALTHCHECK_SIGNAL}}
- Restart policy: {{RESTART_POLICY}}
- Stop condition: {{STOP_CONDITION}}
