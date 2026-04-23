---
quality: 9.1
id: ex_integration_guide_meli
kind: integration_guide
pillar: P04
title: Mercado Livre Integration Guide
version: 0.2.0
quality: 6.8
status: example
author: n03_engineering
created: "2026-04-17"
updated: "2026-04-22"
domain: marketplace_integration
integration_type: OAuth2_REST
tldr: "Integrates Mercado Livre API into a Supabase commerce stack via OAuth 2.0 for product enrichment and long-lived token management."
api_endpoints:
  - GET /sites/{site_id}/search
  - GET /items/{item_id}
  - POST /oauth/token
  - GET /users/me
dependencies:
  - supabase-cli >= 1.0
  - mercadolibre-api-v1
brand_placeholders:
  - BRAND_MELI_CLIENT_ID
  - BRAND_MELI_CLIENT_SECRET
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, example, mercadolivre, meli, integration, oauth2, supabase]
density_score: 0.88
related:
  - bld_knowledge_card_oauth_app_config
  - kc_oauth_app_config
  - bld_tools_supabase_data_layer
  - oauth-app-config-builder
  - bld_output_template_oauth_app_config
  - p01_kc_supabase_edge_functions
  - p01_kc_supabase_cli
  - p03_sp_oauth_app_config_builder
  - bld_instruction_oauth_app_config
  - p09_qg_oauth_app_config
---

## Overview

Integrates Mercado Livre (Brazil, site MLB) into a Supabase commerce stack using OAuth 2.0 authorization code flow. Primary use case: enrich incomplete product catalog entries by querying ML's public catalog for titles, descriptions, and images.

## When to Use

- Filling data gaps in Supabase product catalog using ML public catalog search.
- Connecting ML as a sales channel alongside Shopify and Bling.
- Pulling ML product data (titles, images) to normalize incomplete catalog entries.

## Prerequisites

| Requirement | Value |
|-------------|-------|
| ML developer account | `https://developers.mercadolivre.com.br` |
| Registered ML app | With redirect URI set (see Step 1) |
| Country site | Brazil (`MLB`) |
| API base URL | `https://api.mercadolibre.com` |
| Supabase project | `{{BRAND_SUPABASE_PROJECT_REF}}` |
| OAuth callback URL | `https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/meli-oauth-callback` |

## Architecture

```
Mercado Livre API
  |-- Product catalog search -> edge fn: product-enrich
  |-- OAuth 2.0 callback -> edge fn: meli-oauth-callback
  |-- Token refresh -> edge fn: token-auto-refresh (cron, shared)
Supabase DB: products, meli_tokens
```

## API Endpoints

| Method | Path | Description | Auth |
|--------|------|-------------|------|
| `GET` | `/sites/MLB/search?q={query}` | Search public catalog by keyword | None (public) |
| `GET` | `/items/{item_id}` | Get item details (title, desc, images) | None (public) |
| `GET` | `/sites/MLB/search?category={cat_id}` | Search by ML category | None (public) |
| `POST` | `/oauth/token` | Exchange code or refresh token | Basic client:secret |
| `GET` | `/users/me` | Verify authenticated user identity | Bearer access_token |

## OAuth 2.0 Flow

### Step 1 -- Register Application

1. Go to `https://developers.mercadolivre.com.br/devcenter` -> Create App.
2. Set redirect URI: `https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/meli-oauth-callback`.
3. Copy `client_id` and `client_secret`.

```bash
supabase secrets set MELI_CLIENT_ID={{BRAND_MELI_CLIENT_ID}}
supabase secrets set MELI_CLIENT_SECRET={{BRAND_MELI_CLIENT_SECRET}}
```

### Step 2 -- Authorization Redirect

```
GET https://auth.mercadolibre.com.br/authorization
  ?response_type=code
  &client_id={{BRAND_MELI_CLIENT_ID}}
  &redirect_uri=https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/meli-oauth-callback
  &state={nonce}
```

### Step 3 -- Token Exchange

