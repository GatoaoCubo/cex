---
id: terminal_backend_n05
kind: terminal_backend
nucleus: n05
pillar: P09
mirrors: N00_genesis/P09_config/tpl_terminal_backend.md
overrides:
  tone: strict, deterministic, gate-heavy
  voice: imperative, risk-averse
  sin_lens: IRA
  required_fields:
    - sla_target
    - failure_mode
    - rollback_procedure
  quality_threshold: 9.3
  density_target: 0.90
  example_corpus: 3+ examples with failure modes section
title: "N05 Operations -- Terminal Backend (Production)"
version: 1.0.0
quality: 8.2
tags: [mirror, n05, operations, hermes_assimilation, terminal_backend]
tldr: "N05-owned production backends: local, docker, ssh, daytona, modal, singularity -- with SLA, failure modes, and rollback for each."
related:
  - bld_schema_session_backend
  - bld_collaboration_session_backend
  - p03_ins_vector_store
  - bld_schema_vector_store
  - p11_qg_session_backend
  - bld_config_session_backend
  - bld_schema_memory_architecture
  - p03_sp_session_backend_builder
  - p01_vdb_pinecone
  - bld_tools_session_backend
---

## Ownership

N05 OWNS this kind. Operations controls all production backend configurations,
including resource limits, authentication, cost models, and incident response.

## Backend Matrix (Production View)

| Backend | Serverless | Hibernation | SLA Target | Auth | Cost Model | Failure Mode |
|---------|-----------|-------------|------------|------|------------|--------------|
| local | No | No | 99.0% | none | free | restart process |
| docker | No | No | 99.5% | none | free | restart container |
| ssh | No | No | 99.5% | ssh_key | free | reconnect + retry |
| daytona | Yes | Yes | 99.9% | api_token | per_second | wake + retry |
| modal | Yes | Yes | 99.9% | api_token | per_second | cold-start + retry |
| singularity | No | Yes | 99.0% | none | free | rebind + restart |

## Resource Limits (Per Backend)

| Backend | CPU Cores | Memory GB | Timeout (s) | Max Processes |
|---------|-----------|-----------|-------------|---------------|
| local | 4 | 8 | 3600 | 10 |
| docker | 2 | 4 | 1800 | 5 |
| ssh | varies | varies | 3600 | 5 |
| daytona | 4 | 16 | 7200 | 20 |
| modal | 8 | 32 | 3600 | unlimited |
| singularity | 4 | 8 | 3600 | 10 |

## Authentication (IRA-Enforced)

| Backend | Method | Secret Ref | Rotation Period | Failure on Expired |
|---------|--------|------------|-----------------|-------------------|
| local | none | n/a | n/a | n/a |
| docker | none | n/a | n/a | n/a |
| ssh | ssh_key | vault:ssh/n05_prod | 90d | block connection |
| daytona | api_token | vault:daytona/n05 | 60d | block + alert |
| modal | api_token | vault:modal/n05 | 60d | block + alert |
| singularity | none | n/a | n/a | n/a |

## Failure Modes

| Failure | Detection | Auto-Response | Escalation | SLA |
|---------|-----------|--------------|------------|-----|
| Process crash | exit code != 0 | restart 3x | oncall at 4th | 5min |
| Container OOM | Docker event | restart with +50% mem | oncall | 2min |
| SSH disconnect | socket timeout 30s | reconnect 3x | oncall | 5min |
| Serverless cold start >10s | latency probe | pre-warm | alert | 30s |
| Token expired | 401/403 response | auto-rotate from vault | block if rotation fails | immediate |
| Disk full | df >90% | alert + cleanup old logs | oncall | 15min |

## Rollback Procedure

| Step | Action | Gate |
|------|--------|------|
| 1 | Identify last-good backend config via git log | config exists |
| 2 | Stop current backend process/container | process stopped |
| 3 | Apply last-good config | config valid |
| 4 | Start backend with last-good config | health check pass |
| 5 | Verify via smoke test | smoke pass |

## Integration Points

- `hibernation_policy` (P09): serverless backends pair with idle policy
- `sandbox_config` (P09): backend process isolated per sandbox rules
- `messaging_gateway` (P04): gateway process runs on specified backend
- `schedule` (P12): backend health checks on schedule

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_session_backend]] | upstream | 0.26 |
| [[bld_collaboration_session_backend]] | downstream | 0.26 |
| [[p03_ins_vector_store]] | upstream | 0.25 |
| [[bld_schema_vector_store]] | upstream | 0.25 |
| [[p11_qg_session_backend]] | downstream | 0.23 |
| [[bld_config_session_backend]] | related | 0.22 |
| [[bld_schema_memory_architecture]] | upstream | 0.21 |
| [[p03_sp_session_backend_builder]] | upstream | 0.20 |
| [[p01_vdb_pinecone]] | upstream | 0.20 |
| [[bld_tools_session_backend]] | upstream | 0.20 |
