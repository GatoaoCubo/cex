---
kind: quality_gate
id: p02_qg_training_method
pillar: P11
llm_function: GOVERN
quality: 9.1
title: "Quality Gate Training Method"
version: "1.0.0"
author: n01_review
tags: [training_method, builder, quality_gate]
tldr: "10-gate quality check for training_method: validates frontmatter, learning paradigm, compute profile, hyperparameters, and dataset spec."
domain: "training_method construction"
created: "2026-04-13"
updated: "2026-04-14"
density_score: 0.88
purpose: Quality gate with HARD and SOFT scoring for training_method
related:
  - p11_qg_agent_computer_interface
  - bld_examples_training_method
  - bld_instruction_training_method
  - training-method-builder
  - p11_qg_model_architecture
  - bld_output_template_training_method
  - p11_qg_input_schema
  - p03_sp_training_method_builder
  - bld_schema_training_method
  - p11_qg_knowledge_card
---

## Quality Gate

## Definition
| Field | Value |
|-------|-------|
| metric | weighted soft score + all HARD gates pass |
| threshold | 7.0 to publish; 8.0 for pool; 9.0 for golden |
| operator | AND (all HARD) + weighted average (SOFT) |
| scope | any artifact with kind: training_method |

## HARD Gates
All must pass. Any failure = immediate reject.
| ID | Check | Fail Condition |
|----|-------|----------------|
| H01 | Frontmatter parses as valid YAML | Parse error on any field |
| H02 | ID matches ^p02_tm_[a-z][a-z0-9_]+$ | Wrong prefix, uppercase, or bad chars |
| H03 | kind equals literal training_method | Any other kind value |
| H04 | pillar equals P02 | Wrong pillar |
| H05 | quality field is null | Any non-null value |
| H06 | learning_paradigm is one of: supervised / unsupervised / reinforcement / self_supervised / transfer / hybrid | Unlisted or missing value |
| H07 | compute_intensity is one of: low / medium / high | Unlisted or missing value |
| H08 | Dataset Requirements section present with format and preprocessing | Missing section or missing required fields |
| H09 | Evaluation section present with >= 1 metric | Missing section or no metrics |
| H10 | No credentials, API keys, or tokens in any field | Credential detected |

## SOFT Scoring
Total weights sum to 1.00.
| ID | Dimension | Weight | 10 pts | 5 pts | 0 pts |
|----|-----------|--------|--------|-------|-------|
| S01 | Paradigm specification | 0.20 | Paradigm, objective, label requirements all documented | Paradigm named, objective missing | No paradigm documented |
| S02 | Compute profile completeness | 0.15 | Hardware, memory, training time, parallelism all specified | Hardware specified, time/memory missing | Only intensity label, no details |
| S03 | Hyperparameter coverage | 0.15 | LR, batch_size, epochs, optimizer, scheduler all present | 3+ params present | Fewer than 3 params |
| S04 | Dataset spec quality | 0.15 | Source, size, format, field_mapping, preprocessing all specified | Source + format only | No dataset details |
| S05 | Evaluation strategy | 0.10 | Metrics, validation frequency, convergence criteria all specified | Metrics named, no convergence | No evaluation criteria |
| S06 | Boundary disambiguation | 0.10 | Clearly distinguishes from finetune_config / model_card / reward_model | Partial disambiguation | No boundary conditions |
| S07 | Industry citation | 0.10 | References authoritative sources (SFT, DPO, PPO, LoRA, CAI) | Concepts used but not cited | Generic descriptions only |
| S08 | Density discipline | 0.05 | All content in tables, no padding prose | Minor prose padding | Mostly prose, low density |

**Score = sum(pts * weight) / sum(max_pts * weight) * 10**

## Actions
| Score | Tier | Action |
|-------|------|--------|
| >= 9.0 | Golden | Publish as reference training spec |
| >= 8.0 | Skilled | Publish to pool + log pattern |
| >= 7.0 | Learning | Use but flag for improvement |
| < 7.0 | Rejected | Return to author with gate report |

## Bypass
| Field | Value |
|-------|-------|
| Conditions | Novel training paradigm with no established hyperparameter conventions |
| Approver | N01 researcher or domain expert |

## Examples

# Examples: training_method Artifacts

## Example 1: Supervised Text Classification
```yaml
---
id: p02_tm_text_classification_bert
kind: training_method
pillar: P02
title: "Supervised Text Classification with BERT"
version: "1.0.0"
learning_paradigm: supervised
compute_intensity: medium
domain: NLP
quality: null
---
## Overview
Supervised fine-tuning of BERT-base for binary/multi-class text classification.

## Learning Paradigm
| Attribute | Value |
|-----------|-------|
| paradigm | supervised |
| objective | cross-entropy loss |
| requires_labels | Yes (class labels) |

## Compute Profile
| Attribute | Value |
|-----------|-------|
| intensity | medium |
| hardware | 1x A100 40GB or 4x RTX 3090 |
| memory | ~12GB per GPU |

## Hyperparameters
| Parameter | Value |
|-----------|-------|
| learning_rate | 2e-5 |
| batch_size | 32 |
| epochs | 3 |
| optimizer | adamw |
| warmup_ratio | 0.1 |
```

## Example 2: Self-Supervised Pre-training (MLM)
```yaml
---
id: p02_tm_mlm_pretraining
kind: training_method
pillar: P02
title: "Masked Language Model Pre-training"
learning_paradigm: self_supervised
compute_intensity: high
domain: NLP
quality: null
---
## Overview
Self-supervised pre-training with masked language modeling (MLM) objective.

## Learning Paradigm
| Attribute | Value |
|-----------|-------|
| paradigm | self_supervised |
| objective | MLM (predict masked tokens, 15% mask rate) |
| requires_labels | No |

## Compute Profile
| Attribute | Value |
|-----------|-------|
| intensity | high |
| hardware | 8x A100 80GB (DDP) |
| memory | ~60GB aggregate |
```

## Example 3: Reinforcement Learning from Human Feedback
```yaml
---
id: p02_tm_rlhf_alignment
kind: training_method
pillar: P02
title: "RLHF Alignment Training"
learning_paradigm: reinforcement
compute_intensity: high
domain: LLM_alignment
quality: null
---
## Overview
PPO-based RLHF for aligning LLM outputs to human preferences.

## Learning Paradigm
| Attribute | Value |
|-----------|-------|
| paradigm | reinforcement |
| objective | maximize reward model score via PPO |
| reward_signal | human preference labels + reward_model |
```

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
