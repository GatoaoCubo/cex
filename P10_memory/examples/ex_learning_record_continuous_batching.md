---
id: p10_lr_continuous_batching
kind: learning_record
pillar: P10
title: "Learning: Continuous Batching Performance"
version: 1.0.0
created: 2026-03-05
updated: 2026-03-22
author: orchestrator
quality: 9.0
tags: [continuous-batching, spawn, performance, learning, memory]
tldr: "Continuous batching 1.6x faster than static grid — speed depends on task complexity not model, opus beat sonnet"
density_score: 0.91
decay: 90
source: organization-core/.claude/projects/memory/MEMORY.md
---

# Learning: Continuous Batching Performance

## Event

| Property | Value |
|----------|-------|
| Task | ISOFIX 7/7 batches + CBTEST mixed 3 agent_groups |
| Agent_group | orchestrator (orchestrator) |
| Date | 2026-03-05 |
| Outcome | success |
| Score | 9.0 |

## What Happened

Continuous batching mode (`spawn_grid.ps1 -mode continuous`) was tested with ISOFIX (7 batches, single sat) and CBTEST (mixed research_agent+builder_agent+knowledge_agent). ISOFIX achieved 1.6x speedup over static grid. CBTEST confirmed zero git lock contention at 3 concurrent agent_groups.

## Pattern (success)

| Step | Action | Why It Worked |
|------|--------|---------------|
| 1 | Handoff naming `{MISSION}_batch_{N}_{SAT}.md` | Auto-refill detected batch files by naming convention |
| 2 | Signal-based slot detection `{sat}_complete_{ts}.json` | No polling needed, filesystem signals are atomic |
| 3 | Max 3 concurrent agent_groups | Stayed under 4-terminal BSOD threshold |

## Anti-Pattern (observed)

| Symptom | Root Cause | Fix |
|---------|-----------|-----|
| Expected opus slower than sonnet | Assumed model size = latency | Speed = task complexity, not model. Opus was faster on simpler ISO tasks |

## Evidence

- Input: 7 ISOFIX batches (9 agents each), 6 CBTEST batches (3 sats)
- Output: All batches completed, zero git contention, all signals received
- Metric: 1.6x speedup (ISOFIX), 3 sats confirmed (CBTEST)

## Propagation

- Applies to: Any multi-batch dispatch with > 6 tasks
- Does NOT apply to: Single-task solo spawns, tasks requiring serial dependency

---
*Migrated from: organization MEMORY.md (Dispatch Modes section, tested 2026-03-05)*
