---
id: p08_pat_crew_dispatch
kind: pattern
pillar: P08
version: "1.0.0"
created: "2026-03-30"
updated: "2026-03-30"
author: "pattern-builder"
domain: "orchestration"
quality: 9.1
tags: [pattern, crew, dispatch, orchestration, quality-assurance, multi-agent]
tldr: "Spawn builder+validator sub-agents in sequence per artifact; orchestrator accepts, revises, or rebuilds based on validator result."
name: "Crew Dispatch"
problem: "Whenever a single agent both produces and validates an artifact, production and quality-assurance are conflated, producing no independent check on gate compliance."
solution: "Orchestrator writes handoff, spawns kind-builder (8F, quality: 9.1), then spawns validator; validator score drives accept/revise/rebuild."
context: "Multi-agent orchestration where artifact quality must be verified by an independent agent before acceptance."
forces: ["production speed vs quality independence", "autonomy vs coordination overhead", "sequential crew dependency vs parallel grid throughput"]
consequences: ["independent gate catches builder blind spots", "two spawn cycles per artifact", "auditable validator signal", "parallel crews scale throughput at RAM cost"]
related_patterns: [p08_pat_continuous_batching, p08_pat_construction_triad]
anti_patterns: ["self-validation", "inline review", "skip validator on time pressure"]
applicability: "Use for every production artifact build. Do NOT use for ephemeral scratch files or rapid prototypes below quality threshold."
keywords: [crew, dispatch, builder, validator, orchestrator, handoff, quality-gate, spawn]
---

## Problem

Whenever a single agent produces and validates an artifact, blind spots in production go undetected in review. This recurs on every build where producer and checker are the same entity — systematic gate undercount and false confidence.

## Context

- CEX orchestration layer (N07 or N03) managing builds via spawn scripts
- Every production build where quality gates are contractual
- Without independent validation, H01-H07 failures reach consumers

## Forces

- **Speed vs independence**: single agent is fastest; independent validation adds a spawn cycle
- **Autonomy vs coordination**: sub-agents run headless; orchestrator must write handoffs, monitor signals, route results
- **Sequential vs parallel**: builder completes before validator starts; multiple crews run in parallel

## Solution

Two-stage crew per artifact:

1. **Handoff** — orchestrator writes `.cex/runtime/handoffs/{mission}_{artifact}.md`
2. **kind-builder** — runs 8F; sets `quality: null`; signals complete
3. **validator** — checks H01-H07 + S01-S06; writes verdict signal
4. **Route** — orchestrator reads verdict:

```text
score >= 8.0 + hard gates pass  -->  ACCEPT (commit)
score 7.0-7.9 / soft fail      -->  REVISE (max 2)
hard fail / score < 7.0        -->  REBUILD
```

```python
handoff = write_handoff(mission, kind, path)
builder = spawn("kind-builder", kind=kind, path=path)
await signal(builder, "complete")
validator = spawn("validator", path=path, kind=kind)
result = await signal(validator, "verdict")
if result.score >= 8.0 and result.hard_pass:
    commit(path)
elif retries < 2:
    re_dispatch(builder, feedback=result.issues)
else:
    rebuild(kind)
```

Parallel: N crews via `spawn_grid.ps1`; each independent, no shared files.

## Consequences

Benefits:
- Independent gate catches builder blind spots before commit
- Structured, auditable validator signal
- Grid dispatch scales throughput with N parallel crews

Costs:
- Two spawn cycles per artifact vs single-agent build
- Orchestrator coordination: handoffs, signals, routing
- Sequential dependency: validator idles while builder runs

## Examples

1. **Single crew**: builder produces `pattern` artifact (8F, quality: null); validator returns 8.5, all gates pass; orchestrator commits.
2. **Grid — 6 crews**: 6 artifacts via `spawn_grid.ps1`; 12 signals monitored; 5 accepted first pass, 1 revised once.

## Anti-Patterns

- **Self-validation**: builder checks own output — blind spots persist; no independent signal
- **Inline review**: orchestrator judges directly — no structured checklist; not reproducible
- **Skip validator on deadline**: hard gate failures enter repo; quality debt compounds

## Variants

- **Single-shot**: no REVISE loop; validator verdict is final. For batch throughput over polish.
- **Async retry queue**: validator runs async; failures queue for next orchestrator cycle.

## Related Patterns

- Continuous Batching (`p08_pat_continuous_batching`): fills slots as crews complete
- Construction Triad (`p08_pat_construction_triad`): builder applies Template-First inside 8F

## References

- `.claude/rules/n03-8f-enforcement.md` — hard gate definitions
- `_spawn/spawn_grid.ps1` — parallel crew launch
- `_docs/PLAYBOOK.md` — handoff format and dispatch workflow
