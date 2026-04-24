---
id: tb_{{backend}}
kind: terminal_backend
8f: F5_call
pillar: P09
title: "Terminal Backend: {{backend}}"
backend_type: local | docker | ssh | daytona | modal | singularity
serverless: false
hibernation_capable: false
auth:
  method: none | ssh_key | api_token | oauth
  secret_ref: null
limits:
  cpu_cores: null
  memory_gb: null
  timeout_seconds: 3600
cost_model:
  billing: free | per_second | per_task | subscription
  estimated_usd_per_hour: null
version: 1.0.0
quality: null
tags: [hermes_origin, backend, runtime]
related:
  - p03_ins_vector_store
  - p03_sp_session_backend_builder
  - p01_kc_code_executor
  - p11_qg_session_backend
  - p10_lr_code_executor_builder
  - bld_knowledge_card_code_executor
  - bld_schema_vector_store
  - bld_collaboration_session_backend
  - kc_container_deployment_llm
  - bld_knowledge_card_sandbox_config
density_score: 1.0
updated: "2026-04-22"
---

## Backend Overview

**Type:** {{backend_type}}
**Purpose:** {{one-line description of what this backend provides}}
**Nucleus owner:** N05 Operations

## Connection

```yaml
# Backend-specific connection block
# local: no connection needed
# docker: image, registry, resource limits
# ssh: host, user, key_path
# daytona: workspace_id, api_endpoint
# modal: app_name, stub_name, gpu
# singularity: image_path, bind_mounts
```

## Resource Limits

| Resource | Limit | Unit |
|----------|-------|------|
| CPU | {{cpu_cores}} | cores |
| Memory | {{memory_gb}} | GB |
| Timeout | {{timeout_seconds}} | seconds |

## Authentication

| Field | Value |
|-------|-------|
| Method | {{auth.method}} |
| Secret ref | {{auth.secret_ref}} |

## Cost Model

| Field | Value |
|-------|-------|
| Billing | {{cost_model.billing}} |
| Estimated $/hr | {{cost_model.estimated_usd_per_hour}} |

## Backend Type Comparison

| Backend | Isolation | Startup time | GPU support | Persistent storage | Cost model | Best for |
|---------|-----------|-------------|-------------|-------------------|-----------|----------|
| `local` | None (host process) | Instant | Host GPU | Host filesystem | Free | Development, testing |
| `docker` | Container-level | 2-10s | nvidia-docker | Volumes, bind mounts | Free / per-second | CI/CD, reproducible builds |
| `ssh` | Process-level (remote) | 1-5s | Remote GPU | Remote filesystem | Subscription | Dedicated servers, on-prem |
| `daytona` | Workspace-level | 5-15s | Via workspace config | Workspace volumes | Per-second | Cloud dev environments |
| `modal` | Function-level | 2-5s | A10G, A100, H100 | Ephemeral + volumes | Per-second | Serverless GPU, burst compute |
| `singularity` | Container-level (HPC) | 10-30s | Host GPU passthrough | Bind mounts | Subscription | HPC clusters, research |

### Connection Block Examples

```yaml
# local -- no connection needed
local:
  working_dir: "{{project_root}}"
  env_file: ".env"

# docker
docker:
  image: "{{registry}}/{{image}}:{{tag}}"
  volumes:
    - "{{project_root}}:/workspace"
  environment:
    - "CEX_NUCLEUS={{nucleus}}"
  gpu: false

# ssh
ssh:
  host: "{{ssh_host}}"
  user: "{{ssh_user}}"
  key_path: "{{ssh_key_path}}"
  working_dir: "/home/{{ssh_user}}/workspace"

# daytona
daytona:
  workspace_id: "{{daytona_workspace_id}}"
  api_endpoint: "https://{{daytona_host}}/api"
```

## Resource Limit Reference

Recommended resource limits by workload type.

| Workload | CPU cores | Memory (GB) | Timeout (s) | Disk (GB) | Notes |
|----------|-----------|-------------|-------------|-----------|-------|
| LLM inference (7B) | 4 | 8 | 300 | 20 | CPU-only; GPU preferred |
| LLM inference (70B) | 8 | 16 | 600 | 80 | Requires GPU (A100 40GB+) |
| Code execution (sandbox) | 2 | 4 | 60 | 5 | Isolated, short-lived |
| Builder 8F pipeline | 2 | 4 | 300 | 10 | File I/O + LLM calls |
| Batch compilation | 4 | 8 | 1800 | 20 | CPU-bound, many files |
| Web scraping / fetch | 1 | 2 | 120 | 2 | Network-bound |
| Vector embedding | 4 | 8 | 600 | 30 | GPU accelerated if available |

### Provider Selection Decision Tree

```
Q: Do you need GPU?
  YES -> Q: Inference or training?
    Inference -> Modal (per-second billing, auto-scale)
    Training  -> Singularity (HPC) or SSH (cloud VM with reserved GPU)
  NO -> Q: Serverless / event-driven?
    YES -> Modal (CPU functions) or Daytona (dev workspaces)
    NO  -> Q: Local development?
      YES -> Local (zero overhead) or Docker (reproducible)
      NO  -> SSH (remote) or Docker (container on remote)
```

## Authentication Methods

| Method | Backends | Secret storage | Rotation | Notes |
|--------|----------|---------------|----------|-------|
| `none` | local | N/A | N/A | Development only |
| `ssh_key` | ssh | `~/.ssh/` or `secret_config` | Manual | Ed25519 preferred |
| `api_token` | modal, daytona | `secret_config` (P09) | Quarterly | Scoped to minimum perms |
| `oauth` | daytona | Provider-managed | Auto-refresh | OAuth2 with PKCE |
| `docker_auth` | docker (private registry) | `~/.docker/config.json` | Per-deployment | Use credential helpers |

## Notes

- Configured in `environments/` directory; no code changes required to switch backends
- Switch backends by changing `backend_type` and updating connection block
- Pair with `sandbox_config` for security isolation around code execution
- For GPU workloads, pair with `hibernation_policy` to manage idle cost
- Use `secret_config` (P09) for all authentication credentials; never inline secrets
- Test backend connectivity before dispatch: `python _tools/cex_agent_spawn.py --preflight`

## Relationship to Other Kinds

| Kind | Pillar | Relationship |
|------|--------|-------------|
| `hibernation_policy` | P09 | Governs idle behavior for this backend |
| `sandbox_config` | P09 | Security isolation for code execution |
| `env_config` | P09 | Environment variables injected into backend |
| `secret_config` | P09 | Credentials for backend authentication |
| `rate_limit_config` | P09 | Request limits for serverless backends |
| `agent_card` | P08 | Agent deployment references backend for execution |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_ins_vector_store]] | upstream | 0.22 |
| [[p03_sp_session_backend_builder]] | upstream | 0.19 |
| [[p01_kc_code_executor]] | upstream | 0.18 |
| [[p11_qg_session_backend]] | downstream | 0.18 |
| [[p10_lr_code_executor_builder]] | downstream | 0.18 |
| [[bld_knowledge_card_code_executor]] | upstream | 0.18 |
| [[bld_schema_vector_store]] | upstream | 0.17 |
| [[bld_collaboration_session_backend]] | downstream | 0.15 |
| [[kc_container_deployment_llm]] | upstream | 0.15 |
| [[bld_knowledge_card_sandbox_config]] | upstream | 0.15 |
