---
pillar: P12
llm_function: COLLABORATE
purpose: How smoke-eval-builder works in crews
---

# Collaboration: smoke-eval-builder

## My Role
I provide QUICK SANITY CHECKS before deeper testing.
I do not test deeply (unit-eval-builder).
I do not test pipelines (e2e-eval-builder).

## Crew: "Test Suite"
```
  1. smoke-eval-builder     -> quick sanity (< 30s)
  2. unit-eval-builder      -> deep correctness testing
  3. e2e-eval-builder       -> pipeline integration tests
```

## Crew: "CI Pipeline"
```
  1. smoke-eval-builder     -> gate: if fails, skip rest
  2. unit-eval-builder      -> run only if smoke passes
  3. quality-gate-builder   -> final pass/fail decision
```

## Handoff Protocol
### I Receive
- seeds: scope, domain, critical components
- optional: health endpoints, existing unit_evals to derive from

### I Produce
- smoke_eval artifact in P07_evals/
- committed to: cex/P07_evals/p07_se_{scope_slug}.md

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- unit-eval-builder: provides deep tests from which smoke checks derive

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| unit-eval-builder | Skips deep tests if smoke fails |
| e2e-eval-builder | Skips pipeline tests if smoke fails |
