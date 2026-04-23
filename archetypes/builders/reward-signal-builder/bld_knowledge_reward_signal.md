---
kind: knowledge_card
id: bld_knowledge_card_reward_signal
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for reward_signal production — continuous quality scoring for agent improvement
sources: RLHF literature, DPO paper (Rafailov 2023), Constitutional AI (Anthropic 2022), LLM-as-judge (Zheng 2023)
quality: 9.1
title: "Knowledge Card Reward Signal"
version: "1.0.0"
author: n03_builder
tags: [reward_signal, builder, examples]
tldr: "Golden and anti-examples for reward signal construction, demonstrating ideal structure and common pitfalls."
domain: "reward signal construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_reward_signal
  - p01_kc_reward_and_alignment
  - reward-signal-builder
  - p10_lr_reward_signal_builder
  - bld_instruction_reward_signal
  - p03_sp_reward_signal_builder
  - bld_architecture_reward_signal
  - bld_examples_reward_signal
  - bld_output_template_reward_signal
  - bld_config_reward_signal
---

# Domain Knowledge: reward_signal
## Executive Summary
Reward signals are continuous quality scores that drive agent improvement through learning loops. Unlike quality gates (binary pass/fail) or scoring rubrics (static criteria), reward signals feed live systems: RLHF reward models, DPO preference datasets, Constitutional AI critique cycles, and LLM-as-judge monitoring pipelines. Calibration — scale semantics, baseline, anti-reward-hacking design — is load-bearing.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P11 (Feedback) |
| llm_function | GOVERN (quality enforcement) |
| Signal types | scalar, preference, critique, comparative, implicit |
| Scale options | 0-1, 0-10, binary, -1_to_1 |
| Baseline | minimum acceptable score; triggers retraining or filtering below |
| Frequency | per_turn, per_task, per_session, on_demand |
| Aggregation | mean, weighted_mean, min, max, last |
## Signal Types
| Type | Mechanism | Use case | Hacking risk |
|------|-----------|----------|--------------|
| scalar | LLM-judge assigns 0-1 score | General quality | High if single criterion |
| preference | Human/model picks A > B | RLHF training data | Medium — noise |
| critique | LLM critiques + revises + scores | Constitutional AI | Low — multi-step |
| comparative | N outputs ranked | DPO dataset construction | Medium — drift |
| implicit | Edits, clicks, re-prompts | Production monitoring | Low — ground truth |
## Key Concepts
- **RLHF**: preference pairs -> reward model -> PPO policy optimization
- **DPO**: preference pairs (chosen/rejected) -> direct policy optimization via Bradley-Terry; no reward model
- **Constitutional AI**: LLM evaluates output against principles -> critique + revision; signal type: critique
- **LLM-as-judge**: peer model scores outputs; calibrate against positional and verbosity bias
## Patterns
| Pattern | When to use |
|---------|-------------|
| Multi-criteria scalar | >= 2 weighted criteria (e.g. accuracy 0.4 + tone 0.3 + conciseness 0.3) |
| Preference pairs | RLHF dataset building; human rates A>B |
| Critique cycle | Constitutional AI pipeline; critique -> revise -> score |
| Implicit signal | Production monitoring; edit distance after generation |
- Baseline: set at P20 of human-rated outputs; recalibrate each training cycle
- Criteria: weights sum to 1.0; minimum 2 dimensions; safety dims use `min` aggregation
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Single-dimension reward | Model maximizes proxy; other dimensions degrade |
| No baseline calibration | Cannot distinguish good from acceptable |
| Verbosity bias | LLM-judge rates longer outputs higher; normalize by length |
| Positional bias | Judge prefers first-presented output; swap-and-average |
| Conflating with quality_gate | Continuous scores carry gradient; thresholding discards it |
| Static criteria | Criteria become trivially satisfied; refresh each cycle |
## Application Loops
1. **RLHF**: reward_signal -> reward model -> PPO -> deployment
2. **DPO**: preference pairs -> direct policy optimization -> deployment
3. **Filtering**: score outputs -> exclude below baseline -> training data
4. **Monitoring**: per-turn scores -> alert on rolling average drop -> retraining
## References
- Rafailov (2023): DPO | Bai (2022): Constitutional AI | Zheng (2023): LLM-as-Judge | reward-bench.github.io

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_reward_signal]] | downstream | 0.57 |
| [[p01_kc_reward_and_alignment]] | sibling | 0.54 |
| [[reward-signal-builder]] | downstream | 0.51 |
| [[p10_lr_reward_signal_builder]] | downstream | 0.48 |
| [[bld_instruction_reward_signal]] | downstream | 0.46 |
| [[p03_sp_reward_signal_builder]] | downstream | 0.46 |
| [[bld_architecture_reward_signal]] | downstream | 0.44 |
| [[bld_examples_reward_signal]] | downstream | 0.42 |
| [[bld_output_template_reward_signal]] | downstream | 0.40 |
| [[bld_config_reward_signal]] | downstream | 0.40 |
