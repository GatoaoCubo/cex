---
kind: quality_gate
id: p07_qg_trajectory_eval
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for trajectory_eval
quality: 9.0
title: "Quality Gate Trajectory Eval"
version: "1.1.0"
author: n01_hybrid_review4
tags: [trajectory_eval, builder, quality_gate]
tldr: "Quality gate for trajectory_eval artifacts: HARD structural checks + SOFT 5D scoring."
domain: "trajectory_eval construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.86
related:
  - bld_examples_trajectory_eval
  - bld_output_template_trajectory_eval
  - bld_schema_trajectory_eval
  - p07_qg_benchmark_suite
  - bld_knowledge_card_trajectory_eval
  - bld_instruction_trajectory_eval
  - p07_qg_memory_benchmark
  - p11_qg_benchmark
  - bld_architecture_benchmark
  - bld_architecture_trajectory_eval
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| required_fields_present | 100% | == | frontmatter |
| id_pattern_match | true | == | artifact id |
| step_log_rows | >=1 | >= | body |
| evaluation_metrics_present | true | == | body |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Syntax errors or missing required fields |
| H02 | ID matches ^p07_te_[a-z][a-z0-9_]+$ | ID does not match pattern |
| H03 | kind field equals 'trajectory_eval' | kind is absent or mismatched |
| H04 | agent_id is non-empty | agent_id missing or blank |
| H05 | task_id is non-empty | task_id missing or blank |
| H06 | step_count >= 1 | step_count is zero or absent |
| H07 | Step Log section present with at least one row | Body has no step log table |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D1 | Step coverage | 0.20 | 1.0 = all steps logged with observation+action+outcome |
| D2 | Metric completeness | 0.20 | 1.0 = task_success + path_efficiency + tool_call_accuracy present |
| D3 | Failure analysis depth | 0.20 | 1.0 = first failure step identified with root cause |
| D4 | Benchmark alignment | 0.20 | 1.0 = task_id matches a known benchmark (AgentBench/WebArena/SWE-bench) |
| D5 | Actionability | 0.20 | 1.0 = recommendations target specific step failures |

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
| Experimental agent under active development | Research lead | Issue tracker link |
| Incomplete benchmark environment | QA lead | Environment config hash |

## Examples

## Golden Example
```markdown
---
cex_kind: trajectory_eval
title: "Trajectory Evaluation of RL Agent in Maze Navigation"
description: "Evaluation of a reinforcement learning agent's trajectory in a simulated maze environment using Stable Baselines3 and Gym."
tags: [reinforcement_learning, trajectory_analysis, gym]
---

**Methodology**:
- **Environment**: OpenAI Gym's `MiniGrid-Maze-10x10-v0`
- **Agent**: PPO algorithm implemented with Stable Baselines3 (version 2.0.0)
- **Evaluation Metrics**:
  - Path efficiency (shortest path vs. taken path)
  - Collision rate
  - Time to goal
- **Setup**: 100 episodes, 5 random seeds, 1000 steps per episode
- **Results**:
  - Average path efficiency: 85%
  - Collision rate: 2.3%
  - Time to goal: 120 steps (±15)
```

## Anti-Example 1: Confusing with Static Benchmark
```markdown
---
cex_kind: trajectory_eval
title: "Static Benchmark for Language Model"
description: "Evaluation of a language model on GLUE benchmark tasks."
tags: [nlp, benchmark]
---

**Methodology**:
- **Model**: Hugging Face's `bert-base-uncased`
- **Tasks**: MNLI, SST-2, QQP
- **Metrics**: Accuracy, F1 score
- **Results**:
  - MNLI: 87% accuracy
  - SST-2: 92% accuracy
```
## Why it fails
This example evaluates a static model on benchmark tasks, not agent trajectories. It lacks environment interaction, episode-based metrics, and trajectory-specific analysis.

## Anti-Example 2: Missing Environment Details
```markdown
---
cex_kind: trajectory_eval
title: "Unspecified Agent Evaluation"
description: "Evaluation of an unspecified agent in an unspecified environment."
tags: [unknown]
---

**Methodology**:
- **Agent**: [Not specified]
- **Environment**: [Not specified]
- **Metrics**:
  - "Success rate"
  - "Reward"
- **Results**:
  - "Success rate: 70%"
```
## Why it fails
The example lacks critical details about the environment, agent, and evaluation setup. Metrics like "success rate" are vague without context, making the evaluation non-reproducible and unverifiable.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
