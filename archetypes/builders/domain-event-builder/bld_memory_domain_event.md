---
id: bld_memory_domain_event
kind: entity_memory
pillar: P10
llm_function: INJECT
version: 1.0.0
quality: null
tags: [domain_event, memory, patterns]
title: "Memory Patterns: domain_event"
---
# Memory Patterns: domain_event
## What to Remember
- Event naming: ALWAYS past tense. OrderPlaced NOT PlaceOrder
- Aggregate ownership: each event belongs to EXACTLY ONE aggregate root
- Payload immutability: record state AT occurrence_time, never current state
- Causation chain: event_id -> causation_id -> correlation_id (tracing backbone)

## Common Mistakes to Avoid
| Mistake | Correction |
|---------|-----------|
| Command as event name (ProcessPayment) | Past tense (PaymentProcessed) |
| Missing aggregate_root | Always name the DDD aggregate |
| Mutable payload field | Snapshot only, freeze at occurred_at |
| Conflating with signal | Check: is it business-meaningful? -> domain_event |

## Cross-Kind Memory
- data_contract: publish domain_event schema to consumers via data_contract
- bounded_context: domain_events are scoped to their bounded_context
- workflow: domain_events trigger workflows (one-way dependency)
- audit_log: downstream consumers may convert domain_events to audit_log

## Reuse Signals
Search for existing domain_events before creating new ones:
- grep P12 for de_ prefix files
- check bounded_context event catalog if it exists
