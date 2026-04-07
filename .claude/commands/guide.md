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
- Natural language: "guide me", "ask me first", "let's do this together"

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
