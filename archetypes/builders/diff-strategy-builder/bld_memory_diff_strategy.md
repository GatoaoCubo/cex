---
kind: learning_record
id: p10_lr_diff_strategy_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for diff_strategy construction
quality: 8.7
title: "Learning Record Diff Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [diff_strategy, builder, learning_record]
tldr: "Learned patterns and pitfalls for diff_strategy construction"
domain: "diff_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Observation
Developers often introduce noise by conflating structural changes with content-only differences. Overly aggressive fuzzy matching frequently leads to incorrect patch applications in edge cases.

## Pattern
Decoupling the detection algorithm from the application logic ensures higher reliability. Implementing a strategy-based approach allows for switching between strict and lenient matching without altering the core engine.

## Evidence
Reviewed recent implementations of text-based and structural diffing modules.

## Recommendations
* Isolate the matching algorithm from the patch application logic.
* Define explicit thresholds for fuzzy matching to prevent drift.
* Standardize whitespace and line-ending handling within the strategy.
* Avoid including parsing or formatting logic in the strategy builder.
* Implement regression tests specifically for character-shift edge cases.
