---
kind: quality_gate
id: p09_qg_oauth_app_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for oauth_app_config
quality: 9.0
title: "Quality Gate Oauth App Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [oauth_app_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for oauth_app_config"
domain: "oauth_app_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_oauth_app_config
  - bld_instruction_oauth_app_config
  - oauth-app-config-builder
  - p03_sp_oauth_app_config_builder
  - bld_knowledge_card_oauth_app_config
  - p09_qg_marketplace_app_manifest
  - kc_oauth_app_config
  - bld_output_template_oauth_app_config
  - p04_qg_sdk_example
  - hybrid_review7_n03
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| schema_id | ^p09_oauth_[a-z][a-z0-9_]+.yaml$ | matches | H02 |
| required_fields | 7 | >= | app config |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | invalid YAML syntax |
| H02 | ID matches pattern ^p09_oauth_[a-z][a-z0-9_]+.yaml$ | invalid schema ID |
| H03 | kind field matches 'oauth_app_config' | incorrect kind value |
| H04 | client_id present | missing client_id |
| H05 | redirect_uris are valid URLs | invalid redirect URI format |
| H06 | scopes are non-empty | empty or missing scopes |
| H07 | access token_lifetime <= 3600 (OAuth BCP recommends 5-60 min) | token lifetime exceeds 1h |
| H08 | refresh_token_policy is 'rotating' (OAuth 2.1 / BCP) | static refresh tokens not allowed |
| H09 | grant_types subset of {authorization_code, client_credentials, refresh_token} | implicit/ROPC forbidden by OAuth 2.1 |
| H10 | PKCE (S256) required for authorization_code flow | missing code_challenge_method |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Scope completeness | 0.15 | 1.0 if all required scopes present |
| D02 | Redirect validity | 0.15 | 1.0 if all URIs are HTTPS and registered |
| D03 | Token lifetime | 0.15 | 1.0 if <= 24h and aligned with policy |
| D04 | Refresh policy | 0.15 | 1.0 if 'rolling' or 'fixed' with clear rules |
| D05 | Security practices | 0.10 | 1.0 if PKCE enforced and client secrets rotated |
| D06 | Documentation | 0.10 | 1.0 if app config includes usage examples |
| D07 | Standards compliance | 0.20 | 1.0 if aligns with OAuth 2.1 + RFC 7636 PKCE + RFC 8252 |

## Actions
| Score | Action |
|---|---|
| GOLDEN | >=9.5 | Auto-approve and deploy |
| PUBLISH | >=8.0 | Deploy after review |
| REVIEW | >=7.0 | Require manual review |
| REJECT | <7.0 | Block deployment |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Security exception | CTO | "Bypassed by [name] on [date] for [reason]" |

## Examples

## Golden Example
```yaml
kind: oauth_app_config
name: github_integration
spec:
  client_id: "ghp_1234567890abcdef1234567890abcdef1234"
  client_secret: "supersecretclientsecret"
  redirect_uris:
    - "https://app.example.com/auth/callback"
  scopes:
    - "repo"
    - "user"
  token_lifetimes:
    access_token_expires_in: 3600
    refresh_token_expires_in: 86400
  refresh_policy: "rotate"
```

## Anti-Example 1: Missing Redirect URIs
```yaml
kind: oauth_app_config
name: bad_github_integration
spec:
  client_id: "ghp_0987654321abcdef0987654321abcdef0987"
  client_secret: "anothersecret"
  scopes:
    - "all"
```
## Why it fails
Lacks redirect_uris, allowing any redirect URI which creates open redirect vulnerabilities. Also uses "all" scope, granting excessive permissions.

## Anti-Example 2: Insecure Token Lifetimes
```yaml
kind: oauth_app_config
name: insecure_github_integration
spec:
  client_id: "ghp_1122334455abcdef1122334455abcdef1122"
  client_secret: "insecuresecret"
  redirect_uris:
    - "https://app.example.com/callback"
  scopes:
    - "public_repo"
  token_lifetimes:
    access_token_expires_in: 86400
    refresh_token_expires_in: 31536000
  refresh_policy: "reuse"
```
## Why it fails
Uses 1-year refresh tokens (31536000s) which is excessive and increases risk of token misuse. Refresh policy "reuse" allows tokens to be used indefinitely, violating security best practices.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
