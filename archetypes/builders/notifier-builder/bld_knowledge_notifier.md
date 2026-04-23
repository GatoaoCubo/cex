---
id: bld_knowledge_card_notifier
kind: knowledge_card
pillar: P04
llm_function: INJECT
purpose: Domain knowledge for building notifier artifacts
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
tags: [knowledge_card, notifier, email, sms, slack, discord, firebase, sendgrid, twilio]
quality: 9.1
tldr: "Provider selection, template design, rate limits, and anti-patterns for notification delivery across email, SMS, Slack, Discord, push channels."
density_score: 1.0
title: Knowledge Card ISO - notifier
related:
  - bld_instruction_notifier
  - p03_sp_notifier_builder
  - notifier-builder
  - bld_config_notifier
  - p01_kc_notifier
  - bld_output_template_notifier
  - bld_architecture_notifier
  - bld_examples_notifier
  - p04_notifier_NAME
  - p11_qg_notifier
---
# Knowledge Card: Notification Delivery

## Provider Reference
| Channel | Provider        | Rate Limit Default | Auth               | Notes                         |
|---------|-----------------|--------------------|--------------------|-------------------------------|
| email   | SendGrid        | 100/min            | SENDGRID_API_KEY   | Subject + HTML/text body      |
| email   | AWS SES         | 14/s (sandbox)     | AWS_ACCESS_KEY_ID  | Verify sender domain first    |
| email   | Mailgun         | 100/min            | MAILGUN_API_KEY    | EU/US region matters          |
| sms     | Twilio          | 1/s per number     | TWILIO_AUTH_TOKEN  | 160ch limit, E.164 format     |
| slack   | Slack API       | 1/s per channel    | SLACK_BOT_TOKEN    | Block Kit for rich messages   |
| discord | Discord Webhooks| 5/2s per webhook   | webhook URL        | Embed objects for rich msg    |
| push    | Firebase FCM    | 500/s project      | FIREBASE_SERVER_KEY| TTL, collapse_key for dedup   |
| teams   | Incoming Webhook| 4/s per connector  | webhook URL        | Adaptive Cards format         |

## Template Best Practices
- **Email**: subject <= 60ch (mobile preview), preheader 85-100ch, CTA above fold
- **SMS**: <= 160ch to avoid concatenation cost, include opt-out "Reply STOP"
- **Slack**: use `mrkdwn: true` for formatting, Block Kit for interactive messages
- **Discord**: embeds with color coding by severity (red=critical, orange=high, green=ok)
- **Push (FCM)**: title <= 50ch, body <= 100ch, include deep-link data payload

## Priority Routing
```
critical -> immediate delivery, no batching, retry until ACK, wake on-call
high     -> <= 2 min delivery, retry 3x exponential, deduplicated
normal   -> batched every 5-15 min, best-effort, deduplicated by key
low      -> daily digest, grouped by type, skipped if user opted out
```

## Rate Limiting Patterns
- Per-user: prevent flooding one recipient (max 3/hr for transactional)
- Per-channel: respect provider limits (Slack 1/s, Twilio 1/s per number)
- Burst: allow short burst then throttle (token bucket algorithm)
- Provider ban trigger: exceed limits 3x in 1h -> IP/key flagged

## Anti-Patterns
- No rate_limit on production channels -> provider ban or user unsubscribe storm
- Hardcoding credentials in template -> security incident
- Missing retry on critical channel -> lost alerts, SLA breach
- Same template for all priorities -> alert fatigue (everything looks urgent)
- Notifier listening for HTTP events -> that is a webhook, not a notifier
- Body > 1024 bytes -> exceeds notifier spec contract, move to api_client

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_notifier]] | upstream | 0.45 |
| [[p03_sp_notifier_builder]] | related | 0.44 |
| [[notifier-builder]] | related | 0.42 |
| [[bld_config_notifier]] | related | 0.39 |
| [[p01_kc_notifier]] | sibling | 0.38 |
| [[bld_output_template_notifier]] | related | 0.36 |
| [[bld_architecture_notifier]] | related | 0.36 |
| [[bld_examples_notifier]] | related | 0.31 |
| [[p04_notifier_NAME]] | related | 0.30 |
| [[p11_qg_notifier]] | downstream | 0.29 |
