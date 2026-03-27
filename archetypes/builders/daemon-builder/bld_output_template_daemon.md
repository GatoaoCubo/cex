---
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a daemon artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
---

# Output Template: daemon

```yaml
---
id: p04_daemon_{{name_slug}}
kind: daemon
pillar: P04
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{who_produced}}"
name: "{{human_readable_daemon_name}}"
schedule: "{{continuous_or_cron_or_interval}}"
restart_policy: {{always|on_failure|never}}
signal_handling: "{{sigterm_behavior_summary}}"
quality: null
tags: [daemon, {{tag_2}}, {{tag_3}}]
tldr: "{{dense_summary_max_160ch}}"
description: "{{what_daemon_does_max_200ch}}"
health_check: "{{health_check_strategy}}"
pid_file: "{{pid_file_path}}"
resource_limits: "{{cpu_memory_fd_limits}}"
monitoring: "{{metrics_and_alerting_summary}}"
logging: {{structured|plaintext|syslog}}
graceful_shutdown: "{{shutdown_procedure}}"
max_restarts: "{{N_in_window}}"
---
```

## Overview
{{what_daemon_does_and_why_background_1_to_2_sentences}}
{{who_depends_on_it_and_what_triggers_it}}

## Lifecycle
Schedule: {{schedule_details}}
Startup: {{startup_sequence}}
Restart: {{restart_policy}} — {{restart_behavior_details}}
Shutdown: {{graceful_shutdown_procedure}}

## Signal Handling

| Signal | Response |
|--------|----------|
| SIGTERM | {{sigterm_behavior}} |
| SIGINT | {{sigint_behavior}} |
| SIGHUP | {{sighup_behavior}} |
| {{custom_signal}} | {{custom_behavior}} |

## Monitoring
Health: {{health_check_details}}
Metrics: {{metrics_collected}}
Alerting: {{alert_conditions}}
Logging: {{log_format_and_rotation}}

## References
- {{reference_1}}
- {{reference_2}}
