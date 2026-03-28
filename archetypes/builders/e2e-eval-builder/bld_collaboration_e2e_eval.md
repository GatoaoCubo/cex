---
kind: collaboration
id: bld_collaboration_e2e_eval
pillar: P12
llm_function: COLLABORATE
purpose: How e2e-eval-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: e2e-eval-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "does the full pipeline produce correct output from start to finish?"
I do not test individual units. I do not measure performance.
I validate complete pipelines so teams can confirm end-to-end correctness.
## Crew Compositions
### Crew: "Quality Pipeline"
```
  1. golden-test-builder -> "reference examples for calibration"
  2. benchmark-builder -> "performance baselines"
  3. e2e-eval-builder -> "end-to-end pipeline validation"
```
### Crew: "Release Validation"
```
  1. e2e-eval-builder -> "integration test with stages and fixtures"
  2. guardrail-builder -> "safety boundary verification"
  3. bugloop-builder -> "auto-fix if e2e test fails"
```
## Handoff Protocol
### I Receive
- seeds: pipeline description, stages list, expected final output
- optional: data fixtures, intermediate assertions, environment requirements, cleanup steps
### I Produce
- e2e_eval artifact (.md + .yaml frontmatter)
- committed to: `cex/P07/examples/p07_e2e_{scope}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- golden-test-builder: provides reference examples for expected output comparison
- benchmark-builder: provides performance baselines for pass/fail thresholds
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| bugloop-builder | Triggers correction cycle when e2e test fails |
| guardrail-builder | Validates safety boundaries within e2e context |
