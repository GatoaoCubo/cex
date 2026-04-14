---
id: p11_qg_model_architecture
kind: quality_gate
pillar: P11
title: "Gate: model_architecture"
version: "1.0.0"
quality: null
author: n05_builder
tags: [model_architecture, quality_gate, P11, builder]
tldr: "10 HARD + 10 SOFT quality gates for model_architecture artifacts."
domain: "model_architecture construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
llm_function: GOVERN
---

# Quality Gate: model_architecture

## 10 HARD Gates (All Must Pass)
| # | Gate | Check | Fail Action |
|---|------|-------|------------|
| H01 | Schema compliance | All required frontmatter fields present | Add missing fields |
| H02 | Kind correct | `kind: model_architecture` | Fix kind |
| H03 | Pillar correct | `pillar: P02` | Fix pillar |
| H04 | quality: null | Never self-scored | Set to null |
| H05 | architecture_type enum | From allowed values | Fix to valid enum |
| H06 | parameter_count explicit | Not null, TBD, or unknown | Specify count |
| H07 | Layer Structure table | At least 3 layer rows documented | Add layer table |
| H08 | Parameter Profile | Total parameter count documented | Add param profile |
| H09 | Compute Profile | At least memory footprint documented | Add compute info |
| H10 | No proprietary weights | No model weights, API keys, or tokens | Remove secrets |

## 10 SOFT Gates (Target >= 7/10)
| # | Gate | Check | Weight |
|---|------|-------|--------|
| S01 | Density >= 0.85 | Information density score | 2x |
| S02 | Boundary conditions | Distinguishes from 3+ adjacent kinds | 1x |
| S03 | Connectivity documented | Attention patterns and skip connections | 1x |
| S04 | Framework specified | Named framework (pytorch/jax/etc.) | 1x |
| S05 | FLOPs documented | Inference compute documented | 1x |
| S06 | Training recommendations | Optimizer and LR schedule noted | 1x |
| S07 | Input/output modality | Both specified explicitly | 1x |
| S08 | Param breakdown | Per-component breakdown (not just total) | 1x |
| S09 | tldr present | One-sentence summary in frontmatter | 1x |
| S10 | Context length | Max sequence length documented | 1x |

## Scoring
| Score | Action |
|-------|--------|
| H01-H10 all pass + S >= 7/10 | PUBLISH |
| H01-H10 all pass + S 5-6/10 | PUBLISH with warning |
| Any H fails | REJECT |
| S < 5/10 | REVISE |
