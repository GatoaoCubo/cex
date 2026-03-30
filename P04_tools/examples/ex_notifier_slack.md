---
id: p04_notify_slack
kind: notifier
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: edison
name: "Slack Notifier"
channel: slack
template: "agent_alert"
priority: normal
provider: "Slack"
rate_limit:
  max_per_minute: 30
  max_per_hour: 500
retry_policy:
  max_attempts: 3
  backoff: exponential
template_vars: [agent_name, status, message, timestamp]
delivery_guarantee: at_least_once
quality: null
tags: [notifier, slack, alerts]
tldr: "Slack notifier for agent status alerts via Webhook API with exponential retry"
description: "Sends agent completion, error, and status notifications to Slack channels"
---

# Slack Notifier

## Overview
Sends structured notifications to Slack channels when agents complete tasks, encounter errors, or need human attention. Uses Slack Incoming Webhooks for delivery.

## Template
**Pattern**: `[{{agent_name}}] {{status}}: {{message}} ({{timestamp}})`

**Variables**:
- `agent_name`: Name of the agent that triggered the notification
- `status`: complete | error | warning | blocked
- `message`: Human-readable description of the event
- `timestamp`: ISO 8601 timestamp

**Examples by priority**:
- critical: `[operations_agent] ERROR: Deploy failed — rollback initiated (2026-03-28T14:30:00Z)`
- high: `[builder_agent] WARNING: Build succeeded with 3 test failures (2026-03-28T14:30:00Z)`
- normal: `[research_agent] COMPLETE: Research finished, 12 sources found (2026-03-28T14:30:00Z)`

## Delivery
- rate_limit: 30/min, 500/hr
- retry: 3x exponential backoff
- guarantee: at_least_once
- on_failure: log to stderr + dead-letter queue for manual replay

## Configuration
- endpoint: Slack Incoming Webhook URL
- auth: env var `SLACK_WEBHOOK_URL`
- channel_id: configured per webhook (e.g., #organization-alerts)
