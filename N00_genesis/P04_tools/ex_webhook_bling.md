---
id: ex-webhook-bling
kind: webhook
pillar: P04
title: Bling ERP Webhook Handler
version: 0.1.0
quality: 8.9
status: template
brand_placeholders:
  - BRAND_BLING_WEBHOOK_SECRET
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, bling, webhook]
density_score: 1.0
---

# Bling ERP Webhook Handler

## Purpose
Receives Bling outbound notifications (`produto.alterado`, `estoque.alterado`, `pedido.venda.alterado`, `nfe.emitida`) and mirrors them into Supabase within seconds. Replaces periodic polling, which would exhaust the 120k-req/day quota within hours.

## When to use
- Active Bling ERP integration where inventory and fiscal state must be near-real-time.
- Replacing cron-based pull with event-driven push.
- Reducing Bling API quota consumption to <20% of daily budget.

## Interface
- Endpoint: `POST https://{{BRAND_SUPABASE_PROJECT_REF}}.functions.supabase.co/bling-webhook`
- Body: Bling JSON `{ evento, dados: {...} }`.
- Auth: HMAC header `X-Bling-Signature` (Bling-controlled key pair) OR shared-secret header `X-Webhook-Token` for legacy notifications.

## Brand variables used
- `{{BRAND_BLING_WEBHOOK_SECRET}}` -- shared secret or HMAC key.
- `{{BRAND_SUPABASE_PROJECT_REF}}` -- deploy target.

## Signature verification
Bling v3 uses HMAC-SHA256 over the raw body with the configured webhook key:
```ts
const raw = await req.text();
const sig = req.headers.get("X-Bling-Signature");
const expected = hex(hmacSha256(Deno.env.get("{{BRAND_BLING_WEBHOOK_SECRET}}")!, raw));
if (!timingSafeEqual(sig, expected)) return new Response("invalid", { status: 401 });
```

## Event routing
| Event | Target table | Downstream |
|-------|--------------|------------|
| `produto.incluido` / `produto.alterado` | `products` (source=bling) | enqueue reconcile vs Shopify |
| `produto.excluido` | soft-delete row | alert ops -- deletions rare |
| `estoque.alterado` | `inventory` | trigger `inventory-reconcile` if delta > 5 units |
| `pedido.venda.alterado` | `orders_bling` | sync status to Shopify order |
| `nfe.emitida` | `invoices` | attach PDF url, notify customer |

## Idempotency
Bling MAY send duplicate events during retries. Dedup by `(evento, dados.id, dados.alteradoEm)` tuple in `webhook_inbox_bling` with 7-day TTL.

## Ack timing
Bling treats any non-2xx or a timeout >8s as failure and retries up to 5 times with backoff. Keep handler work under 3s: persist raw event + enqueue async job, then return 200 immediately. Do NOT process synchronously for anything that calls out to Shopify/ML.

## Observability
Emit metric `bling.webhook.{event}.count`; alert if ingress drops to 0 for >15 min during business hours (signal: Bling paused deliveries due to past failures).

## Related artifacts
- `ex_api_client_bling.md`
- `ex_oauth_app_config_bling.md`
- `ex_integration_guide_bling.md`
