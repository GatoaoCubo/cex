---
glob: "**"
alwaysApply: true
description: "Guided Decision Protocol — the balance between co-pilot and autonomous execution"
quality: 9.0
title: "Guided-Decisions"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - auto-accept-handoff
  - p03_sp_orchestration_nucleus
  - p01_kc_orchestration_best_practices
  - skill_guided_decisions
  - SPEC_07_gdp_enforcement
  - output_grid_test_n02
  - p08_ac_orchestrator
  - p12_wf_orchestration_pipeline
  - grid_test_20260407
  - p06_is_orchestration_dispatch
---

# Guided Decision Protocol (GDP)

**As mandatory as 8F. 8F controls HOW to build. GDP controls WHO decides WHAT.**

## The Two Modes

```
┌─────────────────────────────────────────────────────┐
│              CEX Operating Modes                     │
│                                                      │
│  CO-PILOT (user present)    AUTONOMOUS (dispatched)  │
│  ├─ /init                   ├─ /grid                 │
│  ├─ /mission (interactive)  ├─ solo dispatch         │
│  ├─ /build (conversational) ├─ 8F pipeline           │
│  │                          │                        │
│  │  GDP ACTIVE              │  GDP OFF               │
│  │  Present options          │  Read manifest          │
│  │  Wait for user            │  Use decisions          │
│  │  Write manifest           │  Execute autonomously   │
│  └──────────┬───────────────┘                        │
│              │                                        │
│              ▼                                        │
│     .cex/runtime/decisions/                           │
│     decision_manifest.yaml                            │
│     (the bridge between modes)                        │
└─────────────────────────────────────────────────────┘
```

## Rule 1: GDP BEFORE dispatch

Before ANY `/mission` or `/grid` that spawns nuclei:
1. Identify what SUBJECTIVE decisions the mission requires
2. Present them as Decision Points (see `skill_guided_decisions.md`)
3. Collect answers into `decision_manifest.yaml`
4. THEN dispatch with the manifest

## Rule 2: Manifest carries decisions to nuclei

Every handoff file written by dispatch MUST include:
```
## DECISIONS (from user)
See: .cex/runtime/decisions/decision_manifest.yaml
```

Nuclei read the manifest. They do NOT re-ask the user.
They do NOT assume different answers.
The manifest is the SINGLE SOURCE OF TRUTH for subjective decisions.

## Rule 3: Nuclei are FULLY AUTONOMOUS after dispatch

Once dispatched with a manifest:
- Nucleus reads manifest → knows all decisions
- Executes 8F pipeline → no questions asked
- If manifest doesn't cover an edge case → use ★ Recommended + flag it
- Commit, signal, done

A dispatched nucleus NEVER asks the user anything.
A dispatched nucleus NEVER contradicts the manifest.

## Rule 4: No manifest = co-pilot mode

If a nucleus starts WITHOUT a manifest (direct conversation):
- GDP is ACTIVE
- Present Decision Points for subjective choices
- Build the manifest as you go
- Execute after all DPs are resolved

## Explicit trigger: `/guide`

The user can type `/guide` to EXPLICITLY enter co-pilot mode.
See `.claude/commands/guide.md`.

Natural language equivalents (also trigger GDP):
- "guide me", "ask me first", "let's decide together"
- "walk me through", "help me choose", "what do you need from me"

## When to trigger GDP (quick check)

| Situation | GDP? | Why |
|-----------|------|-----|
| User says `/guide` | YES | Explicit trigger |
| User says `/init` | YES | Brand identity is 100% subjective |
| User says `/mission build landing page` | YES | Layout, tone, CTA, colors need decisions |
| User says `/build kc_react_patterns` | NO | Knowledge card is factual, not subjective |
| User says `/grid BRAND_LAUNCH` | YES before grid | Grid needs manifest FIRST |
| N03 runs 8F autonomously | NO | Already has manifest from dispatch |
| User asks "fix this bug" | NO | Mechanical, one correct answer |
| User asks "write copy for my product" | YES | Tone, audience, CTA are subjective |
| User says "just do it" / "you decide" | NO | User explicitly waives GDP |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[auto-accept-handoff]] | related | 0.49 |
| [[p03_sp_orchestration_nucleus]] | related | 0.45 |
| [[p01_kc_orchestration_best_practices]] | related | 0.43 |
| [[skill_guided_decisions]] | related | 0.38 |
| [[SPEC_07_gdp_enforcement]] | related | 0.32 |
| [[output_grid_test_n02]] | related | 0.32 |
| [[p08_ac_orchestrator]] | related | 0.31 |
| [[p12_wf_orchestration_pipeline]] | related | 0.29 |
| [[grid_test_20260407]] | related | 0.28 |
| [[p06_is_orchestration_dispatch]] | related | 0.26 |
