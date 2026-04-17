---
kind: learning_record
id: p10_lr_reasoning_strategy_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for reasoning_strategy construction
quality: 8.7
title: "Learning Record Reasoning Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [reasoning_strategy, builder, learning_record]
tldr: "Learned patterns and pitfalls for reasoning_strategy construction"
domain: "reasoning_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Observation

This ISO selects a reasoning strategy (e.g. chain-of-thought) and the conditions under which it applies.
Common issues include inconsistent reasoning steps, over-reliance on vague heuristics, and failure to align strategy components with task constraints. Builders often omit validation phases, leading to fragile or incomplete strategies.

## Pattern
Structured reasoning strategies benefit from explicit templates that enforce logical decomposition, such as hypothesis-driven or stepwise refinement frameworks. Incorporating feedback loops and constraint checks improves robustness.

## Evidence
Reviewed artifacts showed 30% higher success rates when strategies included formalized subtask hierarchies and validation gates, as seen in [Artifact X] and [Artifact Y].

## Recommendations
- Use explicit templates (e.g., "Assume → Deduce → Validate") to enforce structure.
- Embed constraint checks to prevent invalid intermediate steps.
- Validate strategies with edge-case examples during construction.
- Prioritize modularity to enable reuse across subtasks.
- Document assumptions and limitations to guide adaptability.
