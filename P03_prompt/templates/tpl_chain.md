---
id: "p03_ch_{{PIPELINE_SLUG}}"
kind: chain
pillar: P03
version: 1.0.0
title: Template - Chain
tags: [template, chain, multi-step, reasoning, pipeline]
tldr: "Multi-step prompt chain: each step output feeds the next. Defines steps, schemas, recovery, timeout."
quality: 9.0
updated: "2026-04-07"
domain: "prompt engineering"
author: n03_builder
created: "2026-04-07"
density_score: 1.0
---

# Chain: [NAME]

## Purpose
[WHAT this chain does]
## Chain Definition
```yaml
steps: [STEP_1, STEP_2, STEP_3]
total_timeout_s: [120]
mode: [sequential | parallel_then_merge]
```
## Steps
| # | Name | Input | Output | Gate |
|---|------|-------|--------|------|
| 1 | [STEP_1] | [initial] | [intermediate_1] | [check] |
| 2 | [STEP_2] | [intermediate_1] | [intermediate_2] | [check] |
| 3 | [STEP_3] | [intermediate_2] | [final] | [check] |
## Data Flow
```
Input -> Step1 -> intermediate -> Step2 -> intermediate -> Step3 -> Output
```
## Error Recovery
| Failure | Recovery |
|---------|----------|
| Step 1 | Retry with rephrased prompt |
| Step 2 | Retry with step 1 context |
| Step 3 | Return partial (step 2 output) |
## Quality Gate
1. [ ] >= 2 steps (1 step = not a chain)
2. [ ] Each step has input/output
3. [ ] Total timeout prevents runaway
4. [ ] Error recovery per step

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
