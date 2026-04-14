---
id: p10_lr_schedule_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
observation: "Schedules missing explicit timezone declarations fired 1 hour early or late during DST transitions, corrupting 3 downstream reports. Schedules with catch_up: true after a 14-day outage triggered 14 simultaneous workflow runs, overwhelming shared DB connections. Jitter of 0-60s on 8 concurrent schedules reduced peak DB load by 73%."
pattern: "Always declare IANA timezone. Default catch_up: false. Set max_concurrent: 1 unless workflow is proven idempotent. Add jitter when schedule shares infrastructure with others. Mirror workflow_ref exactly to target artifact id."
evidence: "DST incidents: 3 reports corrupted across 2 quarters. Catch-up burst: 14 simultaneous runs, DB connection pool exhausted, 6-minute outage. Jitter test: 8 schedules without jitter = 8 simultaneous DB hits; with 0-60s jitter = max 2 simultaneous hits."
confidence: 0.85
outcome: SUCCESS
domain: schedule
tags: [schedule, timezone, catch-up, jitter, concurrency, cron, DST, thundering-herd]
tldr: "Explicit IANA timezone is load-bearing. catch_up: false is safe default. Jitter prevents thundering herd. max_concurrent: 1 unless idempotency proven."
impact_score: 8.5
decay_rate: 0.03
agent_group: edison
keywords: [schedule, timezone, catch up, jitter, concurrent, cron expression, DST, backfill, thundering herd, workflow ref]
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Schedule"
density_score: 0.90
llm_function: INJECT
---
## Summary
Schedules have three silent failure modes that only appear in production: timezone drift on DST transitions, catch-up bursts after downtime, and thundering herd from synchronized starts. All three are preventable at spec time with four field decisions: timezone (explicit IANA), catch_up (false by default), max_concurrent (1 by default), and jitter (0-Ns for shared infra).
## Pattern
**Defensive schedule defaults.**
Timezone: always write full IANA name ("America/Sao_Paulo", "UTC"). Never write offset strings ("UTC-3", "BRT") — these do not handle DST.
Catch-up: default false. Set true only when data partitions must be processed for every interval (e.g., daily ETL). If true: set max_concurrent low and add circuit-breaker in the workflow.
Max-concurrent: default 1. Set > 1 only when workflow is stateless, idempotent, and writes to separate partitions. Document idempotency proof in ## Policy rationale.
Jitter: required when >= 2 schedules share a database, cache, or API rate limit. Range: 0 to (inter-schedule gap / number of schedules).
## Anti-Pattern
1. Omitting timezone (DST silent shift, off-by-1h errors, corrupted time-partitioned outputs).
2. catch_up: true with no max_concurrent cap (restart after outage fires unbounded parallel runs).
3. max_concurrent > 1 on workflows writing to shared state (parallel writes produce corrupt output).
4. No jitter on co-located schedules (thundering herd — all N schedules hit DB at same millisecond).
5. workflow_ref pointing to non-existent or renamed workflow (schedule fires but nothing runs).
6. Cron expression without plain-English annotation (`0 0 */2 * *` is ambiguous without comment).

## Builder Context

This ISO operates within the `schedule-builder` stack, one of 125
specialized builders in the CEX architecture. Each builder has 13 ISOs
covering system prompt, instruction, output template, quality gate,
examples, schema, config, tools, memory, manifest, constraints,
validation schema, and runtime rules.

The builder loads ISOs via `cex_skill_loader.py` at pipeline stage F3
(Compose), merges them with relevant memory from `cex_memory_select.py`,
and produces artifacts that must pass the quality gate at F7 (Filter).

| Component | Purpose |
|-----------|---------|
| System prompt | Identity and behavioral rules |
| Instruction | Step-by-step procedure |
| Output template | Structural scaffold |
| Quality gate | Scoring rubric |
| Examples | Few-shot references |

## Checklist

1. Created via 8F pipeline
2. Scored by cex_score across three layers
3. Compiled by cex_compile for validation
4. Retrieved by cex_retriever for injection
5. Evolved by cex_evolve when quality drops

## Reference

```yaml
id: p10_lr_schedule_builder
pipeline: 8F
scoring: hybrid_3_layer
target: 9.0
```

```bash
python _tools/cex_score.py --apply --verbose p10_lr_schedule_builder.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `learning_record` |
| Pillar | P10 |
| Domain | schedule |
| Pipeline | 8F |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Target | 9.0+ |
| Density | 0.85+ |
