---
kind: knowledge_card
id: bld_knowledge_card_trajectory_eval
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for trajectory_eval production
quality: 9.2
title: "Knowledge Card Trajectory Eval"
version: "1.1.0"
author: n01_hybrid_review4
tags: [trajectory_eval, builder, knowledge_card, llm_agent, step_eval]
tldr: "Domain knowledge for evaluating LLM agent decision trajectories: step-level scoring, path analysis, task completion measurement."
domain: "trajectory_eval construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
related:
  - bld_tools_trajectory_eval
  - bld_output_template_trajectory_eval
  - n01_atom_26_evaluation_taxonomy
  - p10_lr_chain_builder
  - bld_instruction_trajectory_eval
  - atom_19_agent_taxonomy_surveys
  - bld_architecture_trajectory_eval
  - bld_architecture_chain
  - bld_schema_trajectory_eval
  - p11_qg_chain
---

## Domain Overview
Trajectory evaluation in the LLM agent context measures the quality of an agent's sequential
decision-making path across a multi-step task. Unlike static benchmarks that score final outputs,
trajectory eval scores EACH step: was the observation interpreted correctly? Was the tool call
necessary and accurate? Did the reasoning chain maintain goal alignment throughout?

Key applications include autonomous coding agents (SWE-bench), web navigation agents (WebArena),
computer-use agents (OSWorld), and API-calling agents (tau-bench). Trajectory eval bridges
offline benchmark scores and production monitoring by decomposing task performance into
granular, diagnosable step records.

## Key Concepts
| Concept | Definition | Source |
|--------|------------|--------|
| Step-level evaluation | Scoring each (observation, reasoning, action) triple individually | AgentBench (Liu et al. 2023) |
| Task success rate | Binary or partial-credit completion of the final goal | SWE-bench (Jimenez et al. 2024) |
| Path efficiency | Steps taken / minimum steps required (closer to 1.0 = better) | WebArena (Zhou et al. 2023) |
| Tool call accuracy | Precision/recall of tool invocations vs. ground-truth trace | tau-bench (Yao et al. 2024) |
| Trajectory completeness | Fraction of required sub-goals reached before terminal state | OSWorld (Xie et al. 2024) |
| Backtrack rate | Frequency of redundant or reversed actions in the trajectory | AgentBench (Liu et al. 2023) |
| Reasoning consistency | Degree to which step-level reasoning aligns with the stated goal | Self-Refine (Madaan et al. 2023) |
| Grounding accuracy | Correctness of environment observations fed into the next step | WebArena (Zhou et al. 2023) |

## Industry Standards and Benchmarks
- **AgentBench** (Liu et al., 2023): Multi-environment LLM-as-agent benchmark; step-level reward signals.
- **WebArena** (Zhou et al., 2023): Web navigation trajectories scored on task_success + efficiency.
- **SWE-bench** (Jimenez et al., 2024): Software engineering agent eval; trajectory = patch + test cycle.
- **OSWorld** (Xie et al., 2024): GUI agent trajectories across 369 computer tasks.
- **tau-bench** (Yao et al., 2024): Tool-agent-user trajectories for retail/airline task simulation.
- **MT-Bench** (Zheng et al., 2023): Multi-turn conversation quality via LLM-as-judge.
- **GAIA** (Mialon et al., 2023): General AI assistant benchmark with tool-use trajectories.

## Common Patterns
1. **Ground-truth trace comparison**: Compare agent trajectory step-by-step against an expert trace.
2. **LLM-as-judge scoring**: Use a judge model to score reasoning quality at each step (MT-Bench pattern).
3. **Partial credit rubrics**: Award partial scores for correct sub-goals even if final goal fails.
4. **Backtrack detection**: Flag and penalize revisiting already-failed states.
5. **Tool provenance tracking**: Log all tool calls with inputs/outputs for replay and diff analysis.

## Pitfalls
- Confusing trajectory_eval (LLM agent step eval) with robotic path planning (Euclidean distance, jerk).
- Using only final-state success as the metric -- misses diagnostic value of step-level analysis.
- Ignoring partial task completion (e.g., agent got 8/10 steps right but scored 0% for missing final step).
- Allowing hallucinated tool outputs to propagate unchecked through the trajectory.
- Comparing trajectories without controlling for environment stochasticity (seed, state).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_trajectory_eval]] | downstream | 0.41 |
| [[bld_output_template_trajectory_eval]] | downstream | 0.36 |
| [[n01_atom_26_evaluation_taxonomy]] | sibling | 0.32 |
| [[p10_lr_chain_builder]] | downstream | 0.32 |
| [[bld_instruction_trajectory_eval]] | downstream | 0.29 |
| [[atom_19_agent_taxonomy_surveys]] | sibling | 0.29 |
| [[bld_architecture_trajectory_eval]] | downstream | 0.29 |
| [[bld_architecture_chain]] | downstream | 0.28 |
| [[bld_schema_trajectory_eval]] | downstream | 0.28 |
| [[p11_qg_chain]] | downstream | 0.26 |
