---
pillar: P12
llm_function: COLLABORATE
purpose: How golden-test-builder works in crews
---

# Collaboration: golden-test-builder

## My Role
I provide CONCRETE EXAMPLES of what quality 9.5+ looks like.
I do not define evaluation CRITERIA (scoring-rubric-builder).
I do not define PASS/FAIL barriers (quality-gate-builder).

## Crew: "Evaluation Pipeline"
```
  1. scoring-rubric-builder -> defines dimensions and weights
  2. golden-test-builder    -> provides reference examples at 9.5+
  3. quality-gate-builder   -> defines pass/fail thresholds
```

## Crew: "Builder Calibration"
```
  1. golden-test-builder    -> golden example of target kind
  2. unit-eval-builder [PLANNED] -> test suite from golden
```

## Handoff Protocol
### I Receive
- seeds: target_kind, domain
- optional: candidate artifact (9.5+ quality), gate references

### I Produce
- golden_test artifact in P07_evals/examples/
- committed to: cex/P07_evals/examples/p07_gt_{case_slug}.md

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
- scoring-rubric-builder: provides evaluation criteria for rationale mapping
- quality-gate-builder: provides gate IDs referenced in rationale

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| scoring-rubric-builder | Uses golden_tests as calibration examples |
| unit-eval-builder [PLANNED] | Derives test cases from golden references |
