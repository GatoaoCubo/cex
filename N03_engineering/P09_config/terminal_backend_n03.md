---
id: terminal_backend_n03
kind: terminal_backend
nucleus: n03
pillar: P09
mirrors: N00_genesis/P09_config/tpl_terminal_backend.md
overrides:
  tone: precise, principled, no-magic
  sin_lens: SOBERBA INVENTIVA
  quality_threshold: 9.3
  density_target: 0.90
  preferred_backends: [local, docker, devcontainer]
backend_type: local
serverless: false
hibernation_capable: false
auth:
  method: none
limits:
  cpu_cores: 4
  memory_gb: 8
  timeout_seconds: 3600
cost_model:
  billing: free
version: 1.0.0
quality: 8.5
tags: [mirror, n03, engineering, hermes_assimilation, terminal_backend]
tldr: "N03 dev backends: local (default), docker, devcontainer. 4-core/8GB baseline for build tasks."
created: "2026-04-18"
related:
  - p10_lr_code_executor_builder
  - p01_kc_code_executor
  - bld_knowledge_card_code_executor
  - bld_knowledge_card_sandbox_config
  - p10_lr_sandbox_config_builder
  - p09_kc_retriever_domain
  - bld_knowledge_card_session_backend
  - p03_sp_sandbox_config_builder
  - p03_sp_playground_config_builder
  - sandbox-config-builder
density_score: 1.0
updated: "2026-04-22"
---

## Axioms

1. **Local first** -- dev environments start local; escalate to docker only when parity is needed.
2. **Explicit resource limits** -- never leave cpu_cores or memory_gb null in a build backend.
3. **Pair with sandbox_config** -- code execution backends must reference a sandbox_config for isolation.

## Supported Backends (N03 Engineering)

| Backend | When to Use | Isolation | N03 Use Case |
|---------|------------|-----------|-------------|
| local | Default dev, fast iteration | host | All standard builds |
| docker | Dependency isolation needed | container | Multi-lang projects, CI parity |
| devcontainer | Team consistency required | container | Shared dev environment spec |
| daytona | Cloud build, no local setup | VM | Remote pair builds (HERMES) |
| modal | GPU inference tasks | container | Model-heavy builds only |

## N03 Default Config

```yaml
backend_type: local
limits:
  cpu_cores: 4
  memory_gb: 8
  timeout_seconds: 3600
sandbox_config_ref: sandbox_config_n03
```

## Anti-Patterns

| Anti-Pattern | Risk | Fix |
|-------------|------|-----|
| Null resource limits | OOM kills silent | Declare cpu_cores + memory_gb always |
| Serverless for interactive builds | Cold start latency breaks feedback loop | serverless: false for dev backends |
| No sandbox_config pairing | Code execution without isolation | Always reference sandbox_config_n03 |
| Daytona for routine local builds | Cost overhead + latency | Use local unless remote parity required |

## Integration

- Pairs with: `sandbox_config_n03` (P09) for isolation policy
- Referenced by: `session_state_n03` (P10) active_backend field
- Boot: `cex_hooks_native.py session-start` reads active backend from `.cex/config/`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p10_lr_code_executor_builder]] | downstream | 0.23 |
| [[p01_kc_code_executor]] | upstream | 0.22 |
| [[bld_knowledge_card_code_executor]] | upstream | 0.22 |
| [[bld_knowledge_card_sandbox_config]] | upstream | 0.21 |
| [[p10_lr_sandbox_config_builder]] | downstream | 0.20 |
| [[p09_kc_retriever_domain]] | related | 0.18 |
| [[bld_knowledge_card_session_backend]] | upstream | 0.18 |
| [[p03_sp_sandbox_config_builder]] | upstream | 0.18 |
| [[p03_sp_playground_config_builder]] | upstream | 0.17 |
| [[sandbox-config-builder]] | related | 0.17 |
