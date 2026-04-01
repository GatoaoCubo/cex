---
id: p01_kc_input_hydration
kind: knowledge_card
type: domain
pillar: P01
title: "Input Hydration Framework"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: frameworks
quality: 8.5
tags: [framework, architecture, llm]
tldr: "Raw user input is incomplete. Hydrate with brand, memory, KC context before any nucleus processes it."
keywords: [hydration, enrichment, context-injection, preprocessing]
density_score: 0.92
---

# Input Hydration Framework

## Hydration Layers
| Layer | Source | What it Adds |
|-------|--------|-------------|
| 1. Brand | brand_config.yaml | Identity, voice, colors |
| 2. Memory | builder memory files | Past learnings, preferences |
| 3. Knowledge | P01 KCs | Domain expertise |
| 4. Decisions | decision_manifest.yaml | User choices |
| 5. Examples | compiled/ artifacts | Reference patterns |

## CEX Implementation
wf_auto_hydrate.md chains all 5 layers.
compose_prompt() in cex_crew_runner.py assembles the hydrated prompt.
