# P09 Config — N06 Commercial

> Strategic Greed · configuration for pricing, campaigns, monetization

## Scope in N06
Runtime settings for the commercial layer: pricing tier definitions,
campaign budget caps, subscription renewal schedules, payment
provider credentials, A/B test allocations. Greed drives
revenue-max — configs here bias toward capture over acquisition.

## Kinds that live here
- `env_config` — env vars for payment providers (Stripe, etc.)
- `secret_config` — payment/billing API keys (gitignored)
- `feature_flag` — monetization toggles (paywalls, trials)
- `rate_limit_config` — throttles on billing operations

## Related
- `tools/` — payment clients and billing webhooks this governs
- `orchestration/` — renewal workflows and dispatch rules
