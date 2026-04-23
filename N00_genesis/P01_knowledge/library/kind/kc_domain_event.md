---
id: p01_kc_domain_event
kind: knowledge_card
type: kind
pillar: P01
title: "Domain Event -- Deep Knowledge for domain_event"
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
domain: domain_event
quality: 8.8
tags: [domain_event, p12, CALL, kind-kc, ddd, event-sourcing]
tldr: "Immutable DDD domain event recording a significant business occurrence; owns aggregate root + causal chain; NOT signal (system) nor audit_log (compliance)."
when_to_use: "Building, reviewing, or reasoning about domain_event artifacts in any bounded context"
keywords: [domain-event, ddd, aggregate, immutable, past-tense]
feeds_kinds: [domain_event]
density_score: null
aliases: ["business event", "domain fact", "aggregate event", "DDD event"]
user_says: ["record what happened", "emit an event", "log domain occurrence", "something happened in the domain"]
long_tails: ["capture an immutable record of a business fact that occurred", "model a significant domain occurrence for event sourcing", "publish an event when a business rule completes"]
related:
  - p01_kc_signal
  - bld_instruction_hook
  - bld_collaboration_hook
  - bld_knowledge_card_hook_config
  - bld_output_template_webhook
  - p01_kc_webhook
  - bld_knowledge_card_signal
  - bld_architecture_hook
  - bld_collaboration_webhook
  - bld_knowledge_card_hook
---

# Domain Event

## Spec
```yaml
kind: domain_event
pillar: P12
llm_function: CALL
max_bytes: 3072
naming: de_{aggregate}_{verb_past_tense}.md
```

## What It Is
A domain_event is an immutable record of something significant that happened in the domain, following the Evans DDD 2003 Domain Events pattern. It captures a business fact at the moment it occurred -- not a system-level metric, not a compliance record. The key properties: named in past tense (OrderPlaced, not PlaceOrder), owned by an aggregate root (Order emits OrderPlaced), carries a snapshot payload (data at occurred_at, not current state), and includes a causal chain (causation_id pointing to the command or event that triggered it, correlation_id for saga tracing).

## Boundary
| Aspect | domain_event | signal | audit_log |
|--------|-------------|--------|-----------|
| Origin | Domain model layer | Infrastructure/observability | Compliance layer |
| Business meaning | Required | None | Partial |
| Mutable? | NO | NO | NO |
| Consumer | Other bounded contexts | Monitoring systems | Auditors/regulators |
| DDD pattern | Domain Events | Observability | SOX/GDPR |

## Causal Chain
Every domain_event carries three IDs:
- event_id: identity of this event (auto-generated UUID)
- causation_id: what caused this event (prior command or event ID)
- correlation_id: saga or trace identifier that groups related events

This enables distributed tracing across multiple bounded contexts without tight coupling.

## Event Schema Evolution
- v1 -> v2: additive fields only (never remove, never rename existing fields)
- Breaking change: new event type name (OrderPlacedV2 is wrong; use OrderConfirmed)
- Consumers must handle unknown fields (open/closed world assumption: open)
- Schema registry (Avro/Protobuf) stores each event_version independently

## Event Sourcing Pattern
domain_event is the primary record in event sourcing:
`aggregate_state = fold(initial_state, [domain_events])`
CEX does not mandate event store, but domain_event schema is compatible with:
- EventStoreDB: native DDD event store
- Kafka + Avro: streaming event bus
- DynamoDB Streams: serverless event sourcing

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Imperative name (ProcessOrder) | Not a fact; command disguised as event | Past tense: OrderProcessed |
| Mutable payload (foreign key only) | Cannot reconstruct state without joins | Snapshot all relevant data at occurred_at |
| System event as domain event (CronJobFired) | No business meaning | Use signal kind for system telemetry |
| Event without aggregate | Orphan event; no ownership | Identify the aggregate root first |

## Decision Tree
- IF significant business fact occurred -> domain_event
- IF system health metric emitted -> signal
- IF compliance record required -> audit_log
- IF data crossing bounded context boundary -> domain_event + data_contract
- IF processing instruction for another system -> command (NOT event)
- DEFAULT: domain_event for any past-tense business occurrence with aggregate root

## Quality Criteria
- GOOD: past tense name, aggregate_root, occurred_at, typed payload, >= 1 causal ID
- GREAT: full causal chain + consumers documented + business invariants + schema_ref
- FAIL: imperative name OR missing aggregate_root OR mutable payload OR no occurred_at

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_signal]] | sibling | 0.40 |
| [[bld_instruction_hook]] | downstream | 0.30 |
| [[bld_collaboration_hook]] | downstream | 0.27 |
| [[bld_knowledge_card_hook_config]] | sibling | 0.24 |
| [[bld_output_template_webhook]] | downstream | 0.24 |
| [[p01_kc_webhook]] | sibling | 0.24 |
| [[bld_knowledge_card_signal]] | sibling | 0.23 |
| [[bld_architecture_hook]] | downstream | 0.23 |
| [[bld_collaboration_webhook]] | downstream | 0.23 |
| [[bld_knowledge_card_hook]] | sibling | 0.23 |
