---
kind: knowledge_card
id: bld_knowledge_card_preference_dataset
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for preference_dataset production
sources: InstructGPT RLHF (2022), DPO Rafailov et al. (2023), Constitutional AI Anthropic (2022), KTO Ethayarajh et al. (2023)
quality: null
title: "Knowledge Card Preference Dataset"
version: "1.0.0"
author: n03_builder
tags: [preference_dataset, builder, knowledge_card]
tldr: "Preference datasets are curated (prompt, chosen, rejected) triplets that encode human preferences for aligning LLMs via RLHF or DPO."
domain: "preference dataset construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Domain Knowledge: preference_dataset

## Executive Summary
A preference_dataset is a curated collection of (prompt, chosen_response, rejected_response) triplets annotated with human or model-assisted preference labels. These datasets are the training signal for alignment techniques: RLHF (reward model training + PPO), DPO (direct policy optimization), KTO (Kahneman-Tversky optimization), and Constitutional AI. Quality depends on annotation consistency, preference signal clarity, and inter-annotator agreement.

## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P11 (Feedback) |
| llm_function | GOVERN (controls training signal quality) |
| Training objectives | rlhf, dpo, kto, constitutional, custom |
| Annotation methods | human, model_assisted, constitutional, hybrid |
| Quality threshold | agreement_rate >= 0.75 (publish), >= 0.85 (golden) |
| Max bytes | 4096 (spec + examples, not full dataset) |
| Machine format | yaml |
| Naming | p11_pd_{scope}.md |

## Alignment Technique Map
| Technique | Dataset Format | Key Paper |
|-----------|---------------|-----------|
| RLHF | (prompt, chosen, rejected) -> reward model | InstructGPT 2022 |
| DPO | (prompt, chosen, rejected) -> direct policy | Rafailov et al. 2023 |
| KTO | (prompt, response, label: bool) -> KT utility | Ethayarajh et al. 2023 |
| Constitutional AI | (prompt, critique, revision) -> self-improvement | Anthropic 2022 |
| RLAIF | (prompt, chosen, rejected) from model as annotator | Bai et al. 2022 |

## Implementation Patterns
| Pattern | When to use |
|---------|-------------|
| Human labeling | Safety-critical domains, high-stakes preferences |
| Model-assisted | Scale annotation cheaply; human review sample |
| Constitutional | Self-critique cycles; explicit principles as annotator |
| Pairwise ranking | Collect multiple responses, rank all, derive pairs |
| Binary preference | Simpler task: 1 chosen, 1 rejected per prompt |

## Quality Factors
- **Agreement rate**: >= 0.75 minimum; >= 0.85 for high-stakes training
- **Rater count**: >= 2 per pair; >= 3 for safety-critical
- **Calibration**: regular rater calibration sessions reduce drift
- **Diversity**: varied prompts avoid reward hacking on narrow distribution
- **Balance**: 50/50 chosen/rejected distribution prevents bias

## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Ambiguous preference signal | Raters cannot agree on chosen -- low agreement rate |
| Single rater per pair | No way to measure agreement; high noise |
| Overlapping with eval set | Data leakage corrupts evaluation metrics |
| Storing full dataset in artifact | 100K pairs in YAML is unmanageable |
| Subjective chosen = "longer" | Length bias corrupts reward model |
| No quality filters | Low-confidence pairs add training noise |

## References
- Ouyang et al., "Training language models to follow instructions with human feedback" (InstructGPT, 2022)
- Rafailov et al., "Direct Preference Optimization" (DPO, 2023)
- Bai et al., "Constitutional AI: Harmlessness from AI Feedback" (2022)
- Ethayarajh et al., "KTO: Model Alignment as Prospect Theoretic Optimization" (2023)
