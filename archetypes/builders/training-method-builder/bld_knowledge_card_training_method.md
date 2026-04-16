---
kind: knowledge_card
id: bld_knowledge_card_training_method
pillar: P01
llm_function: INJECT
quality: 9.1
title: "Knowledge Card: training_method"
version: "1.0.0"
author: n05_builder
tags: [training_method, knowledge_card, P02, ml, learning-paradigm]
tldr: "Core knowledge for training_method artifacts: learning paradigms, compute profiles, hyperparameter conventions, and dataset patterns."
domain: "training_method construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.88
---

# Knowledge: training_method

## What Is a training_method?
A `training_method` artifact specifies how an ML model should be trained: the learning paradigm,
compute intensity, hyperparameter configuration, dataset requirements, and evaluation strategy.
It is the specification layer above individual training jobs (`finetune_config`) and below model
documentation (`model_card`).

## Learning Paradigm Reference
| Paradigm | Objective | Requires Labels | Typical Models |
|----------|-----------|-----------------|----------------|
| supervised | Minimize loss on labeled data | Yes | classifiers, regressors, seq2seq |
| unsupervised | Find structure in unlabeled data | No | autoencoders, clustering, VAE |
| self_supervised | Predict masked/rotated parts of input | No | BERT, GPT, SimCLR, MAE |
| reinforcement | Maximize cumulative reward | Reward signal | DQN, PPO, SAC, RLHF |
| transfer | Adapt pre-trained representations | Few labels | fine-tuned foundation models |
| hybrid | Combine multiple paradigms | Varies | multi-task, curriculum, RLHF |

## Compute Intensity Profiles
| Intensity | Hardware | Memory | Training Time | Examples |
|-----------|----------|--------|--------------|---------|
| low | CPU or single GPU <=8GB | <4GB | minutes to hours | sklearn, small CNNs |
| medium | 1-4 GPU 16-80GB | 8-40GB | hours to days | BERT-scale, LoRA |
| high | Multi-GPU/TPU | >40GB | days to weeks | GPT/LLaMA pre-training |

## Hyperparameter Conventions
| Hyperparameter | Typical Range | Notes |
|---------------|--------------|-------|
| learning_rate | 1e-5 to 1e-2 | Use warmup for large models |
| batch_size | 8 to 512 | Larger = more stable gradients |
| epochs | 1 to 100 | Early stopping recommended |
| optimizer | adam, adamw, sgd | AdamW default for transformers |
| scheduler | linear, cosine, constant | Cosine with warmup is standard |
| weight_decay | 0.0 to 0.1 | Regularization via AdamW |

## Dataset Patterns
| Format | Use Case | Fields |
|--------|----------|--------|
| Alpaca | Instruction following | instruction, input, output |
| ShareGPT | Chat/dialogue | conversations[{from, value}] |
| Parquet | Large-scale training | varies by task |
| CSV/TSV | Tabular tasks | label + feature columns |
| HF Dataset | HuggingFace hub | dataset_name + split + field_map |

## Boundary Conditions
| Situation | Use This | Not This |
|-----------|----------|---------|
| "How to train this model" | training_method | finetune_config |
| "LoRA job for Llama-3-8B" | finetune_config | training_method |
| "Documenting GPT-4o" | model_card | training_method |
| "RL reward function design" | reward_model | training_method |
| "Benchmark evaluation" | benchmark | training_method |
