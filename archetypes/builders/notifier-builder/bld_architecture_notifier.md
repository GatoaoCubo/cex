---
kind: architecture
id: bld_architecture_notifier
pillar: P04
llm_function: CONSTRAIN
purpose: Internal architecture and boundary map for notifier domain
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
tags: [architecture, notifier, P04, boundary, components]
quality: 9.1
tldr: "Notifier = push delivery. Components: channel_router, template_engine, priority_queue, rate_limiter, delivery_engine, retry_handler."
density_score: 1.0
title: Architecture ISO - notifier
related:
  - notifier-builder
  - p01_kc_notifier
  - p03_sp_notifier_builder
  - bld_collaboration_notifier
  - bld_collaboration_webhook
  - bld_instruction_notifier
  - bld_output_template_notifier
  - webhook-builder
  - bld_knowledge_card_notifier
  - bld_examples_notifier
---
# Architecture: notifier

## Component Map
```
[trigger_source] -> [priority_queue] -> [rate_limiter] -> [delivery_engine]
                                                               |
                        [channel_router] <- [template_engine]  |
                               |                               |
                    [provider_adapter]  <----------------------+
                               |
                    [retry_handler] -> [dead_letter_queue]
```

## Components
| Component        | Role                                                              |
|------------------|-------------------------------------------------------------------|
| channel_router   | Selects provider based on channel enum (email->SendGrid, etc.)   |
| template_engine  | Substitutes `{{vars}}` into message template per channel format    |
| priority_queue   | Routes by priority: critical=immediate, low=digest batch         |
| rate_limiter     | Enforces max_per_minute/max_per_hour, implements token bucket    |
| delivery_engine  | Calls provider API, captures delivery receipt or error           |
| retry_handler    | Exponential/linear backoff on failure, respects max_attempts     |
| provider_adapter | Abstracts SendGrid, Twilio, Firebase, Slack, Discord APIs        |

## Boundary: IS vs IS NOT
| IS (notifier)                         | IS NOT (other kind)                        |
|---------------------------------------|--------------------------------------------|
| Push message to user email            | Receive HTTP POST from external system     |
| Send SMS to phone number              | Bidirectional event exchange               |
| Post to Slack channel                 | Full API integration with auth flow        |
| Send Firebase push to device          | Background polling or scheduled job        |
| Post Discord embed                    | Protocol server (MCP)                      |
| In-app notification to user session   | Webhook endpoint listening for events      |

## Data Flow (runtime)
```
1. Caller provides: channel, template_vars values, priority override (optional)
2. priority_queue: assign delivery slot by priority level
3. rate_limiter: check bucket, block or pass
4. template_engine: render message from template + vars
5. channel_router: select provider_adapter for channel
6. delivery_engine: POST to provider API
7. On success: log receipt, clear from queue
8. On failure: retry_handler -> retry or dead_letter_queue
```

## Sizing Constraints
- Artifact spec: max 1024 bytes body (compact spec, not implementation)
- No SDK code in spec — provider_adapter is implementation concern
- Notifier spec consumed by: code-gen, agent, manual implementation
## Confusion Zones
| Scenario | Seems Like | Actually Is | Rule |
|---|---|---|---|
| Receive webhook from Slack | notifier | webhook | webhook=inbound event; notifier=outbound push only |
| Send API request to service | notifier | api_client | api_client=request-response; notifier=fire-and-forget |
| Post message to Discord bot | notifier | mcp_server | mcp_server=protocol; notifier=delivery channel |
## Decision Tree
- Push message to user/channel? → notifier
- Receive inbound event? → webhook
- Full API integration? → api_client
- Bidirectional exchange? → connector
## Neighbor Comparison
| Dimension | notifier | webhook | Difference |
|---|---|---|---|
| Direction | Outbound (push) | Inbound (receive) | Opposite data flow |
| Pattern | Fire-and-forget | Event-driven handler | notifier sends; webhook listens |
| Retry | Built-in backoff | Caller retries | Different retry ownership |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[notifier-builder]] | related | 0.59 |
| [[p01_kc_notifier]] | upstream | 0.58 |
| [[p03_sp_notifier_builder]] | related | 0.57 |
| [[bld_collaboration_notifier]] | related | 0.56 |
| [[bld_collaboration_webhook]] | related | 0.52 |
| [[bld_instruction_notifier]] | upstream | 0.52 |
| [[bld_output_template_notifier]] | related | 0.52 |
| [[webhook-builder]] | related | 0.44 |
| [[bld_knowledge_card_notifier]] | related | 0.43 |
| [[bld_examples_notifier]] | related | 0.43 |
