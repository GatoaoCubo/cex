---
id: p01_kc_webhook
kind: knowledge_card
8f: F3_inject
type: kind
pillar: P01
title: "Webhook — Deep Knowledge for webhook"
version: 1.0.0
created: 2026-03-30
updated: 2026-03-30
author: marketing_agent
domain: webhook
quality: 9.1
tags: [webhook, P04, CALL, kind-kc, event-driven]
tldr: "Event-driven HTTP endpoint (inbound receiver or outbound dispatcher) for async agent-to-service or service-to-agent event exchange with typed payload schemas"
when_to_use: "Building, reviewing, or reasoning about webhook artifacts"
keywords: [webhook, event, http, inbound, outbound]
feeds_kinds: [webhook]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - webhook-builder
  - p03_sp_webhook_builder
  - bld_collaboration_webhook
  - bld_architecture_webhook
  - bld_knowledge_card_webhook
  - bld_memory_webhook
  - bld_instruction_webhook
  - bld_examples_webhook
  - bld_output_template_webhook
  - bld_knowledge_card_connector
---

# Webhook

## Spec
```yaml
kind: webhook
pillar: P04
llm_function: CALL
max_bytes: 1024
naming: p04_webhook_{{event}}.md + .json
core: false
```

## What It Is
A webhook is an HTTP endpoint that receives (inbound) or dispatches (outbound) event payloads asynchronously. It processes events from external systems (Stripe, GitHub, WhatsApp) or pushes events to them on agent-triggered conditions. Its boundary is async event exchange — receive fast, process async. It is NOT an api_client (synchronous request/response pattern) nor a notifier (which delivers user-facing messages, not typed system events).

## Cross-Framework Map
| Framework/Provider | Class/Concept | Notes |
|---|---|---|
| LangChain | n/a (no native webhook kind) | FastAPI endpoint + LC callback |
| LlamaIndex | n/a | Custom FastAPI integration |
| CrewAI | n/a | Webhook triggers crew via REST |
| DSPy | n/a | External trigger pattern |
| Haystack | n/a | REST endpoint wrapping Haystack pipeline |
| OpenAI | n/a | Webhook via external server |
| Anthropic | n/a | Webhook via external server |

## Key Parameters
| Parameter | Type | Default | Tradeoff |
|---|---|---|---|
| direction | str | inbound | inbound / outbound / bidirectional |
| event_type | str | required | Typed to specific event schema |
| signature_header | str | null | Required for production inbound security |

## Patterns
| Pattern | When to Use | Example |
|---|---|---|
| Signature verification | All production inbound endpoints | HMAC-SHA256 on X-Signature header |
| Idempotency key | Retry-safe event processing | Store event_id; skip if already seen |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|---|---|---|
| No signature verification | Spoofed events accepted silently | Verify HMAC or bearer token always |
| Sync heavy processing | Webhook timeout (5-10s limit) | Acknowledge immediately; process async |

## Integration Graph
```
[external_event] --> [webhook_receiver] --> [event_queue / agent_trigger]
[agent_event]    --> [webhook_dispatcher] --> [external_service]
```

## Decision Tree
- IF synchronous request-response needed THEN use api_client
- IF user-facing message delivery THEN use notifier
- IF persistent bidirectional stream THEN use dedicated streaming connection
- DEFAULT: webhook for any async HTTP event exchange with external systems

## Quality Criteria
- GOOD: direction set, event_type typed with schema, async handler
- GREAT: HMAC signature verification, idempotency key, retry queue, dead letter
- FAIL: no signature check, synchronous heavy handler, no event schema defined

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[webhook-builder]] | downstream | 0.57 |
| [[p03_sp_webhook_builder]] | downstream | 0.52 |
| [[bld_collaboration_webhook]] | downstream | 0.51 |
| [[bld_architecture_webhook]] | downstream | 0.49 |
| [[bld_knowledge_card_webhook]] | sibling | 0.45 |
| [[bld_memory_webhook]] | downstream | 0.42 |
| [[bld_instruction_webhook]] | downstream | 0.41 |
| [[bld_examples_webhook]] | downstream | 0.39 |
| [[bld_output_template_webhook]] | downstream | 0.37 |
| [[bld_knowledge_card_connector]] | sibling | 0.36 |
