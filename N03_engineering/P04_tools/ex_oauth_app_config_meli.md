---
id: ex_oauth_app_config_meli
kind: oauth_app_config
8f: F1_constrain
pillar: P09
title: Mercado Livre OAuth 2.0 App Configuration
version: 0.1.0
quality: 8.4
status: template
brand_placeholders:
  - BRAND_MELI_CLIENT_ID
  - BRAND_MELI_CLIENT_SECRET
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, mercadolivre, meli, oauth]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_knowledge_card_oauth_app_config
  - kc_oauth_app_config
  - oauth-app-config-builder
  - p03_sp_oauth_app_config_builder
  - p09_qg_oauth_app_config
  - bld_output_template_oauth_app_config
  - bld_instruction_oauth_app_config
  - bld_schema_oauth_app_config
  - p10_lr_oauth_app_config_builder
  - bld_knowledge_card_thinking_config
---

## Purpose

OAuth 2.0 app configuration for Mercado Livre (MLB) API — defines the authorization code flow, token storage schema, and 6-hour access token refresh strategy for `{{BRAND_MELI_CLIENT_ID}}`.

## When to Use

- Registering and configuring a new ML app for the first time.
- Documenting the token lifecycle for compliance and security review.
- Setting up proactive token refresh to avoid 401 errors in production.

## App Registration

1. Go to `https://developers.mercadolivre.com.br/devcenter` → Create App.
2. Set **Redirect URI**: `https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/meli-oauth-callback`.
3. Set scopes: `offline_access` (required for refresh tokens).
4. Copy client ID and client secret → store:

```bash
supabase secrets set MELI_CLIENT_ID={{BRAND_MELI_CLIENT_ID}}
supabase secrets set MELI_CLIENT_SECRET={{BRAND_MELI_CLIENT_SECRET}}
```

## OAuth 2.0 Parameters

| Parameter | Value |
|-----------|-------|
| Auth endpoint | `https://auth.mercadolibre.com.br/authorization` |
| Token endpoint | `https://api.mercadolibre.com/oauth/token` |
| Grant type | `authorization_code` |
| Response type | `code` |
| Scope | `offline_access` (plus any ML-specific scopes) |
| Access token TTL | 21600s (6 hours) |
| Refresh token TTL | ~180 days |
| Site | `MLB` (Brazil) |

## Authorization URL

```
https://auth.mercadolibre.com.br/authorization
  ?response_type=code
  &client_id={{BRAND_MELI_CLIENT_ID}}
  &redirect_uri=https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/meli-oauth-callback
  &state={nonce}
```

## Token Storage Schema

```sql
create table meli_tokens (
  id            uuid primary key default gen_random_uuid(),
  access_token  text not null,
  refresh_token text not null,
  expires_at    timestamptz not null,
  user_id       bigint,            -- ML user ID
  scope         text,
  created_at    timestamptz default now(),
  updated_at    timestamptz default now()
);
```

## Token Refresh

Access tokens expire in 6 hours. Refresh proactively at 5h 50m:

```http
POST https://api.mercadolibre.com/oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=refresh_token
&client_id={MELI_CLIENT_ID}
&client_secret={MELI_CLIENT_SECRET}
&refresh_token={STORED_REFRESH_TOKEN}
```

Response: new `access_token` + new `refresh_token` (rolling refresh — always store both).

## Cron Setup (shared with Bling)

The `token-auto-refresh` edge function handles both Bling and ML refresh in one pass. Schedule every 5 hours:

```sql
select cron.schedule('meli-token-refresh', '0 */5 * * *',
  $$select net.http_post(url := 'https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/token-auto-refresh')$$);
```

## Interface

| Input | Type | Description |
|-------|------|-------------|
| `MELI_CLIENT_ID` | env secret | OAuth app client ID |
| `MELI_CLIENT_SECRET` | env secret | OAuth app client secret |
| Authorization code | URL param | From ML redirect |

| Output | Description |
|--------|-------------|
| `access_token` | Bearer token for ML API calls |
| `refresh_token` | Rolling long-lived refresh token |

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_MELI_CLIENT_ID}}` | ML OAuth client ID env name |
| `{{BRAND_MELI_CLIENT_SECRET}}` | ML OAuth client secret env name |
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Supabase project (callback URL + DB) |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_oauth_app_config]] | upstream | 0.49 |
| [[kc_oauth_app_config]] | upstream | 0.46 |
| [[oauth-app-config-builder]] | related | 0.43 |
| [[p03_sp_oauth_app_config_builder]] | upstream | 0.34 |
| [[p09_qg_oauth_app_config]] | downstream | 0.31 |
| [[bld_output_template_oauth_app_config]] | upstream | 0.30 |
| [[bld_instruction_oauth_app_config]] | upstream | 0.30 |
| [[bld_schema_oauth_app_config]] | upstream | 0.29 |
| [[p10_lr_oauth_app_config_builder]] | downstream | 0.28 |
| [[bld_knowledge_card_thinking_config]] | upstream | 0.27 |
