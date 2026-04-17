---
id: p10_lr_backpressure_policy_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
observation: "Backpressure configs missing low_watermark caused oscillation: systems alternated rapidly between backpressure and free-flow states without stable recovery. Configs with shed_threshold > 0.95 provided no protection -- buffer was already 95% full before any action. DROP_LATEST without documenting data loss caused 3 production incidents where engineers assumed no data was lost."
pattern: "Set shed_threshold at 0.7-0.8 for early protection. Always set low_watermark at 40-60% of buffer_size for hysteresis. Document data loss risk explicitly for DROP strategies. THROTTLE is safest for pipelines where data loss is unacceptable."
evidence: "Oscillation: 4 configs missing low_watermark all showed rapid state flapping. Threshold: 2 configs with 0.95 threshold gave zero protection. Data loss: 3 incidents all lacked explicit data loss documentation."
confidence: 0.85
outcome: SUCCESS
domain: backpressure_policy
tags: [backpressure, overflow, watermark, shed-threshold, drop-strategy, reactive-streams]
tldr: "70-80% shed threshold + low_watermark hysteresis + explicit data loss docs = stable flow control."
impact_score: 8.5
decay_rate: 0.03
agent_group: edison
keywords: [backpressure, overflow strategy, buffer, watermark, shed threshold, reactive streams, consumer lag]
memory_scope: project
observation_types: [feedback, project]
quality: null
title: "Memory Backpressure Policy"
density_score: 0.90
llm_function: INJECT
---
## Summary

Backpressure policies only work when they activate early enough and recover stably.
Too-late thresholds (> 90%) mean the buffer is already overflowing before any action.
Missing low_watermark creates ping-pong between backpressure and free-flow states.

## Pattern
**70-80% threshold + hysteresis gap + data loss documentation.**

Threshold discipline:
1. shed_threshold: 0.7-0.8 for early protection; 0.5 for latency-sensitive pipelines
2. high_watermark = shed_threshold * buffer_size (must be consistent)
3. low_watermark = 0.4-0.6 * buffer_size (40-60% gap from high for stable recovery)

Strategy selection:
1. THROTTLE: when producer rate is controllable and data loss is unacceptable
2. DROP_LATEST: when newest data can be discarded (metrics, heartbeats, deduplicable)
3. DROP_OLDEST: when in-flight work must complete and new requests can be rejected
4. BUFFER: for short-lived bursts with predictable recovery (< 30s)
5. ERROR: when caller must explicitly handle overflow (payment processing, audit logs)

Documentation discipline:
1. Always state data loss risk for DROP strategies
2. Document which queue/channel is monitored (monitored_queue)
3. Declare consumer lag SLA -- what is acceptable maximum lag

## Anti-Pattern
1. shed_threshold: 0.99 -- buffer overflows before policy activates
2. No low_watermark -- system oscillates rapidly between states
3. DROP without documentation -- engineers assume no data loss in incidents
4. Same policy for all queues -- LLM jobs, metrics, and audit logs need different strategies
5. buffer_size: 10000 without memory budget -- 10K large objects causes OOM
