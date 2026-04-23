---
id: ex_oauth_app_config_shopify
kind: oauth_app_config
pillar: P09
title: Shopify OAuth App Configuration
version: 0.1.0
quality: 8.4
status: template
brand_placeholders:
  - BRAND_SHOPIFY_DOMAIN
  - BRAND_SHOPIFY_API_VERSION
tags: [commerce, template, distillation, shopify, oauth]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_knowledge_card_oauth_app_config
  - bld_collaboration_oauth_app_config
  - kc_oauth_app_config
  - bld_output_template_oauth_app_config
  - oauth-app-config-builder
  - bld_schema_oauth_app_config
  - p09_qg_oauth_app_config
  - p01_kc_supabase_edge_functions
  - p03_sp_oauth_app_config_builder
  - p01_kc_secret_config
---

## Purpose

OAuth 2.0 app configuration for Shopify Admin API access — defines scopes, token storage, and the authorization flow for connecting `{{BRAND_SHOPIFY_DOMAIN}}` to backend services.

## When to Use

- First-time Shopify app installation requiring merchant authorization.
- Rotating Admin API tokens without re-installing the app.
- Documenting required OAuth scopes for security reviews and onboarding.

## App Configuration

| Field | Value |
|-------|-------|
| App type | Custom app (private) |
| API access | Admin API |
| Auth method | Custom app token (not OAuth code flow for private apps) |
| Token storage | Supabase secrets / `.env` |
| Token rotation | Manual (Shopify does not auto-rotate custom app tokens) |

> **Note**: For **public Shopify apps** (multi-merchant), use the full OAuth 2.0 authorization code flow below. For single-store private apps, skip to Token Storage.

## OAuth 2.0 Flow (Public Apps)

```
1. Redirect merchant to:
   https://{{BRAND_SHOPIFY_DOMAIN}}/admin/oauth/authorize
     ?client_id={SHOPIFY_CLIENT_ID}
     &scope={SCOPES}
     &redirect_uri={REDIRECT_URI}
     &state={NONCE}

2. Merchant approves → Shopify redirects to REDIRECT_URI with ?code=...&state=...

3. Validate state == nonce (CSRF check).

4. Exchange code for access token:
   POST https://{{BRAND_SHOPIFY_DOMAIN}}/admin/oauth/access_token
   Body: { client_id, client_secret, code }
   Response: { access_token, scope }

5. Store access_token in Supabase secrets.
```

## Required OAuth Scopes

| Scope | Permission |
|-------|-----------|
| `read_products` | Read product catalog |
| `write_products` | Create/update products |
| `read_inventory` | Read inventory levels |
| `write_inventory` | Update inventory quantities |
| `read_orders` | Read order data (optional, for reporting) |

Minimum required: `read_products, write_products, read_inventory, write_inventory`.

## Token Storage

| Token | Env Var | Storage |
|-------|---------|---------|
| Admin API token | `SHOPIFY_ADMIN_TOKEN` | Supabase Edge secrets |
| Client ID | `SHOPIFY_CLIENT_ID` | Supabase Edge secrets |
| Client secret | `SHOPIFY_CLIENT_SECRET` | Supabase Edge secrets |

```bash
supabase secrets set SHOPIFY_ADMIN_TOKEN=shpat_...
supabase secrets set SHOPIFY_CLIENT_ID=...
supabase secrets set SHOPIFY_CLIENT_SECRET=...
```

## Interface

| Input | Type | Description |
|-------|------|-------------|
| `SHOPIFY_ADMIN_TOKEN` | env secret | Custom app Admin API token |
| `SHOPIFY_CLIENT_ID` | env secret | OAuth app client ID |
| `SHOPIFY_CLIENT_SECRET` | env secret | OAuth app client secret |

| Output | Description |
|--------|-------------|
| Authenticated Shopify API calls | Via `X-Shopify-Access-Token` header |
| Merchant authorization | Completed OAuth flow |

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_SHOPIFY_DOMAIN}}` | Store's myshopify.com domain |
| `{{BRAND_SHOPIFY_API_VERSION}}` | Admin API version string |

## Example Usage

```typescript
// Shopify authenticated request
const shopifyFetch = (path: string, opts: RequestInit = {}) =>
  fetch(
    `https://${Deno.env.get('SHOPIFY_STORE_DOMAIN')}/admin/api/${Deno.env.get('SHOPIFY_API_VERSION')}${path}`,
    {
      ...opts,
      headers: {
        'X-Shopify-Access-Token': Deno.env.get('SHOPIFY_ADMIN_TOKEN')!,
        'Content-Type': 'application/json',
        ...(opts.headers ?? {}),
      },
    }
  );
```


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_oauth_app_config]] | upstream | 0.37 |
| [[bld_collaboration_oauth_app_config]] | downstream | 0.32 |
| [[kc_oauth_app_config]] | upstream | 0.32 |
| [[bld_output_template_oauth_app_config]] | upstream | 0.32 |
| [[oauth-app-config-builder]] | related | 0.30 |
| [[bld_schema_oauth_app_config]] | upstream | 0.27 |
| [[p09_qg_oauth_app_config]] | downstream | 0.27 |
| [[p01_kc_supabase_edge_functions]] | upstream | 0.26 |
| [[p03_sp_oauth_app_config_builder]] | upstream | 0.25 |
| [[p01_kc_secret_config]] | related | 0.24 |
