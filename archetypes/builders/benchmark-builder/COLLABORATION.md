---
pillar: P12
llm_function: COLLABORATE
purpose: How benchmark-builder works in crews
---

# Collaboration: benchmark-builder

## My Role
I MEASURE quantitative performance so other builders have concrete numbers.
I do not define evaluation CRITERIA (scoring-rubric-builder).
I do not test CORRECTNESS (unit-eval-builder).

## Crew: "Model Selection Pipeline"
```
  1. benchmark-builder      -> measures latency, cost, throughput per model
  2. scoring-rubric-builder -> defines quality evaluation criteria
  3. model-card-builder     -> documents chosen model with benchmark data
```

## Crew: "Performance Optimization"
```
  1. benchmark-builder      -> measures baseline performance
  2. unit-eval-builder      -> verifies correctness after optimization
  3. benchmark-builder      -> measures post-optimization (re-run)
```

## Handoff Protocol
### I Receive
- seeds: metric, unit, environment, subjects to compare
- optional: existing baseline data, SLA targets, comparison methodology

### I Produce
- benchmark artifact in P07_evals/examples/
- committed to: cex/P07_evals/examples/p07_bm_{metric_slug}.md

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None directly. Independent at layer 0.
- model-card-builder: provides model specs for comparison setup (optional)

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| model-card-builder | Uses benchmark numbers for performance specs |
| scoring-rubric-builder | References benchmark thresholds for calibration |
| quality-gate-builder | Derives numeric thresholds from benchmark baselines |
