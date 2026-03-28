---
kind: architecture
id: bld_architecture_notifier
pillar: P04
llm_function: CONTEXT
purpose: Internal architecture and boundary map for notifier domain
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: EDISON
tags: [architecture, notifier, P04, boundary, components]
quality: null
tldr: "Notifier = push delivery to users/systems. Components: channel_router, template_engine, priority_queue, rate_limiter, delivery_engine, retry_handler, provider_adapter."
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
| template_engine  | Substitutes {{vars}} into message template per channel format    |
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
