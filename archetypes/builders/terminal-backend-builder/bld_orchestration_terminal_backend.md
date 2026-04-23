---
quality: 8.6
quality: 8.0
kind: collaboration
id: bld_collaboration_terminal_backend
pillar: P12
llm_function: COLLABORATE
purpose: How terminal_backend-builder works in crews with other builders
title: "Collaboration Terminal Backend"
version: "1.0.0"
author: n03_engineering
tags: [terminal_backend, builder, collaboration]
tldr: "Crew role: execution environment selection. Receives from: sandbox-config, env-config. Produces for: N05 session manager, N07 dispatch router"
domain: "terminal_backend construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_collaboration_session_backend
  - bld_collaboration_env_config
  - bld_collaboration_path_config
  - bld_collaboration_sandbox_config
  - bld_collaboration_rbac_policy
  - bld_collaboration_trace_config
  - kc_intent_resolution_map
  - session-backend-builder
  - bld_architecture_session_backend
  - bld_collaboration_multi_modal_config
---

## Crew Role
Declares the execution backend for agent sessions. Answers WHERE code runs and HOW it is authenticated and billed. Does NOT handle security isolation (sandbox-config-builder), environment variables (env-config-builder), or deployment targets (deployment-manifest-builder).

## Receives From

| Builder | What | Format |
|---------|------|--------|
| sandbox-config-builder | Security isolation requirements for the backend session | YAML |
| secret-config-builder | Auth credentials referenced by auth.secret_ref | YAML |
| env-config-builder | Environment variables to inject into the session | YAML |
| runtime-rule-builder | Timeout and retry rules governing session lifecycle | YAML |

## Produces For

| Consumer | What | Format |
|----------|------|--------|
| N05 session manager | Active backend declaration (backend_type + connection config) | YAML |
| N07 dispatch router | Cost model + serverless flag for routing decisions | YAML |
| Hibernation controller | hibernation_capable flag + idle threshold | YAML |
| Cost tracker | billing mode + estimated_usd_per_hour for budget monitoring | YAML |

## Integration Pattern

```
User intent: "run task on GPU"
    |
    N07 (CONSTRAIN): reads terminal_backend YAML in environments/
    |
    N05 (CALL): selects modal backend (backend_type=modal, serverless=true)
    |
    terminal-backend-builder: produces p09_tb_modal.yaml
    |
    sandbox-config-builder: wraps modal session with isolation config
    |
    N05 executes session on Modal with isolation + env vars
```

## Boundary (NEVER do)
- Do NOT define seccomp/namespace/capabilities (sandbox_config owns this)
- Do NOT store env var values (env_config owns this)
- Do NOT specify deployment pipeline steps (deployment_manifest owns this)
- Do NOT define timeout/retry logic (runtime_rule owns this)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_session_backend]] | sibling | 0.39 |
| [[bld_collaboration_env_config]] | sibling | 0.33 |
| [[bld_collaboration_path_config]] | sibling | 0.30 |
| [[bld_collaboration_sandbox_config]] | sibling | 0.30 |
| [[bld_collaboration_rbac_policy]] | sibling | 0.29 |
| [[bld_collaboration_trace_config]] | sibling | 0.29 |
| [[kc_intent_resolution_map]] | upstream | 0.28 |
| [[session-backend-builder]] | upstream | 0.28 |
| [[bld_architecture_session_backend]] | upstream | 0.27 |
| [[bld_collaboration_multi_modal_config]] | sibling | 0.27 |
