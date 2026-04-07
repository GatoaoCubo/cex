---
id: kc_digistore24_ipn
kind: knowledge_card
pillar: P01
version: 1.0.0
created: 2026-03-31
author: n03_builder
domain: webhook_integration
quality: 9.1
tldr: "Digistore24 IPN — form-encoded webhook system with sha512 verification, mandatory 'OK' response, event types, and handler implementation."
tags: [digistore24, ipn, webhook, sha512, form-encoded, payment-notification]
density_score: 1.0
when_to_use: "Apply when digistore24 ipn — form-encoded webhook system with sha512 verification, mandatory 'ok' response, ..."
keywords: [on-rebill-resumed, knowledge-card, on-payment-missed, webhooks, on-chargeback]
linked_artifacts:
  primary: null
  related: []
---

# Digistore24 IPN (Instant Payment Notification)

DS24 IPN is the webhook system used by Digistore24 to notify your server of purchase events. It has critical differences from JSON-based webhook systems (Stripe, Hotmart) that cause integration failures if not handled correctly.

## 1. Critical Differences from Other Webhooks

| Aspect | DS24 IPN | Hotmart Webhook | Stripe Webhook |
|--------|---------|----------------|----------------|
| **Format** | form-encoded | JSON | JSON |
| **Signature** | sha512 hash | sha256 HMAC | sha256 HMAC |
| **Response** | body = exact "OK" | HTTP 200 | HTTP 200 |
| **Content-Type** | application/x-www-form-urlencoded | application/json | application/json |
| **Retry** | Until "OK" received | Limited retries | 3 days, exponential |

**The #1 cause of DS24 IPN failures**: treating it as JSON. DS24 sends form-encoded data. If your handler tries to parse JSON, it will fail silently and DS24 will retry indefinitely.

## 2. IPN Event Types

| Event | Trigger | Action |
|-------|---------|--------|
| `on_payment` | Successful payment (first or one-time) | Grant access, send welcome email |
| `on_payment_missed` | Subscription payment failed | Notify user, grace period |
| `on_refund` | Refund processed | Revoke access, send confirmation |
| `on_chargeback` | Bank chargeback initiated | Revoke access, flag account |
| `on_rebill_resumed` | Subscription reactivated | Restore access |
| `on_rebill_cancelled` | Subscription canceled | Schedule access revocation |
| `on_affiliatelink` | Affiliate link clicked | Track attribution |
| `on_invoice_created` | New invoice generated | Log for accounting |

### Event Priority
| Priority | Events | SLA |
|----------|--------|-----|
| P0 (critical) | on_payment, on_refund, on_chargeback | Process < 5s |
| P1 (important) | on_rebill_cancelled, on_payment_missed | Process < 30s |
| P2 (tracking) | on_affiliatelink, on_invoice_created | Process < 60s |

## 3. IPN Payload Structure (form-encoded)

DS24 sends a POST with `Content-Type: application/x-www-form-urlencoded`. Key fields:

| Field | Type | Example |
|-------|------|---------|
| `event` | string | "on_payment" |
| `api_mode` | string | "live" or "test" |
| `is_test` | string | "0" or "1" |
| `product_id` | string | "12345" |
| `product_name` | string | "Curso de Python" |
| `order_id` | string | "ORD-98765" |
| `transaction_id` | string | "TXN-11111" |
| `email` | string | "buyer@example.com" |
| `first_name` | string | "Hans" |
| `last_name` | string | "Mueller" |
| `amount` | string | "9900" (cents EUR) |
| `currency` | string | "EUR" |
| `pay_method` | string | "SEPA" |
| `affiliate` | string | "aff_username" |
| `sha_sign` | string | sha512 signature |
| `custom` | string | your custom data (URL-encoded) |
| `billing_type` | string | "single" or "rebill" |

**Note**: ALL values are strings. Convert `amount` to int for calculations.

## 4. SHA512 Signature Verification

DS24 signs each IPN with sha512 using your IPN passphrase.

```python
import hashlib
from urllib.parse import parse_qs

def verify_ds24_ipn(body: bytes, passphrase: str) -> bool:
    """Verify DS24 IPN sha512 signature.

    DS24 concatenates all POST fields (sorted alphabetically, excluding sha_sign)
    with the passphrase, then sha512 hashes the result.
    """
    params = parse_qs(body.decode("utf-8"), keep_blank_values=True)
    # Flatten: parse_qs returns lists, take first value
    flat = {k: v[0] for k, v in params.items()}

    received_sign = flat.pop("sha_sign", "")

    # Sort fields alphabetically, concatenate values
    sorted_keys = sorted(flat.keys())
    sign_string = "".join(flat[k] for k in sorted_keys)
    sign_string += passphrase

    computed = hashlib.sha512(sign_string.encode("utf-8")).hexdigest().upper()
    return computed == received_sign.upper()
```

**Critical**:
- Remove `sha_sign` from the fields before computing.
- Sort remaining fields alphabetically by key.
- Concatenate VALUES only (no keys, no separators).
- Append passphrase at the end.
- SHA512 hash, compare uppercase.

