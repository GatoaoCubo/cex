---
kind: collaboration
id: bld_collaboration_webhook
pillar: P04
llm_function: COLLABORATE
version: 1.0.0
created: 2026-03-28
updated: 2026-03-28
author: builder_agent
quality: 9.0
tags: [collaboration, webhook, P04, crew, integration, dependency]
tldr: "webhook-builder crew role: EVENT-DRIVEN HTTP SPECIALIST. Integration Pipeline, Event System, Dual-Direction crew patterns."
density_score: 1.0
title: Collaboration ISO - webhook
---
# Collaboration: webhook-builder
## Crew Role
**Title**: EVENT-DRIVEN HTTP SPECIALIST
**Primary question**: "What events does this endpoint handle, what is the payload schema, and how is it verified and delivered reliably?"
**Produces**: webhook artifact (P04) — event endpoint spec with direction, event types, payload schema, signature verification, retry policy.
**Does NOT produce**: HTTP client calls (api_client), user notifications (notifier), protocol servers (mcp_server), background jobs (daemon).
## Crew Patterns
### Integration Pipeline
Combines event-driven inbound with synchronous outbound and notification delivery.
```
webhook-builder     -> inbound event spec (what we receive)
api-client-builder  -> outbound API call spec (what we call in response)
notifier-builder    -> delivery spec (how we notify end-user of outcome)
```
**Example**: Stripe payment.completed (webhook) -> fetch order details (api_client) -> send receipt email (notifier).
**Handoff**: webhook passes event_type + payload_schema to api_client as trigger context. api_client result feeds notifier as content.
### Event System
Full event infrastructure: inbound capture, internal routing, outbound dispatch.
```
webhook-builder  -> inbound event receiver spec
hook-builder     -> internal lifecycle hook spec (pre/post processing)
daemon-builder   -> persistent event processr spec (consumer loop)
```
**Example**: GitHub push (webhook) -> pre-commit checks (hook) -> CI runner (daemon).
**Handoff**: webhook defines payload schema; hook consumes it as trigger input; daemon receives processed events from hook output queue.
### Dual-Direction Integration
When a system both receives and sends webhooks to the same provider.
```
webhook-builder (inbound)   -> receive provider events
webhook-builder (outbound)  -> send events to provider
api-client-builder          -> synchronous registration/config calls
```
**Example**: Slack app — receives Events API (inbound webhook), sends to Incoming Webhooks URL (outbound webhook), calls Slack REST API (api_client).
## Dependency Map
```
Depends on: NONE — webhook is a base artifact
Depended on by:
  notifier-builder    (webhook event triggers notification)
  hook-builder        (webhook event_type as hook trigger)
  daemon-builder      (webhook payload as queue message format)
  api-client-builder  (webhook event triggers outbound API call)
```
## Handoff Contract
When passing context TO another builder:
```yaml
from: webhook-builder
to: [notifier-builder | api-client-builder | hook-builder]
provides:
  event_type: string
  payload_schema: JSON Schema
  idempotency_key: string
```
When receiving context FROM another builder:
```yaml
from: [api-client-builder | hook-builder]
to: webhook-builder
provides:
  target_url: string
  expected_events: list
```
## Escalation Paths
| Situation | Action |
|-----------|--------|
| Request-response, not event-driven | Redirect to api-client-builder |
| End-user push notification | Redirect to notifier-builder |
| Persistent background processing | Redirect to daemon-builder |
| MCP protocol server | Redirect to mcp-server-builder |
| "Send notification when payment complete" | Clarify: webhook (receive event) + notifier (send to user) |
