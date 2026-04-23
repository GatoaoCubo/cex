---
id: p09_secret_config
kind: secret_config
pillar: P09
version: 1.0.0
title: "Template — Secret Config"
tags: [template, secret, config, security, credentials]
tldr: "Manages sensitive credentials: API keys, tokens, database URLs. Defines storage method, rotation policy, access control, and leak prevention."
quality: 9.0
updated: "2026-04-07"
domain: "configuration management"
author: n03_builder
created: "2026-04-07"
density_score: 0.94
related:
  - p01_kc_secret_config
  - bld_collaboration_secret_config
  - bld_knowledge_card_secret_config
  - p10_lr_secret_config_builder
  - bld_collaboration_env_config
  - kc_env_config
  - bld_knowledge_card_env_config
  - p03_sp_secret_config_builder
  - secret-config-builder
  - bld_architecture_env_config
---

# Secret Config: [SERVICE_NAME]

## Purpose
[WHAT credentials this config manages — API keys, database URLs, auth tokens]

## Secrets Registry

| Secret | Env Var | Required | Rotation |
|--------|---------|----------|----------|
| [API_KEY] | `APP_API_KEY` | yes | [90 days] |
| [DB_URL] | `DATABASE_URL` | yes | [on compromise] |
| [JWT_SECRET] | `JWT_SECRET` | yes | [180 days] |

## Storage

| Method | Environment | Notes |
|--------|------------|-------|
| `.env` file | Development | gitignored, local only |
| GitHub Secrets | CI/CD | Encrypted at rest |
| Railway/Render env | Production | Platform-managed |
| Vault/AWS SSM | Enterprise | Centralized, audited |

## Access Control
- **Who reads**: Only the application process (never logged, never printed)
- **Who rotates**: Ops team or automated rotation script
- **Who audits**: Security review quarterly

## Leak Prevention
- `.env` in `.gitignore` (ALWAYS)
- Pre-commit hook scans for patterns: `sk-`, `ghp_`, `Bearer `, base64 tokens
- CI scan: `trufflehog` or `gitleaks` on every PR
- Runtime: Never log env vars, mask in error messages

## Rotation Procedure
1. Generate new credential in provider dashboard
2. Update in secret store (Railway env, GitHub Secrets)
3. Deploy with new credential
4. Verify service works with new credential
5. Revoke old credential
6. Log rotation in audit trail

## Quality Gate
- [ ] All secrets listed with env var names
- [ ] `.env` is gitignored
- [ ] Rotation schedule defined per secret
- [ ] Leak prevention scan configured

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_secret_config]] | related | 0.54 |
| [[bld_collaboration_secret_config]] | downstream | 0.44 |
| [[bld_knowledge_card_secret_config]] | upstream | 0.40 |
| [[p10_lr_secret_config_builder]] | downstream | 0.33 |
| [[bld_collaboration_env_config]] | downstream | 0.32 |
| [[kc_env_config]] | upstream | 0.31 |
| [[bld_knowledge_card_env_config]] | upstream | 0.31 |
| [[p03_sp_secret_config_builder]] | related | 0.30 |
| [[secret-config-builder]] | related | 0.29 |
| [[bld_architecture_env_config]] | upstream | 0.29 |
