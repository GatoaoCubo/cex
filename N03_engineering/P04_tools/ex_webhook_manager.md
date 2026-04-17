---
id: ex_webhook_manager
kind: webhook
pillar: P04
title: Shopify Webhook Manager
version: 0.1.0
quality: 8.0
status: template
brand_placeholders:
  - BRAND_SHOPIFY_DOMAIN
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, shopify, webhook, manager]
density_score: 1.0
updated: "2026-04-17"
---

## Purpose

CRUD management tool for Shopify webhook subscriptions — lists, registers, tests, and removes webhooks via Shopify Admin API, ensuring required product sync hooks are always active.

## When to Use

- Initial setup: registering the required webhook topics for a new Shopify store.
- Maintenance: verifying all required webhooks are still registered after app reinstall.
- Debugging: testing webhook delivery by triggering a manual test event.
- Cleanup: removing stale or duplicate webhook subscriptions.

## Operations

| Operation | Method | Endpoint | Description |
|-----------|--------|----------|-------------|
| List | GET | `/webhooks.json` | Retrieve all registered webhooks |
| Setup | POST | `/webhooks.json` | Register a new webhook subscription |
| Delete | DELETE | `/webhooks/{id}.json` | Remove a webhook by ID |
| Clear | DELETE (bulk) | `/webhooks/{id}.json` × N | Remove all managed webhooks |
| Test | POST | `/webhooks/{id}/test.json` | Send a test event (if supported) |

## Required Webhooks (Minimum Set)

| Topic | Purpose |
|-------|---------|
| `products/update` | Sync product changes to Supabase |
| `products/create` | Add new Shopify products to Supabase |
| `products/delete` | Remove deleted products from Supabase |
| `inventory_levels/update` | Sync stock quantity changes |

## Edge Function Interface

```typescript
// GET /webhook-manager?action=list
// GET /webhook-manager?action=setup
// GET /webhook-manager?action=clear
// GET /webhook-manager?action=test&id={webhook_id}
```

### Setup Action — Auto-registers missing webhooks

```typescript
const REQUIRED_TOPICS = [
  'products/update', 'products/create', 'products/delete', 'inventory_levels/update',
];

async function setupWebhooks(existingWebhooks: Webhook[]) {
  const existingTopics = new Set(existingWebhooks.map(w => w.topic));
  const callbackBase = `https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1`;

  for (const topic of REQUIRED_TOPICS) {
    if (existingTopics.has(topic)) continue;
    await shopifyFetch('/webhooks.json', {
      method: 'POST',
      body: JSON.stringify({
        webhook: { topic, address: `${callbackBase}/shopify-webhook-handler`, format: 'json' },
      }),
    });
  }
}
```

## Verification (Direction: Outbound Management)

This artifact manages webhooks — it does not receive them. The inbound handler is `ex_webhook_shopify.md`.

For the management endpoint itself:
- Authenticate via Supabase `Authorization: Bearer {SERVICE_KEY}` — not public.
- HMAC verification not applicable (outbound management, not inbound events).

## Retry and Delivery

| Field | Value |
|-------|-------|
| Direction | Outbound (management calls to Shopify Admin API) |
| Auth | `X-Shopify-Access-Token` on all calls |
| Idempotency | Check existing webhooks before creating; skip if topic exists |
| Rate limits | Subject to Shopify Admin API limits (40 req/s) |

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_SHOPIFY_DOMAIN}}` | Store to manage webhooks for |
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Callback base URL for registered webhooks |

## Example Response (List)

```json
{
  "webhooks": [
    {
      "id": 123456789,
      "topic": "products/update",
      "address": "https://{{BRAND_SUPABASE_PROJECT_REF}}.supabase.co/functions/v1/shopify-webhook-handler",
      "format": "json",
      "created_at": "2026-01-15T10:00:00-05:00"
    }
  ]
}
```

## Related Artifacts

| Artifact | Kind | Role |
|----------|------|------|
| `ex_webhook_shopify.md` | webhook | Inbound event handler for registered webhooks |
| `ex_notifier_webhook.md` | notifier | Delivery confirmation and alert system |
| `ex_api_client_shopify.md` | api_client | HTTP client used by this manager |
| `ex_integration_guide_shopify.md` | integration_guide | Full Shopify setup context |
