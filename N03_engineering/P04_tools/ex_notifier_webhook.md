---
id: ex_notifier_webhook
kind: notifier
pillar: P04
title: Webhook Delivery Notifier
version: 0.1.0
quality: null
status: template
brand_placeholders:
  - BRAND_SUPPORT_EMAIL
  - BRAND_SUPABASE_PROJECT_REF
tags: [commerce, template, distillation, notifier, webhook, alerts]
---

## Purpose

Delivery notification layer for webhook events — monitors failed webhook deliveries from Shopify and Bling, aggregates errors, and dispatches alerts via email and Supabase notifications to `{{BRAND_SUPPORT_EMAIL}}`.

## When to Use

- Detecting when Shopify can no longer reach your webhook endpoint.
- Alerting on-call when Bling webhooks fail HMAC verification repeatedly.
- Generating a daily summary of webhook delivery health.
- Triggering re-sync workflows after a delivery outage.

## Notification Channels

| Channel | Trigger | Frequency |
|---------|---------|-----------|
| Email (Resend/SendGrid) | >= 3 delivery failures in 5 min | Immediate |
| Supabase notification row | Any delivery failure | Per event |
| Daily digest | Summary of all webhook events | Daily at 08:00 |
| Slack/WhatsApp (optional) | Critical: endpoint unreachable | Immediate |

## Event Types

| Event | Severity | Action |
|-------|---------|--------|
| `webhook_delivery_failed` | HIGH | Alert + log |
| `hmac_verification_failed` | CRITICAL | Alert + block source IP |
| `endpoint_unreachable` | CRITICAL | Alert + trigger manual sync |
| `duplicate_event_detected` | LOW | Log (idempotency handled) |
| `processing_timeout` | MEDIUM | Alert; check edge function logs |

## Notification Schema

```json
{
  "event": "webhook_delivery_failed",
  "source": "shopify",
  "topic": "products/update",
  "webhook_id": 123456789,
  "delivery_id": "abc-123",
  "error": "endpoint returned 500",
  "retry_count": 3,
  "occurred_at": "2026-04-17T10:00:00Z",
  "product_id": "gid://shopify/Product/789"
}
```

## Delivery Failure Detection

```typescript
// Called by webhook handler on error
async function notifyWebhookFailure(ctx: WebhookContext, error: string) {
  // 1. Insert into webhook_errors table
  await supabase.from('webhook_errors').insert({
    source: ctx.source, topic: ctx.topic, delivery_id: ctx.deliveryId,
    error, occurred_at: new Date().toISOString(),
  });

  // 2. Check threshold: >= 3 errors in 5 min
  const { count } = await supabase.from('webhook_errors')
    .select('*', { count: 'exact', head: true })
    .eq('source', ctx.source)
    .gte('occurred_at', new Date(Date.now() - 300_000).toISOString());

  if (count >= 3) {
    await sendAlertEmail({
      to: Deno.env.get('SUPPORT_EMAIL')!,
      subject: `[ALERT] Webhook failures: ${ctx.source}/${ctx.topic}`,
      body: `${count} delivery failures in 5 minutes. Check edge function logs.`,
    });
  }
}
```

## Retry Escalation Table

| Retry Count | Action |
|-------------|--------|
| 1st failure | Log only |
| 3rd failure in 5 min | Email alert to `{{BRAND_SUPPORT_EMAIL}}` |
| 5th failure | Trigger manual re-sync |
| 10th failure | Mark source as degraded; pause automated sync |

## Interface

| Input | Type | Description |
|-------|------|-------------|
| Webhook error context | Object | Source, topic, delivery ID, error |
| `SUPPORT_EMAIL` | env | Alert recipient |

| Output | Type | Description |
|--------|------|-------------|
| `webhook_errors` row | DB | Persistent error log |
| Alert email | Email | Sent on threshold breach |
| Notification row | DB | `notifications` table entry |

## Brand Variables Used

| Variable | Purpose |
|----------|---------|
| `{{BRAND_SUPPORT_EMAIL}}` | Alert recipient for webhook failures |
| `{{BRAND_SUPABASE_PROJECT_REF}}` | Supabase project for DB logging |

## Related Artifacts

| Artifact | Kind | Role |
|----------|------|------|
| `ex_webhook_shopify.md` | webhook | Primary inbound handler |
| `ex_webhook_bling.md` | webhook | Bling inbound handler |
| `ex_webhook_manager.md` | webhook | Shopify webhook CRUD |
