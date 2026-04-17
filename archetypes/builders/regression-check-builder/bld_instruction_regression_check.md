---
kind: instruction
id: bld_instruction_regression_check
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for regression_check
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Regression Check"
version: "1.0.0"
author: n03_builder
tags: [regression_check, builder, examples]
tldr: "Golden and anti-examples for regression check construction, demonstrating ideal structure and common pitfalls."
domain: "regression check construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
---

# Instructions: How to Produce a regression_check
## Phase 1: RESEARCH
1. Identify the system under test: which prompt, model, pipeline, or agent is being regression-checked
2. Determine the baseline_ref: find the experiment ID, version tag, or named snapshot to compare against — confirm it is resolvable in the target tool
3. Select metrics to compare: enumerate all dimensions that matter (accuracy, latency_p95, cost_per_call, hallucination_rate, pass_rate, etc.)
4. Determine threshold per metric: consult historical variance data; start at 5% relative deviation if no prior data
5. Select the comparison tool: Braintrust, Promptfoo, LangSmith, DeepEval, or costm framework
6. Define fail_action: block (gate deployment), warn (notify but allow), or log (record only)
7. Define cadence: on_pr, on_deploy, daily, on_demand — align with deployment frequency
8. Check for existing regression_check artifacts to avoid duplicates or conflicts with same baseline_ref
9. Confirm slug for id: snake_case, lowercase, no hyphens, describes system + check purpose
## Phase 2: COMPOSE
1. Read SCHEMA.md — source of truth for all fields
2. Read OUTPUT_TEMPLATE.md — fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null — never self-score)
4. Set baseline_ref: use the exact resolvable reference string (experiment ID, git tag, version)
5. Set threshold: numeric value with unit documentation (percentage or decimal)
6. List metrics: concrete measurable names that exist in the chosen tool's evaluator set
7. Write Overview section: system under test, purpose of check, ownership
8. Write Baseline section: what the baseline_ref points to, when it was captured, update policy
9. Write Metrics section: for each metric — definition, measurement method, threshold, direction
10. Write Failure Protocol section: fail_action, notification channels, remediation steps
11. Verify body <= 2048 bytes
12. Verify id matches `^p07_rc_[a-z][a-z0-9_]+$`
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md — verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm id matches `p07_rc_` prefix pattern
4. Confirm kind == regression_check
5. Confirm baseline_ref is a concrete resolvable string (not vague)
6. Confirm threshold is numeric with documented units
7. Confirm metrics list is non-empty and matches ## Metrics section names
8. Confirm fail_action is defined (block | warn | log)
9. HARD gates: frontmatter valid, id pattern matches, baseline_ref present, threshold numeric, metrics non-empty
10. SOFT gates: score against QUALITY_GATES.md
11. Cross-check: is this a comparison (regression_check) or absolute measurement (benchmark)? Is it comparing current vs baseline (regression_check) or testing a single case (golden_test)?
12. Revise if score < 8.0 before outputting
