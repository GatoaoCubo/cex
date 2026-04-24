---
id: n00_secret_config_manifest
kind: knowledge_card
8f: F3_inject
pillar: P09
nucleus: n00
title: "Secret Config -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, secret_config, p09, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_secret_config
  - bld_schema_oauth_app_config
  - bld_schema_integration_guide
  - bld_schema_reranker_config
  - bld_schema_search_strategy
  - bld_schema_sandbox_spec
  - bld_schema_usage_report
  - bld_schema_sandbox_config
  - bld_schema_env_config
  - bld_collaboration_secret_config
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A secret_config defines how secrets (API keys, credentials, tokens) are managed, rotated, and accessed by nuclei and tools. It specifies the secret backend, access patterns, rotation policies, and audit logging requirements without ever storing the secret values themselves, serving as a reference map for secure credential management.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `secret_config` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable config name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| backend | enum | yes | env_var \| vault \| aws_secrets \| azure_keyvault \| local_file |
| secrets | list | yes | Secret definitions (name + metadata, never values) |
| secrets[].name | string | yes | Secret logical name |
| secrets[].env_var | string | no | Environment variable name for env_var backend |
| secrets[].rotation_days | integer | no | Days between mandatory rotation |
| secrets[].last_rotated | date | no | Date of last rotation |
| audit_log | boolean | yes | Whether secret access is logged |
| never_log | list | yes | Secret names that must never appear in logs |

## When to use
- Documenting all secrets required by a nucleus without storing values in git
- Setting up rotation schedules for API keys used in production
- Enabling cex_setup_validator.py to check that required secrets are present

## Builder
`archetypes/builders/secret_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind secret_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: secret_config_n05_apis
kind: secret_config
pillar: P09
nucleus: n05
title: "N05 Operations API Secret Config"
version: 1.0
quality: null
---
backend: env_var
secrets:
  - name: anthropic_api_key
    env_var: ANTHROPIC_API_KEY
    rotation_days: 90
  - name: github_token
    env_var: GITHUB_TOKEN
    rotation_days: 30
audit_log: true
never_log: [anthropic_api_key, github_token]
```

## Related kinds
- `env_config` (P09) -- environment variables that reference secrets
- `oauth_app_config` (P09) -- OAuth client secrets managed through secret_config
- `data_residency` (P09) -- secrets must comply with regional data residency rules

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_secret_config]] | related | 0.47 |
| [[bld_schema_oauth_app_config]] | upstream | 0.42 |
| [[bld_schema_integration_guide]] | upstream | 0.40 |
| [[bld_schema_reranker_config]] | upstream | 0.40 |
| [[bld_schema_search_strategy]] | upstream | 0.39 |
| [[bld_schema_sandbox_spec]] | upstream | 0.39 |
| [[bld_schema_usage_report]] | upstream | 0.39 |
| [[bld_schema_sandbox_config]] | upstream | 0.39 |
| [[bld_schema_env_config]] | upstream | 0.38 |
| [[bld_collaboration_secret_config]] | downstream | 0.38 |
