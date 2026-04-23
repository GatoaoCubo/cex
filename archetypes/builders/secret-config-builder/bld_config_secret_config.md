---
kind: config
id: bld_config_secret_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Secret Config"
version: "1.0.0"
author: n03_builder
tags: [secret_config, builder, examples]
tldr: "Golden and anti-examples for secret config construction, demonstrating ideal structure and common pitfalls."
domain: "secret config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_secret_config
  - p03_sp_secret_config_builder
  - bld_instruction_secret_config
  - bld_examples_secret_config
  - bld_tools_secret_config
  - bld_schema_secret_config
  - bld_output_template_secret_config
  - bld_collaboration_secret_config
  - secret-config-builder
  - p11_qg_secret_config
---
# Config: secret_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p09_sec_{slug}.md` | `p09_sec_openai_api_keys.md` |
| Builder directory | kebab-case | `secret-config-builder/` |
| Frontmatter fields | snake_case | `rotation_policy`, `access_pattern` |
| Secret slug | snake_case, lowercase, no hyphens | `openai_api_keys`, `db_credentials` |
| Secret path placeholders | provider-native format with placeholder suffix | `secret/data/agents/<PLACEHOLDER>` |
| Provider enum values | lowercase, no hyphens | `vault`, `k8s`, `aws`, `portkey` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
Rule: NEVER use real secret values as examples — always `<PLACEHOLDER>` or `${VAR_NAME}`.
## File Paths
- Output: `cex/P09_config/examples/p09_sec_{slug}.md`
- Compiled: `cex/P09_config/compiled/p09_sec_{slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 1024 bytes
- Total (frontmatter + body): ~2000 bytes
- Density: >= 0.80 (no filler)
## Provider Enum
| Value | Backend |
|-------|---------|
| vault | HashiCorp Vault (OSS or HCP) |
| k8s | Kubernetes Secrets + ESO |
| aws | AWS Secrets Manager |
| portkey | Portkey virtual key vault |
| 1password | 1Password Connect / operator |
| sops | SOPS with age or KMS |
## Access Pattern Enum
| Value | Description |
|-------|-------------|
| dynamic | Short-lived lease from provider at runtime |
| static | Fetched once at deploy time; re-deploy to rotate |
| injected | Sidecar/init container injects at pod/container start |
| env | Platform injects as environment variable |
## Rotation Frequency Conventions
| Value | Interval | Risk Profile |
|-------|----------|-------------|
| daily | 24 hours | Low-risk, high-frequency service tokens |
| weekly | 7 days | Standard API keys |
| monthly | 30 days | Certificates, DB passwords |
| on-breach | Immediate | Emergency response only |
## Security Constraints
- audit_log: true is the default — set false only with explicit documented justification
- lease_duration: required when access_pattern == dynamic
- fallback: recommended for any secret used in critical path agents
- namespaces: required when provider == k8s or aws (region scoping)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_secret_config]] | upstream | 0.50 |
| [[p03_sp_secret_config_builder]] | related | 0.48 |
| [[bld_instruction_secret_config]] | upstream | 0.45 |
| [[bld_examples_secret_config]] | upstream | 0.43 |
| [[bld_tools_secret_config]] | upstream | 0.42 |
| [[bld_schema_secret_config]] | related | 0.42 |
| [[bld_output_template_secret_config]] | upstream | 0.41 |
| [[bld_collaboration_secret_config]] | downstream | 0.41 |
| [[secret-config-builder]] | related | 0.40 |
| [[p11_qg_secret_config]] | downstream | 0.34 |
