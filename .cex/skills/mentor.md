---
id: skill_mentor
kind: skill
pillar: P08
description: "Cross-runtime mirror of /mentor -- CEX universal vocabulary navigator"
quality: null
title: "Mentor Skill"
version: "1.0.0"
author: n07_orchestrator
tags: [mentor, vocabulary, taxonomy, skill, cross-runtime]
domain: "CEX system"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Mentor Skill -- Cross-Runtime

> Mirror of `.claude/commands/mentor.md` for Codex, Gemini, and Ollama runtimes.

## Trigger

- User asks: "what kind for X?", "which pillar?", "show kinds", "how does 8F work?"
- User types `/mentor` in any runtime
- User asks about CEX taxonomy, vocabulary, or structure

## Activation

1. Read `N00_genesis/boot/mentor_context.md` (the pre-compiled vocabulary)
2. Enter encyclopedic mode: no sin lens, no GDP, no 8F execution
3. Answer the taxonomy question using tables

## Response Format

Always include for kind queries:

```
| Field | Value |
|-------|-------|
| Kind | {kind_name} |
| Pillar | P{xx} -- {pillar_name} |
| Purpose | {one-line description} |
| Nucleus | N{xx} -- {nucleus_role} |
| Builder | archetypes/builders/{kind}-builder/ |
| Build | python _tools/cex_8f_runner.py "intent" --kind {kind} --execute |
```

## Boundaries

- This skill is READ-ONLY. It never creates or modifies files.
- If the user wants to BUILD, hand off to the build skill / 8F pipeline.
- If the user wants brand setup, hand off to the init skill.

## Context Source

`N00_genesis/boot/mentor_context.md` -- pre-compiled, ~8KB, contains:
- 8F pipeline (all 8 functions with descriptions)
- 12 pillar descriptions (purpose + kind count + owner nuclei)
- 257 kind summaries (name | pillar | purpose)
- Builder structure (13 ISOs per kind)
- Nucleus roles (N00-N07 with sin lens)
