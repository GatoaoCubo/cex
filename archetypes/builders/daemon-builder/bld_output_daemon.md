---
kind: output_template
id: bld_output_template_daemon
pillar: P05
llm_function: PRODUCE
purpose: Template with {{vars}} that the LLM fills to produce a daemon artifact
pattern: every field here exists in SCHEMA.md — template derives, never invents
quality: 9.1
title: "Output Template Daemon"
version: "1.0.0"
author: n03_builder
tags: [daemon, builder, examples]
tldr: "Golden and anti-examples for daemon construction, demonstrating ideal structure and common pitfalls."
domain: "daemon construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_schema_daemon
  - bld_examples_daemon
  - p03_sp_daemon_builder
  - p11_qg_daemon
  - bld_output_template_feature_flag
  - daemon-builder
  - bld_architecture_daemon
  - bld_output_template_input_schema
  - bld_output_template_runtime_rule
  - bld_output_template_golden_test
---

# Output Template: daemon
```yaml
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
```
## Overview
`{{what_daemon_does_and_why_background_1_to_2_sentences}}`
`{{who_depends_on_it_and_what_triggers_it}}`
## Lifecycle
Schedule: `{{schedule_details}}`
Startup: `{{startup_sequence}}`
Restart: `{{restart_policy}}` — `{{restart_behavior_details}}`
Shutdown: `{{graceful_shutdown_procedure}}`
## Signal Handling
| Signal | Response |
|--------|----------|
| SIGTERM | `{{sigterm_behavior}}` |
| SIGINT | `{{sigint_behavior}}` |
| SIGHUP | `{{sighup_behavior}}` |
| `{{costm_signal}}` | `{{costm_behavior}}` |
## Monitoring
Health: `{{health_check_details}}`
Metrics: `{{metrics_collected}}`
Alerting: `{{alert_conditions}}`
Logging: `{{log_format_and_rotation}}`
## References
1. `{{reference_1}}`
2. `{{reference_2}}`

## Template Standards

1. Define all required sections for this output kind
2. Include frontmatter schema with mandatory fields
3. Provide structural markers for post-validation
4. Specify format constraints for markdown YAML JSON
5. Reference the validation_schema for automated checks

## Properties

| Property | Value |
|----------|-------|
| Kind | `output_template` |
| Pillar | P05 |
| Domain | daemon construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_daemon]] | downstream | 0.41 |
| [[bld_examples_daemon]] | downstream | 0.41 |
| [[p03_sp_daemon_builder]] | upstream | 0.41 |
| [[p11_qg_daemon]] | downstream | 0.38 |
| [[bld_output_template_feature_flag]] | sibling | 0.38 |
| [[daemon-builder]] | upstream | 0.37 |
| [[bld_architecture_daemon]] | downstream | 0.36 |
| [[bld_output_template_input_schema]] | sibling | 0.36 |
| [[bld_output_template_runtime_rule]] | sibling | 0.36 |
| [[bld_output_template_golden_test]] | sibling | 0.35 |
