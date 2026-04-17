---
kind: collaboration
id: bld_collaboration_preference_dataset
pillar: P12
llm_function: COLLABORATE
purpose: How preference-dataset-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: null
title: "Collaboration Preference Dataset"
version: "1.0.0"
author: n03_builder
tags: [preference_dataset, builder, collaboration]
tldr: "preference-dataset-builder is the training signal curator in alignment crews."
domain: "preference dataset construction"
created: "2026-04-17"
updated: "2026-04-17"
density_score: 0.90
---

# Collaboration: preference-dataset-builder

## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what are the labeled preference pairs, annotation protocol, and quality filters for this training objective?"
I do not produce evaluation metrics. I do not build reward model weights. I do not define CI expected outputs.
I produce the training signal specification that alignment pipelines consume.

## Crew Compositions

### Crew: "RLHF Alignment Pipeline"
```
  1. eval-dataset-builder -> "evaluation holdout for the domain"
  2. preference-dataset-builder -> "training pairs with annotation protocol"
  3. scoring-rubric-builder -> "reward model evaluation dimensions"
  4. drift-detector-builder -> "monitor for post-training behavioral drift"
```

### Crew: "Model Fine-Tuning"
```
  1. knowledge-card-builder -> "domain knowledge for annotation calibration"
  2. preference-dataset-builder -> "DPO training pairs"
  3. eval-dataset-builder -> "held-out evaluation set"
  4. benchmark-builder -> "performance benchmarks pre/post fine-tuning"
```

## Handoff Protocol

### I Receive
- seeds: domain, task_type, training_objective (rlhf/dpo/kto/constitutional)
- optional: existing annotation guidelines, rater calibration notes
- optional: sample prompts to use for example pairs

### I Produce
- preference_dataset artifact (.md with YAML frontmatter)
- committed to: `N04_knowledge/P11_feedback/p11_pd_{scope}.md`

### I Signal
- signal: complete (with quality score)
- if quality < 8.0: signal retry with failure reasons (most common: vague signal, missing agreement_rate)

## Builders I Depend On
| Builder | Why |
|---------|-----|
| knowledge-card-builder | Domain KCs calibrate annotation criteria |
| eval-dataset-builder | Ensures no overlap between training and evaluation |

## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| drift-detector-builder | Detects when deployed model drifts from trained preferences |
| scoring-rubric-builder | Scoring dimensions should align with preference criteria |
| benchmark-builder | Pre/post fine-tuning benchmarks reference the training objective |

## Conflict Resolution
| Scenario | Resolution |
|----------|-----------|
| Training vs evaluation pairs | preference_dataset = training; eval_dataset = evaluation. NEVER mix. |
| Preference vs correctness labels | Preference is relative (chosen > rejected). Correctness is absolute (right/wrong). Use golden_test for absolute. |
| Dataset spec vs full dataset | Artifact = spec + examples. Full dataset lives in external storage (HuggingFace, S3). |
