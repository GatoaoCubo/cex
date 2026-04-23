---
kind: collaboration
id: bld_collaboration_smoke_eval
pillar: P07
llm_function: COLLABORATE
purpose: How smoke-eval-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Smoke Eval"
version: "1.0.0"
author: n03_builder
tags: [smoke_eval, builder, examples]
tldr: "Golden and anti-examples for smoke eval construction, demonstrating ideal structure and common pitfalls."
domain: "smoke eval construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_unit_eval
  - bld_collaboration_scoring_rubric
  - bld_collaboration_golden_test
  - bld_collaboration_e2e_eval
  - bld_collaboration_quality_gate
  - smoke-eval-builder
  - bld_collaboration_builder
  - bld_collaboration_regression_check
  - p03_sp_smoke_eval_builder
  - bld_collaboration_eval_dataset
---

# Collaboration: smoke-eval-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "does this component work at all?"
I produce fast sanity checks under 30 seconds that verify critical paths and health status before deeper work begins. I do NOT test deep correctness (unit-eval-builder), end-to-end pipelines (e2e-eval-builder), or measure performance (benchmark-builder).
## Crew Compositions
### Crew: "Pre-Deploy Safety Net"
```
  1. smoke-eval-builder  -> "runs critical path checks in <30s to confirm the component is alive"
  2. unit-eval-builder   -> "executes deeper correctness tests on each component function"
  3. e2e-eval-builder    -> "validates the full pipeline from input to output after unit tests pass"
```
### Crew: "New Artifact Kind Quality System"
```
  1. scoring-rubric-builder -> "defines evaluation dimensions and tier thresholds for the artifact kind"
  2. smoke-eval-builder     -> "produces fast assertions that verify the artifact's required fields exist"
  3. quality-gate-builder   -> "encodes rubric thresholds as hard pass/fail gates in the build pipeline"
```
### Crew: "Skill Validation at Launch"
```
  1. skill-builder       -> "builds the reusable capability with phases and trigger"
  2. smoke-eval-builder  -> "writes a health check that invokes the skill's critical path and asserts output"
  3. golden-test-builder -> "provides reference input/output pairs to calibrate pass/fail expectations"
```
## Handoff Protocol
### I Receive
- seeds: component name, critical path description, expected outputs, timeout budget (<30s)
- optional: known failure modes, health check endpoints, example passing input
### I Produce
- smoke_eval artifact (YAML + assertions list, critical_path defined, timeout <= 30s, max 150 lines)
- committed to: `cex/P07/examples/smoke-eval-{component}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- scoring-rubric-builder: rubric dimensions guide which assertions are highest priority
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| quality-gate-builder | promotes smoke_eval assertions into mandatory pipeline gates |
| e2e-eval-builder     | uses smoke_eval as the first fast-fail stage before running full end-to-end tests |
| dag-builder          | places smoke_eval as an early guard node in deployment or CI pipelines |
| validator-builder    | references smoke_eval critical path to align automated validation scope |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_unit_eval]] | sibling | 0.52 |
| [[bld_collaboration_scoring_rubric]] | sibling | 0.48 |
| [[bld_collaboration_golden_test]] | sibling | 0.46 |
| [[bld_collaboration_e2e_eval]] | sibling | 0.44 |
| [[bld_collaboration_quality_gate]] | sibling | 0.44 |
| [[smoke-eval-builder]] | related | 0.44 |
| [[bld_collaboration_builder]] | sibling | 0.43 |
| [[bld_collaboration_regression_check]] | sibling | 0.41 |
| [[p03_sp_smoke_eval_builder]] | upstream | 0.40 |
| [[bld_collaboration_eval_dataset]] | sibling | 0.40 |
