---
id: dispatch
kind: instruction
pillar: P08
description: "Dispatch task to a nucleus. Usage: /dispatch <nucleus> <task>"
quality: 9.1
title: "Dispatch"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# /dispatch — Send Task to Nucleus Builder

Write a handoff file and spawn a nucleus builder.

## Usage

1. `/dispatch n03 rebuild N01 agent artifacts`
2. `/dispatch n01 research competitor analysis for SaaS market`
3. `/dispatch grid MISSION_NAME` — launch parallel grid

## Steps

1. Parse nucleus and task from `$ARGUMENTS`
2. Write handoff file:
   ```
   .cex/runtime/handoffs/{nucleus}_task.md
   ```
   With content: task description, references, commit rules, signal instructions.
3. Dispatch:
   ```bash
   bash _spawn/dispatch.sh solo {nucleus} ""
   ```
   (Task comes from handoff file, not CLI args — avoids nested quote hell)
4. Monitor:
   ```bash
   bash _spawn/dispatch.sh status
   ```
5. After completion, consolidate (especially for Gemini nuclei N01/N04).

## Routing Table

| Domain | Nucleus | CLI |
|--------|---------|-----|
| Build/create | n03 | claude opus |
| Research/analysis | n01 | gemini 2.5-pro |
| Marketing/copy | n02 | claude sonnet |
| Knowledge/docs | n04 | gemini 2.5-pro |
| Code/test/deploy | n05 | codex |
| Sales/pricing | n06 | claude sonnet |

## System Context

This artifact participates in the CEX typed knowledge system, a fractal
architecture with 12 pillars, 8 nuclei, and 125 specialized builders.
Artifacts flow through the 8F pipeline: Focus, Frame, Fetch, Filter,
Format, Forge, Furnish, and Feedback.

Quality is enforced via 3-layer scoring: structural (30%), rubric (30%),
and semantic (40%). All artifacts target quality >= 9.0.

| Layer | Weight | Method |
|-------|--------|--------|
| Structural | 30% | Automated count-based checks |
| Rubric | 30% | Quality gate dimension scoring |
| Semantic | 40% | LLM evaluation (when L1+L2 >= 8.5) |
