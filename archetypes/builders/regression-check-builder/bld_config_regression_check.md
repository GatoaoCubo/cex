---
kind: config
id: bld_config_regression_check
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.1
title: "Config Regression Check"
version: "1.0.0"
author: n03_builder
tags: [regression_check, builder, examples]
tldr: "Golden and anti-examples for regression check construction, demonstrating ideal structure and common pitfalls."
domain: "regression check construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_regression_check
  - p03_sp_regression_check_builder
  - bld_collaboration_regression_check
  - bld_instruction_regression_check
  - bld_schema_regression_check
  - p01_kc_regression_check
  - regression-check-builder
  - bld_tools_regression_check
  - bld_examples_regression_check
  - p11_qg_regression_check
---
# Config: regression_check Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p07_rc_{check_slug}.md` | `p07_rc_summarization_prod_weekly.md` |
| Builder directory | kebab-case | `regression-check-builder/` |
| Frontmatter fields | snake_case | `baseline_ref`, `fail_action`, `comparison_mode` |
| Check slug | snake_case, lowercase, no hyphens | `summarization_prod_weekly`, `chatbot_accuracy_gate` |
| Metric names | snake_case, noun or noun_qualifier | `accuracy`, `latency_p95`, `cost_per_call`, `hallucination_rate` |
| Baseline ref | framework-native format | `experiment/prod-v1.2`, `run/abc123`, `v2.1.0` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.

## File Paths
- Output: `cex/P07_evals/examples/p07_rc_{check_slug}.md`
- Compiled: `cex/P07_evals/compiled/p07_rc_{check_slug}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~4096 bytes
- Density: >= 0.80 (no filler)

## Threshold Conventions
| Mode | Format | Example | Notes |
|------|--------|---------|-------|
| relative | numeric percentage | `5.0` = 5% deviation | Most common — normalizes across metric scales |
| absolute | numeric delta | `0.05` = 0.05 point drop | Use when metric has fixed scale (0.0–1.0) |
Rule: ALWAYS document which convention is used in the artifact body. Mixed conventions in one artifact require per-metric documentation.

## Comparison Mode Enum
| Value | When to use |
|-------|-------------|
| relative | Percentage deviation from baseline value (default) |
| absolute | Fixed-point deviation from baseline value |

## Fail Action Enum
| Value | Meaning | When to use |
|-------|---------|-------------|
| block | Halt deployment or PR merge | Production pipelines, accuracy-critical systems |
| warn | Alert but allow to proceed | Staging, non-critical metrics, early monitoring |
| log | Record only, no alert | New metrics under observation, baseline calibration |

## Tool Invocation Patterns
| Tool | Check invocation |
|------|-----------------|
| Braintrust | `braintrust eval --compare <baseline_ref>` |
| Promptfoo | `promptfoo eval --compare <baseline_file>` |
| LangSmith | UI comparison or SDK `compare_runs(baseline_id, current_id)` |
| DeepEval | `deepeval test run --compare-to <baseline_file>` |
| costm | Document invocation command in ## Baseline section |

## Cadence Values
| Value | Meaning |
|-------|---------|
| on_pr | Runs on every pull request |
| on_deploy | Runs before each deployment |
| daily | Scheduled daily run |
| on_demand | Manual trigger only |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_regression_check]] | upstream | 0.44 |
| [[p03_sp_regression_check_builder]] | upstream | 0.37 |
| [[bld_collaboration_regression_check]] | downstream | 0.37 |
| [[bld_instruction_regression_check]] | upstream | 0.36 |
| [[bld_schema_regression_check]] | upstream | 0.35 |
| [[p01_kc_regression_check]] | upstream | 0.33 |
| [[regression-check-builder]] | upstream | 0.29 |
| [[bld_tools_regression_check]] | upstream | 0.29 |
| [[bld_examples_regression_check]] | upstream | 0.28 |
| [[p11_qg_regression_check]] | downstream | 0.28 |
