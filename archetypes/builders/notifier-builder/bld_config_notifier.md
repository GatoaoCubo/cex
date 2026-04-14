---
kind: config
id: bld_config_notifier
pillar: P04
llm_function: CONSTRAIN
purpose: Runtime configuration constraints for notifier artifacts
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
tags: [config, notifier, P04, constraints]
quality: 9.0
tldr: "Naming rules, size limits, channel enum, priority enum, rate limit conventions, and provider-specific constraints for notifier artifacts."
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
density_score: 1.0
title: Config ISO - notifier
---
# Config: notifier

## Naming
```
filename:  p04_notify_{channel_slug}.md
id:        p04_notify_{channel_slug}
regex:     ^p04_notify_[a-z][a-z0-9_]+$
examples:  p04_notify_slack_deploy, p04_notify_email_welcome, p04_notify_sms_otp
```

## Size
```
max_bytes:      1024  (body only, frontmatter excluded)
machine_format: yaml
layer:          runtime
core:           false
```

## Channel Enum
```
email   -> SendGrid, AWS SES, Mailgun
sms     -> Twilio, AWS SNS
slack   -> Slack API (Bot Token)
discord -> Discord Webhooks
push    -> Firebase FCM, APNs
in_app  -> internal event bus
teams   -> Microsoft Incoming Webhook
```

## Priority Enum + Delivery SLA
```
critical -> immediate, retry until ACK, max_attempts >= 5
high     -> <= 2 min, retry 3x exponential
normal   -> <= 15 min batch, best_effort, deduplicated
low      -> daily digest, grouped, skippable
```

## Rate Limit Conventions (defaults by channel)
```
email:   max_per_minute: 100,  max_per_hour: 2000
sms:     max_per_minute: 60,   max_per_hour: 500
slack:   max_per_minute: 60,   max_per_hour: 500
discord: max_per_minute: 30,   max_per_hour: 300
push:    max_per_minute: 500,  max_per_hour: 10000
in_app:  max_per_minute: 1000, max_per_hour: 50000
```

## Provider-Specific Constraints
| Provider     | Max Message Size | Special Constraint                        |
|--------------|-----------------|-------------------------------------------|
| SendGrid     | 30MB email      | Verify sender domain, DKIM required       |
| Twilio SMS   | 160ch/segment   | E.164 phone format, include STOP opt-out  |
| Slack API    | 3000ch body     | 1 msg/s per channel, Block Kit preferred  |
| Discord      | 2000ch content  | 5 req/2s per webhook, embed 6000ch total  |
| Firebase FCM | 4096 bytes data | TTL 0-2419200s, collapse_key for dedup    |
| AWS SES      | 10MB email      | Sandbox: 1/s, production: 14/s default    |

## Delivery Guarantee Semantics
```
at_least_once: retry_policy required, idempotency key recommended
best_effort:   no retry, no ACK wait, fire-and-forget
```
