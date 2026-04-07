---
id: skill
kind: instruction
pillar: P08
description: "Decompose goal into waves of nucleus work. Usage: /mission <goal>"
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

# /mission

Decompose the goal into a multi-wave execution plan.

## Steps
1. Kill any idle processes first (always)
2. Identify which nuclei are needed (N01-N06)
3. Group into waves (parallel within wave, sequential between waves)
4. Write handoffs to `.cex/runtime/handoffs/`
5. Dispatch each nucleus via `bash _spawn/dispatch.sh solo`
6. Poll for signals every 90s, kill on complete (taskkill /F /PID /T)
7. Synthesize between waves (read results, create specific specs)
8. Consolidate: doctor + flywheel + commit

## Nucleus routing
| Domain | Nucleus |
|--------|---------|
| Research/analysis | N01 |
| Marketing/copy | N02 |
| Build/create | N03 |
| Knowledge/docs | N04 |
| Code/test/deploy | N05 |
| Brand/monetization | N06 |

## Rules
1. N07 never builds directly -- dispatch only
2. GDP before subjective decisions
3. Kill before spawn (principle #6)
4. Synthesize between waves (principle #7)

## Metadata

```yaml
id: artifact
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply artifact.md
```

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
