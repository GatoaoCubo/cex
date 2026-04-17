---
kind: config
id: bld_config_preference_dataset
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints for preference_dataset
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 20
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 7.8
title: "Config Preference Dataset"
version: "1.0.0"
author: n03_builder
tags: [preference_dataset, builder, config]
tldr: "Naming, paths, size limits, and enum constraints for preference_dataset production."
domain: "preference dataset construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---
# Config: preference_dataset Production Rules

## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p11_pd_{scope}.md` | `p11_pd_cex_instruction_dpo.md` |
| Builder directory | kebab-case | `preference-dataset-builder/` |
| Frontmatter fields | snake_case | `training_objective`, `agreement_rate`, `rater_count` |
| Dataset slug | snake_case, lowercase, no hyphens | `cex_instruction_dpo`, `safety_helpfulness_rlhf` |
| Pair IDs | `{slug}_{seq}` | `cex_dpo_001`, `safety_rlhf_042` |

Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.

## File Paths
- Output: `N04_knowledge/P11_feedback/p11_pd_{scope}.md`
- Compiled: `N04_knowledge/P11_feedback/compiled/p11_pd_{scope}.yaml`

## Size Limits (aligned with SCHEMA)
- Body: max 4096 bytes (spec + examples only, not full dataset)
- Total (frontmatter + body): ~8000 bytes
- Density: >= 0.80 (no filler)

## Training Objective Enum
| Value | Technique | When to use |
|-------|-----------|-------------|
| rlhf | Reinforcement Learning from Human Feedback | Reward model training + PPO |
| dpo | Direct Preference Optimization | Policy gradient-free alignment |
| kto | Kahneman-Tversky Optimization | Binary feedback (not pairwise) |
| constitutional | Constitutional AI | Self-critique + revision cycles |
| custom | Custom alignment method | Document technique in description |

## Annotation Method Enum
| Value | Meaning | Min Rater Count |
|-------|---------|-----------------|
| human | Human raters only | 2 |
| model_assisted | LLM generates, human reviews sample | 1 (human) + model |
| constitutional | AI self-annotation via principles | 0 (model only) |
| hybrid | Mix of human and model | 1 (human) + model |

## Quality Thresholds
| agreement_rate | Interpretation | Action |
|----------------|---------------|--------|
| >= 0.85 | High confidence | Publish to production training |
| 0.75-0.84 | Acceptable | Publish with review |
| 0.60-0.74 | Low confidence | Reannotate subset |
| < 0.60 | Unacceptable | Discard or revise signal criteria |
