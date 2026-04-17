---
id: p04_notifier_NAME
kind: notifier
pillar: P04
version: 1.0.0
title: "Template — Notifier"
tags: [template, notifier, alert, webhook, messaging]
tldr: "Configures a notification channel for system events. Supports Slack, email, webhook, and console. Defines triggers, message templates, rate limits, and escalation."
quality: 9.0
updated: "2026-04-07"
domain: "tool integration"
author: n03_builder
created: "2026-04-07"
density_score: 0.97
---

# Notifier: [NAME]

## Purpose
[WHAT events trigger notifications — build failures, quality alerts, task completion]

## Configuration
```yaml
channel: [slack | email | webhook | console | telegram]
endpoint: "[WEBHOOK_URL or EMAIL or CHANNEL_ID]"
auth: "[bearer_token | api_key | none]"
enabled: true
```

## Trigger Rules

| Event | Severity | Action | Example |
|-------|----------|--------|---------|
| build_failed | critical | notify immediately | "8F F7 FAIL: 3 gates failed" |
| quality_below | warning | batch (5min window) | "12 artifacts below 8.0" |
| task_complete | info | notify on completion | "N03 batch1 done: 10 enriched" |
| doctor_fail | critical | notify + escalate | "Builder FAIL: oversized ISO" |

## Message Template
```
[{severity}] {event_type}
Source: {nucleus} | {timestamp}
Detail: {message}
Action: {suggested_action}
```

## Rate Limiting
- **Max per minute**: [5] — prevents notification storms
- **Dedup window**: [300s] — same event type suppressed for 5min
- **Quiet hours**: [none | 22:00-07:00] — batch during quiet hours

## Escalation
| Level | After | Action |
|-------|-------|--------|
| 1 | Immediate | Notify configured channel |
| 2 | 15min no ACK | Notify backup channel |
| 3 | 30min no ACK | Page on-call (if configured) |

## Quality Gate
- [ ] Channel type specified
- [ ] At least 2 trigger events defined
- [ ] Rate limit configured (prevent spam)
- [ ] Message template includes severity + source
