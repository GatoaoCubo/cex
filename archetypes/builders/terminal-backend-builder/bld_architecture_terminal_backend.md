---
quality: 8.8
quality: 8.2
kind: architecture
id: bld_architecture_terminal_backend
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of terminal_backend -- inventory, dependencies, position in P09 stack
title: "Architecture Terminal Backend"
version: "1.0.0"
author: n03_engineering
tags: [terminal_backend, builder, architecture]
tldr: "Component map of terminal_backend: 6 backend adapters, auth layer, cost model, environments/ convention"
domain: "terminal_backend construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.90
related:
  - bld_collaboration_session_backend
  - bld_architecture_onboarding_flow
  - bld_architecture_session_backend
  - bld_architecture_app_directory_entry
  - bld_architecture_discovery_questions
  - bld_architecture_legal_vertical
  - bld_architecture_benchmark_suite
  - bld_architecture_sdk_example
  - bld_architecture_fintech_vertical
  - bld_architecture_healthcare_vertical
---

## Component Inventory

| Name | Role | Owner | Status |
|------|------|-------|--------|
| Backend Adapter | Translates terminal_backend YAML to provider-specific config | N05 | Active |
| Auth Resolver | Reads auth.method + secret_ref and resolves credentials | N05 | Active |
| Resource Limit Enforcer | Applies cpu/memory/timeout limits at session start | N05 | Active |
| Cost Model Tracker | Records billing events per session for budget reporting | N05 | Active |
| Hibernation Controller | Triggers suspend/wake for hibernation_capable backends | N05 | Active (daytona only) |
| Environment Switcher | Swaps active backend by reading environments/ directory | N07 | Active |

## Backend Adapter Map

| backend_type | Adapter | Connection Config |
|--------------|---------|-------------------|
| local | LocalAdapter | none (host OS) |
| docker | DockerAdapter | image, registry, runtime (runc/gVisor) |
| ssh | SSHAdapter | host, user, port, key_path |
| daytona | DaytonaAdapter | workspace_id, api_endpoint |
| modal | ModalAdapter | app_name, stub_name, gpu |
| singularity | SingularityAdapter | image_path, bind_mounts |

## Dependencies

| From | To | Type |
|------|----|------|
| Backend Adapter | secret_config | Data (auth credentials) |
| Backend Adapter | sandbox_config | Control (isolation layer wrapping session) |
| Backend Adapter | env_config | Data (env vars injected into session) |
| Cost Model Tracker | runtime_rule | Control (budget rules trigger alerts) |
| Hibernation Controller | hibernation_policy | Control (policy defines idle threshold) |

## Architectural Position

terminal_backend sits at the bottom of the P09 execution stack:

```
N05 agent intent
    |
    v
terminal_backend (WHERE to run)
    |
    +-- sandbox_config (HOW to isolate)
    |
    +-- env_config (WHAT vars to inject)
    |
    +-- runtime_rule (WHEN to timeout/retry)
    |
    +-- secret_config (HOW to authenticate)
```

Switching backends (e.g., local -> modal for GPU) requires only a YAML swap in `environments/`.
No agent code changes. This is the "no code changes required" guarantee from HERMES.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_session_backend]] | downstream | 0.28 |
| [[bld_architecture_onboarding_flow]] | sibling | 0.28 |
| [[bld_architecture_session_backend]] | sibling | 0.27 |
| [[bld_architecture_app_directory_entry]] | sibling | 0.27 |
| [[bld_architecture_discovery_questions]] | sibling | 0.27 |
| [[bld_architecture_legal_vertical]] | sibling | 0.27 |
| [[bld_architecture_benchmark_suite]] | sibling | 0.26 |
| [[bld_architecture_sdk_example]] | sibling | 0.26 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.26 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.26 |
