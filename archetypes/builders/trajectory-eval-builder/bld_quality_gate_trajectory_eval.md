---
kind: quality_gate
id: p07_qg_trajectory_eval
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for trajectory_eval
quality: null
title: "Quality Gate Trajectory Eval"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [trajectory_eval, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for trajectory_eval"
domain: "trajectory_eval construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
| metric | threshold | operator | scope |  
|---|---|---|---|  
| trajectory_coverage | 95% | >= | all episodes |  
| divergence_from_optimal | 10% | <= | all episodes |  
| reward_consistency | 0.95 | >= | all episodes |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| p07_te_trajectory_coverage.md | Trajectory coverage meets threshold | <95% coverage in any episode |  
| p07_te_divergence_check.md | Divergence from optimal path | >10% deviation in any episode |  
| p07_te_reward_consistency.md | Reward consistency across episodes | <0.95 correlation coefficient |  
| p07_te_collision_check.md | No collisions in trajectory | Collision detected in any episode |  
| p07_te_smoothness_check.md | Trajectory smoothness | Jerk exceeds 2.0 m/s³ in any segment |  
| p07_te_goal_reachability.md | Goal reachability | <90% success rate in goal completion |  
| p07_te_time_efficiency.md | Time efficiency | >15% longer than optimal path |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| 1 | Coverage | 0.15 | 1.0 for 95%+ |  
| 2 | Divergence | 0.12 | 1.0 for <=10% |  
| 3 | Consistency | 0.10 | 1.0 for 0.95+ |  
| 4 | Smoothness | 0.08 | 1.0 for jerk <2.0 |  
| 5 | Collision | 0.07 | 1.0 for no collisions |  
| 6 | Reward | 0.10 | 1.0 for 0.95+ |  
| 7 | Completeness | 0.15 | 1.0 for 90%+ success |  
| 8 | Adaptability | 0.13 | 1.0 for dynamic path adjustments |  

## Actions  
| Score | Action |  
|---|---|  
| >=9.5 | GOLDEN |  
| >=8.0 | PUBLISH |  
| >=7.0 | REVIEW |  
| <7.0 | REJECT |  

## Bypass  
| conditions | approver | audit trail |  
|---|---|---|  
| Critical safety override | Senior engineer | Signed approval + timestamp |  
| Experimental trajectory | Lead researcher | Lab log entry |  
| Simulated environment only | QA lead | Simulation config hash |
