---
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of pattern artifacts
pattern: few-shot learning — LLM reads these before producing
---

# Examples: pattern-builder

## Golden Example

INPUT: "Document the Continuous Batching pattern for multi-satellite task processing"

OUTPUT:

```yaml
---
id: p08_pat_continuous_batching
kind: pattern
pillar: P08
version: "1.0.0"
created: "2026-03-26"
updated: "2026-03-26"
author: "builder"
domain: "orchestration"
quality: null
tags: [pattern, batching, orchestration, parallel, multi-satellite]
tldr: "Auto-refill satellite slots from queue as tasks complete, eliminating idle time between waves"
name: "Continuous Batching"
problem: "Sequential wave execution leaves satellites idle between batches"
solution: "Auto-refill available slots from a queue as each satellite completes"
context: "Multi-satellite orchestration with >6 independent tasks"
forces: ["throughput vs resource limits", "parallelism vs git contention", "queue depth vs RAM ceiling"]
consequences: ["1.6x speedup over sequential", "zero idle between waves", "requires independent tasks", "max 3 concurrent satellites (RAM)"]
related_patterns: [p08_pat_wave_execution, p08_pat_signal_monitor]
anti_patterns: ["manual slot management", "unbounded parallelism"]
applicability: "Use when >6 independent tasks across <=3 satellites. Do NOT use for dependent tasks or shared-file edits."
keywords: [batching, parallel, queue, throughput, spawn]
---
```

## Problem
When orchestrating multi-satellite work in waves (batch N completes, then batch N+1 starts), satellites sit idle between waves. If batch 1 has 3 tasks finishing at different times, the fastest satellite waits for the slowest before batch 2 begins.

## Context
- Environment: Orchestrator managing 2-3 satellites via spawn scripts
- Frequency: every multi-satellite mission with >6 tasks
- Severity: 40% throughput waste in sequential wave execution

## Forces
- **Throughput vs resources**: more parallelism = faster, but RAM limits to 3 satellites
- **Independence vs contention**: parallel tasks must not edit same files (git conflicts)
- **Queue depth vs complexity**: deeper queues need naming conventions and signal tracking

## Solution
Replace static wave execution with a queue-drain loop:
1. Fill all available slots (up to 3) with tasks from queue
2. Monitor signals for completion (poll every 15s)
3. When a satellite completes, immediately assign next queued task
4. Repeat until queue empty

```text
Queue: [T1, T2, T3, T4, T5, T6, T7]
Slots: [SAT_A, SAT_B, SAT_C]

T=0:  SAT_A=T1, SAT_B=T2, SAT_C=T3  (queue: T4-T7)
T=5:  SAT_A done -> SAT_A=T4          (queue: T5-T7)
T=8:  SAT_C done -> SAT_C=T5          (queue: T6-T7)
...continues until queue empty
```

## Consequences
Benefits:
- 1.6x throughput over sequential waves (measured on ISOFIX 7/7)
- Zero idle time between task completions
- Auto-scales to available slots

Costs:
- Tasks MUST be independent (no shared file edits)
- Requires signal monitoring infrastructure
- Naming convention overhead ({MISSION}_batch_{N}_{SAT}.md)

## Examples
1. **ISOFIX Mission**: 7 batches across researcher+builder+knowledge-engine, 1.6x speedup confirmed
2. **CBTEST Mixed**: 3 satellites, mixed complexity, zero git contention

## Anti-Patterns
- **Manual Slot Management**: manually tracking which satellite is free wastes orchestrator time
- **Unbounded Parallelism**: launching >3 satellites causes BSOD (RAM exhaustion)

## Related Patterns
- Wave Execution: predecessor pattern (static batches); continuous batching improves on it
- Signal Monitor: required infrastructure for detecting slot availability

## References
- records/skills/continuous_batching/SKILL.md
- spawn_grid.ps1 -mode continuous

WHY THIS IS GOLDEN:
- quality: null (H05 pass)
- id matches p08_pat_ pattern (H02 pass)
- kind: pattern (H04 pass)
- 21 fields present including all 14 required (H06 pass)
- name: 2 words "Continuous Batching" (H08 pass)
- problem describes recurring situation (H09 pass)
- forces has 3 tensions (S02 pass)
- consequences has 2 costs (S03 pass)
- Examples has 2 applications (S04 pass)
- All 9 body sections present (S07 pass)

## Anti-Example

INPUT: "Document the batching approach"

BAD OUTPUT:
```yaml
---
id: batching
kind: approach
quality: 9.0
name: "batching"
problem: "things are slow"
---

Batching is a great way to speed things up. You should use batching whenever
possible because it makes everything faster and more efficient.
In conclusion, batching is recommended for all workloads.
```

FAILURES:
1. id: no `p08_pat_` prefix -> H02 FAIL
2. kind: "approach" not "pattern" -> H04 FAIL
3. quality: 9.0 (self-assigned) -> H05 FAIL
4. name: 1 word, not descriptive enough -> H08 FAIL
5. problem: "things are slow" is not concrete recurring situation -> H09 FAIL
6. Missing required fields: pillar, version, created, updated, author, domain, tags, tldr, solution -> H06 FAIL
7. No forces section -> S02 FAIL
8. No consequences (only benefits claimed) -> S03 FAIL
9. Body is filler prose ("great way", "whenever possible", "in conclusion") -> S08 FAIL
10. No body sections (Problem, Context, Forces, etc.) -> S07 FAIL
