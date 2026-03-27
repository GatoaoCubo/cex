---
pillar: P07
llm_function: COLLABORATE
purpose: How scoring-rubric-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
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
- seeds: artifact kind name, quality criteria description, target audience, automation preference
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
