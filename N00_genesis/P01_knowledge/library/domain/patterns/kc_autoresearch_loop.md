---
id: p01_kc_autoresearch_loop
kind: knowledge_card
type: domain
pillar: P01
title: "AutoResearch Loop — Autonomous Experiment Pattern"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: patterns
quality: 9.1
tags: [autoresearch, karpathy, experiment, autonomous, loop, self-improvement]
tldr: "Karpathy's AutoResearch pattern: 3-file architecture (goals + modifiable + metric), autonomous loop (modify → run → measure → keep/discard), git as experiment ledger."
when_to_use: "When you have a clear scalar metric and want autonomous improvement"
keywords: [autoresearch, experiment-loop, keep-discard, git-versioning, autonomous]
density_score: 1.0
linked_artifacts:
  primary: null
  related: []
related:
  - p01_kc_experiment_driven_development
  - p12_wf_auto_evolve
  - p03_sp_optimizer_builder
  - eval-metric-builder
  - p01_kc_prompt_evolution
  - eval-framework-builder
  - p01_kc_optimizer
  - loop
  - bld_collaboration_eval_metric
  - p03_sp_hitl_config_builder
---

# AutoResearch Loop

## Core Pattern

Give an AI agent one file to modify, one metric to optimize, and let it run experiments autonomously. Keep what improves, discard what doesn't.

## 3-File Architecture

| File | Role | Who writes | Who reads |
|------|------|-----------|-----------|
| `program.md` | Goals, constraints, rules | Human | Agent |
| `train.py` | The single modifiable target | Agent | Metric |
| `prepare.py` | Immutable evaluation metric | Human | Agent (read-only) |

## The Loop

```
LOOP FOREVER:
  1. Analyze current state → form hypothesis
  2. Modify the target file
  3. Run evaluation (fixed time budget)
  4. Measure result (one scalar metric)
  5. IF improved → git commit (KEEP)
     IF not → git reset (DISCARD)
  6. Log result to results.tsv
  7. NEVER STOP until human interrupts
```

## 3 Conditions for Success

1. **Clear metric** — one number, one direction (lower/higher)
2. **Automated evaluation** — no human in the loop during experiments
3. **One file to modify** — scope constraint prevents chaos

## When NOT to Use

- Metric is subjective (brand design, UX "feel")
- Evaluation requires human judgment per iteration
- Multiple coupled files must change together
- The loop would be too slow (>1 hour per experiment)

## Anti-Pattern

Bad metric → confident optimization in wrong direction. "If you give it a bad metric, it will very confidently optimize the wrong thing." — Karpathy

## CEX Mapping

| AutoResearch | CEX |
|-------------|-----|
| program.md | CLAUDE.md + spec + quality_gate |
| train.py | Any .md artifact |
| prepare.py | cex_score.py + cex_compile.py |
| results.tsv | .cex/experiments/results.tsv |
| git commit | cex_evolve.py keep |
| git reset | cex_evolve.py discard |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_experiment_driven_development]] | sibling | 0.41 |
| [[p12_wf_auto_evolve]] | downstream | 0.27 |
| [[p03_sp_optimizer_builder]] | downstream | 0.19 |
| [[eval-metric-builder]] | downstream | 0.19 |
| [[p01_kc_prompt_evolution]] | sibling | 0.18 |
| [[eval-framework-builder]] | downstream | 0.18 |
| [[p01_kc_optimizer]] | sibling | 0.18 |
| [[loop]] | downstream | 0.17 |
| [[bld_collaboration_eval_metric]] | downstream | 0.16 |
| [[p03_sp_hitl_config_builder]] | downstream | 0.16 |
