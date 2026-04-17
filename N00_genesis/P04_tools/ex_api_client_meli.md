---
id: ex-api-client-meli
kind: api_client
pillar: P04
title: Mercado Livre API Client
version: 0.1.0
quality: 9.0
status: template
brand_placeholders:
  - BRAND_MELI_API_URL
  - BRAND_MELI_CLIENT_ID
  - BRAND_MELI_CLIENT_SECRET
  - BRAND_MELI_ACCESS_TOKEN
  - BRAND_MELI_USER_ID
tags: [commerce, template, distillation, mercado_livre, api_client]
density_score: 1.0
---

# Mercado Livre API Client

## Purpose
Typed client for Mercado Livre (ML) / Mercado Libre public API. Covers listings (`items`), stock (`multiget`), orders (`orders`), and product enrichment (`products` catalog) for pulling missing attributes into Supabase.

## When to use
- Brand sells on ML and needs catalog sync parity with Shopify.
- Product data enrichment: ML has richer attributes (GTIN, brand, category) than some Shopify imports.
- Order pipeline: receive ML orders and mirror into the same `orders` table the storefront uses.

## Interface
- Base URL: `{{BRAND_MELI_API_URL}}` (default `https://api.mercadolibre.com`).
- Auth: `Authorization: Bearer <access_token>` -- 6-hour lifetime, 6-month refresh window.
- User-scoped endpoints require `{{BRAND_MELI_USER_ID}}` (numeric seller ID) in the path.

## Brand variables used
- `{{BRAND_MELI_API_URL}}` -- pinned for sandbox/prod swap.
- `{{BRAND_MELI_CLIENT_ID}}`, `{{BRAND_MELI_CLIENT_SECRET}}` -- OAuth app.
- `{{BRAND_MELI_ACCESS_TOKEN}}` -- env var of current token (token-manager rewrites).
- `{{BRAND_MELI_USER_ID}}` -- seller identifier on ML.

## Rate limits
- 10000 req/hour per app, burst 200 req/min. Bucket per endpoint family, not global.
- Search endpoints (`/sites/MLB/search`) have a separate lower limit (~1000/hr).
- Client MUST read `X-RateLimit-*` response headers and back off pre-emptively at 80% consumption.

## Refresh contract
Same shape as Bling (6h access / long-lived refresh). Differences:
- ML refresh_token ROTATES every exchange; the OLD one is invalidated immediately.
- If a refresh fails with `invalid_grant`, the user MUST re-authorize -- no automatic recovery.
- Persist via token-manager under key `meli`.

## Common operations
| Op | Endpoint |
|----|----------|
| Get item | `GET /items/{id}` |
| Batch get (up to 20 ids) | `GET /items?ids=MLB1,MLB2,...` |
| List seller items | `GET /users/{{BRAND_MELI_USER_ID}}/items/search` |
| Update stock | `PUT /items/{id}` with `{available_quantity}` |
| List orders (recent) | `GET /orders/search?seller={{BRAND_MELI_USER_ID}}&order.date_created.from=...` |
| Product enrichment | `GET /products/{catalog_product_id}` |

## Enrichment pattern (primary use case)
When a Supabase product lacks GTIN/brand/category:
1. Search ML catalog: `GET /sites/MLB/search?q=<title>&limit=1`.
2. Take top hit's `catalog_product_id`, fetch product detail.
3. Map `attributes[]` -> our schema; merge only missing fields (never overwrite brand-curated data).
4. Persist with `source=meli_enrichment` audit row.

## Related artifacts
- `ex_oauth_app_config_meli.md`
- `ex_integration_guide_meli.md`
- `ex_api_client_meli_enrich.md` (referenced, not in this wave)
