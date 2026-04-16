---
kind: examples
id: bld_examples_reward_model
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of reward_model artifacts
quality: 8.9
title: "Examples Reward Model"
version: "1.0.0"
author: wave1_builder_gen
tags: [reward_model, builder, examples]
tldr: "Golden and anti-examples of reward_model artifacts"
domain: "reward_model construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

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
