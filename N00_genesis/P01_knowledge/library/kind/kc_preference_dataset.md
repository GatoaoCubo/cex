---
id: p01_kc_preference_dataset
kind: knowledge_card
type: kind
pillar: P11
title: "Preference Dataset -- Deep Knowledge for preference_dataset"
version: 1.0.0
created: 2026-04-17
updated: 2026-04-17
author: builder_agent
domain: preference_dataset
quality: 8.8
tags: [preference_dataset, P11, GOVERN, kind-kc, rlhf, dpo, alignment]
tldr: "preference_dataset curates (prompt, chosen, rejected) triplets for LLM alignment training via RLHF, DPO, KTO, or Constitutional AI."
when_to_use: "Building, reviewing, or reasoning about preference_dataset artifacts"
keywords: [preference_dataset, rlhf, dpo, kto, alignment, chosen_rejected, annotation, instructgpt]
feeds_kinds: [preference_dataset]
density_score: 0.92
linked_artifacts:
  primary: null
  related: []
related:
  - p01_kc_reward_and_alignment
  - bld_knowledge_card_reward_signal
  - bld_collaboration_reward_signal
  - bld_instruction_reward_signal
  - reward-signal-builder
  - bld_collaboration_finetune_config
  - bld_examples_reward_signal
  - bld_tools_reward_model
  - bld_config_finetune_config
  - bld_schema_reward_signal
---

# Preference Dataset

## Spec
```yaml
kind: preference_dataset
pillar: P11
llm_function: GOVERN
max_bytes: 4096
naming: p11_pd_{scope}.md
core: true
```

## What It Is
A preference_dataset is a curated collection of (prompt, chosen_response, rejected_response)
triplets annotated with human or model-assisted preference labels. These datasets are the
training signal for LLM alignment techniques: RLHF, DPO, KTO, Constitutional AI, and SPIN.

## Alignment Technique Map
| Technique | Dataset Format | Key Paper |
|-----------|---------------|-----------|
| RLHF | (prompt, chosen, rejected) -> reward model | InstructGPT 2022 |
| DPO | (prompt, chosen, rejected) directly | Rafailov et al. 2023 |
| KTO | (prompt, response, label: desirable/undesirable) | Ethayarajh et al. 2023 |
| Constitutional AI | (prompt, principle-revised response, original) | Anthropic 2022 |
| SPIN | Self-play iteration on own outputs | Chen et al. 2024 |

## Key Parameters
| Parameter | Type | Notes |
|-----------|------|-------|
| training_objective | enum | rlhf, dpo, kto, constitutional, custom |
| annotation_method | enum | human, model_assisted, constitutional, hybrid |
| agreement_rate | float [0,1] | Annotator consistency; publish >= 0.75 |
| pairs_count | int | Dataset size in (prompt, chosen, rejected) triplets |
| domains | list[string] | Subject domains covered |
| preference_criteria | list[string] | What annotators evaluated (helpfulness, safety, etc.) |

## Annotation Quality Gates
| Gate | Threshold | Description |
|------|-----------|-------------|
| Publish | agreement_rate >= 0.75 | Minimum annotator consistency for training |
| Golden | agreement_rate >= 0.85 | High-quality alignment signal |
| Reject | agreement_rate < 0.60 | Re-annotate -- signal is noise |

## Patterns
| Pattern | When to Use | Config |
|---------|-------------|--------|
| Human-annotated | High-stakes alignment | annotation_method: human, pairs: 1000+ |
| Model-assisted | Speed + scale | annotation_method: model_assisted, human_review: 10% |
| Constitutional | Principle-driven | annotation_method: constitutional, principles: [...] |
| Domain-specific | Narrow fine-tuning | domains: [medical], annotation: specialist |

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| No preference_criteria | Annotators choose inconsistently | Define explicit criteria before annotation |
| Low agreement_rate | Noisy signal degrades model | Clarify criteria, re-annotate, raise pay |
| Single-domain only | Model learns domain bias | Balanced multi-domain sampling |
| chosen == rejected | Zero learning signal | Validate pairs are meaningfully different |

## Integration Graph
```
annotation_pipeline --> [preference_dataset] --> reward_model training (RLHF)
                               |              --> DPO fine-tuning
                        scoring_rubric          --> KTO training
                        quality_gate (agreement_rate check)
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_reward_and_alignment]] | sibling | 0.42 |
| [[bld_knowledge_card_reward_signal]] | sibling | 0.34 |
| [[bld_collaboration_reward_signal]] | downstream | 0.28 |
| [[bld_instruction_reward_signal]] | upstream | 0.24 |
| [[reward-signal-builder]] | related | 0.22 |
| [[bld_collaboration_finetune_config]] | downstream | 0.22 |
| [[bld_examples_reward_signal]] | upstream | 0.22 |
| [[bld_tools_reward_model]] | upstream | 0.20 |
| [[bld_config_finetune_config]] | upstream | 0.20 |
| [[bld_schema_reward_signal]] | related | 0.20 |
