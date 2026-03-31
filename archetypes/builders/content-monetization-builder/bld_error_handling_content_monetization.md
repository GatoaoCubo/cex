---
kind: error_handling
id: bld_error_handling_content_monetization
pillar: P11
llm_function: GOVERN
purpose: Failure modes, retry logic, fallbacks for content monetization pipeline
---

# Error Handling: content_monetization

## Per-Stage Failure Matrix
| Stage | Error | Severity | Recovery |
|-------|-------|----------|----------|
| S1 PARSE | No monetizable assets found | FATAL | Return error, request content audit |
| S1 PARSE | Asset classification ambiguous | LOW | Default to generic content type |
| S2 PRICING | Margin below floor (30%) | HIGH | Raise price or reduce pipeline cost |
| S2 PRICING | No competitor data available | MEDIUM | Use industry benchmark pricing |
| S2 PRICING | Currency mismatch | FATAL | Validate currency in config before pricing |
| S3 CREDITS | Pipeline cost unknown for operation | HIGH | Block operation until cost mapped |
| S3 CREDITS | Credit balance insufficient | MEDIUM | Apply overdraft_policy (block/notify/allow) |
| S3 CREDITS | Credit pack purchase fails | HIGH | Retry 3x → redirect to support |
| S4 CHECKOUT | Payment provider timeout | HIGH | Retry 3x exponential → show error page |
| S4 CHECKOUT | Webhook signature invalid | FATAL | Reject event, log for security audit |
| S4 CHECKOUT | Duplicate webhook (same event_id) | NORMAL | Idempotency check → skip silently |
| S4 CHECKOUT | Card declined | MEDIUM | Return decline reason, suggest alternative |
| S4 CHECKOUT | Provider API key invalid (401) | FATAL | Alert admin, block checkout |
| S5 COURSES | Module content missing | HIGH | Show placeholder, notify content team |
| S5 COURSES | Drip schedule conflict | LOW | Default to immediate access |
| S5 COURSES | Certification threshold not met | NORMAL | Show progress, suggest review |
| S6 ADS | Budget exhausted | MEDIUM | Pause campaign, notify admin |
| S6 ADS | Pixel not firing | HIGH | Fallback to UTM tracking, alert |
| S6 ADS | CPA above target | MEDIUM | Reduce bid, narrow audience |
| S7 EMAILS | Provider rate limit (429) | HIGH | Queue + retry with backoff |
| S7 EMAILS | Bounce rate > 5% | HIGH | Pause sequence, clean list |
| S7 EMAILS | Unsubscribe during sequence | NORMAL | Remove from sequence, respect opt-out |
| S8 VALIDATE | Margin check fails | HIGH | Return to S2 PRICING, adjust |
| S8 VALIDATE | Webhook test fails | HIGH | Return to S4 CHECKOUT, fix config |
| S9 DEPLOY | Mock→live cutover fails | FATAL | Rollback to mock, investigate |

## Webhook Retry Policy
```yaml
retry:
  max_attempts: 5
  backoff: exponential
  delays: [1s, 2s, 4s, 8s, 16s]
  idempotency_key: "event_id"
  dedup_window: 24h
  on_max_retries: alert_admin
```

## Credit Insufficient Flow
```
User triggers operation (cost: N credits)
  → Check balance >= N
    → YES: deduct N, execute operation
    → NO: check overdraft_policy
      → block: return "insufficient credits" + pack purchase CTA
      → notify_then_block: send low-credit email, block operation
      → allow_negative: execute, set balance negative, send warning
```

## Circuit Breaker (per provider)
3 consecutive failures → OPEN (maintenance page) → 15min → HALF-OPEN (test tx) → success: CLOSE | fail: OPEN 30min, escalate.

## Degradation Strategy
| Level | Condition | Action |
|-------|-----------|--------|
| Full | All systems operational | Normal 9-stage pipeline |
| Partial | Checkout down, rest OK | Accept orders, queue payment |
| Minimal | Multiple providers down | Show maintenance, send email when restored |
| Emergency | Data inconsistency detected | Freeze billing, manual reconciliation |
