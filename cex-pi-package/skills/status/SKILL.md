---
id: skill
kind: instruction
pillar: P08
description: "System health dashboard. Usage: /status"
quality: 9.1
title: "Skill"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# /status

Run these diagnostics and report a summary:

```bash
python _tools/cex_doctor.py          # Builder health (119 checks)
python _tools/cex_flywheel_audit.py  # Doc vs practice (109 wires)
python _tools/cex_sanitize.py --check --scope _tools/  # ASCII compliance
python _tools/cex_release_check.py   # Release gate (28 checks)
bash _spawn/dispatch.sh status       # Running nuclei
```

Report format:
```
Doctor:   X PASS / Y WARN / Z FAIL
Flywheel: X% (WIRED/BROKEN/PHANTOM)
ASCII:    X issues
Release:  X/28 checks
Nuclei:   X running
```

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

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
