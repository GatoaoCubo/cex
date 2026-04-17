---
id: ex_api_client_meli
kind: api_client
pillar: P04
title: Mercado Livre API Client
version: 0.1.0
quality: 8.0
status: template
brand_placeholders:
  - BRAND_MELI_CLIENT_ID
tags: [commerce, template, distillation, mercadolivre, meli, api_client]
density_score: 1.0
updated: "2026-04-17"
---

## Purpose

HTTP client specification for Mercado Livre (MLB) REST API — covers product catalog search, item detail retrieval, and product enrichment operations with OAuth 2.0 bearer token authentication.

## When to Use

- Querying ML catalog to enrich Supabase product records with missing titles, descriptions, or images.
- Checking ML item availability or pricing for competitive reference.
- Pulling product attributes from ML's structured catalog (category-specific fields).

## Base Configuration

| Field | Value |
|-------|-------|
| `base_url` | `https://api.mercadolibre.com` |
| `auth_strategy` | Bearer token (OAuth 2.0) |
| `auth_header` | `Authorization: Bearer {access_token}` |
| `content_type` | `application/json` |
| `timeout_ms` | `15000` |
| `max_retries` | `3` |
| `backoff` | exponential, base 1s, cap 16s |
| `site_id` | `MLB` (Brazil) |
| `token_source` | `meli_tokens` table in Supabase |

## Endpoints

| Method | Path | Params | Returns | Error Codes |
|--------|------|--------|---------|-------------|
| GET | `/sites/MLB/search` | `q`, `limit`, `offset`, `category` | `results[]` | 400, 429 |
| GET | `/items/{item_id}` | — | Item detail | 404, 401 |
| GET | `/items` | `ids` (comma-separated, max 20) | `body[]` (multi-get) | 400 |
| GET | `/categories/{category_id}` | — | Category + attributes | 404 |
| GET | `/sites/MLB/listing_types` | — | Listing type list | 401 |
| GET | `/currency_conversions/search` | `from`, `to` | Rate | 400 |

## Rate Limiting

| Limit | Window | Notes |
|-------|--------|-------|
| 10 req/s | Per access token | Default quota |
| 500 req/day | Free tier | Varies by app permissions |

On `429`: back off 2s; if `Retry-After` header present, use it.

## Pagination

Pattern: **offset-based**.

```
GET /sites/MLB/search?q=ração gato&limit=50&offset=0
GET /sites/MLB/search?q=ração gato&limit=50&offset=50
...until results.length < limit
```

Max `limit` per call: 50 (search endpoint).

## Error Handling

| HTTP Status | Meaning | Action |
|-------------|---------|--------|
| `200` | Success | Parse body |
| `400` | Bad request / invalid params | Log; do not retry |
| `401` | Token expired | Refresh token; retry once |
| `403` | Forbidden scope | Check app scopes; escalate |
| `404` | Item not found / deactivated | Skip; log |
| `429` | Rate limited | Exponential back off |
| `500` | ML server error | Retry (max 3) |

## Usage Pattern: Product Enrichment

```typescript
async function enrichFromMeli(supabaseProduct: Product): Promise<Partial<Product>> {
  const token = await getValidMeliToken();
  // Search by EAN or product name
  const query = supabaseProduct.ean ?? supabaseProduct.title;
  const res = await fetch(
    `https://api.mercadolibre.com/sites/MLB/search?q=${encodeURIComponent(query)}&limit=5`,
    { headers: { Authorization: `Bearer ${token}` } }
  );
  const { results } = await res.json();
  if (!results.length) return {};
  const best = results[0];
  // Fetch full detail
  const detail = await fetch(`https://api.mercadolibre.com/items/${best.id}`,
    { headers: { Authorization: `Bearer ${token}` } });
  const item = await detail.json();
  return { meli_id: item.id, description: item.plain_text, meli_price: item.price };
}
```

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_MELI_CLIENT_ID}}` | ML OAuth app client ID (for token management) |

## Related Artifacts

| Artifact | Kind | Role |
|----------|------|------|
| `ex_integration_guide_meli.md` | integration_guide | Full setup guide |
| `ex_oauth_app_config_meli.md` | oauth_app_config | OAuth token management |
| `ex_research_pipeline_marketplace_scrap.md` | research_pipeline | Automated ML catalog audit |
