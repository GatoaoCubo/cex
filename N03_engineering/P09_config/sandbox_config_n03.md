---
id: sandbox_config_n03
kind: sandbox_config
nucleus: n03
pillar: P09
overrides:
  tone: precise, principled, no-magic
  sin_lens: SOBERBA INVENTIVA
  quality_threshold: 9.3
  density_target: 0.90
  default_platform: local
  security_posture: strict
platform: local
sandbox_type: isolated
version: 1.0.0
quality: 8.4
tags: [mirror, n03, engineering, hermes_assimilation, sandbox_config]
tldr: "N03 code sandbox defaults: strict CPU/memory, network isolation, read-only root for LLM-generated code execution."
created: "2026-04-18"
related:
  - bld_examples_sandbox_config
  - bld_output_template_sandbox_config
  - bld_instruction_sandbox_config
  - bld_knowledge_card_sandbox_config
  - p01_kc_code_executor
  - bld_knowledge_card_code_executor
  - p04_exec_python_sandbox
  - p10_lr_code_executor_builder
  - p03_sp_code_executor_builder
  - sandbox-spec-builder
density_score: 1.0
---

## Axioms

1. **LLM-generated code is untrusted** -- always isolate; never execute in host context.
2. **Strict by default** -- relax isolation per scenario with documented justification.
3. **Pair with terminal_backend** -- sandbox_config defines isolation; terminal_backend defines the runtime.

## N03 Default Sandbox Config

```yaml
resource_limits:
  cpu: 2
  memory_mb: 1024
  disk_mb: 2048
  timeout_seconds: 60
  max_pids: 100

network:
  mode: none
  egress: none
  allowed_hosts: []
  dns: false

filesystem:
  root: /tmp/n03_sandbox
  read_only_root: true
  scratch_dir: /tmp
  scratch_size_mb: 512

isolation:
  runtime: docker
  namespaces: [pid, net, mnt, uts, ipc]
  seccomp_profile: default
  capabilities:
    drop: [ALL]
    add: []
  no_new_privs: true

audit:
  syscall_logging: false
  log_destination: .cex/runtime/sandbox/
  log_retention_days: 1
```

## Scenario Overrides

| Scenario | Override | Justification |
|----------|---------|--------------|
| devcontainer build | read_only_root: false, timeout: 3600 | Dev env requires write access |
| doc-only builds | sandbox: none | Pure .md artifact; no code execution needed |
| GPU inference | runtime: modal, gpu: A10G | Modal serverless GPU sandbox |

## Anti-Patterns

| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| No timeout_seconds | Build hangs indefinitely | Always set; 60s for code exec, 3600s for dev env |
| network: host | Data exfiltration / lateral movement | network: none or egress whitelist |
| capabilities.drop: [] | Full privilege escalation surface | drop: [ALL] minimum |
| seccomp_profile: none | Kernel attack surface exposed | seccomp_profile: default always |

## Integration

- Referenced by: `terminal_backend_n03` sandbox_config_ref field
- Pairs with: `hibernation_policy` for idle Daytona/Modal backends
- Validated by: `cex_doctor.py --sandbox` (H01-H07 gates)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_sandbox_config]] | upstream | 0.49 |
| [[bld_output_template_sandbox_config]] | upstream | 0.41 |
| [[bld_instruction_sandbox_config]] | upstream | 0.38 |
| [[bld_knowledge_card_sandbox_config]] | upstream | 0.30 |
| [[p01_kc_code_executor]] | upstream | 0.30 |
| [[bld_knowledge_card_code_executor]] | upstream | 0.27 |
| [[p04_exec_python_sandbox]] | upstream | 0.27 |
| [[p10_lr_code_executor_builder]] | downstream | 0.27 |
| [[p03_sp_code_executor_builder]] | upstream | 0.24 |
| [[sandbox-spec-builder]] | related | 0.24 |
