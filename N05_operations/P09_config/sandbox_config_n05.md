---
id: sandbox_config_n05
kind: sandbox_config
8f: F1_constrain
nucleus: n05
pillar: P09
mirrors: N00_genesis/P09_config/tpl_sandbox_config.md
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
title: "N05 Operations -- Sandbox Isolation Config"
version: "1.1.0"
created: "2026-04-17"
updated: "2026-04-18"
author: "{{BRAND_EMAIL}}"
domain: "operations, tool-execution, process-management"
quality: 8.6
tags: [mirror, n05, operations, hermes_assimilation, sandbox_config, isolation, security-boundary]
tldr: "N05-owned sandbox: strictest isolation, audit logging, file write scoped to N05+runtime dirs, IRA-enforced gates."
sandbox_type: isolated
platform: native
backend_types: [native, daytona, modal, singularity]
density_score: 1.0
related:
  - bld_output_template_sandbox_config
  - p09_qg_sandbox_config
  - bld_examples_sandbox_config
  - bld_instruction_sandbox_config
  - bld_knowledge_card_sandbox_config
  - p10_lr_code_executor_builder
  - sandbox-spec-builder
  - p03_sp_sandbox_config_builder
  - bld_knowledge_card_code_executor
  - p01_kc_code_executor
---

## Ownership

N05 OWNS this kind. Operations controls all sandbox configurations including
backend-specific isolation (native, daytona, modal, singularity). IRA lens:
strictest isolation by default, audit everything.

## Resource Limits

| Resource | Limit | Unit |
|----------|-------|------|
| CPU | 2 | cores |
| RAM | 1024 | MB |
| Disk write | 512 | MB |
| Timeout | 1800 | seconds |
| Max processes | 5 | count |

## Filesystem Scope

```yaml
read_only_root: true
allowed_write: [N05_operations/, .cex/runtime/signals/, .cex/runtime/audit/, compiled/]
allowed_read: ["**"]
denied_write: [.cex/config/, .env, boot/, "N0[0-47]_*/"]
scratch_dir: .cex/runtime/audit/
scratch_size_mb: 64
```

## Network Policy

```yaml
mode: whitelist
egress: whitelist
allowed_hosts: [localhost, api.anthropic.com]
allowed_ports: [11434, 443]
arbitrary_http: false
dns: false
```

## Tool Execution

```yaml
allowed_scripts: [_tools/cex_*.py, _spawn/dispatch.sh]
allowed_dispatch_verbs: [status, stop]
denied_dispatch_verbs: [solo, grid, swarm]
git_commit_scope: N05_operations/
git_force_push: false
```

## Isolation

```yaml
runtime: native
enforcement: pre-execution-hook
hook: _tools/cex_hooks_native.py
no_new_privs: true
capabilities_drop: [arbitrary_http, cross_nucleus_write, force_push]
env_read: ["CEX_*"]
env_write: []
kill_other_nuclei: false
```

## Audit

```yaml
pre_execution_validation: true
post_execution_log: true
log_destination: .cex/runtime/audit/n05_audit.jsonl
log_retention_days: 30
log_fields: [timestamp, tool, verb, path, result, duration_ms]
```

## Backend-Specific Overrides (HERMES)

| Backend | Isolation | Network | Filesystem | Notes |
|---------|-----------|---------|-----------|-------|
| native | process-level | whitelist | read-only root | Default |
| daytona | workspace-level | VPC | workspace-scoped | Serverless sandbox |
| modal | container-level | none (outbound blocked) | ephemeral | GPU workloads |
| singularity | container-level | host network | bind-mount only | HPC clusters |

## Failure Modes

| Failure | Detection | Response | Escalation |
|---------|-----------|----------|------------|
| Sandbox escape attempt | capability violation in audit log | kill process + alert | immediate page |
| Write to denied path | hook rejection | block + log | review queue |
| Network policy violation | egress to non-whitelisted host | drop + log | alert |
| Resource limit exceeded | OOM/CPU throttle | kill process | retry with limits |
| Audit log corruption | write error | pause execution | oncall |

## Rollback Procedure

| Step | Action | Gate |
|------|--------|------|
| 1 | Identify last-good sandbox config via git log | config exists |
| 2 | Stop all sandboxed processes | processes stopped |
| 3 | Apply last-good config | config valid |
| 4 | Restart processes in new sandbox | health check pass |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_sandbox_config]] | upstream | 0.30 |
| [[p09_qg_sandbox_config]] | downstream | 0.28 |
| [[bld_examples_sandbox_config]] | upstream | 0.28 |
| [[bld_instruction_sandbox_config]] | upstream | 0.28 |
| [[bld_knowledge_card_sandbox_config]] | upstream | 0.27 |
| [[p10_lr_code_executor_builder]] | downstream | 0.27 |
| [[sandbox-spec-builder]] | related | 0.24 |
| [[p03_sp_sandbox_config_builder]] | upstream | 0.24 |
| [[bld_knowledge_card_code_executor]] | upstream | 0.24 |
| [[p01_kc_code_executor]] | upstream | 0.23 |
