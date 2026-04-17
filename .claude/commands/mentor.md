---
id: mentor
kind: instruction
pillar: P08
description: "Universal CEX vocabulary mentor -- 8F + 12P + 257K. Usage: /mentor [question]"
quality: 9.0
title: "Mentor"
version: "1.0.0"
author: n07_orchestrator
tags: [mentor, vocabulary, taxonomy, kinds, pillars, 8f]
tldr: "Encyclopedic mode: answer any question about CEX kinds, pillars, builders, or pipeline."
domain: "CEX system"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.92
---

# /mentor -- CEX Universal Vocabulary

> **Industry pattern**: taxonomy navigator / knowledge base Q&A.
> **What it does**: loads the full CEX vocabulary (8F pipeline, 12 pillars, 257 kinds,
>   8 nuclei) and answers any structural question without a sin lens.
> **When to use**: "What kind for X?", "Which pillar owns Y?", "Show all P07 kinds",
>   "How does 8F work?", "What's the difference between agent and agent_card?"

## Steps

1. Load the mentor context document:
   Read: `N00_genesis/boot/mentor_context.md`

2. Activate encyclopedic mode:
   - No sin lens (N00 archetype, neutral)
   - No GDP (factual, not subjective)
   - No 8F pipeline execution (query, not build)
   - Pure taxonomy navigation and explanation

3. Parse the user's question (`$ARGUMENTS`):

   | Question pattern | Response type |
   |------------------|---------------|
   | "What kind for X?" | Kind recommendation with pillar + nucleus + builder path |
   | "Which pillar owns X?" | Pillar explanation with all kinds in that pillar |
   | "Show all P{xx} kinds" | Full kind table for that pillar |
   | "How does 8F work?" | Pipeline walkthrough with examples |
   | "What's the difference between X and Y?" | Side-by-side comparison table |
   | "Which nucleus handles X?" | Nucleus routing explanation |
   | "How many kinds?" | Summary stats (257 kinds, 12 pillars, 259 builders) |
   | No argument | Show the 12-pillar overview + "ask me anything" |

4. Answer concisely using tables. Always include:
   - Kind name
   - Pillar code (P01-P12)
   - One-line purpose
   - Builder path: `archetypes/builders/{kind}-builder/`
   - Build command: `python _tools/cex_8f_runner.py "intent" --kind {kind} --execute`

## Examples

```
/mentor what kind for a landing page?
/mentor show all P04 kinds
/mentor difference between agent and agent_card
/mentor which nucleus builds prompts?
/mentor how does F7 GOVERN work?
/mentor
```

## Behavior Rules

- Never trigger GDP (this is factual, not subjective)
- Never execute 8F pipeline (this is a query, not a build)
- Never apply a sin lens (encyclopedic neutrality)
- Always cite the source: `N00_genesis/boot/mentor_context.md`
- If the user asks to BUILD something, redirect to `/build`
- If the user asks about THEIR brand, redirect to `/init`
- Keep answers under 50 lines unless explicitly asked for more
