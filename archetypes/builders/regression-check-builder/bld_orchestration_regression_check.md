---
kind: collaboration
id: bld_collaboration_regression_check
pillar: P12
llm_function: COLLABORATE
purpose: How regression-check-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.1
title: "Collaboration Regression Check"
version: "1.0.0"
author: n03_builder
tags: [regression_check, builder, examples]
tldr: "Golden and anti-examples for regression check construction, demonstrating ideal structure and common pitfalls."
domain: "regression check construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_golden_test
  - bld_collaboration_eval_dataset
  - bld_collaboration_quality_gate
  - bld_collaboration_smoke_eval
  - regression-check-builder
  - bld_collaboration_builder
  - bld_collaboration_benchmark
  - bld_collaboration_unit_eval
  - bld_collaboration_red_team_eval
  - p03_sp_regression_check_builder
---

# Collaboration: regression-check-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what baseline do we compare against, what metrics, and what deviation threshold triggers a failure?"
I do not measure absolute performance. I do not test isolated correctness.
I configure comparison gates so pipelines can detect quality degradation before it reaches production.

## Crew Compositions
### Crew: "Eval Pipeline"
```
  1. eval-dataset-builder  -> "dataset for evaluation runs"
  2. regression-check-builder -> "baseline comparison config (current vs prior experiment)"
  3. guardrail-builder     -> "deployment gate consuming fail_action signal"
```

### Crew: "Quality Gate System"
```
  1. benchmark-builder        -> "absolute performance baseline (first run only)"
  2. regression-check-builder -> "comparison config for subsequent runs vs benchmark"
  3. scoring-rubric-builder   -> "per-metric scoring criteria"
  4. quality-gate-builder     -> "composite pass/fail gate aggregating all checks"
```

### Crew: "LLM Deployment Safety"
```
  1. unit-eval-builder        -> "isolated correctness tests per component"
  2. golden-test-builder      -> "reference case validation"
  3. regression-check-builder -> "end-to-end regression vs production baseline"
  4. smoke-eval-builder       -> "rapid post-deploy sanity check"
```

## Handoff Protocol
### I Receive
- seeds: system under test, candidate baseline_ref, metric names, threshold preference
- optional: tool preference (Braintrust/Promptfoo/LangSmith/DeepEval), fail_action policy, cadence
- optional: prior regression_check artifacts to extend or replace

### I Produce
- regression_check artifact (.md + .yaml frontmatter)
- committed to: `cex/P07_evals/examples/p07_rc_{slug}.md`

### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons

## Builders I Depend On
| Builder | Why |
|---------|-----|
| eval-dataset-builder | Dataset used for evaluation runs must exist before baseline can be captured |
| benchmark-builder | First-run absolute measurement often becomes the initial baseline_ref |

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| guardrail-builder | Guardrails consume fail_action signal to enforce deployment gates |
| quality-gate-builder | Composite quality gates incorporate regression_check results |
| dag-builder | DAGs orchestrate regression checks as nodes in evaluation pipelines |

## Boundary Decisions (When to Route Away)
| Request | Route to | Reason |
|---------|----------|--------|
| "Measure absolute accuracy of my model" | benchmark-builder | No baseline comparison — absolute measurement |
| "Test if this single prompt returns the right answer" | unit-eval-builder | Isolated correctness, no baseline |
| "Check if output matches this gold standard" | golden-test-builder | Single reference case, not versioned comparison |
| "Quick smoke test after deploy" | smoke-eval-builder | Sanity check, no baseline comparison needed |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_golden_test]] | sibling | 0.46 |
| [[bld_collaboration_eval_dataset]] | sibling | 0.44 |
| [[bld_collaboration_quality_gate]] | sibling | 0.42 |
| [[bld_collaboration_smoke_eval]] | sibling | 0.41 |
| [[regression-check-builder]] | upstream | 0.41 |
| [[bld_collaboration_builder]] | sibling | 0.40 |
| [[bld_collaboration_benchmark]] | sibling | 0.38 |
| [[bld_collaboration_unit_eval]] | sibling | 0.38 |
| [[bld_collaboration_red_team_eval]] | sibling | 0.35 |
| [[p03_sp_regression_check_builder]] | upstream | 0.35 |
