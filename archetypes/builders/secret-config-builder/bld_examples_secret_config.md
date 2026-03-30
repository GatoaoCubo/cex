---
kind: examples
id: bld_examples_secret_config
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of secret_config artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: secret-config-builder
## Golden Example
INPUT: "Create secret config for OpenAI and Anthropic API keys used by research_agent research agent, stored in HashiCorp Vault with daily rotation"
OUTPUT:
```yaml
id: p09_sec_llm_api_keys
kind: secret_config
pillar: P09
version: "1.0.0"
created: "2026-03-29"
updated: "2026-03-29"
author: "builder_agent"
name: "LLM API Keys — research_agent Research Agent"
provider: vault
rotation_policy:
  frequency: daily
  method: automatic
encryption:
  at_rest: AES-256-GCM
  in_transit: TLS 1.3
access_pattern: dynamic
quality: null
tags: [secret_config, vault, llm-keys, P09]
tldr: "Vault-backed LLM API keys for research_agent with daily auto-rotation and dynamic leases"
description: "Manages OpenAI and Anthropic API keys for research_agent research agent via Vault dynamic secrets"
secret_paths:
  - "secret/data/agents/shaka/openai"
  - "secret/data/agents/shaka/anthropic"
lease_duration: "1h"
audit_log: true
namespaces: ["agents/shaka"]
fallback: "env"
```
## Overview
Manages LLM provider API keys (OpenAI, Anthropic) for the research_agent research agent.
Keys rotate daily via Vault auto-rotation; research_agent retrieves a short-lived lease at task start.
## Provider
Backend: HashiCorp Vault — AppRole auth (role_id + secret_id injected at boot)
Paths:
- `secret/data/agents/shaka/openai` — OpenAI API key (sk-<PLACEHOLDER>)
- `secret/data/agents/shaka/anthropic` — Anthropic API key (sk-ant-<PLACEHOLDER>)
AppRole role: `agents-shaka-reader` (read-only on `secret/data/agents/shaka/*`)
## Rotation Policy
- Frequency: daily (00:00 UTC)
- Method: automatic (Vault rotation Lambda)
- Trigger: schedule + on-breach (PagerDuty webhook)
- Rollback: previous version retained for 2h in Vault KV v2 history
## Access Pattern
Pattern: dynamic — research_agent requests a lease-bound token at task start via AppRole login.
1. Boot: inject role_id + secret_id via K8s init container
2. Task start: `vault write auth/approle/login role_id=<PLACEHOLDER> secret_id=<PLACEHOLDER>`
3. Read: `vault kv get secret/data/agents/shaka/openai`
4. Lease TTL: 1h — renewed if task exceeds TTL
Fallback: env injection (OPENAI_API_KEY env var) if Vault unreachable

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p09_sec_ pattern (H02 pass)
- kind: secret_config (H04 pass)
- provider is valid enum: vault (H06 pass)
- rotation_policy has frequency + method (H06 pass)
- encryption has at_rest + in_transit (H06 pass)
- access_pattern is valid enum: dynamic (H06 pass)
- audit_log: true (H09 pass)
- NO real secrets — all placeholders (H10 pass)
- All 4 body sections present: Overview, Provider, Rotation Policy, Access Pattern (H07 pass)
- tags: 4 items, includes "secret_config" (S02 pass)
- tldr: 73 chars <= 160 (S01 pass)

## Anti-Example
INPUT: "Config for database password"
BAD OUTPUT:
```yaml
id: db-password-config
kind: config
provider: database
password: "myS3cr3tP@ss!"
quality: 8.5
tags: [db]
```
Database password config.
FAILURES:
1. id: "db-password-config" has hyphens, no `p09_sec_` prefix -> H02 FAIL
2. kind: "config" not "secret_config" -> H04 FAIL
3. quality: 8.5 (not null) -> H05 FAIL
4. password: "myS3cr3tP@ss!" is a REAL SECRET in plaintext -> H10 FAIL (critical)
5. provider: "database" is not a valid enum value -> H06 FAIL
6. Missing: rotation_policy, encryption, access_pattern, version, created, updated, author, tldr -> H06 FAIL
7. tags: only 1 item, missing "secret_config" -> S02 FAIL
8. Body missing all 4 required sections -> H07 FAIL
9. No rotation_policy — credential never rotates -> H06 FAIL
10. No encryption declared — security posture unknown -> H06 FAIL
