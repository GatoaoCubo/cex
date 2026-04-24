---
id: n00_terminal_backend_manifest
kind: knowledge_card
8f: F3_inject
pillar: P09
nucleus: n00
title: "Terminal Backend -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, terminal_backend, p09, n00, archetype, hermes]
density_score: 1.0
related:
  - bld_schema_sandbox_spec
  - bld_schema_integration_guide
  - bld_schema_vector_store
  - bld_schema_memory_architecture
  - bld_schema_session_backend
  - bld_schema_reranker_config
  - bld_schema_benchmark_suite
  - bld_schema_oauth_app_config
  - bld_schema_sandbox_config
  - bld_schema_memory_scope
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A terminal_backend selects and configures the execution environment where agent-generated code, CLI tools, and tasks actually run. It abstracts over six supported backends (local, Docker, SSH, Daytona, Modal, Singularity) so agents switch environments by changing YAML config, not code. Owned by N05 Operations; configured in `environments/` directory.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier (p09_tb_{{backend}}) |
| kind | string | yes | Always `terminal_backend` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable backend name |
| backend_type | enum | yes | local \| docker \| ssh \| daytona \| modal \| singularity |
| serverless | bool | yes | Whether the backend is serverless (no persistent VM) |
| hibernation_capable | bool | yes | Whether backend supports hibernation to cut idle cost |
| auth.method | enum | yes | none \| ssh_key \| api_token \| oauth |
| auth.secret_ref | string | no | Reference to secret_config artifact |
| limits.cpu_cores | integer | no | CPU core allocation (null = provider default) |
| limits.memory_gb | float | no | Memory ceiling in GB |
| limits.timeout_seconds | integer | yes | Max session lifetime before forced teardown |
| cost_model.billing | enum | yes | free \| per_second \| per_task \| subscription |
| cost_model.estimated_usd_per_hour | float | no | Approximate cost (null if free) |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |

## When to use
- Switching execution targets without changing agent logic (local dev -> Modal cloud)
- Configuring remote SSH backends for execution on private GPU clusters
- Declaring serverless backends (Modal, Daytona) with per-task billing and auto-hibernation
- Documenting cost model for budget-aware orchestration routing

## Boundary
- NOT `sandbox_config` -- sandbox_config defines security isolation (seccomp, namespaces); terminal_backend defines WHERE code runs
- NOT `env_config` -- env_config stores environment variables; terminal_backend defines the execution target
- NOT `deployment_manifest` -- deployment_manifest is for shipping to production; terminal_backend is the dev/runtime execution layer

## Builder
`archetypes/builders/terminal-backend-builder/`

Run: `python _tools/cex_8f_runner.py "configure modal backend" --kind terminal_backend --execute`

## Template variables (open for instantiation)
- `{{backend}}` -- backend type slug (local, docker, ssh, daytona, modal, singularity)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{AUTH_METHOD}}` -- authentication mechanism

## Example (minimal -- local)
```yaml
---
id: p09_tb_local
kind: terminal_backend
pillar: P09
title: "Terminal Backend: local"
backend_type: local
serverless: false
hibernation_capable: false
auth:
  method: none
  secret_ref: null
limits:
  cpu_cores: null
  memory_gb: null
  timeout_seconds: 3600
cost_model:
  billing: free
  estimated_usd_per_hour: null
version: 1.0.0
quality: null
tags: [hermes_origin, backend, runtime]
---
```

## Related kinds
- `sandbox_config` (P09) -- security isolation layer that wraps the terminal backend
- `env_config` (P09) -- environment variables injected into the backend session
- `runtime_rule` (P09) -- timeout and retry rules that govern backend behavior
- `secret_config` (P09) -- credentials referenced by auth.secret_ref

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_sandbox_spec]] | upstream | 0.42 |
| [[bld_schema_integration_guide]] | upstream | 0.39 |
| [[bld_schema_vector_store]] | upstream | 0.39 |
| [[bld_schema_memory_architecture]] | upstream | 0.39 |
| [[bld_schema_session_backend]] | upstream | 0.38 |
| [[bld_schema_reranker_config]] | upstream | 0.38 |
| [[bld_schema_benchmark_suite]] | upstream | 0.38 |
| [[bld_schema_oauth_app_config]] | upstream | 0.37 |
| [[bld_schema_sandbox_config]] | upstream | 0.37 |
| [[bld_schema_memory_scope]] | upstream | 0.37 |