**Store `DS24_IPN_PASSPHRASE` as ENV_VAR.** Never log, never expose. Set in DS24 vendor dashboard under IPN settings.

## 5. Mandatory "OK" Response

**This is non-negotiable.** DS24 expects the response body to be the exact string `OK`.

```python
from fastapi import FastAPI, Request
from fastapi.responses import PlainTextResponse

app = FastAPI()

@app.post("/webhooks/ds24")
async def ds24_ipn(request: Request):
    body = await request.body()
    passphrase = os.environ["DS24_IPN_PASSPHRASE"]

    if not verify_ds24_ipn(body, passphrase):
        # Log for security audit but STILL return "OK"
        # to prevent DS24 from retrying forever
        logger.warning("DS24 IPN signature verification failed")
        return PlainTextResponse("OK")  # See note below

    params = parse_qs(body.decode(), keep_blank_values=True)
    event = params.get("event", [""])[0]

    # Process asynchronously to respond quickly
    await process_ds24_event(event, params)

    return PlainTextResponse("OK")
```

### Response Rules
| Response | DS24 Behavior |
|----------|--------------|
| Body = "OK" | Event marked as delivered. No retry. |
| Body = anything else | DS24 retries (increasing intervals). |
| HTTP 4xx/5xx | DS24 retries. |
| Timeout (> 30s) | DS24 retries. |
| No response | DS24 retries indefinitely. |

**Controversial choice above**: Returning "OK" even on signature failure prevents infinite retries. Log the failure, alert your team, but don't let a verification bug cause DS24 to DDoS your endpoint. Some teams prefer to return non-OK on verification failure — your call based on risk tolerance.

## 6. Idempotency

Use `order_id` or `transaction_id` as idempotency key:

```python
async def process_ds24_event(event: str, params: dict):
    order_id = params.get("order_id", [""])[0]

    # Dedup check
    if await db.exists("ds24_events", order_id, event):
        return  # Already processed

    await db.insert("ds24_events", order_id, event, params)

    if event == "on_payment":
        await grant_access(params)
    elif event == "on_refund":
        await revoke_access(params)
    elif event == "on_chargeback":
        await handle_chargeback(params)
    elif event == "on_rebill_cancelled":
        await schedule_revocation(params)
```

**Compound key**: `(order_id, event)` — same order can have multiple events (payment → refund → chargeback).

## 7. Testing IPN

### From DS24 Dashboard
1. Go to vendor dashboard → product → IPN settings.
2. Enter your endpoint URL.
3. Set passphrase.
4. Click "Send test IPN".
5. Verify: your handler returns "OK", signature validates, event is logged.

### Local Development
```bash
# Use ngrok to expose local server
ngrok http 8000

# Configure DS24 IPN URL to ngrok URL
# https://abc123.ngrok.io/webhooks/ds24
```

### Test vs Live Events
| Field | Test | Live |
|-------|------|------|
| `is_test` | "1" | "0" |
| `api_mode` | "test" | "live" |
| Real charge | No | Yes |
| Real payout | No | Yes |

**Rule**: Always check `is_test` in your handler. Log test events but don't trigger real business logic (access grants, email sends) in production.

## 8. Error Handling Pattern

```python
@app.post("/webhooks/ds24")
async def ds24_ipn(request: Request):
    try:
        body = await request.body()
        if not verify_ds24_ipn(body, os.environ["DS24_IPN_PASSPHRASE"]):
            logger.error("DS24 IPN verification failed", extra={"body_len": len(body)})
            return PlainTextResponse("OK")

        params = parse_qs(body.decode(), keep_blank_values=True)
        await process_ds24_event(params)

    except Exception:
        # ALWAYS return "OK" — handle errors async
        logger.exception("DS24 IPN processing error")

    return PlainTextResponse("OK")  # ALWAYS
```

**Pattern**: Respond "OK" immediately, process asynchronously. If processing fails, your retry mechanism handles it — not DS24's.

## 9. Common Gotchas

| Gotcha | Impact | Fix |
|--------|--------|-----|
| Parsing as JSON | Handler crashes, DS24 retries forever | Use `parse_qs()` on form-encoded body |
| Returning JSON `{"status":"ok"}` | DS24 retries forever | Return plain text "OK" exactly |
| Not removing sha_sign before verification | Signature always fails | Pop sha_sign first |
| Case-sensitive signature comparison | Random failures | Compare uppercase |
| Processing in request thread | Timeout → retry | Process async, respond immediately |
| Not handling all event types | Missed refunds/chargebacks | Handle all 8 events |
| Same passphrase for all products | Security risk | Unique passphrase per product if possible |

## Regras de Ouro

1. **form-encoded, NOT JSON** — this is the #1 integration killer.
2. **Response body = "OK"** — exactly, always, no exceptions.
3. **SHA512 uppercase** — remove sha_sign, sort alphabetically, append passphrase.
4. **Respond first, process later** — async processing prevents timeouts.
5. **Compound idempotency** — `(order_id, event)` because one order has multiple lifecycle events.
6. **Test before live** — use DS24 test IPN button; verify signature + "OK" response + event logging.


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating
