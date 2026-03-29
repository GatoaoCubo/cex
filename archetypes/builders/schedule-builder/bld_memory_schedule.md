---
id: p10_lr_schedule_builder
kind: learning_record
pillar: P10
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: edison
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
satellite: edison
keywords: [schedule, timezone, catch up, jitter, concurrent, cron expression, DST, backfill, thundering herd, workflow ref]
---

## Summary
Schedules have three silent failure modes that only appear in production: timezone drift on DST transitions, catch-up bursts after downtime, and thundering herd from synchronized starts. All three are preventable at spec time with four field decisions: timezone (explicit IANA), catch_up (false by default), max_concurrent (1 by default), and jitter (0-Ns for shared infra).
A schedule that omits timezone relies on the server's local time — which shifts by 1 hour twice yearly on DST-observing timezones. A schedule with catch_up: true after a 2-week maintenance window fires every missed interval simultaneously. A set of 10 schedules all starting at 09:00:00.000 hammers the database with simultaneous connections.
## Pattern
**Defensive schedule defaults.**
Timezone rule:
- Always write full IANA name: "America/Sao_Paulo", "Europe/London", "UTC"
- Never write offset strings: "UTC-3", "BRT" — these do not handle DST
- UTC is a valid explicit choice for data pipelines where DST is irrelevant
Catch-up rule:
- Default: false — missed runs are skipped
- Set true only when: data has partitions that must be processed for every interval (e.g., daily ETL with partition keys)
- If true: always set max_concurrent low and add circuit-breaker in the workflow
Max-concurrent rule:
- Default: 1 — prevents resource exhaustion and output corruption from parallel writes
- Set > 1 only when: workflow is stateless, idempotent, and writes to separate partitions
- Document the idempotency proof in ## Policy rationale
Jitter rule:
- Required when: >= 2 schedules share a database, cache, or API rate limit
- Range: 0 to (inter-schedule gap / number of schedules) — e.g., 8 schedules in same minute = 0-7s each
- Implementation: scheduler adds random delay in [0, jitter_max] before firing
## Anti-Pattern
- Omitting timezone (DST silent shift, off-by-1h errors, corrupted time-partitioned outputs).
- catch_up: true with no max_concurrent cap (restart after outage fires unbounded parallel runs).
- max_concurrent > 1 on workflows that write to shared state (parallel writes produce corrupt output).
- No jitter on co-located schedules (thundering herd — all N schedules hit DB at same millisecond).
- workflow_ref pointing to a non-existent or renamed workflow (schedule fires but nothing runs; silent failure).
- Cron expression without plain-English annotation (0 0 */2 * * is ambiguous — every 2 days or every 2 months?).
## Context
The 1024-byte body limit for schedule forces discipline: Overview (80 bytes), Trigger (200 bytes), Workflow (200 bytes), Policy (400 bytes) = ~880 bytes with 144 bytes margin. Policy is the most valuable section — it documents four decisions (catch_up, max_concurrent, jitter, on-failure) that determine whether the schedule is safe in production. Allocate budget accordingly.
