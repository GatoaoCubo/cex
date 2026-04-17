---
id: validate
kind: instruction
pillar: P08
description: "Validate CEX artifacts. Usage: /validate [file|all]"
quality: 9.0
title: "Validate"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# /validate — Check Artifact Quality

Run validation hooks on artifacts.

## Usage

1. `/validate all` — validate all 101 nucleus artifacts
2. `/validate N07_admin/P02_model/agent_admin.md` — validate specific file
3. `/validate` (no args) — validate all staged git files

## Steps

1. If `$ARGUMENTS` is "all":
   ```bash
   python _tools/cex_hooks.py validate-all
   ```
2. If `$ARGUMENTS` is a file path:
   ```bash
   python _tools/cex_hooks.py validate $ARGUMENTS
   ```
3. If no arguments:
   ```bash
   python _tools/cex_hooks.py pre-commit
   ```
4. Also run doctor:
   ```bash
   python _tools/cex_doctor.py
   ```
5. Report summary: errors, warnings, score distribution.

## Properties

| Property | Value |
|----------|-------|
| Kind | `` |
| Pillar |  |
| Domain | CEX system |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

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
