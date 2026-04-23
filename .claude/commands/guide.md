---
description: "Guided Decision Mode — ask me before building. Usage: /guide [topic] or /guide <goal>"
quality: 9.0
title: "Guide"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - skill_guided_decisions
  - ctx_cex_new_dev_guide
  - auto-accept-handoff
  - spec_n07_operational_intelligence
  - SPEC_07_gdp_enforcement
  - p03_sp_orchestration_nucleus
  - p01_kc_autonomy
  - p01_kc_cex_as_digital_asset
  - p01_kc_orchestration_best_practices
  - bld_collaboration_contributor_guide
---

# /guide — Co-pilot Mode

> **Industry pattern**: Human-in-the-loop (HITL) via guided workflow.
> **What it does**: Switches from "LLM assumes everything" to "LLM asks, user decides".
> **When it ends**: Decision Manifest is written → execution becomes autonomous.

## Trigger

Any of these activate guided mode:
- `/guide` (alone) — "guide me through whatever comes next"
- `/guide build a landing page` — "guide me through the decisions for THIS goal"
- `/guide brand` — "guide me through brand setup" (same as `/init`)
- `/guide --plan-loop <goal>` — iterate the plan with user until approved (new)
- Natural language: "guide me", "ask me first", "let's do this together"

## --plan-loop (BORIS_MERGE B5)

Use `--plan-loop` when the user wants to iterate on the **spec/plan** itself
before any dispatch. Loop exits only when user says "approved", "go", "dispatch",
or `/auto`. Typical flow:

1. Draft initial plan (waves, nuclei, artifacts) from goal.
2. Show plan; collect feedback (adds/cuts/reorders).
3. Revise plan; show diff.
4. Repeat 2-3 until user approves.
5. Write final spec to `.cex/runtime/plans/plan_<name>.md` and decision manifest.
6. Hand off to `/grid` or `/mission` for execution.

The loop never produces artifacts -- only the plan/spec. Guardrail: max 8
iterations before forcing a summary and requiring explicit continue.

## Behavior

### Step 1: Identify what needs deciding

From the user's goal, list the SUBJECTIVE decisions:

```
━━━ Guide Mode ━━━

Your goal: "build a landing page"

I'll need your input on 4 things before I start:
  1. Who is this for? (audience)
  2. What should it look like? (style/layout)
  3. What's the main message? (hero copy)
  4. What should they do? (CTA)

Everything else — file structure, code, deployment — I handle.

Let's start.
━━━━━━━━━━━━━━━━━━
```

### Step 2: Present Decision Points

Use the GDP format from `skill_guided_decisions.md`:
- 3-5 numbered options per DP
- ★ Recommended with reason
- Freetext always accepted
- 2-3 DPs at a time, preview between rounds

### Step 3: Lock decisions

After all DPs answered → write `.cex/runtime/decisions/decision_manifest.yaml`.
Show Final Review. User confirms.

### Step 4: Execute

Once confirmed → switch to autonomous mode.
If dispatching: `bash _spawn/dispatch.sh solo/grid`
If building in-session: proceed with 8F pipeline using manifest.

## Quick Reference

| User says | What happens |
|-----------|-------------|
| `/guide` | "What are we building? I'll ask before I assume." |
| `/guide build X` | Decompose X → identify DPs → ask → execute |
| `/guide brand` | Redirect to `/init` flow |
| `/build X` (no /guide) | Check if decisions are needed. If yes, trigger GDP automatically. |
| `/mission X` | GDP Phase 1 → Autonomous Phase 2 (already wired) |

## The Rule

**When in doubt, `/guide`. When manifest exists, execute.**

Every subjective decision left to the LLM is a revision the user will need later.
Every decision the user makes upfront is output that matches on the first try.

## Exit Guide Mode

- User says "just do it" or "you decide" → apply all ★ Recommended, flag as auto_filled
- User says "skip" on a DP → apply ★ Recommended for that one
- All DPs answered → guide mode ends automatically
- `/auto` or "go autonomous" → lock manifest as-is, dispatch

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[skill_guided_decisions]] | related | 0.33 |
| [[ctx_cex_new_dev_guide]] | related | 0.32 |
| [[auto-accept-handoff]] | related | 0.29 |
| [[spec_n07_operational_intelligence]] | related | 0.25 |
| [[SPEC_07_gdp_enforcement]] | related | 0.25 |
| [[p03_sp_orchestration_nucleus]] | related | 0.24 |
| [[p01_kc_autonomy]] | related | 0.23 |
| [[p01_kc_cex_as_digital_asset]] | related | 0.23 |
| [[p01_kc_orchestration_best_practices]] | related | 0.22 |
| [[bld_collaboration_contributor_guide]] | related | 0.22 |
