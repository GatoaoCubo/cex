---
pillar: P12
llm_function: COLLABORATE
purpose: How scoring-rubric-builder works in crews
---

# Collaboration: scoring-rubric-builder

## My Role
I define HOW to evaluate quality across multiple dimensions.
I do not provide concrete EXAMPLES (golden-test-builder).
I do not enforce PASS/FAIL barriers (quality-gate-builder).

## Crew: "Evaluation Pipeline"
```
  1. scoring-rubric-builder -> defines dimensions and weights
  2. golden-test-builder    -> provides reference examples at 9.5+
  3. quality-gate-builder   -> defines pass/fail thresholds
```

## Crew: "New Kind Evaluation Setup"
```
  1. scoring-rubric-builder -> rubric for the new kind
  2. golden-test-builder    -> golden examples calibrated to rubric
  3. quality-gate-builder   -> gates derived from rubric dimensions
  4. validator-builder [PLANNED] -> code implementing gates
```

## Handoff Protocol
### I Receive
- seeds: target_kinds, domain, existing quality dimensions
- optional: industry framework reference, golden_test candidates

### I Produce
- scoring_rubric artifact in P07_evals/examples/
- committed to: cex/P07_evals/examples/p07_sr_{framework_slug}.md

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None directly. Independent at layer 0.
- golden-test-builder: provides calibration examples (optional, enhances rubric)

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| golden-test-builder | Uses rubric dimensions for rationale mapping |
| quality-gate-builder | Derives SOFT gate dimensions from rubric |
| unit-eval-builder [PLANNED] | Uses criteria for test assertions |
