---
kind: collaboration
id: bld_collaboration_golden_test
pillar: P12
llm_function: COLLABORATE
purpose: How golden-test-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Golden Test"
version: "1.0.0"
author: n03_builder
tags: [golden_test, builder, examples]
tldr: "Golden and anti-examples for golden test construction, demonstrating ideal structure and common pitfalls."
domain: "golden test construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_few_shot_example
  - bld_collaboration_builder
  - bld_collaboration_action_prompt
  - bld_collaboration_response_format
  - bld_collaboration_prompt_version
  - bld_collaboration_e2e_eval
  - bld_collaboration_benchmark
  - bld_collaboration_quality_gate
  - golden-test-builder
  - bld_architecture_kind
---

# Collaboration: golden-test-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what does a perfect artifact of this kind look like?"
I do not define evaluation criteria. I do not measure performance.
I produce quality-calibration references so evaluation systems have a gold standard for comparison.
## Crew Compositions
### Crew: "Quality Pipeline"
```
  1. golden-test-builder -> "reference examples (quality 9.5+)"
  2. benchmark-builder -> "performance baselines"
  3. e2e-eval-builder -> "end-to-end pipeline validation against golden"
```
### Crew: "Builder Calibration"
```
  1. golden-test-builder -> "perfect artifact example for target kind"
  2. few-shot-example-builder -> "format examples derived from golden"
  3. action-prompt-builder -> "prompt calibrated to produce golden-quality output"
```
## Handoff Protocol
### I Receive
- seeds: target artifact kind, quality gates for that kind
- optional: existing high-quality artifacts (9.5+), rationale mapping
### I Produce
- golden_test artifact (.md + .yaml frontmatter with input/output/rationale)
- committed to: `cex/P07/examples/p07_golden_{kind}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Golden tests are selected from existing high-quality output.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| e2e-eval-builder | Compares pipeline output against golden reference |
| few-shot-example-builder | Derives format examples from golden artifacts |
| action-prompt-builder | Calibrates prompts using golden output as target |
| benchmark-builder | Uses golden output quality as performance ceiling |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_few_shot_example]] | sibling | 0.45 |
| [[bld_collaboration_builder]] | sibling | 0.43 |
| [[bld_collaboration_action_prompt]] | sibling | 0.42 |
| [[bld_collaboration_response_format]] | sibling | 0.39 |
| [[bld_collaboration_prompt_version]] | sibling | 0.39 |
| [[bld_collaboration_e2e_eval]] | sibling | 0.39 |
| [[bld_collaboration_benchmark]] | sibling | 0.37 |
| [[bld_collaboration_quality_gate]] | sibling | 0.36 |
| [[golden-test-builder]] | upstream | 0.36 |
| [[bld_architecture_kind]] | upstream | 0.36 |
