---
pillar: P12
llm_function: COLLABORATE
purpose: How unit-eval-builder works in crews
---

# Collaboration: unit-eval-builder

## My Role
I provide VERIFICATION of individual agent/prompt correctness.
I do not define evaluation CRITERIA (scoring-rubric-builder).
I do not provide REFERENCE examples (golden-test-builder).

## Crew: "Evaluation Pipeline"
```
  1. scoring-rubric-builder -> defines dimensions and weights
  2. golden-test-builder    -> provides reference examples at 9.5+
  3. unit-eval-builder      -> verifies correctness with assertions
  4. quality-gate-builder   -> defines pass/fail thresholds
```

## Crew: "Test Suite"
```
  1. unit-eval-builder      -> individual agent tests
  2. smoke-eval-builder     -> quick sanity checks
  3. e2e-eval-builder       -> pipeline integration tests
```

## Handoff Protocol
### I Receive
- seeds: target, target_kind, domain
- optional: golden_test reference, gate list from target builder

### I Produce
- unit_eval artifact in P07_evals/
- committed to: cex/P07_evals/p07_ue_{target_slug}.md

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- scoring-rubric-builder: provides evaluation criteria for assertion mapping
- golden-test-builder: provides reference outputs for expected_output

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| golden-test-builder | Uses unit_evals to validate golden candidates |
| e2e-eval-builder | Composes unit_evals into pipeline tests |
| smoke-eval-builder | Derives quick checks from unit_eval assertions |
