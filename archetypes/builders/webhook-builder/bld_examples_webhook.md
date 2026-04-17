---
kind: examples
id: bld_examples_webhook
pillar: P04
llm_function: GOVERN
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.0
tags: [examples, webhook, P04, golden, anti-pattern]
tldr: "Golden: Stripe payment.completed inbound webhook. Anti: minimal broken artifact with annotated gate failures."
density_score: 1.0
domain: "examples artifact construction"
title: "Examples Webhook"
---
# Examples: webhook
## GOLDEN — Stripe payment.completed (inbound)
**Prompt**: "Create webhook for Stripe payment.completed inbound"
**Output**:
```markdown
---
id: p04_webhook_payment_completed
kind: webhook
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
name: "Stripe Payment Completed"
direction: inbound
event_type: "payment_intent.succeeded"
event_types:
  - "payment_intent.succeeded"
  - "payment_intent.payment_failed"
payload_schema:
  type: object
  required: [id, type, data]
  properties:
    id: {type: string, description: "Stripe event ID (evt_...)"}
    type: {type: string, description: "Event type string"}
    data: {type: object, description: "PaymentIntent object"}
signature_method: hmac_sha256
signature_header: "Stripe-Signature"
retry_policy: {max_attempts: 5, backoff: exponential, backoff_base_ms: 1000}
idempotency_key: "data.object.id"
timeout_ms: 30000
quality: null
tags: [webhook, payment_completed, stripe, P04]
tldr: "Inbound Stripe webhook for payment_intent events with HMAC-SHA256 verification."
---
## Overview
Inbound webhook receiving Stripe PaymentIntent events. HMAC-SHA256 signature verified via Stripe-Signature header before payload processing.
## Events
### payment_intent.succeeded
**Trigger**: Charge captured, funds confirmed.
**Payload**: `{"id":"evt_01","type":"payment_intent.succeeded","data":{"object":{"id":"pi_01","amount":4999,"currency":"usd"}}}`
### payment_intent.payment_failed
**Trigger**: Charge declined or auth failed.
**Payload**: `{"id":"evt_02","type":"payment_intent.payment_failed","data":{"object":{"id":"pi_02","last_payment_error":{"code":"card_declined"}}}}`
## Verification
- **Method**: hmac_sha256 via `Stripe-Signature` header
- **Secret**: env var `STRIPE_WEBHOOK_SECRET`
- **Algorithm**: `t=timestamp,v1=signature` — verify before parse
## Retry & Delivery
- **Max attempts**: 5 over 3 days (Stripe managed)
- **Timeout**: 30000ms — respond 2xx within 30s
- **Idempotency**: `data.object.id` — deduplicate on PaymentIntent ID
- **Dead-letter**: `webhook_failures` table after 5 retries
```
**Gate result**: PASS — H01-H10 pass, soft_score ~8.8
## ANTI-PATTERN — Broken minimal artifact
**Prompt**: "Create webhook" (no direction, no event, no schema)
**Bad output** (annotated):
```markdown
---
id: my_webhook          # FAIL H02: missing p04_webhook_ prefix
kind: webhook
direction: receive      # FAIL H06: must be "inbound" not "receive"
event_type: ""          # FAIL H07: empty string
payload_schema: {}      # FAIL H08: empty schema
quality: 8.5            # FAIL H04: must be null
tags: [webhook]
tldr: "My webhook"
---
## Overview
This webhook receives events.
```
**Gate failures**:
- H02: id `my_webhook` — missing `p04_webhook_` prefix
- H04: quality must be null, not 8.5
- H06: direction "receive" not in enum {inbound, outbound}
- H07: event_type empty string
- H08: payload_schema empty object
- S03: no signature_method (security failure for inbound)
- S04: no retry_policy
**Corrective**: Ask for direction, event source, event name, payload fields before producing.
## Checklist
1. Direction: inbound/outbound? 2. Event type named? 3. Payload JSON Schema?
4. Signature (hmac_sha256 default)? 5. Retry+backoff? 6. Idempotency key?
