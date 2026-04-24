---
id: ex-notifier-webhook
kind: notifier
8f: F5_call
pillar: P04
title: Outbound Webhook Notifier
version: 0.1.0
quality: 8.9
status: template
brand_placeholders:
  - BRAND_NAME
  - BRAND_NOTIFIER_DEFAULT_URL
  - BRAND_NOTIFIER_HMAC_SECRET
  - BRAND_SUPPORT_EMAIL
tags: [commerce, template, distillation, notifier, webhook]
density_score: 1.0
related:
  - webhook-builder
  - bld_collaboration_webhook
  - p03_sp_webhook_builder
  - bld_knowledge_card_webhook
  - p04_notify_slack
  - bld_architecture_webhook
  - p01_kc_webhook
  - p01_kc_notifier
  - p04_webhook_NAME
  - bld_architecture_notifier
---

# Outbound Webhook Notifier

## Purpose
Generic dispatcher that emits signed JSON notifications to downstream consumers (ops Slack, analytics warehouse, customer-facing webhook subscribers) whenever an event of interest fires inside the brand's edge functions. It centralizes retry, dedup, and signing so each edge function doesn't reinvent the loop.

## When to use
- You need to notify >1 downstream consumer from a single event.
- Downstream consumer wants HMAC-signed, retriable delivery.
- You want a single place to add a new delivery target (migrate Slack -> Teams, swap ops email).

## When NOT to use
- One-off, fire-and-forget log -> use structured logging, not the notifier.
- In-process callback -> use function composition, not a webhook round-trip.

## Interface
```ts
notifier.send({
  event: "sync_run_completed" | "stock_low" | "order_paid" | "oauth_expired" | ...,
  payload: unknown,
  targets?: string[],   // URLs; defaults to brand config
  trace_id?: string,
}): Promise<{ delivered: DeliveryResult[] }>
```

## Brand variables used
- `{{BRAND_NAME}}` -- included in payload metadata.
- `{{BRAND_NOTIFIER_DEFAULT_URL}}` -- default ops target (e.g. Slack Incoming Webhook).
- `{{BRAND_NOTIFIER_HMAC_SECRET}}` -- env var name of signing key.
- `{{BRAND_SUPPORT_EMAIL}}` -- fallback human contact in the payload metadata.

## Payload shape (contract)
```json
{
  "event": "sync_run_completed",
  "timestamp": "2026-04-16T03:15:22Z",
  "brand": "{{BRAND_NAME}}",
  "trace_id": "uuid-v4",
  "payload": { /* event-specific */ },
  "support": "{{BRAND_SUPPORT_EMAIL}}"
}
```
Always flat `payload` key; never nest events. Consumers dispatch on `event`.

## Signing
Header: `X-{{BRAND_NAME}}-Signature: sha256=<hex>`
Body: raw JSON, signed with HMAC-SHA256 using `{{BRAND_NOTIFIER_HMAC_SECRET}}`. Consumers must compute and compare with timing-safe equality.

## Retry policy
- Attempts: 5. Schedule: 0, 10s, 60s, 5min, 30min.
- Any 2xx = success. 4xx (non-429) = permanent fail, no retry, alert ops. 429/5xx = retry.
- On final fail, persist to `notifier_dead_letter` with full payload; operator can replay.

## Dedup
Event + `trace_id` tuple deduped for 10 minutes to prevent retries from producing double-delivered duplicates when the worker crashes mid-attempt.

## Rate limiting
Per-target token bucket: default 10 req/sec. Targets with lower limits (Slack Incoming Webhook = 1/sec per channel) configured via `notifier_targets` table.

## Observability
Emit metrics `notifier.event.{event}.count`, `notifier.target.{host}.latency_ms`, `notifier.dead_letter.count`. Alert when dead-letter count >0 over 5-min window.

## Related artifacts
- `ex_webhook_manager.md` -- inbound counterpart.
- `ex_workflow_multi_marketplace_sync.md` -- a notifier consumer.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[webhook-builder]] | related | 0.41 |
| [[bld_collaboration_webhook]] | related | 0.40 |
| [[p03_sp_webhook_builder]] | related | 0.38 |
| [[bld_knowledge_card_webhook]] | downstream | 0.37 |
| [[p04_notify_slack]] | sibling | 0.35 |
| [[bld_architecture_webhook]] | related | 0.34 |
| [[p01_kc_webhook]] | upstream | 0.33 |
| [[p01_kc_notifier]] | upstream | 0.33 |
| [[p04_webhook_NAME]] | related | 0.33 |
| [[bld_architecture_notifier]] | related | 0.33 |
