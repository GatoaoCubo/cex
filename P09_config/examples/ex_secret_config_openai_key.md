---
id: p09_secret_openai_key
kind: secret_config
pillar: P09
name: "OpenAI API Key Configuration"
description: "Secret management config for OpenAI API key with Vault storage, 90-day rotation, and access audit"
provider: vault
rotation_policy: "90d"
encryption: aes256
access_audit: enabled
version: 1.0.0
created: 2026-03-29
author: builder_agent
quality: 9.0
tags: [secret, openai, api-key, vault, rotation, encryption]
---

# Secret Config: OpenAI API Key

## Overview

Configuration for managing the OpenAI API key used by organization's model router (fallback path when Anthropic is unavailable). Stored in HashiCorp Vault with AES-256 encryption, 90-day automatic rotation, and full access audit trail.

## Secret Identity

| Field | Value |
|-------|-------|
| Secret name | `organization/prod/openai_api_key` |
| Vault path | `secret/data/organization/prod/openai_api_key` |
| Environment variable | `OPENAI_API_KEY` |
| Provider | HashiCorp Vault (self-hosted on Railway) |
| Encryption | AES-256-GCM at rest, TLS 1.3 in transit |
| Format | `sk-proj-...` (56 chars) |

## Rotation Policy

```yaml
rotation:
  interval: 90d
  method: automatic
  steps:
    1_generate: "Create new key in OpenAI dashboard API > API Keys"
    2_store: "vault kv put secret/organization/prod/openai_api_key value=sk-proj-NEW"
    3_verify: "curl https://api.openai.com/v1/models -H 'Authorization: Bearer NEW'"
    4_deploy: "Railway redeploy to pick up new Vault value"
    5_revoke: "Delete old key in OpenAI dashboard after 24h grace period"
  next_rotation: "2026-06-27"
  last_rotation: "2026-03-29"
  alert_before: 14d  # Slack alert 14 days before expiry
```

## Access Control

| Role | Permission | Justification |
|------|-----------|---------------|
| orchestrator (orchestrator) | read | Routes model requests, needs key for fallback |
| operations_agent (deploy) | read | Injects into Railway env during deployment |
| builder_agent (build) | none | Build agent never calls external LLMs directly |
| research_agent (research) | read | Research may use GPT for cross-model comparison |
| Admin (human) | read/write/rotate | Full lifecycle management |

### Vault Policy
```hcl
path "secret/data/organization/prod/openai_api_key" {
  capabilities = ["read"]
  allowed_parameters = {
    "version" = []
  }
}

path "secret/metadata/organization/prod/openai_api_key" {
  capabilities = ["read", "list"]
}
```

## Audit Configuration

```yaml
audit:
  enabled: true
  log_destination: "vault/audit/openai_key_access.log"
  events_tracked:
    - read       # Every time the secret is fetched
    - update     # Key rotation events
    - delete     # Revocation events
    - denied     # Unauthorized access attempts
  retention: 365d
  alert_on:
    - denied                              # Any unauthorized access attempt
    - read_count_exceeds: 100/hour        # Anomalous read pattern
    - read_from_unknown_ip: true          # Access from non-Railway IPs
```

## Environment Integration

### Railway (Production)
```bash
# Secret injected via Vault agent sidecar
# Railway service variable references Vault path
OPENAI_API_KEY=vault:secret/data/organization/prod/openai_api_key#value
```

### Local Development
```bash
# .env.local (gitignored, never committed)
OPENAI_API_KEY=sk-proj-dev-PLACEHOLDER

# Or fetch from Vault directly:
export OPENAI_API_KEY=$(vault kv get -field=value secret/organization/dev/openai_api_key)
```

### CI/CD (GitHub Actions)
```yaml
# Stored as GitHub secret, NOT in Vault (GitHub manages its own encryption)
env:
  OPENAI_API_KEY: ${{ secrets.OPENAI_API_KEY_CI }}
  # CI key has lower rate limits ($5/day budget cap)
```

## Emergency Procedures

| Scenario | Action | Time Target |
|----------|--------|-------------|
| Key leaked in logs | Revoke immediately in OpenAI dashboard, rotate in Vault, redeploy | < 15 min |
| Key leaked in git commit | `git filter-branch` to remove, revoke + rotate, notify team | < 30 min |
| Vault unavailable | Fallback to Railway env variable (manually set, temporary) | < 5 min |
| OpenAI disables key | Generate new key, store in Vault, redeploy | < 10 min |
| Anomalous usage spike | Freeze key via OpenAI dashboard spending limit, investigate | < 5 min |

## Validation

```python
import os
import httpx

def validate_openai_key() -> dict:
    key = os.environ.get("OPENAI_API_KEY", "")

    # Format check
    assert key.startswith("sk-proj-"), "Key must be project-scoped (sk-proj-*)"
    assert len(key) >= 40, "Key too short — possible truncation"

    # Liveness check (cheapest possible API call)
    r = httpx.get(
        "https://api.openai.com/v1/models",
        headers={"Authorization": f"Bearer {key}"},
        timeout=5.0
    )
    assert r.status_code == 200, f"Key validation failed: {r.status_code}"

    return {"status": "valid", "models_available": len(r.json()["data"])}
```

## Anti-Patterns
- Storing API key in `.env` committed to git (use .env.local, gitignored)
- Sharing one key across prod/staging/dev (use separate keys per environment)
- No rotation policy (compromised keys persist indefinitely)
- Logging the full key value in audit (log last 4 chars only: `...xxxx`)
- Hardcoding key in application code instead of environment variable
