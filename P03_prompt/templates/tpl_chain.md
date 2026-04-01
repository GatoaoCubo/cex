---
id: "p03_ch_{{PIPELINE_SLUG}}"
kind: chain
version: 1.0.0
title: Template - Chain
tags: [template, chain, multi-step, reasoning, pipeline]
tldr: "Multi-step prompt chain: each step output feeds the next. Defines steps, schemas, recovery, timeout."
quality: 8.6
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
- [ ] >= 2 steps (1 step = not a chain)
- [ ] Each step has input/output
- [ ] Total timeout prevents runaway
- [ ] Error recovery per step
