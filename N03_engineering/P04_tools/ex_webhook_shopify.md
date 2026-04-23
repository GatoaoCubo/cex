---
id: ex_webhook_shopify
kind: webhook
pillar: P04
title: Shopify Webhook Handler
version: 0.1.0
quality: 8.3
status: template
brand_placeholders:
  - BRAND_SHOPIFY_DOMAIN
  - BRAND_SHOPIFY_WEBHOOK_SECRET
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, shopify, webhook]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_knowledge_card_webhook
  - webhook-builder
  - p01_kc_webhook
  - p03_sp_webhook_builder
  - bld_architecture_webhook
  - kc_hotmart_api
  - bld_output_template_webhook
  - bld_memory_webhook
  - bld_instruction_webhook
  - bld_examples_webhook
---

## Purpose

Inbound webhook handler for Shopify store events — validates HMAC-SHA256 signatures and processes `products/update`, `products/create`, `products/delete`, and `inventory_levels/update` payloads into the Supabase `products` table.

## When to Use

- Receiving real-time product change events from Shopify without polling.
- Keeping Supabase product data in sync within seconds of a Shopify admin action.
- Triggering downstream workflows (inventory reconciliation, SEO generation) on product events.

## Events

| Event Topic | Trigger Condition | Payload Fields |
|-------------|------------------|----------------|
| `products/update` | Any product field changed in Shopify admin | `id`, `title`, `handle`, `variants`, `images`, `status` |
| `products/create` | New product published in Shopify | Same as update |
| `products/delete` | Product deleted from Shopify | `id` only |
| `inventory_levels/update` | Inventory quantity changed at any location | `inventory_item_id`, `location_id`, `available` |

## Verification

| Field | Value |
|-------|-------|
| Method | `HMAC-SHA256` |
| Header | `X-Shopify-Hmac-Sha256` (base64-encoded) |
| Secret env | `{{BRAND_SHOPIFY_WEBHOOK_SECRET}}` |
| Algorithm | `HMAC(secret, rawBody, SHA256)` → base64 → compare constant-time |

```typescript
async function verifyShopifyHmac(req: Request, secret: string): Promise<boolean> {
  const hmacHeader = req.headers.get('X-Shopify-Hmac-Sha256') ?? '';
  const body = await req.arrayBuffer();
  const key = await crypto.subtle.importKey('raw', new TextEncoder().encode(secret), { name: 'HMAC', hash: 'SHA-256' }, false, ['sign']);
  const sig = await crypto.subtle.sign('HMAC', key, body);
  const computed = btoa(String.fromCharCode(...new Uint8Array(sig)));
  return computed === hmacHeader; // timing-safe comparison recommended
}
```

**Never process a webhook that fails HMAC validation.** Return `401` immediately.

## Retry and Delivery

| Field | Value |
|-------|-------|
| Direction | Inbound |
| Delivery guarantee | At-least-once (Shopify retries for 48h on non-2xx) |
| Idempotency key | `X-Shopify-Webhook-Id` header |
| Timeout (your endpoint) | Must respond within **5 seconds**; heavy work goes async |
| Retry schedule | Shopify: 19 attempts over 48h (exponential) |

**Pattern**: validate → acknowledge (200) → process async.

```typescript
// Acknowledge immediately, process in background
Deno.serve(async (req) => {
  const verified = await verifyShopifyHmac(req.clone(), Deno.env.get('SHOPIFY_WEBHOOK_SECRET')!);
  if (!verified) return new Response('Unauthorized', { status: 401 });
  const topic = req.headers.get('X-Shopify-Topic') ?? '';
  const id = req.headers.get('X-Shopify-Webhook-Id') ?? '';
  // Idempotency: check if id already processed
  EdgeRuntime.waitUntil(processEvent(topic, await req.json(), id));
  return new Response('OK', { status: 200 });
});
```

## Interface

| Input | Type | Description |
|-------|------|-------------|
| `X-Shopify-Hmac-Sha256` | header | HMAC-SHA256 signature (base64) |
| `X-Shopify-Topic` | header | Event topic string |
| `X-Shopify-Webhook-Id` | header | Unique delivery ID for idempotency |
| Request body | JSON | Event payload |

| Output | Description |
|--------|-------------|
| `200 OK` | Accepted (always if verified) |
| `401` | HMAC verification failed |
| Supabase upsert | Product row updated/inserted/deleted |

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_SHOPIFY_DOMAIN}}` | Source store domain |
| `{{BRAND_SHOPIFY_WEBHOOK_SECRET}}` | HMAC validation secret (env name) |
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Target Supabase project |

## Example Webhook Registration

```bash
curl -X POST \
  https://{{BRAND_SHOPIFY_DOMAIN}}/admin/api/2024-01/webhooks.json \
  -H "X-Shopify-Access-Token: $SHOPIFY_ADMIN_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{
    "webhook": {
      "topic": "products/update",
      "address": "https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/shopify-webhook-handler",
      "format": "json"
    }
  }'
```


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_webhook]] | downstream | 0.35 |
| [[webhook-builder]] | related | 0.31 |
| [[p01_kc_webhook]] | upstream | 0.30 |
| [[p03_sp_webhook_builder]] | related | 0.28 |
| [[bld_architecture_webhook]] | related | 0.27 |
| [[kc_hotmart_api]] | upstream | 0.27 |
| [[bld_output_template_webhook]] | related | 0.25 |
| [[bld_memory_webhook]] | downstream | 0.23 |
| [[bld_instruction_webhook]] | upstream | 0.22 |
| [[bld_examples_webhook]] | related | 0.21 |
