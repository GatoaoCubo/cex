---
id: kc_terminal_backend
kind: knowledge_card
8f: F3_inject
pillar: P01
nucleus: n00
title: "Knowledge Card: terminal_backend"
version: 1.0
quality: 9.0
tags: [terminal_backend, p09, hermes, execution_environment, backend, runtime]
density_score: 0.95
upstream_source: NousResearch/hermes-agent environments/
related:
  - bld_knowledge_card_code_executor
  - p01_kc_code_executor
  - p01_vdb_pinecone
  - bld_collaboration_code_executor
  - sandbox-config-builder
  - bld_collaboration_sandbox_config
  - bld_collaboration_session_backend
  - p03_sp_code_executor_builder
  - p03_sp_sandbox_config_builder
  - bld_knowledge_card_sandbox_config
---

## Definition

`terminal_backend` is a P09 config artifact that declares the execution environment where
agent-invoked terminal sessions, CLI tools, and code runs. It abstracts over six supported
backends so nucleus operators switch execution targets by swapping a YAML file, not patching code.

**Origin:** NousResearch/hermes-agent `environments/` directory. HERMES supports 6 backends
natively: Local, Docker, SSH, Daytona, Singularity, Modal.

## Six Supported Backends

| Backend | Type | Auth | Serverless | Hibernation | Billing |
|---------|------|------|------------|-------------|---------|
| `local` | Bare metal / host OS | none | no | no | free |
| `docker` | Container (runc/gVisor) | none | no | no | free/infra |
| `ssh` | Remote host via SSH | ssh_key | no | no | infra |
| `daytona` | Cloud dev environment | api_token | yes | yes | per_task |
| `modal` | Serverless GPU/CPU | api_token | yes | no | per_second |
| `singularity` | HPC container (Apptainer) | none/ssh | no | no | HPC quota |

## Key Fields

| Field | Type | Purpose |
|-------|------|---------|
| `backend_type` | enum | Selects from 6 supported backends |
| `serverless` | bool | Whether backend spawns on demand (no persistent VM) |
| `hibernation_capable` | bool | Whether idle backend can hibernate to cut cost |
| `auth.method` | enum | none, ssh_key, api_token, oauth |
| `auth.secret_ref` | string | Pointer to `secret_config` artifact |
| `limits.timeout_seconds` | int | Max session lifetime before forced teardown |
| `cost_model.billing` | enum | free, per_second, per_task, subscription |

## Boundaries

| Confused with | Why it is different |
|---------------|---------------------|
| `sandbox_config` | sandbox_config = security isolation (seccomp, namespaces, capabilities); terminal_backend = WHERE code runs (execution target selection) |
| `env_config` | env_config = environment variables injected into the session; terminal_backend = the execution target itself |
| `deployment_manifest` | deployment_manifest = production ship spec; terminal_backend = dev/runtime execution layer |
| `runtime_rule` | runtime_rule = timeout/retry/limit rules applied during execution; terminal_backend = the backend those rules apply to |

## Dialectic: sandbox_config + terminal_backend

The two kinds are complementary, not interchangeable:
- `terminal_backend` answers: WHERE does the code run? (local, docker, modal...)
- `sandbox_config` answers: HOW is that run isolated? (namespaces, seccomp, capabilities)

A fully governed execution pipeline uses BOTH: terminal_backend selects the target;
sandbox_config wraps the execution in security isolation.

## Builder

`archetypes/builders/terminal-backend-builder/` (13 ISOs)

```bash
python _tools/cex_8f_runner.py "configure modal serverless backend" \
  --kind terminal_backend --execute
```

## Examples

### Local (dev default)
```yaml
id: p09_tb_local
kind: terminal_backend
backend_type: local
serverless: false
hibernation_capable: false
auth:
  method: none
limits:
  timeout_seconds: 3600
cost_model:
  billing: free
```

### Modal (GPU serverless)
```yaml
id: p09_tb_modal
kind: terminal_backend
backend_type: modal
serverless: true
hibernation_capable: false
auth:
  method: api_token
  secret_ref: p09_secret_modal_api
limits:
  cpu_cores: 8
  memory_gb: 16
  timeout_seconds: 900
cost_model:
  billing: per_second
  estimated_usd_per_hour: 0.72
```

### SSH (private cluster)
```yaml
id: p09_tb_ssh_gpu_cluster
kind: terminal_backend
backend_type: ssh
serverless: false
hibernation_capable: false
auth:
  method: ssh_key
  secret_ref: p09_secret_ssh_cluster_key
limits:
  cpu_cores: 32
  memory_gb: 128
  timeout_seconds: 86400
cost_model:
  billing: subscription
  estimated_usd_per_hour: 0.0
```

## Integration Points

- `secret_config` (P09): `auth.secret_ref` points to a secret_config artifact
- `sandbox_config` (P09): wraps terminal_backend session for security isolation
- `env_config` (P09): environment variables injected into the backend session
- `runtime_rule` (P09): timeout/retry rules governing session behavior
- `hibernation_policy` (P09, HERMES): controls auto-hibernate for cost savings on idle backends

## Configuration Convention

Backends are configured in `environments/` directory of the HERMES agent workspace.
No code changes are required to switch backends -- only YAML swap.

```
environments/
  local.yaml        -> terminal_backend (backend_type: local)
  docker.yaml       -> terminal_backend (backend_type: docker)
  modal.yaml        -> terminal_backend (backend_type: modal)
  daytona.yaml      -> terminal_backend (backend_type: daytona)
  ssh_cluster.yaml  -> terminal_backend (backend_type: ssh)
  singularity.yaml  -> terminal_backend (backend_type: singularity)
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_code_executor]] | sibling | 0.22 |
| [[p01_kc_code_executor]] | sibling | 0.21 |
| [[p01_vdb_pinecone]] | related | 0.21 |
| [[bld_collaboration_code_executor]] | downstream | 0.20 |
| [[sandbox-config-builder]] | downstream | 0.20 |
| [[bld_collaboration_sandbox_config]] | downstream | 0.20 |
| [[bld_collaboration_session_backend]] | downstream | 0.20 |
| [[p03_sp_code_executor_builder]] | downstream | 0.19 |
| [[p03_sp_sandbox_config_builder]] | downstream | 0.19 |
| [[bld_knowledge_card_sandbox_config]] | sibling | 0.18 |
