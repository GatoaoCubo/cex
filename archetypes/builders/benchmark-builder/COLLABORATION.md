---
pillar: P12
llm_function: COLLABORATE
purpose: How benchmark-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
---

# Collaboration: benchmark-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "how fast, how cheap, and how well does this perform under load?"
I do not define quality criteria. I do not test correctness.
I measure performance quantitatively so teams can set baselines and detect regressions.

## Crew Compositions

### Crew: "Quality Pipeline"
```
  1. golden-test-builder -> "reference examples (quality calibration)"
  2. benchmark-builder -> "performance baselines (latency, cost, throughput)"
  3. e2e-eval-builder -> "end-to-end pipeline validation"
```

### Crew: "Performance Optimization"
```
  1. benchmark-builder -> "baseline measurements before optimization"
  2. bugloop-builder -> "detect-fix-verify cycle for performance regressions"
  3. benchmark-builder -> "post-optimization measurements for comparison"
```

## Handoff Protocol

### I Receive
- seeds: target system/agent name, metrics to measure (latency, cost, throughput)
- optional: baseline values, environment constraints, iteration count

### I Produce
- benchmark artifact (.md + .yaml frontmatter)
- committed to: `cex/P07/examples/p07_benchmark_{scope}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
None — independent builder (layer 0). Benchmarks can be defined for any system.

## Builders That Depend On Me

| Builder | Why |
|---------|-----|
| bugloop-builder | Uses benchmark thresholds as detection triggers |
| e2e-eval-builder | References benchmark baselines for pass/fail criteria |
| fallback-chain-builder | Uses latency/cost benchmarks to calibrate timeouts |
