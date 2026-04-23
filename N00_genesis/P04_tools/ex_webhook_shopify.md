---
id: ex-webhook-shopify
kind: webhook
pillar: P04
title: Shopify Inbound Webhook Handler
version: 0.1.0
quality: 9.0
status: template
brand_placeholders:
  - BRAND_SHOPIFY_DOMAIN
  - BRAND_SHOPIFY_WEBHOOK_SECRET
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, shopify, webhook]
density_score: 1.0
related:
  - webhook-builder
  - bld_knowledge_card_webhook
  - p03_sp_webhook_builder
  - bld_architecture_webhook
  - bld_memory_webhook
  - p01_kc_webhook
  - kc_hotmart_api
  - bld_collaboration_webhook
  - bld_output_template_webhook
  - p04_webhook_NAME
---

# Shopify Inbound Webhook Handler

## Purpose
HMAC-validated edge function that receives Shopify topic notifications (`products/update`, `inventory_levels/update`, `orders/create`, `orders/paid`) and routes them to internal Supabase tables + downstream sync queues.

## When to use
- You need near-real-time mirroring of Shopify state into Supabase.
- Downstream systems (Bling ERP, ML, reporting warehouse) must react to catalog/inventory/order events.
- You want to avoid polling Shopify Admin API (rate-limit pressure).

## Interface
- Endpoint: `POST https://{{BRAND_SUPABASE_PROJECT_REF}}.functions.supabase.co/shopify-webhook-handler`
- Required headers: `X-Shopify-Topic`, `X-Shopify-Hmac-Sha256`, `X-Shopify-Shop-Domain`, `X-Shopify-Webhook-Id`.
- Body: JSON payload matching Shopify topic schema.
- Response: `200 OK` within 5s (Shopify timeout) or Shopify retries with exponential backoff.

## Brand variables used
- `{{BRAND_SHOPIFY_DOMAIN}}` -- expected shop domain for origin validation.
- `{{BRAND_SHOPIFY_WEBHOOK_SECRET}}` -- env var name holding HMAC shared secret.
- `{{BRAND_SUPABASE_PROJECT_REF}}` -- deploy target.

## HMAC validation (non-negotiable)
```ts
const raw = await req.text(); // MUST be raw body, not parsed
const given = req.headers.get("X-Shopify-Hmac-Sha256");
const expected = base64(hmacSha256(Deno.env.get("{{BRAND_SHOPIFY_WEBHOOK_SECRET}}")!, raw));
if (!timingSafeEqual(given, expected)) return new Response("invalid hmac", { status: 401 });
```
Reject in <1ms on failure -- never parse body first.

## Idempotency
- Dedup by `X-Shopify-Webhook-Id`; cache last 10k IDs in `webhook_inbox` table (TTL 48h).
- Duplicate ID -> return `200 OK` without reprocessing (Shopify retries are not errors).

## Topic routing
| Topic | Action |
|-------|--------|
| `products/update` | upsert `products` row, enqueue `product-sync-webhook` |
| `products/delete` | soft-delete (`deleted_at=now()`) |
| `inventory_levels/update` | update `inventory` row, trigger `inventory-reconcile` if delta > threshold |
| `orders/create` | insert `orders`, enqueue partner notifications |
| `orders/paid` | mark order paid, enqueue fulfillment + tax recording |

## Ordering guarantees
Shopify does NOT guarantee event order. Always compare `updated_at` in payload vs stored row; ignore stale events (`payload.updated_at < stored.updated_at`).

## Observability
Emit structured log `{topic, webhook_id, shop, ms, outcome}` on every invocation. Failed HMAC counts as `outcome=rejected` (critical alert if > 5/min).

## Related artifacts
- `ex_api_client_shopify.md` -- outbound counterpart.
- `ex_webhook_manager_shopify.md` -- registers/removes webhook subscriptions.
- `ex_notifier_webhook.md` -- downstream notification delivery.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[webhook-builder]] | related | 0.26 |
| [[bld_knowledge_card_webhook]] | downstream | 0.25 |
| [[p03_sp_webhook_builder]] | related | 0.24 |
| [[bld_architecture_webhook]] | related | 0.22 |
| [[bld_memory_webhook]] | downstream | 0.22 |
| [[p01_kc_webhook]] | upstream | 0.21 |
| [[kc_hotmart_api]] | upstream | 0.20 |
| [[bld_collaboration_webhook]] | related | 0.20 |
| [[bld_output_template_webhook]] | related | 0.18 |
| [[p04_webhook_NAME]] | sibling | 0.18 |
