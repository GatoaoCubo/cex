---
id: ex_integration_guide_bling
kind: integration_guide
pillar: P04
title: Bling ERP Integration Guide
version: 0.1.0
quality: null
status: template
brand_placeholders:
  - BRAND_BLING_API_KEY
  - BRAND_BLING_CLIENT_ID
  - BRAND_BLING_CLIENT_SECRET
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, bling, erp, integration]
---

## Purpose

Step-by-step integration guide for connecting Bling ERP (Brazilian) to a Supabase product catalog — covers OAuth 2.0 authorization, product sync via API v3, inbound webhooks for stock events, and scheduled token refresh.

## When to Use

- Connecting a Bling ERP account to manage Brazilian fiscal documents (NF-e) alongside a Shopify/Supabase commerce stack.
- Keeping product stock quantities in Bling synchronized with Supabase.
- Automating product creation in Bling from Supabase catalog entries.

## Prerequisites

| Requirement | Value |
|-------------|-------|
| Bling plan | Pro or above (API v3 access required) |
| API version | v3 (REST + OAuth 2.0) |
| Base URL | `https://www.bling.com.br/Api/v3` |
| OAuth app registration | `https://developer.bling.com.br` |
| Supabase project | `{{BRAND_SUPABASE_PROJECT_REF}}` |

## Architecture

```
Bling ERP API v3 (OAuth 2.0)
      |
      |-- REST endpoints ---------> edge function: sync-bling-product
      |                             edge function: sync-all-products-bling
      |                             edge function: bling-create-missing
      |
      |-- Webhooks (HMAC) -------> edge function: bling-webhook
      |
      |-- Token refresh ----------> edge function: token-auto-refresh (cron)
      |
Supabase DB (products, bling_tokens tables)
```

## OAuth 2.0 Authorization Flow

Bling uses standard OAuth 2.0 authorization code flow.

### Step 1 — Register OAuth App

1. Go to `https://developer.bling.com.br` → create an application.
2. Set redirect URI to: `https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/bling-oauth-callback`.
3. Note the `client_id` and `client_secret` → store in Supabase secrets as `{{BRAND_BLING_CLIENT_ID}}` and `{{BRAND_BLING_CLIENT_SECRET}}`.

### Step 2 — Authorize (One-Time)

```
GET https://www.bling.com.br/Api/v3/oauth/authorize
  ?response_type=code
  &client_id={{BRAND_BLING_CLIENT_ID}}
  &state={random_nonce}
```

Redirect to this URL from your admin UI. Bling redirects back with `?code=...`.

### Step 3 — Exchange Code for Tokens

The `bling-oauth-callback` edge function handles this automatically:

```typescript
const tokenRes = await fetch('https://www.bling.com.br/Api/v3/oauth/token', {
  method: 'POST',
  headers: { 'Content-Type': 'application/x-www-form-urlencoded' },
  body: new URLSearchParams({
    grant_type: 'authorization_code',
    code,
    redirect_uri: REDIRECT_URI,
    client_id: Deno.env.get('BLING_CLIENT_ID')!,
    client_secret: Deno.env.get('BLING_CLIENT_SECRET')!,
  }),
});
const { access_token, refresh_token, expires_in } = await tokenRes.json();
// Store in Supabase bling_tokens table
```

Token TTL: access token ~60 minutes; refresh token ~6 months.

### Step 4 — Deploy Edge Functions

```bash
supabase functions deploy bling-oauth-callback
supabase functions deploy bling-webhook
supabase functions deploy sync-bling-product
supabase functions deploy sync-all-products-bling
supabase functions deploy token-auto-refresh

supabase secrets set BLING_CLIENT_ID={{BRAND_BLING_CLIENT_ID}}
supabase secrets set BLING_CLIENT_SECRET={{BRAND_BLING_CLIENT_SECRET}}
```

### Step 5 — Scheduled Token Refresh

Create a cron job in Supabase (or pg_cron) to call `token-auto-refresh` every 50 minutes:

```sql
select cron.schedule('bling-token-refresh', '*/50 * * * *',
  $$select net.http_post(url := 'https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/token-auto-refresh',
    headers := '{"Authorization": "Bearer {SUPABASE_SERVICE_KEY}"}')$$);
```

### Step 6 — Initial Sync

Invoke `sync-all-products-bling` to push existing Supabase catalog to Bling:

```bash
curl -X POST \
  https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/sync-all-products-bling \
  -H "Authorization: Bearer $SUPABASE_SERVICE_KEY"
```

## Interface

| Input | Type | Description |
|-------|------|-------------|
| `BLING_CLIENT_ID` | env secret | OAuth app client ID |
| `BLING_CLIENT_SECRET` | env secret | OAuth app client secret |
| `BLING_ACCESS_TOKEN` | DB (bling_tokens) | Current access token |
| `BLING_REFRESH_TOKEN` | DB (bling_tokens) | Refresh token |

| Output | Description |
|--------|-------------|
| Supabase `products` rows | Updated with `bling_id`, `bling_synced_at` |
| Bling product records | Created/updated via API v3 |

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_BLING_API_KEY}}` | Legacy API key (v2 fallback only) |
| `{{BRAND_BLING_CLIENT_ID}}` | OAuth 2.0 client ID env name |
| `{{BRAND_BLING_CLIENT_SECRET}}` | OAuth 2.0 client secret env name |
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Supabase project reference |

## Related Artifacts

| Artifact | Kind | Role |
|----------|------|------|
| `ex_api_client_bling.md` | api_client | HTTP client for Bling API v3 |
| `ex_webhook_bling.md` | webhook | Inbound Bling stock event handler |
| `ex_oauth_app_config_bling.md` | oauth_app_config | OAuth flow config |
| `ex_workflow_multi_marketplace_sync.md` | workflow | Multi-marketplace orchestration |
