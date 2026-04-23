---
id: p01_kc_reward_and_alignment
kind: knowledge_card
type: domain
pillar: P01
title: 'Reward Modeling and Alignment: RLHF, DPO, Constitutional AI'
version: 1.0.0
created: 2026-03-29
updated: 2026-03-29
author: builder_agent
domain: alignment_research
origin: src_standards_global
quality: 9.1
tags:
- rlhf
- dpo
- constitutional-ai
- alignment
- reward-model
- preference
tldr: LLM alignment evolved from RLHF (reward model from human preferences) through Constitutional AI (self-critique from
  principles) to DPO (direct preference optimization without reward model), establishing the training vocabulary for safe,
  helpful AI systems.
when_to_use: When understanding LLM training pipelines, choosing between RLHF vs DPO for fine-tuning, implementing safety
  guardrails, or designing evaluation criteria for model outputs.
keywords:
- rlhf
- dpo
- constitutional-ai
- reward-model
- preference-data
- alignment
long_tails:
- difference between rlhf and dpo for fine-tuning
- how constitutional ai self-critique works
axioms:
- Alignment is the bridge between raw capability and safe deployment — every production LLM uses some form of preference optimization
linked_artifacts:
  adw: null
  agent: null
  hop: null
feeds_kinds:
- reward_signal
- quality_gate
- llm_judge
- scoring_rubric
- eval_dataset
- golden_test
density_score: 0.87
related:
  - bld_knowledge_card_reward_signal
  - bld_collaboration_reward_signal
  - reward-signal-builder
  - bld_knowledge_card_reward_model
  - bld_tools_reward_model
  - reward-model-builder
  - bld_examples_reward_signal
  - bld_tools_reward_signal
  - bld_examples_reward_model
  - bld_instruction_reward_signal
---

# Knowledge Card: Reward Modeling and Alignment

## Quick Reference
```yaml
topic: LLM Alignment — RLHF, DPO, Constitutional AI
scope: Reward modeling, preference optimization, safety training
owner: Anthropic, OpenAI, Stanford, DeepMind
criticality: high
timeline: 2017-2024
```

## Core Methods

### RLHF — Reinforcement Learning from Human Feedback (Christiano et al., 2017; Stiennon et al., 2020)
- **Core idea**: Train a reward model from human preference comparisons, then optimize the LLM policy against it
- **Pipeline**: Pretrain LLM -> Collect human comparisons -> Train reward model -> RL fine-tune (PPO)
- **Key terms introduced**:
  - **Reward model**: Neural network predicting human preference scores
  - **Human feedback**: Pairwise comparisons ("response A is better than B")
  - **Preference data**: Dataset of ranked response pairs
  - **Policy** (LLM as): The language model treated as an RL policy to optimize
- **Status**: Foundational — every major LLM provider uses RLHF or a derivative

### Constitutional AI (Bai et al., 2022 — Anthropic)
- **Core idea**: Replace some human feedback with AI self-critique guided by a set of principles (the "constitution")
- **Pipeline**: Generate -> Self-critique against principles -> Self-revise -> Use revised outputs for training
- **Key terms introduced**:
  - **Constitution**: Set of principles the AI uses to judge its own outputs
  - **Critique**: AI-generated assessment of its own response
  - **Revision**: AI-generated improvement based on critique
  - **Harmlessness / Helpfulness**: Dual objectives for alignment
- **Key insight**: Scalable — reduces dependency on expensive human annotators
- **Status**: Core to Anthropic's approach; "harmlessness/helpfulness" adopted as alignment vocabulary

### DPO — Direct Preference Optimization (Rafailov et al., 2023 — Stanford)
- **Core idea**: Optimize LLM directly on preference data without training a separate reward model
- **Mechanism**: Reformulate the RLHF objective as a simple classification loss on preference pairs
- **Key terms introduced**:
  - **Direct preference optimization**: Skip the reward model entirely
  - **Policy (LLM as)**: Same as RLHF but optimized via cross-entropy, not PPO
  - **Preference data**: Same format as RLHF (chosen vs rejected pairs)
- **Key insight**: Simpler, more stable, computationally cheaper than RLHF
- **Status**: Standard fine-tuning method — widely adopted alongside/replacing RLHF

## Method Comparison

| Dimension | RLHF | Constitutional AI | DPO |
|-----------|------|-------------------|-----|
| Human data needed | High (pairwise comparisons) | Lower (principles + some human data) | Moderate (preference pairs) |
| Reward model | Yes (separate neural net) | Yes (AI-generated labels) | No (implicit in loss function) |
| Training stability | Lower (RL + reward hacking) | Moderate | Higher (supervised loss) |
| Compute cost | High (PPO training loop) | Moderate | Lower (single-stage) |
| Scalability | Limited by human annotators | High (AI self-critique) | High (just needs preference data) |
| Alignment target | Maximize reward model score | Follow constitutional principles | Match preference distribution |

## Evolution
```text
[RLHF 2017-2020: reward model + PPO] -> [Constitutional AI 2022: self-critique from principles] -> [DPO 2023: direct optimization without reward model]
```

## Key Vocabulary (Industry-Standard)

| Term | Origin | Status |
|------|--------|--------|
| Reward model | RLHF (Christiano 2017) | Universal |
| Human feedback | RLHF | Universal |
| Preference (data) | RLHF | Universal |
| Policy (LLM as) | RLHF / DPO | Adopted |
| Constitutional AI | Anthropic (Bai 2022) | Adopted (Anthropic-centric term) |
| Critique / Revision | Constitutional AI | Niche |
| Harmlessness / Helpfulness | Constitutional AI | Universal alignment vocab |
| Direct Preference Optimization | DPO (Rafailov 2023) | Standard fine-tuning term |

## Practical Implications for Agent Systems

| Scenario | Relevance |
|----------|-----------|
| Output quality scoring | organization quality gates (>= 7.0) parallel reward model scoring |
| Self-critique loops | Constitutional AI pattern maps to agent Reflexion |
| Preference-based routing | DPO-style preference data can train agent routing models |
| Safety guardrails | All three methods inform when/how to refuse or redirect |

## Golden Rules
- RLHF is the gold standard for understanding alignment — know the pipeline even if you use DPO
- DPO is preferred for practical fine-tuning: simpler, cheaper, more stable
- Constitutional AI's insight (self-critique from principles) applies beyond training — use it for runtime evaluation
- Preference data quality matters more than quantity — garbage comparisons produce garbage alignment

## References
- Christiano et al. 2017: "Deep Reinforcement Learning from Human Preferences"
- Stiennon et al. 2020: "Learning to Summarize with Human Feedback"
- Bai et al. 2022: "Constitutional AI: Harmlessness from AI Feedback"
- Rafailov et al. 2023: "Direct Preference Optimization: Your Language Model Is Secretly a Reward Model"
- Source: src_standards_global.md (Section 3: Academic Origins)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_reward_signal]] | sibling | 0.55 |
| [[bld_collaboration_reward_signal]] | downstream | 0.41 |
| [[reward-signal-builder]] | downstream | 0.38 |
| [[bld_knowledge_card_reward_model]] | sibling | 0.34 |
| [[bld_tools_reward_model]] | downstream | 0.33 |
| [[reward-model-builder]] | downstream | 0.31 |
| [[bld_examples_reward_signal]] | downstream | 0.31 |
| [[bld_tools_reward_signal]] | downstream | 0.31 |
| [[bld_examples_reward_model]] | downstream | 0.27 |
| [[bld_instruction_reward_signal]] | downstream | 0.27 |
