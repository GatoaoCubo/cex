---
id: auto-accept-handoff
kind: runtime_rule
pillar: P12
description: "--auto-accept semantics: after manifest, nucleus executes without re-prompting."
quality: null
title: "Auto-Accept Handoff"
version: "1.0.0"
author: n03_builder
tags: [rule, dispatch, autonomy, boris_merge]
tldr: "Handoffs with --auto-accept carry the authority to override any remaining subjective gate; used after manifest lock."
domain: "CEX system"
created: "2026-04-15"
updated: "2026-04-15"
density_score: 0.88
---

# --auto-accept Handoff Flag

## The Problem

After GDP decisions are written to `decision_manifest.yaml`, nuclei still
sometimes stall on **unexpected** subjective choices at F4 REASON
(e.g. a new GDP gate introduced mid-flight). This halts grid execution
and breaks the "dispatched nuclei never ask the user" rule.

## The Rule

Handoff frontmatter MAY include `auto_accept: true`. When set:

1. Nucleus reads `decision_manifest.yaml` normally.
2. For any subjective decision **not covered** by the manifest:
   - Apply the builder's `* Recommended` default.
   - Log the auto-filled choice to `.cex/runtime/decisions/autofilled/<timestamp>_<nucleus>.yaml`
   - Continue 8F without stopping.
3. Nucleus NEVER re-prompts user under any circumstance.
4. At F8 COLLABORATE, the autofilled log gets linked in the commit message.

## Frontmatter Form

```yaml
---
nucleus: n03
task: dispatch
created: 2026-04-15T16:10:00-03:00
auto_accept: true            # <-- new
auto_accept_reason: "BORIS_MERGE manifest locked; GDP frozen"
---
```

## Propagation

- `dispatch.sh` forwards the flag via env `CEX_AUTO_ACCEPT=1` to boot wrappers.
- Boot wrappers (`boot/n0X_*.ps1`) export it into the nucleus session.
- Nuclei check `CEX_AUTO_ACCEPT` before any GDP gate at F4.

## Guardrails

1. `auto_accept` is **not** a bypass of H01-H07 quality gates -- F7 still blocks.
2. Autofilled decisions are auditable via `.cex/runtime/decisions/autofilled/`.
3. N07 MAY retroactively override by editing the manifest and re-dispatching.
4. If a nucleus cannot find any reasonable default (no * Recommended exists),
   it writes a `BLOCKED` signal instead of asking -- N07 decides next step.

## When to use

| Situation | auto_accept? |
|-----------|--------------|
| Grid dispatch of 6 nuclei in wave | YES (manifest is locked) |
| Overnight `/mission evolve` | YES (user not present) |
| Solo interactive `/dispatch n03 "task"` | NO (user is there) |
| `/guide --plan-loop` resume | NO (explicit iteration) |
| Autonomous loops (`ScheduleWakeup` fired) | YES |

## Relation to GDP (guided-decisions.md)

GDP decides **what** (user owns subjective choices).
`auto_accept` decides **how to handle gaps** in the manifest (LLM owns defaults).
The two coexist: manifest answers what it covers, auto_accept fills the rest.

## Interaction with shared-file-proposal

`auto_accept` does NOT authorize direct edits to protected shared files --
proposals still required. Autonomy is about decisions, not about merge safety.

## Example (BORIS_MERGE Wave B handoff)

```yaml
---
nucleus: n03
task: BORIS_MERGE_WAVE_B
auto_accept: true
auto_accept_reason: "Wave B decisions locked in plan_boris_merge.md"
---
# Task
Execute B1-B8 as specified. Any open gate: apply * Recommended + log.
```
