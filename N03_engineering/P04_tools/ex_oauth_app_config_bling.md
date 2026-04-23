---
id: ex_oauth_app_config_bling
kind: oauth_app_config
pillar: P09
title: Bling ERP OAuth 2.0 App Configuration
version: 0.1.0
quality: 8.4
status: template
brand_placeholders:
  - BRAND_BLING_CLIENT_ID
  - BRAND_BLING_CLIENT_SECRET
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, bling, erp, oauth]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_knowledge_card_oauth_app_config
  - oauth-app-config-builder
  - kc_oauth_app_config
  - p03_sp_oauth_app_config_builder
  - bld_output_template_oauth_app_config
  - p09_qg_oauth_app_config
  - bld_schema_oauth_app_config
  - bld_tools_supabase_data_layer
  - bld_instruction_oauth_app_config
  - bld_knowledge_card_thinking_config
---

## Purpose

OAuth 2.0 configuration for Bling ERP API v3 — defines the authorization code flow, token storage schema, and proactive refresh strategy for maintaining a valid access token against `{{BRAND_BLING_CLIENT_ID}}`.

## When to Use

- Initializing Bling ERP integration for the first time (one-time authorization).
- Documenting the token lifecycle for security audits.
- Implementing the token refresh scheduler as a Supabase cron.

## App Registration

1. Navigate to `https://developer.bling.com.br` → Applications → New App.
2. Set **Redirect URI**: `https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/bling-oauth-callback`.
3. Copy `client_id` and `client_secret`.
4. Store as Supabase secrets:

```bash
supabase secrets set BLING_CLIENT_ID={{BRAND_BLING_CLIENT_ID}}
supabase secrets set BLING_CLIENT_SECRET={{BRAND_BLING_CLIENT_SECRET}}
```

## OAuth 2.0 Parameters

| Parameter | Value |
|-----------|-------|
| Authorization endpoint | `https://www.bling.com.br/Api/v3/oauth/authorize` |
| Token endpoint | `https://www.bling.com.br/Api/v3/oauth/token` |
| Grant type | `authorization_code` |
| Response type | `code` |
| Token TTL (access) | ~3600 seconds |
| Token TTL (refresh) | ~180 days |
| Redirect URI | `https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/bling-oauth-callback` |

## Token Storage Schema

```sql
create table bling_tokens (
  id          uuid primary key default gen_random_uuid(),
  access_token  text not null,
  refresh_token text not null,
  expires_at    timestamptz not null,
  scope         text,
  created_at    timestamptz default now(),
  updated_at    timestamptz default now()
);
-- Only one row expected; use upsert on id = fixed UUID constant.
```

## Token Refresh Strategy

Access tokens expire in ~60 minutes. Proactive refresh at 50-minute intervals via Supabase `pg_cron`:

```sql
select cron.schedule(
  'bling-token-refresh',
  '*/50 * * * *',
  $$
    select net.http_post(
      url := 'https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/token-auto-refresh',
      headers := jsonb_build_object('Authorization', 'Bearer ' || current_setting('app.service_key'))
    );
  $$
);
```

## Refresh Token Request

```http
POST https://www.bling.com.br/Api/v3/oauth/token
Content-Type: application/x-www-form-urlencoded

grant_type=refresh_token
&refresh_token={STORED_REFRESH_TOKEN}
&client_id={BLING_CLIENT_ID}
&client_secret={BLING_CLIENT_SECRET}
```

## Interface

| Input | Type | Description |
|-------|------|-------------|
| `BLING_CLIENT_ID` | env secret | OAuth app client ID |
| `BLING_CLIENT_SECRET` | env secret | OAuth app client secret |
| Authorization code | URL param | Short-lived code from OAuth redirect |

| Output | Description |
|--------|-------------|
| `access_token` | Bearer token for API v3 calls |
| `refresh_token` | Long-lived token for refresh flow |
| `expires_in` | Seconds until access token expiry |

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_BLING_CLIENT_ID}}` | Bling OAuth app client ID env name |
| `{{BRAND_BLING_CLIENT_SECRET}}` | Bling OAuth app client secret env name |
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Supabase project for callback URL |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_oauth_app_config]] | upstream | 0.46 |
| [[oauth-app-config-builder]] | related | 0.42 |
| [[kc_oauth_app_config]] | upstream | 0.41 |
| [[p03_sp_oauth_app_config_builder]] | upstream | 0.31 |
| [[bld_output_template_oauth_app_config]] | upstream | 0.30 |
| [[p09_qg_oauth_app_config]] | downstream | 0.29 |
| [[bld_schema_oauth_app_config]] | upstream | 0.28 |
| [[bld_tools_supabase_data_layer]] | upstream | 0.28 |
| [[bld_instruction_oauth_app_config]] | upstream | 0.27 |
| [[bld_knowledge_card_thinking_config]] | upstream | 0.27 |
