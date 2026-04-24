---
id: ex_api_client_shopify
kind: api_client
8f: F5_call
pillar: P04
title: Shopify Admin API Client
version: 0.1.0
quality: 8.3
status: template
brand_placeholders:
  - BRAND_SHOPIFY_DOMAIN
  - BRAND_SHOPIFY_API_VERSION
tags: [commerce, template, distillation, shopify, api_client]
density_score: 1.0
updated: "2026-04-17"
related:
  - kc_api_reference
  - kc_integration_guide
  - p01_kc_llm_output_parsing_validation
  - bld_knowledge_card_client
  - bld_tools_social_publisher
  - n06_api_access_pricing
  - kc_hotmart_api
  - p01_kc_canva_connect_api
  - p04_webhook_NAME
  - p01_kc_supabase_edge_functions
---

## Purpose

HTTP client specification for Shopify Admin REST API — covers product CRUD, inventory management, and bulk sync operations against `{{BRAND_SHOPIFY_DOMAIN}}`.

## When to Use

- Pulling the full product catalog from Shopify into Supabase.
- Pushing product title/SEO field updates from Supabase back to Shopify.
- Syncing a single product by ID in response to a DB event.

## Base Configuration

| Field | Value |
|-------|-------|
| `base_url` | `https://{{BRAND_SHOPIFY_DOMAIN}}/admin/api/{{BRAND_SHOPIFY_API_VERSION}}` |
| `auth_strategy` | `api_key` (header: `X-Shopify-Access-Token`) |
| `content_type` | `application/json` |
| `timeout_ms` | `30000` |
| `max_retries` | `3` |
| `backoff` | exponential, base 1s, cap 16s |

## Endpoints

| Method | Path | Params | Returns | Error Codes |
|--------|------|--------|---------|-------------|
| GET | `/products.json` | `limit`, `page_info`, `fields` | `products[]` | 401, 429, 503 |
| GET | `/products/{id}.json` | `fields` | `product` | 404, 401 |
| PUT | `/products/{id}.json` | body: product object | `product` | 400, 422, 429 |
| GET | `/inventory_levels.json` | `location_ids`, `limit` | `inventory_levels[]` | 401 |
| POST | `/inventory_levels/set.json` | body: inventory level | `inventory_level` | 400, 422 |
| GET | `/webhooks.json` | `topic`, `limit` | `webhooks[]` | 401 |
| POST | `/webhooks.json` | body: webhook object | `webhook` | 422 |
| DELETE | `/webhooks/{id}.json` | — | 200 OK | 404 |

## Rate Limiting

| Tier | Limit | Reset |
|------|-------|-------|
| REST (Standard) | 40 req/app/store/s (leaky bucket) | Continuous |
| REST (Plus) | 80 req/app/store/s | Continuous |
| Bulk operations | 1 concurrent query | Per operation |

Headers returned: `X-Shopify-Shop-Api-Call-Limit: used/total`.

**Retry strategy**: On `429`, read `Retry-After` header (seconds). On `503`, exponential backoff starting 1s.

## Pagination

Pattern: **cursor-based** via `page_info` token.

```
GET /products.json?limit=250
→ Link: <...page_info=abc123>; rel="next"
GET /products.json?limit=250&page_info=abc123
→ Link: <...page_info=def456>; rel="next"
```

Iterate until `Link` header has no `rel="next"`.

## Error Handling

| HTTP Status | Meaning | Action |
|-------------|---------|--------|
| `200` | Success | Parse body |
| `400` | Bad request | Log, do not retry |
| `401` | Unauthorized | Alert; check token scope |
| `404` | Not found | Skip; may have been deleted |
| `422` | Unprocessable | Log validation errors; do not retry |
| `429` | Rate limited | Back off per `Retry-After` |
| `503` | Shopify unavailable | Exponential retry (max 3) |

## Known Issues

- **Double-UTF-8 encoding**: Some product titles arrive double-encoded (e.g., `PortÃ£o` instead of `Portão`). Decode twice at ingestion; see `ex_validator_inventory_invariants.md`.
- **Field filtering**: Always use `?fields=id,title,variants,images` to avoid large payloads. Full product objects can be 50KB+.

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_SHOPIFY_DOMAIN}}` | Store domain (e.g., `my-brand.myshopify.com`) |
| `{{BRAND_SHOPIFY_API_VERSION}}` | API version (e.g., `2024-01`) |

## Example Usage

```typescript
// Fetch all products with cursor pagination
async function fetchAllShopifyProducts(): Promise<Product[]> {
  const base = `https://${Deno.env.get('SHOPIFY_STORE_DOMAIN')}/admin/api/${Deno.env.get('SHOPIFY_API_VERSION')}`;
  const headers = { 'X-Shopify-Access-Token': Deno.env.get('SHOPIFY_ADMIN_TOKEN')! };
  let url = `${base}/products.json?limit=250&fields=id,title,handle,variants,images,status`;
  const products: Product[] = [];

  while (url) {
    const res = await fetch(url, { headers });
    if (res.status === 429) {
      const wait = parseInt(res.headers.get('Retry-After') ?? '2');
      await new Promise(r => setTimeout(r, wait * 1000));
      continue;
    }
    const data = await res.json();
    products.push(...data.products);
    const link = res.headers.get('Link') ?? '';
    const match = link.match(/<([^>]+)>; rel="next"/);
    url = match ? match[1] : '';
  }
  return products;
}
```


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kc_api_reference]] | upstream | 0.27 |
| [[kc_integration_guide]] | upstream | 0.22 |
| [[p01_kc_llm_output_parsing_validation]] | upstream | 0.22 |
| [[bld_knowledge_card_client]] | upstream | 0.21 |
| [[bld_tools_social_publisher]] | related | 0.20 |
| [[n06_api_access_pricing]] | downstream | 0.19 |
| [[kc_hotmart_api]] | upstream | 0.19 |
| [[p01_kc_canva_connect_api]] | upstream | 0.19 |
| [[p04_webhook_NAME]] | related | 0.19 |
| [[p01_kc_supabase_edge_functions]] | upstream | 0.18 |
