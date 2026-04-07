---
id: status
kind: instruction
pillar: P08
description: "Show full CEX system status. Usage: /status"
quality: 9.0
title: "Status"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# /status — System Health Dashboard

## Steps

1. Run system test (quick mode):
   ```bash
   python _tools/cex_system_test.py --quick
   ```
2. Check quality distribution:
   ```bash
   grep -r "^quality:" N0*/ --include="*.md" | sed 's/.*quality: //' | sort | uniq -c | sort -k2 -n
   ```
3. Check for quality:null remnants:
   ```bash
   grep -r "^quality: null" N0*/ --include="*.md" | wc -l
   ```
4. Recent signals:
   ```bash
   ls -lt .cex/runtime/signals/ | head -10
   ```
5. Recent learning records:
   ```bash
   ls -lt .cex/learning_records/ | head -10
   ```
6. Git status:
   ```bash
   git log --oneline -5
   git status --short
   ```
7. Report summary as a formatted table.

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
