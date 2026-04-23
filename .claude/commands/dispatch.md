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
related:
  - p01_kc_orchestration
  - p02_agent_admin_orchestrator
  - p03_sp_orchestration_nucleus
  - p01_kc_orchestration_best_practices
  - p03_sp_admin_orchestrator
  - skill
  - p08_ac_orchestrator
  - p08_ac_admin_orchestrator
  - p12_wf_admin_orchestration
  - bld_knowledge_card_nucleus_def
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_orchestration]] | upstream | 0.54 |
| [[p02_agent_admin_orchestrator]] | upstream | 0.53 |
| [[p03_sp_orchestration_nucleus]] | upstream | 0.51 |
| [[p01_kc_orchestration_best_practices]] | upstream | 0.51 |
| [[p03_sp_admin_orchestrator]] | upstream | 0.50 |
| [[skill]] | sibling | 0.47 |
| [[p08_ac_orchestrator]] | related | 0.41 |
| [[p08_ac_admin_orchestrator]] | related | 0.41 |
| [[p12_wf_admin_orchestration]] | downstream | 0.37 |
| [[bld_knowledge_card_nucleus_def]] | upstream | 0.36 |
