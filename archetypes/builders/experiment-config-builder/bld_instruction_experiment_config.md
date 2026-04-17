---
kind: instruction
id: bld_instruction_experiment_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for experiment_config
pattern: 3-phase pipeline (research -> compose -> validate)
quality: 9.0
title: "Instruction Experiment Config"
version: "1.0.0"
author: n03_builder
tags: [experiment_config, builder, instruction, P09]
tldr: "3-phase process: research experiment scope and metrics, compose variant catalog and statistical parameters, validate gates."
domain: "experiment config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
---

# Instructions: How to Produce an experiment_config
## Phase 1: RESEARCH
1. Identify the experiment subject: is this a prompt variant test, a feature rollout, a model comparison, or a UI/UX test?
2. Write the hypothesis: a falsifiable statement in the form "If [variant change] then [expected outcome] measured by [metric]"
3. Catalog all variants: name each (control = baseline, treatment_N = change being tested), describe what differs
4. Identify the primary metric: the single KPI that determines the winning variant (e.g., task_completion_rate, response_quality_score)
5. Identify guardrail metrics: metrics that must NOT regress even if the primary metric improves (e.g., latency_p99, error_rate)
6. Define traffic allocation: percentage for each variant; consider segment constraints (power_users only, new_users only, all)
7. Determine statistical parameters: significance threshold (default 0.05), minimum detectable effect (MDE), estimated sample size
8. Define experiment duration: how many days or how many samples before concluding
9. Check existing experiment_configs via brain_query [IF MCP] for the same domain -- avoid duplicate experiments
## Phase 2: COMPOSE
1. Read SCHEMA.md -- source of truth for all fields
2. Read OUTPUT_TEMPLATE.md -- fill the template following SCHEMA constraints
3. Fill all required frontmatter fields; set `quality: null` -- never self-score
4. Write **Overview** section: what is being tested, why it matters, what decision it enables
5. Write **Variants** section: table with columns name, type (control/treatment), description, key parameter changes
6. Write **Traffic Split** section: allocation table per variant (must sum to 100), segment rules, hold-out percentage if any
7. Write **Metrics** section: primary metric with direction and winning threshold; guardrail metrics with acceptable limits
8. Write **Statistical Parameters** section: significance_threshold, MDE, sample_size_target, duration_days, power calculation method
9. Write **Lifecycle** section: current status (draft/running/paused/concluded), key dates, decision criteria for conclusion
10. Confirm body <= 4096 bytes
## Phase 3: VALIDATE
1. Check QUALITY_GATES.md -- verify each HARD gate manually
2. Confirm YAML frontmatter parses without errors
3. Confirm `id` matches `^p09_ec_[a-z][a-z0-9_]+$`
4. Confirm variants list has at least 2 entries and first entry is "control"
5. Confirm traffic_split percentages sum to exactly 100
6. Confirm primary_metric is defined and single
7. Confirm guardrail_metrics is present (even if empty list)
8. Confirm significance_threshold and min_detectable_effect are specified
9. Confirm `quality` is null
10. Confirm body <= 4096 bytes
11. Cross-check: is this a temporary controlled trial? If this is a permanent on/off toggle it belongs in `feature_flag`.
    If these are deployment variables they belong in `env_config`. If this is a scoring rubric it belongs in `quality_gate`.
12. If score < 8.0: revise in the same pass before outputting
