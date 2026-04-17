---
id: ex-oauth-app-config-shopify
kind: oauth_app_config
pillar: P04
title: Shopify OAuth App Config
version: 0.1.0
quality: null
status: template
brand_placeholders:
  - BRAND_SHOPIFY_APP_CLIENT_ID
  - BRAND_SHOPIFY_APP_CLIENT_SECRET
  - BRAND_SHOPIFY_STORE_DOMAIN
  - BRAND_DOMAIN
tags: [commerce, template, distillation, shopify, oauth]
---

# Shopify OAuth App Config

## Purpose
OAuth 2.0 authorization-code flow configuration for a custom Shopify app, used to obtain an offline `admin_access_token` with explicit scopes. Only needed for public/distributable apps; custom apps installed on a single store can skip OAuth and use an Admin API access token directly.

## When to use
- Multi-merchant app serving several stores.
- Replacing long-lived private app tokens (deprecated by Shopify for new apps).
- You need embedded-app session tokens (App Bridge) on top of a persisted offline token.

## Interface
- Install URL: `https://{{BRAND_SHOPIFY_STORE_DOMAIN}}/admin/oauth/authorize?client_id={{BRAND_SHOPIFY_APP_CLIENT_ID}}&scope=<scopes>&redirect_uri=<redirect>&state=<nonce>`
- Callback: `https://{{BRAND_DOMAIN}}/oauth/shopify/callback` (must match exactly).
- Token endpoint: `POST https://{{BRAND_SHOPIFY_STORE_DOMAIN}}/admin/oauth/access_token` with `{client_id, client_secret, code}`.

## Brand variables used
- `{{BRAND_SHOPIFY_APP_CLIENT_ID}}` -- public, safe to ship in client code.
- `{{BRAND_SHOPIFY_APP_CLIENT_SECRET}}` -- SECRET, server-side only.
- `{{BRAND_SHOPIFY_STORE_DOMAIN}}` -- `brand.myshopify.com` for single-store; template placeholder `{shop}` for multi-tenant.
- `{{BRAND_DOMAIN}}` -- app's canonical domain for redirect_uri.

## Required scopes (minimal, justify each)
| Scope | Justification |
|-------|---------------|
| `read_products` | catalog mirror to Supabase |
| `write_products` | title/SEO push back |
| `read_inventory` | stock reconcile |
| `write_inventory` | auto-correct reconcile |
| `read_orders` | order pipeline |
| `read_customers` | optional, only if CRM needs it |

Unused scopes = automatic rejection in Shopify app review. Keep list tight.

## State + PKCE
- Generate cryptographically random `state`; store in signed cookie or Supabase row keyed by session; verify on callback.
- PKCE is NOT supported by Shopify OAuth (2025). Rely on `state` + HMAC of callback query params.

## Callback HMAC verification
Shopify signs the callback query string. Before exchanging `code` for token:
```ts
const { hmac, ...rest } = parseQuery(url);
const msg = Object.entries(rest).sort().map(([k,v])=>`${k}=${v}`).join("&");
const valid = timingSafeEqual(hmac, hex(hmacSha256(CLIENT_SECRET, msg)));
if (!valid) throw new Error("callback tampered");
```

## Token storage
Store `access_token` + `shop_domain` + `scope` + `installed_at` in `shopify_installations` table. Tokens do NOT expire but SHOULD be invalidated when scope changes -- re-run OAuth on scope upgrade.

## Uninstall webhook
Always register `app/uninstalled`; on receipt delete the installation row + purge related data within 48h (GDPR/LGPD compliance).

## Related artifacts
- `ex_api_client_shopify.md` -- consumes the resulting token.
- `ex_integration_guide_shopify.md` -- end-to-end setup.
