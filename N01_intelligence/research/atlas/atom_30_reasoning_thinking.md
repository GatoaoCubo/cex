---
id: atom_30_reasoning_thinking
kind: knowledge_card
pillar: P01
quality: 9.0
title: "Reasoning and Thinking Vocabulary"
tags: [reasoning, thinking, cot, framework-atlas]
date: 2026-04-13
---

# Comprehensive Guide to Reasoning Approaches, Training Methods, and Inference-Time Compute

## 1. Introduction
This document provides a structured overview of **reasoning approaches**, **training methodologies**, and **inference-time compute strategies** critical to modern large language models (LLMs). It integrates technical concepts, model capabilities, and pipeline-stage mappings to enable systematic reasoning system design and evaluation.

---

## Boundary
This artifact defines terminology, methodologies, and frameworks for reasoning and thinking in LLMs. It is not a technical implementation guide, nor does it cover model-specific architectures or deployment considerations.

---

## Related Kinds
- **model_training**: Covers training methods like RLHF and DPO, which are referenced in this artifact's training approaches section.  
- **inference_pipeline**: Describes compute strategies (e.g., MCTS, PRM) mapped to the 8F pipeline in this document.  
- **ethical_alignment**: Includes alignment techniques like Constitutional AI (CAI) discussed in the training section.  
- **knowledge_management**: References the 8F pipeline's role in reasoning persistence and artifact storage.  

---

## 2. Core Concepts

### 2.1 Reasoning
**Definition**: A cognitive process involving problem-solving, logical deduction, and multi-step planning. In LLMs, it manifests as explicit reasoning traces (e.g., `think` blocks), structured thought processes (e.g., Tree of Thoughts), or implicit knowledge application.

**Key Properties**:
- **Visibility**: Varies by model (e.g., `reasoning.effort` in o-series, `thinking_level` in Gemini).
- **Budget Control**: Governed by parameters like `budget_tokens`, `effort`, or `thinking_budget`.
- **Tool Integration**: Supports interleaved reasoning (ReAct), persisted reasoning items (OpenAI), or standard tool use.

### 2.2 Thinking
**Definition**: The computational process of generating internal reasoning steps, often visible as `think` blocks or `reasoning_trace` artifacts. Thinking is distinct from final output generation and is critical for auditability and verification.

**Types**:
- **Sequential**: CoT, Zero-shot CoT, Auto-CoT.
- **Multi-Path**: Self-Consistency, CISC.
- **Structured**: ToT, GoT, AoT.
- **Agentic**: ReAct, Reflexion, Self-Refine.

---

## 3. Training Approaches

### 3.1 Reinforcement Learning (RL)
- **RLHF**: Reinforcement Learning from Human Feedback (e.g., o1/o3).
- **RLVR**: Reinforcement Learning with Verifiable Rewards (math/code correctness).
- **RLAIF**: Reinforcement Learning from AI Feedback (Anthropic).
- **Constitutional AI (CAI)**: Training via ethical constraints (e.g., alignment with human values).

### 3.2 Policy Optimization
- **PPO**: Proximal Policy Optimization.
- **GRPO**: Group Relative Policy Optimization (DeepSeek R1).
- **DPO**: Direct Preference Optimization.
- **KTO**: Kahneman-Tversky Optimization.
- **ODPO**: Offset Direct Preference Optimization.

### 3.3 Reward Modeling
- **ORM**: Outcome Reward Model (evaluates final results).
- **PRM**: Process Reward Model (evaluates step-by-step reasoning).
- **PAV**: Process Advantage Verifier (enhances PRM with advantage scoring).
- **R-PRM**: Enhanced PRM with domain-specific rubrics.

### 3.4 Distillation
- **CoT Distillation**: Transfer reasoning patterns from teacher models.
- **Curriculum Distillation**: Gradual complexity increase in training data.
- **Multi-Teacher Distillation**: Aggregates knowledge from multiple models.

