---
kind: architecture
id: bld_architecture_reward_signal
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of reward_signal — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Reward Signal"
version: "1.0.0"
author: n03_builder
tags: [reward_signal, builder, examples]
tldr: "Golden and anti-examples for reward signal construction, demonstrating ideal structure and common pitfalls."
domain: "reward signal construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_reward_signal_builder
  - p11_qg_reward_signal
  - bld_output_template_reward_signal
  - bld_instruction_reward_signal
  - bld_examples_reward_signal
  - reward-signal-builder
  - bld_collaboration_reward_signal
  - bld_knowledge_card_reward_signal
  - bld_schema_reward_signal
  - p01_kc_reward_signal
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| signal_type | Computation mechanism — how the reward is produced | reward_signal | required |
| scale | Numeric range with semantic meaning at boundaries | reward_signal | required |
| model | Producer of the reward score (LLM or human) | reward_signal | required |
| criteria | Weighted quality dimensions with low/high anchors | reward_signal | required |
| baseline | Minimum acceptable score within scale range | reward_signal | required |
| frequency | Cadence at which the signal is evaluated | reward_signal | required |
| aggregation | Method for combining multi-criteria scores | reward_signal | required |
| scoring_rubric | Static criteria taxonomy that informs criteria ofsign | P11 | upstream |
| quality_gate | Binary pass/fail consumer of reward scores | P11 | downstream |
| training_pipeline | RLHF/DPO consumer that ingests reward scores | P02 | consumer |
| monitoring_pipeline | Production consumer tracking rolling average vs baseline | P09 | consumer |
| guardrail | Execution constraint — minimum score before output is served | P11 | external |
## Dependency Graph
```
scoring_rubric    --informs-->   criteria
model             --produces-->  signal_type
criteria          --computes-->  scale
aggregation       --combines-->  criteria
baseline          --gates-->     aggregation
signal_type       --produces-->  reward_score
reward_score      --feeds-->     training_pipeline
reward_score      --feeds-->     monitoring_pipeline
reward_score      --gates-->     quality_gate
guardrail         --depends-->   baseline
```
| From | To | Type | Data |
|------|----|------|------|
| scoring_rubric | criteria | informs | dimension names and definitions |
| model | signal_type | produces | numeric score or preference label |
| criteria | scale | computes | weighted sum producing final score |
| aggregation | criteria | combines | mean/weighted_mean/min/max/last |
| baseline | aggregation | gates | threshold triggering retraining or filtering |
| signal_type | reward_score | produces | scalar, preference pair, critique, ranking, implicit |
| reward_score | training_pipeline | feeds | chosen/rejected pairs or scalar rewards for RLHF/DPO |
| reward_score | monitoring_pipeline | feeds | rolling average vs baseline for production health |
| reward_score | quality_gate | gates | continuous score consumed by binary pass/fail gate |
| guardrail | baseline | depends | execution policy uses baseline as minimum serving threshold |
## Boundary Table
| reward_signal IS | reward_signal IS NOT |
|-----------------|----------------------|
| Continuous numeric score driving learning | Binary pass/fail decision (that is quality_gate) |
| Produced per-turn, per-task, or on-demand | Static criteria taxonomy (that is scoring_rubric) |
| Feeds RLHF, DPO, filtering, or monitoring loops | Operational KPI tracking business outcome (that is metric/kpi) |
| Calibrated with baseline and scale semantics | Raw log or event stream (that is telemetry) |
| Consumed by training or monitoring pipelines | Human judgment artifact with no quantification (that is rubric) |
| Multi-criteria to prevent reward hacking | Single-number score with no decomposition |
## Layer Map
| Layer | Components | Purpose |
|-------|-----------|---------|
| definition | signal_type, scale, model | Specify what is scored and how |
| decomposition | criteria, aggregation | Break quality into weighted dimensions |
| calibration | baseline, frequency | Anchor signal to meaningful thresholds |
| governance | guardrail, quality_gate | Enforce minimum standards at serving time |
| consumers | training_pipeline, monitoring_pipeline | Drive improvement and detect regression |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_reward_signal_builder]] | downstream | 0.54 |
| [[p11_qg_reward_signal]] | downstream | 0.52 |
| [[bld_output_template_reward_signal]] | upstream | 0.49 |
| [[bld_instruction_reward_signal]] | upstream | 0.47 |
| [[bld_examples_reward_signal]] | upstream | 0.46 |
| [[reward-signal-builder]] | downstream | 0.44 |
| [[bld_collaboration_reward_signal]] | downstream | 0.42 |
| [[bld_knowledge_card_reward_signal]] | upstream | 0.40 |
| [[bld_schema_reward_signal]] | downstream | 0.35 |
| [[p01_kc_reward_signal]] | downstream | 0.34 |
