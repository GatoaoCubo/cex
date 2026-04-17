---
id: bld_rules_event_stream
kind: knowledge_card
pillar: P04
title: "Event Stream Builder -- Rules"
version: 1.0.0
quality: null
tags: [builder, event_stream, rules]
llm_function: CONSTRAIN
---
# Rules: event_stream
## Absolute Rules (HARD -- never violate)
1. Partition key must be defined: never use round-robin for entity-ordered events.
2. Retention must include both time (hours) and bytes: one alone is incomplete.
3. Delivery semantics must be explicit: ambiguous delivery causes data loss or duplication.
4. Every consumer that needs independent offset tracking must be a separate consumer group.
5. Schema format must be specified: untyped event streams are a maintenance hazard.
6. quality: null always -- never self-score.
## Soft Rules (RECOMMEND)
1. Use BACKWARD compatibility mode by default: allows adding optional fields without breaking consumers.
2. Monitoring lag threshold should be <= 10% of expected throughput-to-processing ratio.
3. Retention: default 168 hours (7 days) unless replay requirements dictate more.
4. Partition count: right-size to throughput estimate, not maximum possible.
## Boundary Rules
1. THIS BUILDER handles: event_stream (P04)
2. NOT this builder: webhook (single outbound HTTP push) -> webhook-builder
3. NOT this builder: signal (internal CEX nucleus signal) -> not a user-facing kind
4. NOT this builder: process_manager (event routing + state machine) -> process-manager-builder
5. NOT this builder: api_client (HTTP consumer) -> api-client-builder
## CEX-Specific Rules
1. id pattern: p04_es_{slug} -- always prefix p04_es_
2. Pillar: always P04 (Tools)
3. Producing nucleus: N05 (Operations) for infra config, N03 for domain design
4. max_bytes: 3072
