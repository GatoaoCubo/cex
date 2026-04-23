---
id: n00_oauth_app_config_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "OAuth App Config -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, oauth_app_config, p09, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_oauth_app_config
  - bld_schema_sso_config
  - bld_schema_reranker_config
  - bld_schema_sandbox_config
  - bld_schema_usage_report
  - bld_schema_dataset_card
  - bld_schema_benchmark_suite
  - bld_schema_integration_guide
  - bld_schema_thinking_config
  - bld_schema_multimodal_prompt
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
An oauth_app_config defines the OAuth2 or PKCE application configuration for partner integrations: client credentials, authorized redirect URIs, scopes, and token management settings. It enables CEX to authenticate with external services and allows third-party applications to authenticate with CEX APIs securely.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `oauth_app_config` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable app config name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| flow | enum | yes | authorization_code \| pkce \| client_credentials \| device_code |
| client_id | string | yes | OAuth2 client identifier (non-secret) |
| client_secret_ref | string | no | Reference to secret_config (never store secret inline) |
| redirect_uris | list | yes | Authorized callback URLs |
| scopes | list | yes | OAuth scopes this app requests |
| token_endpoint | string | yes | Provider token URL |
| auth_endpoint | string | yes | Provider authorization URL |
| token_expiry_seconds | integer | no | Access token lifetime |
| refresh_enabled | boolean | no | Whether refresh tokens are used |

## When to use
- Configuring OAuth for a CEX nucleus to call external APIs (GitHub, Slack, HubSpot)
- Setting up PKCE flow for a browser-based CEX companion app
- Defining client credentials for server-to-server API authentication

## Builder
`archetypes/builders/oauth_app_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind oauth_app_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: oauth_github_n05
kind: oauth_app_config
pillar: P09
nucleus: n05
title: "GitHub OAuth for N05 Operations"
version: 1.0
quality: null
---
flow: authorization_code
client_id: "ghclient_abc123"
client_secret_ref: secret_config_github_n05
redirect_uris: [https://cex.local/callback]
scopes: [repo, read:org]
token_endpoint: https://github.com/login/oauth/access_token
auth_endpoint: https://github.com/login/oauth/authorize
```

## Related kinds
- `secret_config` (P09) -- stores the client_secret referenced here
- `sso_config` (P09) -- SSO integrations that extend OAuth with SAML/OIDC
- `permission` (P09) -- scopes granted by OAuth map to CEX permission rules

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_oauth_app_config]] | upstream | 0.61 |
| [[bld_schema_sso_config]] | upstream | 0.46 |
| [[bld_schema_reranker_config]] | upstream | 0.46 |
| [[bld_schema_sandbox_config]] | upstream | 0.45 |
| [[bld_schema_usage_report]] | upstream | 0.44 |
| [[bld_schema_dataset_card]] | upstream | 0.44 |
| [[bld_schema_benchmark_suite]] | upstream | 0.44 |
| [[bld_schema_integration_guide]] | upstream | 0.44 |
| [[bld_schema_thinking_config]] | upstream | 0.43 |
| [[bld_schema_multimodal_prompt]] | upstream | 0.43 |
