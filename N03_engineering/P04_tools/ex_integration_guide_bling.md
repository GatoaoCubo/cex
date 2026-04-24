---
quality: 9.1
id: ex_integration_guide_bling
kind: integration_guide
8f: F6_produce
pillar: P04
title: Bling ERP Integration Guide
version: 0.2.0
quality: 6.8
status: example
author: n03_engineering
created: "2026-04-17"
updated: "2026-04-22"
domain: erp_integration
integration_type: OAuth2_REST
tldr: "Connects Bling ERP (Brazilian) to Supabase via OAuth 2.0 and REST API v3 for product sync, webhook stock events, and scheduled token refresh."
api_endpoints:
  - GET /produtos
  - POST /produtos
  - PATCH /produtos/{id}
  - POST /oauth/token
  - POST /webhooks
dependencies:
  - supabase-cli >= 1.0
  - bling-api-v3
brand_placeholders:
  - BRAND_BLING_CLIENT_ID
  - BRAND_BLING_CLIENT_SECRET
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, example, bling, erp, integration, oauth2, supabase]
density_score: 0.88
related:
  - bld_tools_supabase_data_layer
  - p01_kc_supabase_edge_functions
  - p01_kc_supabase_cli
  - kc_erp_integration
  - bld_knowledge_card_oauth_app_config
  - p01_kc_bling_erp_field_parametrization
  - p12_wf_supabase_setup
  - p01_kc_supabase_self_hosting
  - p01_kc_bling_erp_automation_boundary
  - kc_oauth_app_config
---

## Overview

Connects Bling ERP (Brazilian fiscal/inventory) to a Supabase product catalog using OAuth 2.0 authorization code flow, REST API v3, inbound HMAC webhooks for stock events, and a pg_cron token refresh job.

## When to Use

- Syncing Brazilian NF-e fiscal documents alongside a Shopify/Supabase commerce stack.
- Keeping Bling stock quantities synchronized with Supabase in real time.
- Automating product creation in Bling from Supabase catalog entries.

## Prerequisites

| Requirement | Value |
|-------------|-------|
| Bling plan | Pro or above (API v3 required) |
| API version | v3 (REST + OAuth 2.0) |
| Base URL | `https://www.bling.com.br/Api/v3` |
| OAuth app | Register at `https://developer.bling.com.br` |
| Supabase project | `{{BRAND_SUPABASE_PROJECT_REF}}` |

## Architecture

```
Bling ERP API v3 (OAuth 2.0)
  |-- REST endpoints -> edge fn: sync-bling-product, bling-create-missing
  |-- Webhooks (HMAC) -> edge fn: bling-webhook
  |-- Token refresh -> edge fn: token-auto-refresh (pg_cron every 50 min)
Supabase DB: products, bling_tokens
```

## API Endpoints

| Method | Path | Description | Auth |
|--------|------|-------------|------|
| `GET` | `/produtos` | List products (paginated) | Bearer access_token |
| `POST` | `/produtos` | Create product | Bearer access_token |
| `PATCH` | `/produtos/{id}` | Update product fields | Bearer access_token |
| `GET` | `/estoques` | Get stock levels | Bearer access_token |
| `POST` | `/oauth/token` | Exchange code or refresh token | Basic client_id:secret |
| `POST` | `/webhooks` | Register webhook endpoint | Bearer access_token |

## OAuth 2.0 Flow

### Step 1 -- Register App

1. Go to `https://developer.bling.com.br` -> create application.
2. Set redirect URI: `https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/bling-oauth-callback`.
3. Store credentials: `supabase secrets set BLING_CLIENT_ID={{BRAND_BLING_CLIENT_ID}} BLING_CLIENT_SECRET={{BRAND_BLING_CLIENT_SECRET}}`.

### Step 2 -- Authorization Redirect

```
GET https://www.bling.com.br/Api/v3/oauth/authorize
  ?response_type=code
  &client_id={{BRAND_BLING_CLIENT_ID}}
  &state={nonce}
```

