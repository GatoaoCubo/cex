---
kind: quality_gate
id: p11_qg_webhook
pillar: P11
llm_function: GOVERN
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.1
tags: [quality_gate, webhook, P11, validation]
tldr: "10 HARD gates (any failure = reject) + 12 SOFT dims (score 0-10, threshold 7.0)"
density_score: 1.0
domain: "examples artifact construction"
title: Quality Gate ISO - webhook
target_kind: webhook
hard_gates: 10
soft_dims: 12
related:
  - bld_examples_webhook
  - bld_instruction_webhook
  - bld_output_template_webhook
  - webhook-builder
  - bld_config_webhook
  - p03_sp_webhook_builder
  - bld_schema_webhook
  - bld_memory_webhook
  - p01_kc_webhook
  - bld_architecture_webhook
---

## Quality Gate

# Gate: webhook

## HARD Gates (any failure = immediate reject)

| ID | Gate | Check |
|----|------|-------|
| H01 | YAML valid | Frontmatter parses without error |
| H02 | ID pattern | id matches `^p04_webhook_[a-z][a-z0-9_]+$` |
| H03 | Kind correct | kind == "webhook" |
| H04 | Quality null | quality == null (never self-scored) |
| H05 | Required fields | id, name, direction, event_type, payload_schema all present |
| H06 | Direction enum | direction is exactly "inbound" or "outbound" |
| H07 | Event type set | event_type is non-empty string |
| H08 | Payload schema | payload_schema is defined object, not empty `{}` |
| H09 | Size limit | body <= 1024 bytes (exclude frontmatter) |
| H10 | No lifecycle | Body contains no "server", "daemon", "listen forever", "start()" |

## SOFT Scoring (0-10 per dimension, threshold >= 7.0)

| Dim | Name | What earns full score |
|-----|------|-----------------------|
| S01 | Event coverage | All event_types listed with trigger conditions |
| S02 | Payload docs | Each event has payload_schema with field descriptions |
| S03 | Signature verification | Method + header + secret env var documented |
| S04 | Retry policy | max_attempts, backoff strategy, backoff_base_ms present |
| S05 | Idempotency | idempotency_key field identified in payload |
| S06 | Error handling | Dead-letter or failure fallback described |
| S07 | Timeout | timeout_ms explicitly set |
| S08 | Boundary clarity | Clearly NOT api_client / notifier / mcp_server |
| S09 | Domain specificity | Provider named (Stripe/GitHub/Slack/costm), not generic |
| S10 | Testability | Payload examples are valid JSON, realistic values |
| S11 | Security posture | Inbound: signature verified before parse; outbound: HTTPS only |
| S12 | Delivery guarantees | At-least-once or exactly-once semantics stated |

## Scoring Formula

```
soft_score = mean(S01..S12)
pass = all(H01..H10) AND soft_score >= 7.0
```

## Common Failures

- H06: direction = "receive" instead of "inbound" — use enum values only
- H08: payload_schema: {} — must define at minimum `type: object`
- H09: body too long — compress examples, remove prose padding
- S03: inbound webhook with signature_method: none — security gate will flag
- S04: outbound without retry_policy — fire-and-forget is unacceptable
- S11: signature verified after parsing — must verify raw_body before JSON decode

## Examples

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

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
