---
pillar: P12
llm_function: COLLABORATE
purpose: How e2e-eval-builder works in crews
---

# Collaboration: e2e-eval-builder

## My Role
I provide PIPELINE INTEGRATION TESTING across multiple agents.
I do not test individual agents (unit-eval-builder).
I do not check quick sanity (smoke-eval-builder).

## Crew: "Test Suite"
```
  1. smoke-eval-builder     -> quick sanity (< 30s)
  2. unit-eval-builder      -> individual agent tests
  3. e2e-eval-builder       -> pipeline integration tests
```

## Crew: "Release Validation"
```
  1. smoke-eval-builder     -> gate: if fails, abort release
  2. e2e-eval-builder       -> full pipeline test
  3. quality-gate-builder   -> final pass/fail decision
```

## Handoff Protocol
### I Receive
- seeds: pipeline, stages, domain
- optional: workflow definition, unit_eval results, data fixtures

### I Produce
- e2e_eval artifact in P07_evals/
- committed to: cex/P07_evals/p07_e2e_{pipeline_slug}.md

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- unit-eval-builder: provides individual agent test results
- smoke-eval-builder: must pass before e2e runs
- workflow-builder: defines pipeline being tested

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| quality-gate-builder | Uses e2e results for final pass/fail |
| benchmark-builder | Aggregates pipeline metrics from e2e runs |
