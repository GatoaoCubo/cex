---
kind: knowledge_card
id: bld_kc_terminal_backend
pillar: P01
llm_function: INJECT
purpose: Linked KC reference for terminal_backend builder
quality: 8.0
title: "Knowledge Card Link: Terminal Backend"
version: "1.0.0"
author: n03_engineering
tags: [terminal_backend, builder, knowledge_card]
tldr: "Pointer to kc_terminal_backend.md -- Honcho-adjacent execution backend abstraction from HERMES"
domain: "terminal_backend construction"
created: "2026-04-18"
updated: "2026-04-18"
density_score: 0.88
related:
  - bld_architecture_session_backend
  - bld_architecture_sandbox_spec
  - bld_architecture_oauth_app_config
  - bld_architecture_marketplace_app_manifest
  - bld_architecture_sso_config
  - bld_architecture_playground_config
  - bld_architecture_data_residency
  - bld_architecture_usage_quota
  - bld_architecture_white_label_config
  - bld_architecture_env_config
---

## Primary KC
`N00_genesis/P01_knowledge/library/kind/kc_terminal_backend.md`

## Key Facts for Builder
- 6 supported backends: local, docker, ssh, daytona, modal, singularity
- Origin: NousResearch/hermes-agent `environments/` directory
- No code changes required to switch backends -- YAML only
- `serverless: true` is ONLY valid for modal and daytona
- `hibernation_capable: true` is ONLY valid for daytona
- Boundary: terminal_backend = WHERE; sandbox_config = HOW isolated; env_config = WHAT vars

## Related KCs

| KC | Pillar | Relationship |
|----|--------|-------------|
| `kc_sandbox_config` | P09 | Security isolation wrapping terminal session |
| `kc_env_config` | P09 | Env vars injected into terminal session |
| `kc_secret_config` | P09 | Credentials for auth.secret_ref |
| `kc_runtime_rule` | P09 | Timeout/retry rules applied to session |

## Upstream Sources
- NousResearch/hermes-agent: `environments/` directory, 6 backend definitions
- HERMES spec: "Six Supported Backends: Local / Docker / SSH / Daytona / Singularity / Modal"
- HERMES: "Configured in environments/ directory; no code changes required to switch"

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_session_backend]] | downstream | 0.20 |
| [[bld_architecture_sandbox_spec]] | downstream | 0.19 |
| [[bld_architecture_oauth_app_config]] | downstream | 0.19 |
| [[bld_architecture_marketplace_app_manifest]] | downstream | 0.19 |
| [[bld_architecture_sso_config]] | downstream | 0.18 |
| [[bld_architecture_playground_config]] | downstream | 0.18 |
| [[bld_architecture_data_residency]] | downstream | 0.18 |
| [[bld_architecture_usage_quota]] | downstream | 0.18 |
| [[bld_architecture_white_label_config]] | downstream | 0.17 |
| [[bld_architecture_env_config]] | downstream | 0.17 |
