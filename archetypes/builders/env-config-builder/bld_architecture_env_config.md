---
kind: architecture
id: bld_architecture_env_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of env_config — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Env Config"
version: "1.0.0"
author: n03_builder
tags: [env_config, builder, examples]
tldr: "Golden and anti-examples for env config construction, demonstrating ideal structure and common pitfalls."
domain: "env config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - env-config-builder
  - p03_sp_env_config_builder
  - bld_collaboration_env_config
  - bld_examples_kind
  - p01_kc_secret_config
  - bld_knowledge_card_env_config
  - bld_examples_env_config
  - bld_collaboration_path_config
  - p11_qg_env_config
  - bld_tools_env_config
---
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| scope | The system boundary this config covers: global, agent_group, service | env-config-builder | required |
| variables | Catalog of env vars: name, type, default, description, sensitivity | env-config-builder | required |
| validation_rules | Per-variable constraints: regex, range, enum, required flag | env-config-builder | required |
| sensitive_vars | List of secret/key vars with masking rules (never log, never expose) | env-config-builder | required |
| override_precedence | Resolution order: runtime env > .env file > hardcoded default | env-config-builder | required |
| defaults | Default values applied when var is absent from environment | env-config-builder | required |
| required_vars | Variables that must be present for the system to start (startup gate) | env-config-builder | required |
| optional_vars | Variables that enable optional features when present | env-config-builder | optional |
| metadata | config id, version, pillar, scope, author, created date | env-config-builder | required |
## Dependency Graph
```
guardrail (P11) --constrains--> env_config (security rules for sensitive var handling)
env_config --consumed_by--> boot_config (P02) (boot reads env vars at provider startup)
env_config --consumed_by--> daemon (P04) (daemon reads vars for config at launch)
env_config --consumed_by--> connector (P04) (connector reads API keys, base URLs from env)
env_config --consumed_by--> client (P04) (client reads auth tokens, endpoints from env)
env_config --consumed_by--> mcp_server (P04) (MCP server reads transport config from env)
feature_flag (P09) --independent-- env_config (feature_flag is on/off toggle logic, not var spec)
path_config (P09) --independent-- env_config (path_config covers filesystem paths specifically)
runtime_rule (P09) --independent-- env_config (runtime_rule governs behavior like timeouts/retries)
```
| From | To | Type | Data |
|------|----|------|------|
| guardrail | env_config | constrains | security rules for masking and exposure of sensitive vars |
| env_config | boot_config | consumed_by | env vars read at provider startup |
| env_config | daemon | consumed_by | config vars, secret values, paths at launch |
| env_config | connector | consumed_by | API keys, base URLs, auth credentials |
| env_config | client | consumed_by | auth tokens, endpoint URLs, timeouts |
| env_config | mcp_server | consumed_by | transport config, port, auth mode |
## Boundary Table
| env_config IS | env_config IS NOT |
|--------------|-------------------|
| A specification of environment variables: names, types, defaults, validation | A boot_config (P02) — boot_config is per-provider model startup configuration |
| Covers any variable that changes between deployment environments | A feature_flag (P09) — feature_flag is an on/off logical toggle with rollout logic |
| Follows 12-Factor App principle: config lives in environment, not code | A path_config (P09) — path_config specifies filesystem paths specifically |
| Declares sensitivity level and masking rules for secrets | A permission (P09) — permission governs access control, not variable values |
| Specifies validation rules (regex, enum, range) per variable | A runtime_rule (P09) — runtime_rule governs behavioral limits like timeouts and retries |
| Defines override precedence: runtime > file > default | A knowledge_card (P01) — KC distills domain knowledge, not system configuration |
| Has required_vars that gate system startup if absent | A connector (P04) — connector defines integration spec; env_config feeds it values |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Safety | guardrail, sensitive_vars | Enforce masking rules and prevent secret exposure |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[env-config-builder]] | downstream | 0.60 |
| [[p03_sp_env_config_builder]] | upstream | 0.52 |
| [[bld_collaboration_env_config]] | downstream | 0.52 |
| [[bld_examples_kind]] | upstream | 0.47 |
| [[p01_kc_secret_config]] | downstream | 0.41 |
| [[bld_knowledge_card_env_config]] | upstream | 0.40 |
| [[bld_examples_env_config]] | upstream | 0.38 |
| [[bld_collaboration_path_config]] | downstream | 0.38 |
| [[p11_qg_env_config]] | downstream | 0.36 |
| [[bld_tools_env_config]] | upstream | 0.36 |
