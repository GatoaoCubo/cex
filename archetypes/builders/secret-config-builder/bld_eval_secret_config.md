---
kind: quality_gate
id: p11_qg_secret_config
pillar: P11
llm_function: GOVERN
purpose: Golden and anti-examples of secret_config artifacts
pattern: few-shot learning — LLM reads these before producing
quality: 9.0
title: "Gate: secret_config"
version: "1.0.0"
author: "builder_agent"
tags: [quality-gate, secret-config, P09, credentials, rotation, encryption]
tldr: "Pass/fail gate for secret_config artifacts: provider validity, rotation policy completeness, encryption posture, access pattern, and no plaintext secrets."
domain: "credential and secret management specification — provider, rotation policy, encryption posture, and access pattern"
created: "2026-03-29"
updated: "2026-03-29"
density_score: 0.90
related:
  - p11_qg_search_tool
  - bld_instruction_secret_config
  - bld_examples_secret_config
  - p03_sp_secret_config_builder
  - p11_qg_function_def
  - p11_qg_vision_tool
  - bld_output_template_secret_config
  - p11_qg_chunk_strategy
  - bld_schema_secret_config
  - p10_lr_secret_config_builder
---

## Quality Gate

# Gate: secret_config
## Definition
| Field | Value |
|---|---|
| metric | secret_config artifact quality score |
| threshold | 7.0 (publish >= 8.0, golden >= 9.5) |
| operator | weighted_sum |
| scope | all artifacts with `kind: secret_config` |
## HARD Gates
All must pass (AND logic). Any single failure = REJECT.
| ID | Check | Fail Condition |
|---|---|---|
| H01 | Frontmatter parses as valid YAML | Parse error on frontmatter block |
| H02 | ID matches `^p09_sec_[a-z][a-z0-9_]+$` | ID contains uppercase, hyphens, or missing prefix |
| H03 | ID equals filename stem | `id: p09_sec_foo` but file is `p09_sec_bar.md` |
| H04 | Kind equals literal `secret_config` | `kind: config` or `kind: env_config` or any other value |
| H05 | Quality field is null | `quality: 7.5` or any non-null value |
| H06 | All required fields present | Missing `provider`, `rotation_policy`, `encryption`, or `access_pattern` |
| H07 | All 4 body sections present | Missing Overview, Provider, Rotation Policy, or Access Pattern section |
| H08 | Provider is valid enum | `provider: database` or any non-enum value |
| H09 | rotation_policy has both frequency and method | Missing frequency or method sub-field |
| H10 | NO plaintext secrets in file | Real API keys, passwords, or tokens found (not placeholders) |
| H11 | encryption has both at_rest and in_transit | Missing either at_rest or in_transit sub-field |
| H12 | access_pattern is valid enum | Value not in: dynamic, static, injected, env |
## SOFT Scoring
Weights sum to 100%.
| Dimension | Weight | Criteria |
|---|---|---|
| Rotation policy completeness | 1.0 | frequency, method, trigger, and rollback all defined |
| Encryption specificity | 1.0 | Algorithm named (AES-256-GCM, not just "encrypted") |
| Access pattern documentation | 1.0 | Step-by-step retrieval instructions in body |
| Secret path completeness | 0.5 | All relevant paths listed as placeholders |
| Lease and TTL definition | 0.5 | lease_duration set when access_pattern == dynamic |
| Audit log posture | 1.0 | audit_log declared; justification provided if false |
| Fallback definition | 0.5 | Fallback provider or method defined for critical secrets |
| Namespace/region scoping | 0.5 | namespaces listed when provider == k8s or aws |
| Boundary clarity | 1.0 | Explicitly not env_config, permission, or feature_flag |
| Domain specificity | 1.0 | Content specific to declared credential type and use case |
| Provider auth method | 1.0 | Auth method (AppRole, IAM, SA token) documented in Provider section |
| Rollback procedure | 1.0 | What happens if rotation fails — recovery steps defined |
## Actions
| Score | Tier | Action |
|---|---|---|
| >= 9.5 | Golden | Publish to pool as golden reference |
| >= 8.0 | Publish | Publish to pool, add to routing index |
| >= 7.0 | Review | Flag for improvement before publish |
| < 7.0 | Reject | Return to author with specific gate failures |
## Bypass
| Field | Value |
|---|---|
| conditions | Internal development stub only, never used in production agents |
| approver | Author self-certification with comment explaining dev-only scope |
| audit_trail | Bypass note in frontmatter comment with expiry date |
| expiry | 7d — secret configs must reach >= 7.0 or be removed (shorter than cli_tool — security risk) |
| never_bypass | H01 (unparseable YAML), H05 (self-scored artifacts), H10 (plaintext secrets — immediate security violation) |

## Examples

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
quality: 8.9
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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
