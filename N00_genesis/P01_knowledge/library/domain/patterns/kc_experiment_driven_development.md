---
id: p01_kc_experiment_driven_development
kind: knowledge_card
8f: F3_inject
type: domain
pillar: P01
title: "Experiment-Driven Development"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: patterns
quality: 9.0
tags: [experiment, development, ab-testing, metric, autonomous, optimization]
tldr: "Generalization of AutoResearch: any domain with a clear metric can be improved through autonomous experiment loops — marketing, code, prompts, pricing."
when_to_use: "Generalizing AutoResearch beyond ML training to any measurable domain"
keywords: [experiment-driven, ab-testing, metric-optimization, autonomous-loop]
density_score: 0.93
related:
  - p01_kc_autoresearch_loop
  - p03_sp_optimizer_builder
  - p01_kc_optimizer
  - bld_collaboration_eval_metric
  - p11_qg_experiment_config
  - eval-metric-builder
  - p01_kc_prompt_evolution
  - eval-framework-builder
  - p01_kc_experiment_config
  - n01_atom_26_evaluation_taxonomy
---

# Experiment-Driven Development

## Core Idea

AutoResearch is not just for ML. Any domain with a measurable outcome can use the same pattern: hypothesis → modify → measure → keep/discard.

## Domain Applications

| Domain | Modifiable | Metric | Evaluation |
|--------|-----------|--------|------------|
| ML Training | model architecture (train.py) | val_bpb (lower=better) | Fixed 5-min training run |
| Website Speed | HTML/CSS/JS | Load time (ms, lower=better) | Puppeteer benchmark |
| Prompt Engineering | system prompt | Output quality score | LLM-as-judge |
| Marketing Copy | Email/ad text | Conversion rate | A/B test results |
| Trading Strategy | Buy/sell rules | Sharpe ratio | Backtesting engine |
| Code Performance | Algorithm | Execution time (ms) | Benchmark suite |
| KC Quality | Knowledge card | Density + quality score | cex_score.py |

## The Generalized 3-File Pattern

| Component | Purpose | Constraint |
|-----------|---------|-----------|
| **Goal Document** | What to optimize, what constraints | Human-written, immutable during run |
| **Target Artifact** | The single thing being modified | Agent-written, one file only |
| **Evaluation Script** | How to measure success | Immutable, automated, returns scalar |

## Key Insight: Metric Selection

"Most marketing teams run 30 experiments per year. The next generation will run 36,000." The bottleneck is not execution (AI agents make that free) — it's knowing WHAT to measure.

| Metric Quality | Result |
|---------------|--------|
| Good metric (load time, conversion rate) | Genuine improvement |
| Bad metric (word count, character count) | Confident wrong optimization |
| Subjective metric (looks nice, feels good) | Random walk, no convergence |

## Anti-Pattern: Gaming the Metric

If the metric is gameable (e.g., "make text shorter" measured by character count), the agent will degenerate content to pass the metric. Always pair a primary metric with a constraint (e.g., "shorter BUT all required sections present").

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_autoresearch_loop]] | sibling | 0.36 |
| [[p03_sp_optimizer_builder]] | downstream | 0.23 |
| [[p01_kc_optimizer]] | sibling | 0.22 |
| [[bld_collaboration_eval_metric]] | downstream | 0.22 |
| [[p11_qg_experiment_config]] | downstream | 0.20 |
| [[eval-metric-builder]] | downstream | 0.20 |
| [[p01_kc_prompt_evolution]] | sibling | 0.20 |
| [[eval-framework-builder]] | downstream | 0.20 |
| [[p01_kc_experiment_config]] | sibling | 0.19 |
| [[n01_atom_26_evaluation_taxonomy]] | sibling | 0.19 |
