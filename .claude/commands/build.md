---
id: build
kind: instruction
pillar: P08
description: "Build a CEX artifact via 8F pipeline. Usage: /build <intent>"
quality: 9.1
title: "Build"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - skill
  - doctor
  - research_then_build
  - validate
  - build_and_review
  - full_pipeline
  - status
  - p03_ap_{{ACTION_SLUG}}
  - p03_up_dispatch_agent_group
  - n04_knowledge
---

# /build — Create CEX Artifact

Execute the full 8F pipeline to produce a new artifact.

## Steps

1. Parse the intent: `$ARGUMENTS`
2. Run the 8F Motor to resolve kind:
   ```bash
   python _tools/cex_8f_runner.py "$ARGUMENTS" --execute --verbose
   ```
3. If the runner produces a valid artifact (PASS verdict):
   - Compile: `python _tools/cex_compile.py {output_path}`
   - Validate: `python _tools/cex_hooks.py post-save {output_path}`
   - Commit: `git add {output_path} && git commit -m "[N03] build {kind} via 8F"`
4. If FAIL after retries:
   - Show the issues from F7
   - Suggest manual fixes

## Examples
```
/build create a knowledge card about RAG chunking strategies
/build create an agent for code review automation
/build create a workflow for sales funnel optimization
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[skill]] | sibling | 0.55 |
| [[doctor]] | sibling | 0.54 |
| [[research_then_build]] | related | 0.52 |
| [[validate]] | sibling | 0.52 |
| [[build_and_review]] | related | 0.51 |
| [[full_pipeline]] | related | 0.49 |
| [[status]] | sibling | 0.44 |
| [[p03_ap_{{ACTION_SLUG}}]] | upstream | 0.43 |
| [[p03_up_dispatch_agent_group]] | upstream | 0.38 |
| [[n04_knowledge]] | sibling | 0.37 |
