---
kind: instruction
id: bld_instruction_backpressure_policy
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for backpressure_policy
pattern: 3-phase pipeline (define -> compose -> validate)
quality: 7.1
title: "Instruction Backpressure Policy"
version: "1.0.0"
author: n03_builder
tags: [backpressure_policy, builder, instruction]
tldr: "3-phase: define overflow strategy and buffer, compose with thresholds, validate boundary vs circuit_breaker."
domain: "backpressure policy construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Instructions: How to Produce a backpressure_policy

## Phase 1: DEFINE
1. Identify the producer-consumer pair (e.g. event queue -> LLM processor, API ingest -> database writer)
2. Determine overflow_strategy: what happens when consumer cannot keep up:
   - DROP_LATEST: discard newest items (prefer freshness over completeness)
   - DROP_OLDEST: discard oldest items (prefer recency)
   - BUFFER: accumulate up to buffer_size, then overflow
   - THROTTLE: slow producer to match consumer rate
   - ERROR: raise exception and let caller handle
3. Set buffer_size: maximum items to buffer before overflow activates
4. Set shed_threshold: percentage of buffer capacity at which to start shedding (e.g. 0.8 = start at 80%)
5. Define high_watermark: absolute queue depth triggering active backpressure
6. Define low_watermark: queue depth at which normal flow resumes
7. Set request_batch_size: items requested per demand signal (Reactive Streams model)
8. Specify monitored_queue: which queue/channel/topic this policy governs

## Phase 2: COMPOSE
1. Read SCHEMA.md and OUTPUT_TEMPLATE.md
2. Fill frontmatter: all required fields (quality: null)
3. Set id: `p09_bp_{scope_slug}` -- verify pattern `^p09_bp_[a-z][a-z0-9_]+$`
4. Write Overview section: producer-consumer context and why backpressure is needed
5. Write Strategy section: overflow_strategy with rationale
6. Write Thresholds section: buffer_size, shed_threshold, watermarks
7. Write Flow section: request_batch_size, demand signaling protocol
8. Verify body <= 2048 bytes

## Phase 3: VALIDATE
1. Confirm id matches `^p09_bp_[a-z][a-z0-9_]+$`
2. Confirm kind == backpressure_policy
3. Confirm overflow_strategy is one of: DROP_LATEST, DROP_OLDEST, BUFFER, THROTTLE, ERROR
4. Confirm buffer_size is positive integer
5. Confirm shed_threshold is float in [0.0, 1.0]
6. Confirm all 4 body sections present: Overview, Strategy, Thresholds, Flow
7. Cross-check: not circuit_breaker (no state machine), not rate_limit_config (no RPM/TPM)
8. Confirm quality: null
9. Revise if score < 8.0
