---
kind: quality_gate
id: p07_qg_reward_model
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for reward_model
quality: 9.0
title: "Quality Gate Reward Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [reward_model, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for reward_model"
domain: "reward_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_examples_reward_model
  - p02_qg_rl_algorithm
  - p10_lr_reward_model_builder
  - p07_qg_benchmark_suite
  - bld_knowledge_card_reward_model
  - reward-model-builder
  - bld_tools_reward_model
  - p07_qg_eval_metric
  - p09_qg_marketplace_app_manifest
  - p07_qg_cohort_analysis
---

## Quality Gate

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| Reward Model Validity | 100% | equals | All reward configurations |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML valid | Invalid YAML syntax |
| H02 | ID matches pattern | ID does not match `^p07_rwm_[a-zA-Z0-9]+$` |
| H03 | kind matches | `kind` ≠ `reward_model` |
| H04 | Reward parameters defined | Missing required parameters (e.g., `weight`, `threshold`) |
| H05 | Threshold numeric | Threshold is non-numeric or out of range |
| H06 | Outcome alignment | Outcomes not linked to measurable KPIs |
| H07 | Documentation exists | No README or configuration guide provided |
| H08 | Versioning applied | Missing `version` field or invalid format |
| H09 | No duplicate IDs | Duplicate ID detected in configuration |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | YAML Structure | 0.15 | 1.0 if valid, 0.5 if partial, 0.0 if invalid |
| D02 | ID Pattern | 0.10 | 1.0 if matches, 0.0 otherwise |
| D03 | Kind Consistency | 0.10 | 1.0 if correct, 0.0 otherwise |
| D04 | Reward Parameters | 0.15 | 1.0 if complete, 0.5 if partial, 0.0 if missing |
| D05 | Threshold Validity | 0.10 | 1.0 if numeric and valid, 0.0 otherwise |
| D06 | Outcome Alignment | 0.15 | 1.0 if aligned, 0.5 if weak, 0.0 if none |
| D07 | Documentation | 0.10 | 1.0 if present, 0.0 otherwise |
| D08 | Versioning | 0.10 | 1.0 if valid, 0.0 otherwise |
| D09 | Duplicate Checks | 0.05 | 1.0 if no duplicates, 0.0 otherwise |

## Actions
| Score | Action |
|---|---|
| GOLDEN (≥9.5) | Auto-approve and notify stakeholders |
| PUBLISH (≥8.0) | Require review by PM and QA |
| REVIEW (≥7.0) | Flag for feedback and minor fixes |
| REJECT (<7.0) | Block deployment; require rework |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Emergency fix required | CTO | "Bypassed by [CTO] on [date] for critical issue" |
| Legacy system compatibility | CTO | "Bypassed by [CTO] on [date] for legacy integration" |

## Examples

## Golden Example
```yaml
title: "Dialogue Quality Reward Model"
description: "Reward model for evaluating conversational AI based on coherence, relevance, and safety"
metrics:
  - name: "coherence_score"
    type: "float"
    description: "Score from 0-1 based on linguistic coherence"
  - name: "task_completion"
    type: "binary"
    description: "1 if user goal is achieved, 0 otherwise"
scoring_rules:
  - if: "response contains harmful content"
    then: "coherence_score = 0; task_completion = 0"
  - if: "response directly answers question"
    then: "task_completion = 1"
  - if: "response uses 3+ grammatical errors"
    then: "coherence_score -= 0.3"
example:
  input: "Explain quantum physics"
  output: "Quantum physics studies particles at atomic scales..."
  scores: {coherence_score: 0.95, task_completion: 1}
```

## Anti-Example 1: Vague Metrics
```yaml
title: "Generic Reward Model"
description: "Make things better"
metrics:
  - name: "quality"
    type: "unknown"
    description: "How good the output is"
```
## Why it fails
Lacks specific, measurable metrics. "Quality" is subjective without defined criteria, scoring rules, or calculation methods. Fails to provide actionable guidance for implementation.

## Anti-Example 2: Algorithm Confusion
```yaml
title: "PPO Reward Model"
description: "Uses PPO algorithm for training"
metrics:
  - name: "reward"
    type: "float"
    description: "Calculated by PPO during training"
```
## Why it fails
Mixes reward model configuration with training algorithm details. The boundary explicitly excludes RL algorithms. The "reward" metric is defined by the training process rather than the evaluation criteria itself.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
