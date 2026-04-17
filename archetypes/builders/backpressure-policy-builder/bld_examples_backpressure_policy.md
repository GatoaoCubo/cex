---
kind: examples
id: bld_examples_backpressure_policy
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of backpressure_policy artifacts
pattern: few-shot learning -- LLM reads these before producing
quality: 8.6
title: "Examples Backpressure Policy"
version: "1.0.0"
author: n03_builder
tags: [backpressure_policy, builder, examples]
tldr: "Golden and anti-examples for backpressure_policy construction: overflow strategy, buffer, watermarks."
domain: "backpressure policy construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Examples: backpressure-policy-builder

## Golden Example
INPUT: "Create backpressure policy for LLM job queue"
OUTPUT:
```yaml
id: p09_bp_llm_job_queue
kind: backpressure_policy
pillar: P09
version: "1.0.0"
created: "2026-04-17"
updated: "2026-04-17"
author: "builder_agent"
overflow_strategy: "DROP_LATEST"
buffer_size: 100
shed_threshold: 0.8
high_watermark: 80
low_watermark: 40
request_batch_size: 5
monitored_queue: "llm_job_queue"
quality: null
tags: [backpressure_policy, llm_job_queue, reactive_streams]
tldr: "LLM job queue: DROP_LATEST at 80% capacity; 5-item batches; resume at 40 items"
```

## Overview
Controls flow for the async LLM job processing queue. When the consumer (LLM processor)
lags behind the producer (API ingest), drops newest requests to protect queue stability.

## Strategy
**Overflow strategy**: DROP_LATEST
Rationale: LLM jobs are user requests; newest duplicates are more likely to be retried
by the client than oldest queued items. Dropping newest preserves in-flight work.

| Strategy | Behavior | Data loss risk |
|----------|----------|---------------|
| DROP_LATEST | New jobs rejected when buffer >= 80% | Medium -- new requests rejected |

## Thresholds
- Buffer capacity: 100 items
- Shedding begins at: 80% (80 items)
- Active backpressure (high watermark): 80 items
- Normal flow resumes (low watermark): 40 items

## Flow
- Demand signal batch size: 5 items per request
- Protocol: Reactive Streams
- Queue monitored: llm_job_queue
- Consumer lag SLA: < 30 seconds per job

WHY THIS IS GOLDEN:
- overflow_strategy: DROP_LATEST (valid enum value) -- H07 pass
- buffer_size: 100 (positive integer) -- H08 pass
- shed_threshold: 0.8 (float in [0.0, 1.0]) -- H09 pass
- All 4 body sections present -- H10 pass
- quality: null -- H05 pass
- id matches ^p09_bp_ pattern -- H02 pass
- high_watermark (80) == shed_threshold (0.8) * buffer_size (100) -- consistent
- low_watermark (40) < high_watermark (80) -- valid hysteresis window

## Anti-Example
INPUT: "Create backpressure for my queue"
BAD OUTPUT:
```yaml
id: my-queue-backpressure
kind: flow-policy
overflow_strategy: "slow it down"
buffer_size: -50
shed_threshold: 1.5
quality: 8.0
tags: [queue]
```
FAILURES:
1. id: "my-queue-backpressure" has hyphens, no p09_bp_ prefix -> H02 FAIL
2. kind: "flow-policy" not "backpressure_policy" -> H04 FAIL
3. overflow_strategy: "slow it down" not in enum -> H07 FAIL
4. buffer_size: -50 is negative -> H08 FAIL
5. shed_threshold: 1.5 not in [0.0, 1.0] -> H09 FAIL
6. quality: 8.0 (not null) -> H05 FAIL
7. Missing monitored_queue, pillar, version, tags -- H06 FAIL
8. Missing all 4 body sections -- H10 FAIL
