---
id: p01_kc_notifier
kind: knowledge_card
type: kind
pillar: P01
title: "Notifier — Deep Knowledge for notifier"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: marketing_agent
domain: notifier
quality: 9.1
tags: [notifier, P04, CALL, kind-kc]
tldr: "One-way push notification delivery to user or system channels (Slack, email, SMS, Discord) — fire-and-confirm with template rendering, no bidirectional event"
when_to_use: "Building, reviewing, or reasoning about notifier artifacts"
keywords: [notification, slack, email, sms, push]
feeds_kinds: [notifier]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - notifier-builder
  - bld_architecture_notifier
  - bld_instruction_notifier
  - p03_sp_notifier_builder
  - bld_output_template_notifier
  - bld_examples_notifier
  - bld_collaboration_notifier
  - bld_knowledge_card_notifier
  - p04_notify_slack
  - bld_schema_notifier
---

# Notifier

## Spec
```yaml
kind: notifier
pillar: P04
llm_function: CALL
max_bytes: 1024
naming: p04_notify_{{channel}}.md + .yaml
core: false
```

## What It Is
A notifier delivers one-way push notifications to user or system channels (Slack, email, SMS, Discord, Teams). It renders a message from a template and dispatches it via the channel's API. Its boundary is delivery confirmation — it sends and confirms, nothing more. It is NOT a webhook (which handles bidirectional event-driven HTTP) nor an api_client (which supports full CRUD operations against an external service).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | SlackToolkit, GmailToolkit | Multi-action toolkits; notifier is send-only |
| LlamaIndex | n/a (no native notifier) | Custom function_def over channel API |
| CrewAI | Custom tool wrapping Slack/email SDK | No native notifier kind |
| DSPy | n/a | Function wrapping |
| Haystack | n/a | Custom pipeline component |
| OpenAI | function_def over send_slack etc. | No native; user-defined tool |
| Anthropic | tool_use over notify endpoint | No native; user-defined tool |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| channel | str | required | slack / email / sms / discord |
| priority | str | normal | urgent = bypass rate limit |
| template | str | required | Renders context variables into message |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Async fire-and-confirm | Non-blocking agent delivery | await slack.send(); check delivery_id |
| Template-driven | Consistent formatting per alert type | Jinja2 template per event category |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| Sync blocking send | Stalls agent on slow channel API | Use async or background task queue |
| No delivery confirmation | Silent failure undetected | Check API response status code |

## Integration Graph
```
[agent_event / alert] --> [notifier] --> [channel_delivery_confirmation]
                               |
                       [template, channel_api, priority]
```

## Decision Tree
- IF bidirectional event exchange needed THEN use webhook
- IF full API integration with CRUD THEN use api_client
- DEFAULT: notifier for any one-way user or system alert delivery

## Quality Criteria
- GOOD: channel defined, template rendered, async send confirmed
- GREAT: delivery confirmation, retry on transient failure, priority routing
- FAIL: sync blocking call, no template, no error handling on failed send

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[notifier-builder]] | downstream | 0.48 |
| [[bld_architecture_notifier]] | downstream | 0.46 |
| [[bld_instruction_notifier]] | downstream | 0.46 |
| [[p03_sp_notifier_builder]] | downstream | 0.45 |
| [[bld_output_template_notifier]] | downstream | 0.42 |
| [[bld_examples_notifier]] | downstream | 0.41 |
| [[bld_collaboration_notifier]] | downstream | 0.41 |
| [[bld_knowledge_card_notifier]] | sibling | 0.36 |
| [[p04_notify_slack]] | downstream | 0.35 |
| [[bld_schema_notifier]] | downstream | 0.34 |
