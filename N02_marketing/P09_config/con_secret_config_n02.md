---
id: con_secret_config_n02
kind: secret_config
pillar: P09
nucleus: n02
title: Marketing Secret Config
version: 1.0
quality: 9.0
tags: [config, secrets, security, marketing, runtime]
density_score: 1.0
---


<!-- 8F: F1 constrain=P09/secret_config F2 become=secret_config-builder F3 inject=nucleus_def_n02+n02_rules+kc_secret_config+P09_schema
     F4 reason=pointer_registry_for_sensitive_marketing_integrations F5 call=shell_command,apply_patch F6 produce=3985 bytes
     F7 govern=frontmatter_sections_ascii_density_linecount F8 collaborate=N02_marketing/P09_config/con_secret_config_n02.md -->

# Purpose

| Item | Definition |
|------|------------|
| Mission fit | Secret registry for N02 integrations and delivery tools |
| Creative Lust lens | Protects the backstage machinery so seductive campaigns never leak trust-destroying credentials |
| Primary use | Document secret names, storage backends, and rotation policy without exposing values |
| Scope | API keys and client secrets used by N02 workflows |
| Why registry matters | Marketing speed often touches many tools; a pointer map prevents sloppy secret handling |

## Values

| Secret Name | Provider | Env Var | Storage | Rotation Policy |
|-------------|----------|---------|---------|-----------------|
| openai_primary | openai | OPENAI_API_KEY | env | 90d |
| anthropic_fallback | anthropic | ANTHROPIC_API_KEY | env | 90d |
| canva_oauth_client | canva | CANVA_CLIENT_ID | env | 180d |
| canva_oauth_secret | canva | CANVA_CLIENT_SECRET | env | 90d |
| notebooklm_token | notebooklm | NOTEBOOKLM_API_KEY | env | 90d |

## Secret Handling Rules

| Rule | Value |
|------|-------|
| secret values in source | blocked |
| committed .env files | blocked |
| local runtime injection | allowed via shell env only |
| production injection | platform env or vault only |
| rotation reminder owner | n07 or deployment operator |
| breach response | rotate, revoke, audit references |

## Storage Policy

| Storage Mode | Allowed | Reason |
|--------------|---------|--------|
| env | yes | Simple and aligned with local CLI execution |
| vault | yes | Preferred when centralized secret management exists |
| source_file | no | Too easy to leak through git or logs |
| markdown_embed | no | Violates the registry-only contract |

## Rationale

| Decision | Reason |
|----------|--------|
| Separate Canva ID and secret entries | Client identity and credential lifecycle differ |
| 90-day default rotation | Balanced security baseline for active integrations |
| 180-day client ID rotation | Public-ish identifier rotates less often than secret material |
| Registry only, never value storage | Preserves trust and keeps audits straightforward |
| Breach response table | Marketing tools often sprawl; response must be fast and repeatable |

## Example

```yaml
secret_reference:
  secret_name: openai_primary
  provider: openai
  env_var: OPENAI_API_KEY
  storage: env
  rotation_policy: 90d
```

| Example Scenario | Result | Why |
|------------------|--------|-----|
| Value pasted into markdown | block | Secret value exposure |
| Env var referenced by name only | allow | Registry pattern followed |
| .env committed to repo | block | Source exposure risk |
| Rotation date exceeded | revise | Secret must be renewed |

## Operational Notes

| Note | Guidance |
|------|----------|
| Logging | Never print secret values or full tokens |
| Testing | Use placeholder names, not live secrets |
| Sharing | Reference the secret name and env var only |
| Decommission | Revoke secret and remove registry entry after migration |

## Properties

| Property | Value |
|----------|-------|
| Kind | secret_config |
| Pillar | P09 |
| Nucleus | n02 |
| Provider count | 4 |
| Storage default | env |
| Rotation baseline | 90d |
| Value retention | none in source |
| Main risk prevented | credential leakage during campaign operations |
| Governance mode | registry plus rotation policy |
| Save path | N02_marketing/P09_config/con_secret_config_n02.md |
