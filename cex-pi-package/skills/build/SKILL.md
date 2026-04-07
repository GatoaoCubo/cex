---
id: skill
kind: instruction
pillar: P08
description: "Build a CEX artifact via 8F pipeline. Usage: /build <intent>"
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

# /build

You are executing the CEX 8F pipeline. Follow these phases:

## F1 CONSTRAIN
Resolve the user's intent to: kind, pillar, schema.
Read `.cex/kinds_meta.json` to find the matching kind.

## F2 BECOME
Load the builder: `archetypes/builders/{kind}-builder/` (13 ISOs).

## F3 INJECT
Load context: KC, examples, brand config, memory, similar artifacts.

## F4 REASON
Plan the artifact. If subjective decisions needed, ask the user (GDP).

## F5 CALL
Use tools to enrich: search existing artifacts, check memory, load brand.

## F6 PRODUCE
Generate the artifact with complete YAML frontmatter. quality: null (never self-score).

## F7 GOVERN
Check against quality gate. If below 8.0, revise.

## F8 COLLABORATE
Save, compile (`python _tools/cex_compile.py <path>`), commit, signal.

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: artifact
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply artifact.md
```

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
