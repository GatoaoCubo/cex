---
kind: instruction
id: bld_instruction_drift_detector
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for drift_detector
pattern: 3-phase pipeline (scope -> compose -> validate)
quality: 7.1
title: "Instruction Drift Detector"
version: "1.0.0"
author: n03_builder
tags: [drift_detector, builder, instruction]
tldr: "3-phase process: scope drift target and statistical method, compose detector config, validate gates."
domain: "drift detector construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Instructions: How to Produce a drift_detector

## Phase 1: SCOPE
1. Identify what to monitor: input features, model outputs, behavioral patterns, or latency
2. Determine drift type: data drift (input distribution), concept drift (label/output distribution), prediction drift (output distribution), behavioral drift (response patterns)
3. Select statistical test: PSI for numerical with known baseline; KS for continuous distributions; chi-square/JS for categorical; embedding distance for text
4. Define reference window: fixed baseline (training data stats), rolling window (last N days), or seasonal baseline
5. Define production window: batch size or time window for comparison
6. Set threshold severity levels: warning (early detection) and critical (action required)
7. Declare alert destination: webhook URL, log file, signal file, or monitoring platform
8. Identify features or output dimensions to monitor (be specific, not "everything")

## Phase 2: COMPOSE
1. Read SCHEMA.md -- source of truth for all fields
2. Read OUTPUT_TEMPLATE.md -- fill `{{vars}}` following SCHEMA constraints
3. Fill frontmatter: all required fields (quality: null)
4. Write detection_method: statistical test + parameters
5. Write window_config: reference and production window specs
6. Write thresholds: warning and critical levels per feature
7. Write alert_rule: destination, frequency, suppression rules
8. Write features_monitored: list of input/output dimensions
9. Write Overview: 2 sentences on what this detector monitors and why
10. Verify body <= 3072 bytes

## Phase 3: VALIDATE
1. Check QUALITY_GATES.md -- verify each HARD gate manually
2. Confirm id matches `^p11_dd_[a-z][a-z0-9_]+$`
3. Confirm kind == drift_detector
4. Confirm detection_method is declared (not empty)
5. Confirm threshold has at least one level (warning or critical)
6. Confirm features_monitored is non-empty
7. HARD gates: frontmatter valid, id pattern, method declared, threshold set
8. Cross-check: not regression_check (no code test assertions), not benchmark (no eval metrics)
9. Revise if score < 8.0 -- most common fix: add window_config or alert_rule specifics
