---
id: p04_notify_slack
kind: notifier
pillar: P04
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
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
quality: 9.0
tags: [notifier, slack, alerts]
tldr: "Slack notifier for agent status alerts via Webhook API with exponential retry"
description: "Sends agent completion, error, and status notifications to Slack channels"
domain: "tool integration"
title: "Notifier Slack"
density_score: 0.92
related:
  - bld_examples_notifier
  - bld_output_template_notifier
  - notifier-builder
  - bld_instruction_notifier
  - bld_collaboration_notifier
  - p01_kc_notifier
  - p03_sp_notifier_builder
  - bld_architecture_notifier
  - bld_memory_notifier
  - bld_knowledge_card_notifier
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

## Cross-References

- **Pillar**: P04 (Tools)
- **Kind**: `notifier`
- **Artifact ID**: `p04_notify_slack`
- **Tags**: [notifier, slack, alerts]

## Integration Points

| Component | Role |
|-----------|------|
| Pillar P04 | Tools domain |
| Kind `notifier` | Artifact type |
| Pipeline | 8F (F1→F8) |

## Artifact Metadata

```yaml
kind: notifier
pillar: P04
pipeline: 8F
scoring: hybrid_3_layer
compilation: cex_compile
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_notifier]] | related | 0.45 |
| [[bld_output_template_notifier]] | related | 0.43 |
| [[notifier-builder]] | related | 0.39 |
| [[bld_instruction_notifier]] | upstream | 0.36 |
| [[bld_collaboration_notifier]] | related | 0.36 |
| [[p01_kc_notifier]] | upstream | 0.35 |
| [[p03_sp_notifier_builder]] | related | 0.35 |
| [[bld_architecture_notifier]] | related | 0.33 |
| [[bld_memory_notifier]] | related | 0.32 |
| [[bld_knowledge_card_notifier]] | related | 0.28 |