```typescript
const res = await fetch('https://api.mercadolibre.com/oauth/token', {
  method: 'POST',
  headers: { Accept: 'application/json', 'Content-Type': 'application/x-www-form-urlencoded' },
  body: new URLSearchParams({
    grant_type: 'authorization_code', code,
    redirect_uri: REDIRECT_URI,
    client_id: Deno.env.get('MELI_CLIENT_ID')!,
    client_secret: Deno.env.get('MELI_CLIENT_SECRET')!,
  }),
});
const { access_token, refresh_token, expires_in } = await res.json();
// access_token TTL: 21600s (6h); refresh_token TTL: ~180 days
```

### Step 4 -- Deploy Functions

```bash
supabase functions deploy meli-oauth-callback
supabase functions deploy product-enrich
```

### Step 5 -- Scheduled Token Refresh

| Token | TTL | Refresh trigger |
|-------|-----|-----------------|
| Access token | 21600s (6h) | Proactive refresh at 5h 55m |
| Refresh token | ~180 days | Re-authorize if expired |

```sql
select cron.schedule('meli-token-refresh', '55 5 * * *',
  $$select net.http_post(
    url := 'https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/token-auto-refresh',
    headers := '{"Authorization":"Bearer {SUPABASE_SERVICE_KEY}"}')$$);
```

### Step 6 -- Product Enrichment

```bash
curl -X POST \
  https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/product-enrich \
  -H "Authorization: Bearer $SUPABASE_SERVICE_KEY" \
  -d '{"supabase_product_id": "uuid-here"}'
```

The `product-enrich` function queries ML catalog by EAN or keyword and backfills missing `title`, `description`, and `images` columns.

## Error Codes

| Code | Meaning | Resolution |
|------|---------|------------|
| 401 | Expired or invalid access_token | Refresh token; re-authorize if refresh expired |
| 403 | App not authorized for resource | Check app permissions in ML Dev Center |
| 404 | Item not found in ML catalog | Skip enrichment; mark `ml_enriched: false` |
| 429 | Rate limit exceeded | ML default: 10 req/s; add 100ms delay between calls |
| 500 | ML server error | Retry with exponential backoff (max 3x) |

## Interface

| Input | Type | Description |
|-------|------|-------------|
| `MELI_CLIENT_ID` | env secret | ML OAuth app client ID |
| `MELI_CLIENT_SECRET` | env secret | ML OAuth app client secret |
| `MELI_ACCESS_TOKEN` | DB meli_tokens | Current access token |
| `supabase_product_id` | POST body | UUID of product to enrich |

| Output | Description |
|--------|-------------|
| Enriched Supabase product rows | Title, description, images backfilled from ML |
| ML access token | Stored in `meli_tokens` table |

## Troubleshooting

| Symptom | Cause | Fix |
|---------|-------|-----|
| 401 on every enrichment call | Token expired, cron not running | Verify pg_cron is enabled; check service key |
| No items found in search | Keyword too specific or wrong site | Use `MLB` site; try EAN search first |
| Enrichment overwrites good data | product-enrich not checking nulls | Add `WHERE title IS NULL` guard in edge fn |
| Token refresh loop | refresh_token expired | Trigger re-authorization flow manually |

## Brand Variables

| Variable | Purpose |
|----------|---------|
| `{{BRAND_MELI_CLIENT_ID}}` | ML OAuth client ID env name |
| `{{BRAND_MELI_CLIENT_SECRET}}` | ML OAuth client secret env name |
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Supabase project for callback and DB |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_oauth_app_config]] | upstream | 0.41 |
| [[kc_oauth_app_config]] | upstream | 0.39 |
| [[bld_tools_supabase_data_layer]] | related | 0.38 |
| [[oauth-app-config-builder]] | downstream | 0.36 |
| [[bld_output_template_oauth_app_config]] | downstream | 0.33 |
| [[p01_kc_supabase_edge_functions]] | upstream | 0.33 |
| [[p01_kc_supabase_cli]] | upstream | 0.29 |
| [[p03_sp_oauth_app_config_builder]] | upstream | 0.28 |
| [[bld_instruction_oauth_app_config]] | upstream | 0.27 |
| [[p09_qg_oauth_app_config]] | downstream | 0.27 |
