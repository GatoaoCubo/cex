---
kind: collaboration
id: bld_collaboration_scoring_rubric
pillar: P07
llm_function: COLLABORATE
purpose: How scoring-rubric-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Scoring Rubric"
version: "1.0.0"
author: n03_builder
tags: [scoring_rubric, builder, examples]
tldr: "Golden and anti-examples for scoring rubric construction, demonstrating ideal structure and common pitfalls."
domain: "scoring rubric construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_quality_gate
  - scoring-rubric-builder
  - bld_collaboration_golden_test
  - bld_collaboration_smoke_eval
  - bld_knowledge_card_scoring_rubric
  - bld_collaboration_builder
  - bld_collaboration_validator
  - bld_architecture_kind
  - p01_kc_scoring_rubric
  - bld_collaboration_validation_schema
---

# Collaboration: scoring-rubric-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how should we measure quality of this artifact kind?"
I design evaluation frameworks with weighted dimensions, tier thresholds, and calibration anchors. I do NOT build reference examples for calibration (golden-test-builder), enforce pass/fail barriers in pipelines (quality-gate-builder), or measure performance benchmarks (benchmark-builder).
## Crew Compositions
### Crew: "Evaluation System Bootstrap"
```
  1. scoring-rubric-builder -> "designs dimensions, weights, and tier thresholds for the artifact kind"
  2. golden-test-builder    -> "produces reference examples that calibrate each rubric dimension"
  3. quality-gate-builder   -> "translates rubric thresholds into enforceable pass/fail pipeline gates"
```
### Crew: "Builder Quality Governance"
```
  1. scoring-rubric-builder -> "defines how to score builder output (dimensions + weights summing to 100%)"
  2. smoke-eval-builder     -> "produces quick sanity checks that verify the rubric can be applied"
  3. unit-eval-builder      -> "builds detailed tests that exercise each rubric dimension independently"
```
### Crew: "New Artifact Kind Launch"
```
  1. type-def-builder       -> "defines the artifact schema and required fields"
  2. scoring-rubric-builder -> "specifies how artifact instances will be evaluated"
  3. validator-builder      -> "implements automated validation logic derived from the rubric gates"
```
## Handoff Protocol
### I Receive
- seeds: artifact kind name, quality criteria ofscription, target audience, automation preference
- optional: existing scoring examples, inter-rater reliability target, tier names (e.g. gold/silver/bronze)
### I Produce
- scoring_rubric artifact (YAML + Markdown, dimensions with weights summing to 100%, max 250 lines)
- committed to: `cex/P07/examples/scoring-rubric-{kind}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- golden-test-builder: reference examples are needed to calibrate scale anchors (what a score of 9 looks like)
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| quality-gate-builder | translates rubric tier thresholds into hard pass/fail gates |
| golden-test-builder  | uses rubric dimensions as the framework for selecting calibration examples |
| smoke-eval-builder   | needs rubric dimensions to know which assertions matter most |
| validator-builder    | implements automated checks derived from the rubric's hard criteria |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_quality_gate]] | sibling | 0.56 |
| [[scoring-rubric-builder]] | related | 0.50 |
| [[bld_collaboration_golden_test]] | sibling | 0.46 |
| [[bld_collaboration_smoke_eval]] | sibling | 0.42 |
| [[bld_knowledge_card_scoring_rubric]] | upstream | 0.39 |
| [[bld_collaboration_builder]] | sibling | 0.39 |
| [[bld_collaboration_validator]] | sibling | 0.39 |
| [[bld_architecture_kind]] | downstream | 0.38 |
| [[p01_kc_scoring_rubric]] | related | 0.38 |
| [[bld_collaboration_validation_schema]] | sibling | 0.37 |
