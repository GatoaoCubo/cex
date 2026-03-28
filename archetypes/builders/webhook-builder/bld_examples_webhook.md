---
kind: examples
id: bld_examples_webhook
pillar: P04
llm_function: DEMONSTRATE
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: EDISON
quality: null
tags: [examples, webhook, P04, golden, anti-pattern]
tldr: "Golden: Stripe payment.completed inbound. Anti: minimal broken artifact with annotated gate failures."
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
author: EDISON
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
    id:
      type: string
      description: "Stripe event ID (evt_...)"
    type:
      type: string
      description: "Event type string"
    data:
      type: object
      description: "Event data containing the PaymentIntent object"
signature_method: hmac_sha256
signature_header: "Stripe-Signature"
retry_policy:
  max_attempts: 5
  backoff: exponential
  backoff_base_ms: 1000
idempotency_key: "data.object.id"
timeout_ms: 30000
quality: null
tags: [webhook, payment_completed, stripe, P04]
tldr: "Inbound Stripe webhook receiving payment_intent.succeeded and .payment_failed events with HMAC-SHA256 verification."
---
## Overview

Inbound webhook receiving Stripe PaymentIntent events. Stripe calls this
endpoint after payment success or failure. HMAC-SHA256 signature verified
via Stripe-Signature header before payload processing.

## Events

### payment_intent.succeeded

**Trigger**: Charge captured, funds confirmed by Stripe.

**Payload example**:
```json
{"id":"evt_01","type":"payment_intent.succeeded","data":{"object":{"id":"pi_01","amount":4999,"currency":"usd","status":"succeeded"}}}
```

### payment_intent.payment_failed

**Trigger**: Charge declined or authentication failed.

**Payload example**:
```json
{"id":"evt_02","type":"payment_intent.payment_failed","data":{"object":{"id":"pi_02","last_payment_error":{"code":"card_declined"}}}}
```

## Verification

- **Method**: hmac_sha256
- **Header**: `Stripe-Signature`
- **Secret**: env var `STRIPE_WEBHOOK_SECRET`
- **Algorithm**: Stripe format `t=timestamp,v1=signature` — verify before parse

## Retry & Delivery

- **Max attempts**: 5 over 3 days (Stripe managed)
- **Backoff**: exponential, base 1000ms
- **Timeout**: 30000ms — respond 2xx within 30s
- **Idempotency key**: `data.object.id` — deduplicate on PaymentIntent ID
- **Dead-letter**: log to `webhook_failures` table after 5 Stripe retries
```

**Gate result**: PASS — all H01-H10 pass, soft_score ~8.8

---

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
- H02: id `my_webhook` does not match `^p04_webhook_[a-z][a-z0-9_]+$`
- H04: quality must be null, not 8.5
- H06: direction "receive" not in enum {inbound, outbound}
- H07: event_type is empty
- H08: payload_schema is empty object
- S03: no signature_method — inbound with no verification (security failure)
- S04: no retry_policy
- S09: no provider named — generic and unusable

**Corrective action**: Ask user for direction, event source, event name, and
at least one payload field before producing artifact.