### Step 3 -- Token Exchange

```typescript
const res = await fetch('https://www.bling.com.br/Api/v3/oauth/token', {
  method: 'POST',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  body: new URLSearchParams({
    grant_type: 'authorization_code', code,
    redirect_uri: REDIRECT_URI,
    client_id: Deno.env.get('BLING_CLIENT_ID')!,
    client_secret: Deno.env.get('BLING_CLIENT_SECRET')!,
  }),
});
const { access_token, refresh_token, expires_in } = await res.json();
// access_token TTL: ~60 min; refresh_token TTL: ~6 months
```

### Step 4 -- Deploy Functions

```bash
supabase functions deploy bling-oauth-callback
supabase functions deploy bling-webhook
supabase functions deploy sync-bling-product
supabase functions deploy sync-all-products-bling
supabase functions deploy token-auto-refresh
```

### Step 5 -- Token Refresh Cron

```sql
select cron.schedule('bling-token-refresh', '*/50 * * * *',
  $$select net.http_post(
    url := 'https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/token-auto-refresh',
    headers := '{"Authorization":"Bearer {SUPABASE_SERVICE_KEY}"}')$$);
```

### Step 6 -- Initial Sync

```bash
curl -X POST \
  https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/sync-all-products-bling \
  -H "Authorization: Bearer $SUPABASE_SERVICE_KEY"
```

## Error Codes

| Code | Meaning | Resolution |
|------|---------|------------|
| 401 | Invalid or expired access_token | Trigger token refresh, retry once |
| 403 | Insufficient scope or plan | Verify Bling Pro plan; check scopes |
| 422 | Validation error (missing required field) | Inspect `errors[]` in response body |
| 429 | Rate limit exceeded | Backoff 60s; Bling v3 limit: 3 req/s |
| 500 | Bling server error | Retry with exponential backoff (max 3x) |

## Interface

| Input | Type | Description |
|-------|------|-------------|
| `BLING_CLIENT_ID` | env secret | OAuth app client ID |
| `BLING_CLIENT_SECRET` | env secret | OAuth app client secret |
| `BLING_ACCESS_TOKEN` | DB bling_tokens | Current access token |
| `BLING_REFRESH_TOKEN` | DB bling_tokens | Refresh token |

| Output | Description |
|--------|-------------|
| Supabase `products` rows | Updated with `bling_id`, `bling_synced_at` |
| Bling product records | Created/updated via API v3 |

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| 401 on every call | Token not refreshing | Check pg_cron job; verify service key |
| Products not appearing in Bling | Missing required fields | Validate `codigo` and `nome` are present |
| Webhook not firing | Endpoint not registered | Re-run webhook registration POST |
| HMAC mismatch on webhook | Wrong secret stored | Re-set `BLING_WEBHOOK_SECRET` in Supabase |

## Brand Variables

| Variable | Purpose |
|----------|---------|
| `{{BRAND_BLING_CLIENT_ID}}` | OAuth 2.0 client ID env name |
| `{{BRAND_BLING_CLIENT_SECRET}}` | OAuth 2.0 client secret env name |
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Supabase project reference |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_supabase_data_layer]] | related | 0.44 |
| [[p01_kc_supabase_edge_functions]] | upstream | 0.36 |
| [[p01_kc_supabase_cli]] | upstream | 0.34 |
| [[kc_erp_integration]] | upstream | 0.31 |
| [[bld_knowledge_card_oauth_app_config]] | upstream | 0.28 |
| [[p01_kc_bling_erp_field_parametrization]] | upstream | 0.28 |
| [[p12_wf_supabase_setup]] | downstream | 0.28 |
| [[p01_kc_supabase_self_hosting]] | upstream | 0.27 |
| [[p01_kc_bling_erp_automation_boundary]] | upstream | 0.27 |
| [[kc_oauth_app_config]] | upstream | 0.26 |
