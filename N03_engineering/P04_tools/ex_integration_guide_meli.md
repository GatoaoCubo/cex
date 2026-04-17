---
id: ex_integration_guide_meli
kind: integration_guide
pillar: P04
title: Mercado Livre Integration Guide
version: 0.1.0
quality: null
status: template
brand_placeholders:
  - BRAND_MELI_CLIENT_ID
  - BRAND_MELI_CLIENT_SECRET
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, mercadolivre, meli, integration]
---

## Purpose

Step-by-step guide for integrating Mercado Livre (ML) API into a Supabase commerce stack — covers OAuth 2.0 authorization code flow, product enrichment via ML catalog, and long-lived token management with proactive refresh.

## When to Use

- Enriching product data gaps in Supabase using Mercado Livre's public catalog.
- Connecting ML as a sales channel alongside Shopify and Bling.
- Pulling ML product titles, descriptions, or images to fill incomplete catalog entries.

## Prerequisites

| Requirement | Value |
|-------------|-------|
| ML Developer account | `https://developers.mercadolivre.com.br` |
| Application | Registered ML app with redirect URI |
| Country | Brazil (`MLB` site ID) |
| API base | `https://api.mercadolibre.com` |
| Supabase project | `{{BRAND_SUPABASE_PROJECT_REF}}` |
| OAuth callback | `https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/meli-oauth-callback` |

## Architecture

```
Mercado Livre API
      |
      |-- Product catalog search -> edge function: product-enrich
      |
      |-- OAuth 2.0  -----------> edge function: meli-oauth-callback
      |
      |-- Token refresh ----------> edge function: token-auto-refresh (cron, shared)
      |
Supabase DB (products, meli_tokens tables)
```

## OAuth 2.0 Authorization Flow

### Step 1 — Register Application

1. Go to `https://developers.mercadolivre.com.br/devcenter` → Create App.
2. Set redirect URI: `https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/meli-oauth-callback`.
3. Copy `client_id` and `client_secret`.

```bash
supabase secrets set MELI_CLIENT_ID={{BRAND_MELI_CLIENT_ID}}
supabase secrets set MELI_CLIENT_SECRET={{BRAND_MELI_CLIENT_SECRET}}
```

### Step 2 — Authorization Redirect

```
GET https://auth.mercadolibre.com.br/authorization
  ?response_type=code
  &client_id={{BRAND_MELI_CLIENT_ID}}
  &redirect_uri=https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/meli-oauth-callback
  &state={nonce}
```

### Step 3 — Token Exchange (meli-oauth-callback)

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
// Store tokens; ML access token TTL: 6 hours; refresh: ~6 months
```

### Step 4 — Deploy Functions

```bash
supabase functions deploy meli-oauth-callback
supabase functions deploy product-enrich
```

### Step 5 — Product Enrichment

The `product-enrich` function queries ML catalog by keyword or EAN to fill missing fields:

```bash
curl -X POST \
  https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/product-enrich \
  -H "Authorization: Bearer $SUPABASE_SERVICE_KEY" \
  -d '{"supabase_product_id": "uuid-here"}'
```

## Token TTL and Refresh

| Token | TTL | Refresh strategy |
|-------|-----|-----------------|
| Access token | 21600s (6h) | Proactive refresh at 5h 55m |
| Refresh token | ~180 days | Re-authorize if expired |

Add ML refresh to the shared `token-auto-refresh` cron or schedule separately:

```sql
select cron.schedule('meli-token-refresh', '55 5 * * *', ...);
```

## Interface

| Input | Type | Description |
|-------|------|-------------|
| `MELI_CLIENT_ID` | env secret | ML OAuth app client ID |
| `MELI_CLIENT_SECRET` | env secret | ML OAuth app client secret |
| `MELI_ACCESS_TOKEN` | DB | Current access token |

| Output | Description |
|--------|-------------|
| Enriched Supabase product rows | Title, description, images from ML |
| ML access token | Stored in `meli_tokens` table |

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_MELI_CLIENT_ID}}` | ML OAuth client ID env name |
| `{{BRAND_MELI_CLIENT_SECRET}}` | ML OAuth client secret env name |
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Supabase project for callback + DB |

## Related Artifacts

| Artifact | Kind | Role |
|----------|------|------|
| `ex_api_client_meli.md` | api_client | HTTP client spec for ML API |
| `ex_oauth_app_config_meli.md` | oauth_app_config | OAuth flow config |
| `ex_workflow_multi_marketplace_sync.md` | workflow | Multi-marketplace orchestration |
| `ex_research_pipeline_marketplace_scrap.md` | research_pipeline | Automated ML catalog audit |
