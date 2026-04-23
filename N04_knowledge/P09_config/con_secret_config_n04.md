---
id: con_secret_config_n04
kind: secret_config
pillar: P09
nucleus: n04
title: Knowledge Secret Config
version: 1.0
quality: 9.0
tags: [config, secrets, knowledge, credentials, rotation]
name: knowledge_provider_secrets
provider: vault_or_platform_env
rotation_policy: mixed_60d_90d_120d
density_score: 1.0
related:
  - bld_collaboration_secret_config
  - p01_kc_secret_config
  - p09_secret_config
  - p09_secret_openai_key
  - secret-config-builder
  - bld_config_secret_config
  - bld_knowledge_card_secret_config
  - bld_examples_secret_config
  - bld_instruction_secret_config
  - p03_sp_secret_config_builder
---
<!-- 8F: F1 constrain=P09/secret_config F2 become=secret-config-builder F3 inject=n04-knowledge+kc_secret_config+P09 examples+repo env patterns F4 reason=pointer registry for secrets used by knowledge indexing services F5 call=shell,apply_patch F6 produce=4757 bytes F7 govern=frontmatter+ascii+density+80-line self-check F8 collaborate=N04_knowledge/P09_config/con_secret_config_n04.md -->
# Knowledge Secret Config
## Purpose
N04 touches embedding providers, vector stores, and export channels that all require credentials.
The Knowledge Gluttony lens wants broad source access, but secret handling must stay pointer-based: store references, rotation policy, and access pattern here, never the secret values themselves.
This artifact is the secret registry for N04 runtime dependencies.
## Values
| Secret id | Env var | Provider | Required | Rotation policy | Storage |
|-----------|---------|----------|----------|-----------------|---------|
| n04_openai_embedding | `OPENAI_API_KEY` | openai | yes | 90d | vault_or_platform_env |
| n04_anthropic_rerank | `ANTHROPIC_API_KEY` | anthropic | yes | 90d | vault_or_platform_env |
| n04_vector_store_token | `N04_VECTOR_API_KEY` | vector_store | yes | 60d | vault |
| n04_export_webhook | `N04_EXPORT_WEBHOOK_TOKEN` | internal_webhook | no | 60d | platform_env |
| n04_cache_signing_key | `N04_CACHE_SIGNING_KEY` | internal | yes | 120d | vault |
## Access Pattern
| Secret id | Reader | Retrieval mode | Notes |
|-----------|--------|----------------|-------|
| n04_openai_embedding | embedding worker | env injection | never printed |
| n04_anthropic_rerank | rerank worker | env injection | only synthesis path |
| n04_vector_store_token | vector client | vault fetch then memory-only | no disk persistence |
| n04_export_webhook | export job | platform env | optional, only for outbound bundles |
| n04_cache_signing_key | cache service | vault fetch at startup | rotates with cache flush |
## Rotation Procedure
| Step | Action |
|------|--------|
| 1 | generate replacement credential at provider |
| 2 | write new value to vault or platform secret store |
| 3 | deploy or restart only affected N04 workers |
| 4 | run liveness check against provider |
| 5 | revoke old credential after validation window |
| 6 | log rotation event with secret id, operator, and timestamp |
## Leak Prevention
| Control | Rule |
|---------|------|
| source control | no secret value in markdown, yaml, env examples, or code |
| logging | mask values, show only secret id and last 4 chars when unavoidable |
| local files | `.env` not committed; production prefers vault or platform env |
| scanning | pre-commit and CI secret scanning enabled |
| exports | contested or external bundles never include secret-bearing config |
## Example
```yaml
secret_id: n04_vector_store_token
env_var: N04_VECTOR_API_KEY
provider: vector_store
rotation_policy: 60d
storage: vault
access_pattern:
  mode: startup_fetch
  cache_in_memory: true
  write_to_disk: false
```
## Rationale
| Decision | Knowledge Gluttony angle | Benefit |
|----------|--------------------------|---------|
| provider-specific secret ids | N04 wants many integrations without losing clarity | clear blast radius on compromise |
| shorter rotation for vector token | knowledge index access is high leverage | tighter breach window |
| startup fetch for signing key | greedy cache services still avoid disk residue | lower persistence risk |
| optional export webhook token | not all deployments need outbound export | fewer secrets in minimal installs |
| never embed values in docs | evidence-rich systems attract attention; docs must not become loot | safer collaboration |
## Incident Response
| Scenario | Required action |
|----------|-----------------|
| key exposed in logs | revoke immediately, rotate, inspect log retention |
| secret leaked in git | purge history if needed, rotate, notify reviewers |
| vault unavailable | use platform env fallback only for approved critical paths |
| suspicious read spike | freeze affected secret, audit callers, reissue credential |
## Properties
| Property | Value |
|----------|-------|
| Secret count | 5 |
| Required secrets | 4 |
| Optional secrets | 1 |
| Primary storage mode | vault or platform env |
| Rotation windows | 60d, 90d, 120d |
| Disk persistence allowed | no |
| Audit required | yes |
| CI secret scan expected | yes |
| Secret values present | no |
| Governing principle | pointer registry only |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_secret_config]] | downstream | 0.53 |
| [[p01_kc_secret_config]] | related | 0.46 |
| [[p09_secret_config]] | sibling | 0.46 |
| [[p09_secret_openai_key]] | sibling | 0.42 |
| [[secret-config-builder]] | related | 0.42 |
| [[bld_config_secret_config]] | related | 0.41 |
| [[bld_knowledge_card_secret_config]] | upstream | 0.40 |
| [[bld_examples_secret_config]] | upstream | 0.39 |
| [[bld_instruction_secret_config]] | upstream | 0.34 |
| [[p03_sp_secret_config_builder]] | related | 0.31 |
