---
id: ex-integration-guide-meli
kind: integration_guide
8f: F6_produce
pillar: P04
title: Mercado Livre Integration Guide
version: 0.1.0
quality: 8.8
status: template
brand_placeholders:
  - BRAND_NAME
  - BRAND_MELI_CLIENT_ID
  - BRAND_MELI_CLIENT_SECRET
  - BRAND_MELI_USER_ID
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, mercado_livre, integration_guide]
density_score: 0.98
related:
  - bld_knowledge_card_oauth_app_config
  - oauth-app-config-builder
  - bld_tools_supabase_data_layer
  - kc_oauth_app_config
  - p03_sp_oauth_app_config_builder
  - p01_kc_supabase_cli
  - bld_knowledge_card_thinking_config
  - p03_sp_brand_nucleus
  - p02_agent_commercial_nucleus
  - bld_output_template_oauth_app_config
---

# Mercado Livre Integration Guide

## Purpose
Connect {{BRAND_NAME}} to Mercado Livre for dual-channel selling, product enrichment (category/brand/GTIN), and unified order pipeline. ML is a higher-volume / lower-margin channel than Shopify; keep SKUs identical so reporting stays clean.

## When to use
- Brand sells or plans to sell on ML in addition to Shopify.
- Existing Supabase products have attribute gaps that ML catalog can fill.
- Multi-country sellers (MLB + MLA + MLM) needing per-site token management.

## Prerequisites
- Mercado Livre seller account in good standing.
- ML dev app created at `https://developers.mercadolivre.com.br/devcenter`.
- Supabase tables: `meli_tokens`, `products`, `orders_meli`, `meli_enrichment_log`.

## Architecture

```
Mercado Livre
  |-- OAuth <-- [meli-oauth-callback]
  |-- Notifications push -> [meli-notifications-handler] (TBD)
  |-- REST <-- [product-enrich]         (enrich missing Supabase products)
  |-- REST <-- [meli-order-poll]        (cron fallback to notifications)
  |
  +-- Token refresh <-- [token-auto-refresh] -- mutex per user_id
```

## Brand variables used
All in frontmatter. `{{BRAND_MELI_USER_ID}}` is captured during OAuth callback and stored with tokens; it's not a pre-configured env var.

## Setup steps
1. **Create ML dev app** -- set redirect URI to `https://{{BRAND_DOMAIN}}/oauth/meli/callback` exactly.
2. **Request API access** -- ML approval can take 24-72h; apps start in `pending` state.
3. **Connect seller account** -- UI "Connect ML" button redirects to authorize URL; on approval, callback stores tokens + `user_id`.
4. **Deploy edge functions**:
   ```bash
   supabase functions deploy meli-oauth-callback
   supabase functions deploy product-enrich
   ```
5. **Schedule refresher** -- reuse `token-auto-refresh` with mutex per-brand; ML refresh races corrupt tokens.
6. **Enrichment sweep** -- run `product-enrich` in `dry_run=true` on all Supabase products with missing `gtin` OR `brand` OR `category_id`; review output before applying.

## Verification checklist
- [ ] `GET /users/{{BRAND_MELI_USER_ID}}` returns 200 with stored token.
- [ ] Authorize -> callback -> user lands at `/admin/integracoes?meli=ok` and token row exists.
- [ ] Force-expire token -> next API call triggers refresh; new `refresh_token` persisted; old one errors on reuse.
- [ ] Enrichment dry-run produces a human-readable diff; apply only after product manager review.

## Quirks + gotchas
- Refresh token rotation is destructive: always refresh in a single-writer mutex.
- Different regions (MLB/MLA/MLM) have separate APIs; if brand expands, provision separate token rows keyed by `site_id`.
- ML notifications use long-poll subscriptions -- outside scope of this guide; start with cron poll if traffic is low.
- Stock pushes to ML are eventually consistent: `available_quantity` update appears in listings within ~60s.

## Related artifacts
- `ex_api_client_meli.md`
- `ex_oauth_app_config_meli.md`
- `ex_workflow_multi_marketplace_sync.md`

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_oauth_app_config]] | upstream | 0.30 |
| [[oauth-app-config-builder]] | downstream | 0.28 |
| [[bld_tools_supabase_data_layer]] | related | 0.27 |
| [[kc_oauth_app_config]] | upstream | 0.25 |
| [[p03_sp_oauth_app_config_builder]] | upstream | 0.23 |
| [[p01_kc_supabase_cli]] | upstream | 0.22 |
| [[bld_knowledge_card_thinking_config]] | upstream | 0.21 |
| [[p03_sp_brand_nucleus]] | upstream | 0.19 |
| [[p02_agent_commercial_nucleus]] | upstream | 0.19 |
| [[bld_output_template_oauth_app_config]] | downstream | 0.19 |
