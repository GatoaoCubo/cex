---
quality: 8.8
quality: 8.2
kind: config
id: bld_config_terminal_backend
pillar: P09
llm_function: CONSTRAIN
purpose: Configuration knobs and tuning parameters for terminal_backend builder
title: "Config Terminal Backend"
version: "1.0.0"
author: n03_engineering
tags: [terminal_backend, builder, config]
tldr: "Builder configuration: default timeout, cost alert threshold, environment directory, hibernation idle threshold"
domain: "terminal_backend construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.88
related:
  - bld_collaboration_session_backend
  - bld_schema_session_backend
  - bld_examples_session_backend
  - bld_schema_vector_store
  - bld_config_session_backend
  - bld_examples_kind
  - p01_kc_session_backend
  - session-backend-builder
  - p03_sp_session_backend_builder
  - bld_collaboration_kind
---

## Builder Knobs

| Knob | Default | Purpose |
|------|---------|---------|
| `default_timeout_seconds` | 3600 | Applied when timeout_seconds not specified by user |
| `environments_dir` | `environments/` | Directory where backend YAML files are stored |
| `cost_alert_threshold_usd_per_hour` | 5.0 | Warn orchestrator when estimated cost exceeds this |
| `hibernation_idle_minutes` | 15 | Minutes of idle before triggering hibernation (daytona) |
| `ssh_connection_timeout_seconds` | 30 | Timeout for SSH handshake |
| `docker_pull_timeout_seconds` | 120 | Timeout for docker image pull before session start |
| `max_session_retry_attempts` | 3 | Retry count on session start failure |

## Environment Directory Convention

```
environments/
  local.yaml          # default dev backend
  docker.yaml         # containerized execution
  ssh_cluster.yaml    # private GPU cluster
  daytona.yaml        # cloud dev environment
  modal.yaml          # serverless GPU
  singularity.yaml    # HPC container
```

The active backend is selected by the agent runtime via environment variable or config.
N07 can dispatch with a specific backend by pointing to the YAML file path.

## Cost Safeguards

When `cost_model.billing` is `per_second` or `per_task`:
1. Builder emits a WARN if no `cost_model.estimated_usd_per_hour` is set
2. N07 routing checks `cost_alert_threshold_usd_per_hour` before dispatch
3. Sessions exceeding the threshold trigger a signal to N05 for review

## Auth Safety

| auth.method | Required secret_ref | secret_config kind |
|-------------|--------------------|--------------------|
| none | No | - |
| ssh_key | Yes | p09_secret_{{name}} |
| api_token | Yes | p09_secret_{{name}} |
| oauth | Yes | p09_secret_{{name}} (oauth token) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_session_backend]] | downstream | 0.24 |
| [[bld_schema_session_backend]] | upstream | 0.22 |
| [[bld_examples_session_backend]] | upstream | 0.20 |
| [[bld_schema_vector_store]] | upstream | 0.20 |
| [[bld_config_session_backend]] | sibling | 0.20 |
| [[bld_examples_kind]] | upstream | 0.19 |
| [[p01_kc_session_backend]] | downstream | 0.18 |
| [[session-backend-builder]] | related | 0.18 |
| [[p03_sp_session_backend_builder]] | upstream | 0.18 |
| [[bld_collaboration_kind]] | downstream | 0.18 |
