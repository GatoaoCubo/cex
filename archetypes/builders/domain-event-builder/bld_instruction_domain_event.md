---
id: bld_instruction_domain_event
kind: instruction
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for domain_event
version: 1.0.0
quality: null
tags: [domain_event, builder, instruction]
title: "Instruction Domain Event Builder"
---
# Instructions: How to Produce a domain_event
## Phase 1: IDENTIFY
1. Name the event in past tense: OrderPlaced, PaymentFailed, UserRegistered
2. Identify the aggregate root that owns this event (Order, Payment, User)
3. Identify the bounded context (sales, billing, identity)
4. Determine event version (start at v1, increment on schema change)
5. Check: is this truly domain-significant, not a system heartbeat or log entry?
## Phase 2: COMPOSE
1. Read bld_schema_domain_event.md for required fields
2. Set id: de_{aggregate}_{past_tense_verb}_{version} (snake_case)
3. Fill payload fields: all data carried by the event at occurrence time
4. Record causation_id (what caused this), correlation_id (saga/trace)
5. Set occurred_at as ISO-8601 UTC timestamp (do NOT use processed_at)
6. Set quality: null -- never self-score
## Phase 3: VALIDATE
1. HARD gates (all must pass):
   - id follows pattern de_{aggregate}_{verb}
   - kind == domain_event
   - quality == null
   - occurred_at is present and ISO-8601
   - aggregate_root is named
   - bounded_context is named
   - payload section present with >= 1 field
2. SOFT gates:
   - causation_id and correlation_id present for traceability
   - event is named in past tense
   - payload fields are typed (string, int, uuid, etc.)
   - consumers array lists subscribing contexts
