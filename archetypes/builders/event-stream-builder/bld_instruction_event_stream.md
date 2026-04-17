---
id: bld_instruction_event_stream
kind: instruction
pillar: P04
title: "Event Stream Builder -- Instruction"
version: 1.0.0
quality: 5.4
tags: [builder, event_stream, instruction]
llm_function: REASON
density_score: 0.83
updated: "2026-04-17"
---
# Instructions: How to Produce an event_stream
## Phase 1: RESEARCH
1. Identify the domain events flowing through this stream -- what facts are being published?
2. Determine the producer: which service or aggregate emits events to this stream?
3. Determine consumers: which services subscribe and what consumer groups do they form?
4. Decide partitioning strategy: what is the partition key? (orderId, userId, etc.)
5. Set retention policy: how long must events be retained? (reprocessing, audit, replay)
6. Choose delivery semantics: at-most-once, at-least-once, or exactly-once?
7. Define schema: what is the event envelope format (Avro, Protobuf, JSON Schema)?
## Phase 2: COMPOSE
1. Read bld_schema_event_stream.md -- source of truth for required fields
2. Fill frontmatter: id pattern p04_es_{slug}, kind: event_stream, quality: null
3. Write Producer section: who writes to this stream, at what rate
4. Write Consumer Groups section: each group with offset policy and lag tolerance
5. Write Partitioning section: key, count, ordering guarantee
6. Write Retention section: time + bytes, replay window
7. Write Schema section: format, registry, compatibility mode
8. Write Operations section: monitoring, alerting, lag thresholds
## Phase 3: VALIDATE
1. HARD gates: id matches `p04_es_[a-z][a-z0-9_]+`, kind == event_stream, quality == null
2. Producer and at least one consumer group defined
3. Partition key and count specified
4. Retention policy defined (time AND bytes)
5. Delivery semantics specified
