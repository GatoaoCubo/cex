---
kind: error_handling
id: bld_error_handling_content_monetization
pillar: P11
llm_function: GOVERN
version: 1.0.0
created: 2026-03-31
updated: 2026-03-31
author: n03_engineering
domain: content_monetization
purpose: Error taxonomy, recovery strategies, and retry policies for content monetization pipeline
quality: null
tags: [error-handling, content-monetization, payment, webhook, credits, retry]
tldr: "Error handling for 9-stage monetization pipeline — payment failures, webhook retries, credit insufficient, margin violations, provider outages."
density_score: 0.91
---

# Error Handling: content-monetization-builder

## Error Taxonomy

### Payment Errors (S4 CHECKOUT)

| Error | Cause | Severity | Recovery |
|-------|-------|----------|----------|
| PAYMENT_DECLINED | Card declined, insufficient funds | HIGH | Notify user, suggest alternative method, retry 1x after 24h |
| PAYMENT_FRAUD | Fraud detection triggered | CRITICAL | Block transaction, flag account, do NOT retry |
| WEBHOOK_DUPLICATE | Same event received twice | LOW | Deduplicate via idempotency_key, return 200/OK, skip processing |
| WEBHOOK_SIGNATURE_INVALID | HMAC/sha512 mismatch | CRITICAL | Reject payload, log attempt, alert ops — possible tampering |
| WEBHOOK_TIMEOUT | Provider timeout waiting for response | MEDIUM | Hotmart: return 200 fast. DS24: return "OK" fast. Process async |
| PROVIDER_OUTAGE | Stripe/Hotmart/DS24 API down | HIGH | Queue event, retry with exponential backoff, switch to fallback if configured |
| CHARGEBACK_RECEIVED | Customer disputed charge | HIGH | Revoke access, freeze credits, log for dispute response |
| SUBSCRIPTION_LAPSED | Renewal failed after retries | MEDIUM | Downgrade to free tier, send win-back email sequence |

### Credit Errors (S3 CREDITS)

| Error | Cause | Severity | Recovery |
|-------|-------|----------|----------|
| CREDITS_INSUFFICIENT | Balance < operation cost | MEDIUM | If block: reject + upsell. If notify: warn + allow 1x. If allow_negative: log debt |
| CREDITS_OVERDRAFT | Negative balance after operation | HIGH | Block further operations, send top-up notification, log debt amount |
| CREDIT_COST_UNMAPPED | Operation has no credit cost defined | CRITICAL | Reject operation — untracked ops leak margin. Add to pipeline_costs |
| CREDIT_REFRESH_FAILED | Monthly credit reset failed | HIGH | Retry 3x, alert ops, manual credit adjustment |

### Pricing Errors (S2 PRICING)

| Error | Cause | Severity | Recovery |
|-------|-------|----------|----------|
| MARGIN_BELOW_FLOOR | Tier margin < floor_margin_pct | CRITICAL | Block publish. Raise price or reduce credit allocation |
| TIER_CONFLICT | Duplicate tier name or overlapping features | MEDIUM | Reject config, show conflict details |
| PRICE_FORMAT_INVALID | Float instead of centavos/cents integer | CRITICAL | Reject config. Convert: R$49.90 → 4990 |

### Webhook Platform-Specific

#### Hotmart (BR)
| Error | Cause | Recovery |
|-------|-------|----------|
| HOTTOK_MISMATCH | sha256 HMAC fails against HOTMART_HOTTOK | Reject. Verify HOTMART_HOTTOK env var is current |
| TOKEN_EXPIRED | OAuth2 bearer token expired | Refresh via client_credentials flow, retry request |
| EVENT_UNKNOWN | Unrecognized event type in payload | Log + ignore. Do NOT fail — Hotmart may add new events |

#### Digistore24 (INT)
| Error | Cause | Recovery |
|-------|-------|----------|
| IPN_NOT_OK | Response body was not exact string "OK" | DS24 retries indefinitely. Fix handler to return "OK" |
| IPN_JSON_PARSE | Attempted JSON parse on form-encoded body | Fix parser: DS24 IPN is form-encoded, NOT JSON |
| SHA512_MISMATCH | Signature verification failed | Reject. Verify DS24_IPN_PASSPHRASE env var |
| SANDBOX_LEAK | Production handler received sandbox event | Block. Check DS24_SANDBOX_MODE env var routing |

### Course Errors (S5 COURSES)

| Error | Cause | Recovery |
|-------|-------|----------|
| MODULE_EMPTY | Module has zero lessons | Reject config — empty modules confuse users |
| DRIP_CONFLICT | Drip schedule overlaps or gaps | Warn, auto-fix to sequential drip_days |
| CERTIFICATION_NO_THRESHOLD | certification: true but no completion_threshold | Default to 0.80, warn builder |

### Email Errors (S7 EMAILS)

| Error | Cause | Recovery |
|-------|-------|----------|
| SEQUENCE_NO_TRIGGER | Email sequence without behavioral trigger | Reject — time-only sequences miss intent |
| PROVIDER_RATE_LIMIT | Email API rate limit hit | Queue + exponential backoff (Resend: 10/s, SendGrid: 600/min) |
| BOUNCE_HARD | Permanent delivery failure | Remove from sequence, mark address invalid |

## Retry Policy

| Category | Max Retries | Backoff | Timeout |
|----------|------------|---------|---------|
| Payment webhook | 5 | Exponential: 1s, 2s, 4s, 8s, 16s | 30s per attempt |
| DS24 IPN response | N/A (DS24 retries us) | Fix handler immediately | Return "OK" within 5s |
| Credit operations | 3 | Linear: 1s, 2s, 3s | 10s per attempt |
| Email delivery | 3 | Exponential: 5m, 30m, 2h | 24h total |
| Provider API calls | 3 | Exponential: 1s, 5s, 25s | 60s per attempt |

## Escalation Matrix

| Level | Condition | Action |
|-------|-----------|--------|
| L0 Auto | Retry succeeds | Log + continue |
| L1 Alert | All retries exhausted | Notify ops channel, queue for manual |
| L2 Incident | Payment security (fraud, signature invalid) | Block + alert security team |
| L3 Critical | Provider outage > 30min, chargeback spike | Engage provider support, consider fallback |

## Circuit Breaker

| Provider | Trip After | Reset After | Fallback |
|----------|-----------|------------|----------|
| Hotmart | 5 failures in 5min | 10min half-open test | Queue events, alert ops |
| DS24 | 5 failures in 5min | 10min half-open test | Queue events, alert ops |
| Stripe | 3 failures in 2min | 5min half-open test | Queue events |
| Email provider | 10 failures in 10min | 15min half-open test | Buffer emails |

## Mock Mode Error Behavior
In mock_mode: true, all errors return synthetic responses for testing:
- Payment: always succeeds (test card)
- Webhook: validates signature against test secret
- Credits: infinite balance (but logs real costs)
- Email: logs to console instead of sending
