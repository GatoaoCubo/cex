---
id: con_secret_config_n03
kind: secret_config
pillar: P09
nucleus: n03
title: Engineering Secret Config
version: 1.0
quality: 9.0
tags: [config, secrets, security, engineering, n03]
density_score: 1.0
---


<!-- 8F: F1 constrain=P09/secret_config F2 become=secret-config-builder F3 inject=nucleus_def_n03, kc_secret_config, kc_env_config, P09_config, runtime context
     F4 reason=pointer registry for N03 secrets without storing secret values F5 call=rg, Get-Content, apply_patch F6 produce=4279 bytes
     F7 govern=frontmatter+sections+tables+ascii+self-check F8 collaborate=save N03_engineering/P09_config/con_secret_config_n03.md -->

# Engineering Secret Config

## Purpose

| Field | Value |
|-------|-------|
| Mission fit | Secret pointer registry for N03 build, compile, and collaboration workflows |
| Pride lens | Secret handling is disciplined invisibility: perfect control with zero disclosure |
| Primary use | Document secret identifiers, providers, rotation policy, and retrieval pattern |
| Boundary | Contains metadata only, never secret values |
| Storage posture | Environment or managed vault injection only |
| Failure prevented | Hardcoded credentials, undocumented rotation, and unclear ownership |

## Values

| Secret name | Provider | Runtime reference | Rotation policy | Access pattern | Owner |
|-------------|----------|-------------------|-----------------|---------------|-------|
| `anthropic_api_key` | env_or_vault | `ANTHROPIC_API_KEY` | `90_day_rotate_or_on_exposure` | injected into process env | platform_owner |
| `openai_api_key` | env_or_vault | `OPENAI_API_KEY` | `90_day_rotate_or_on_exposure` | injected into process env | platform_owner |
| `github_token` | env_or_vault | `GITHUB_TOKEN` | `60_day_rotate_or_on_scope_change` | injected into process env | platform_owner |
| `canva_client_secret` | vault_preferred | `CANVA_CLIENT_SECRET` | `90_day_rotate` | vault fetch then env injection | platform_owner |
| `signal_channel_key` | env_or_vault | `CEX_SIGNAL_KEY` | `180_day_rotate` | injected into process env | ops_owner |

## Secret Rules

| Rule ID | Statement | Why it matters |
|---------|-----------|----------------|
| `S01` | No secret value may appear in markdown, YAML examples, or compiled artifacts | Metadata must never become leakage |
| `S02` | Every runtime secret referenced by N03 env config must have a row here | Traceability beats tribal knowledge |
| `S03` | Rotation on suspected exposure overrides scheduled rotation | Incident response beats calendar purity |
| `S04` | Provider choice `vault_preferred` is mandatory for multi-user deployment surfaces | Shared systems deserve stronger handling |
| `S05` | Owner field must resolve to an accountable role, not a person nickname | Governance survives staff changes |
| `S06` | Deprecated secrets remain documented until all consumers are migrated | Retirement must be auditable |

## Rationale

| Design choice | Why it exists | Pride expression |
|---------------|---------------|------------------|
| Pointer registry format | Lets config stay explicit without becoming hazardous | Clarity without exposure |
| Rotation policy per secret | Not all credentials carry the same operational risk | Nuance is part of rigor |
| Role-based ownership | Secrets outlive individual operators | Durable governance |
| `vault_preferred` for shared deployments | Stronger default for collaborative environments | Excellence where risk is highest |
| Exposure-triggered rotation | Good security responds to events, not only schedules | Active stewardship |
| Small curated secret set | Document what N03 truly needs, not every possible key | Minimal trusted surface |

## Example

```yaml
name: openai_api_key
provider: env_or_vault
runtime_reference: OPENAI_API_KEY
rotation_policy: 90_day_rotate_or_on_exposure
access_pattern:
  mode: injected_env
  value_persisted_in_repo: false
owner: platform_owner
notes:
  - referenced by env config
  - never rendered in compiled artifacts
```

## Properties

| Property | Value |
|----------|-------|
| Nucleus | `n03` |
| Pillar | `P09` |
| Kind | `secret_config` |
| Secret records | `5` |
| Value disclosure allowed | `false` |
| Default rotation baseline | `90_day_rotate` |
| Ownership model | `role_based` |
| Lens | `Inventive Pride` |