### 3.5 Self-Training
- **STaR**: Self-Taught Reasoner (iterative training with generated data).
- **RFT**: Rejection Sampling Fine-Tuning.
- **Rejection Sampling**: Filters low-quality training examples.

---

## 4. Inference-Time Compute Strategies

### 4.1 Search-Based Methods
- **Tree Search**: MCTS, LATS, SR-MCTS, rStar.
- **Beam Search**: Reasoning beam search, diverse beam search.
- **Best-of-N**: Parallel sampling + verifier selection.
- **Lookahead**: Forward simulation + PRM scoring.

### 4.2 Prompting-Based Methods
- **Sequential**: CoT, Zero-shot CoT, Auto-CoT, PoT, ThoT.
- **Multi-Path**: Self-Consistency, CISC, Universal Self-Consistency.
- **Structured**: ToT, GoT, AoT.
- **Decomposition**: Least-to-Most, Plan-and-Solve, Skeleton-of-Thought.
- **Agentic**: ReAct, Reflexion, Self-Refine, MIRROR.

### 4.3 Hybrid Approaches
- **MCTS + PRM**: rStar-Math, AlphaProof.
- **Self-Play + Verification**: Combines reinforcement learning with reasoning checks.
- **Pipeline Integration**: Maps compute strategies to the 8F pipeline for systematic execution.

---

## 5. 8F Pipeline Integration
| Stage | Description | Reasoning Role |
|------|-------------|----------------|
| **1. Define** | Problem scope and constraints | Sets boundaries for reasoning tasks |
| **2. Frame** | Translate problem into model inputs | Structures prompts for LLMs |
| **3. Execute** | Run inference with compute strategies | Applies MCTS, PRM, or beam search |
| **4. Filter** | Remove invalid or low-quality outputs | Uses PRM scoring or rejection sampling |
| **5. Aggregate** | Combine outputs from multiple strategies | Enhances robustness via Self-Consistency |
| **6. Analyze** | Evaluate reasoning quality and alignment | Uses ORM, PAV, or R-PRM |
| **7. Adapt** | Refine strategies based on feedback | Adjusts `budget_tokens` or `thinking_level` |
| **8. Store** | Persist reasoning artifacts for audit | Saves `reasoning_trace` or `think` blocks |

---

## 6. Model Comparison Matrix
| Model | Reasoning Method | Training Approach | Inference Strategy | Ethical Alignment |
|------|------------------|-------------------|--------------------|-------------------|
| **o-series** | `reasoning.effort` | RLHF, RLVR | MCTS, PRM | Constitutional AI |
| **Gemini** | `thinking_level` | DPO, KTO | Beam search, lookahead | PAV, R-PRM |
| **DeepSeek R1** | Structured ToT | GRPO, ODPO | Hybrid (MCTS + PRM) | Ethical constraints |
| **Anthropic** | Agentic ReAct | RLAIF | Self-Play + Verification | Alignment via CAI |

---

## 7. Glossary
- **CoT**: Chain-of-Thought prompting, which explicitly guides LLMs through reasoning steps.
- **PRM**: Process Reward Model, which evaluates intermediate reasoning steps for quality.
- **R-PRM**: Enhanced PRM with domain-specific rubrics for precise evaluation.
- **MCTS**: Monte Carlo Tree Search, a search algorithm for planning and decision-making.
- **ReAct**: Reasoning + Acting, combining logical deduction with tool use.
- **rStar**: Reinforcement Learning + Tree Search, optimized for math reasoning tasks.
- **CISC**: Contrastive Self-Consistency, a multi-path reasoning technique for robustness.

---

## 8. Conclusion
This guide synthesizes the latest advancements in reasoning, training, and inference strategies for LLMs. By leveraging the 8F pipeline, models can systematically integrate reasoning capabilities while ensuring alignment with ethical, computational, and performance constraints. Future work should focus on cross-model benchmarking and open-source tooling for reasoning verification.