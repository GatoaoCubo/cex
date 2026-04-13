---
id: atom_30_reasoning_thinking
kind: knowledge_card
pillar: P01
quality: 8.8
title: "Reasoning and Thinking Vocabulary"
tags: [reasoning, thinking, cot, framework-atlas]
date: 2026-04-13
---

# Comprehensive Guide to Reasoning Approaches, Training Methods, and Inference-Time Compute

## 1. Introduction
This document provides a structured overview of **reasoning approaches**, **training methodologies**, and **inference-time compute strategies** critical to modern large language models (LLMs). It integrates technical concepts, model capabilities, and pipeline-stage mappings to enable systematic reasoning system design and evaluation.

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
- **Self-Play + Verification**: Mutual improvement loops.
- **Extended Thinking**: Anthropic adaptive thinking, OpenAI reasoning effort.

---

## 5. 8F Pipeline Integration

| 8F Stage | Reasoning Concept | Application |
|---------|------------------|-------------|
| **F1 CONSTRAIN** | Compute Budget Allocation | Sets `budget_tokens`, `effort`, or `thinking_budget` based on task complexity. |
| **F2 BECOME** | Reasoning Strategy Selection | Uses `reasoning_strategy` to choose CoT, ToT, MCTS, etc. |
| **F3 INJECT** | Context-Grounded Reasoning | Injects KCs, examples, and prior traces as context. |
| **F4 REASON** | Core Reasoning Execution | Executes extended thinking (CoT, ToT) with full budget. |
| **F5 CALL** | Tool-Augmented Reasoning | Implements ReAct (interleaved thinking + tool calls). |
| **F6 PRODUCE** | Generation with Reasoning Trace | Outputs both reasoning trace (`reasoning_trace`) and final artifact. |
| **F7 GOVERN** | PRM / Verification Chain | Applies PRM to score steps; triggers verification if score < threshold. |
| **F8 COLLABORATE** | Reasoning Persistence | Stores `reasoning_trace` as artifact; feeds reward signals for training. |

---

## 6. Model Comparison Matrix

| Dimension | Anthropic Claude | OpenAI o-series | DeepSeek R1 | Google Gemini |
|---------|------------------|------------------|-------------|----------------|
| **Reasoning Visibility** | Summarized thinking (default) | Hidden by default; summary available | Full `think` tags visible | Configurable via `thinking_level` |
| **Budget Control** | `budget_tokens` or `effort` (adaptive) | `reasoning.effort` (6 levels) | No explicit budget (model-controlled) | `thinking_budget` or `thinking_level` |
| **Multi-Turn Continuity** | Thinking signatures (encrypted) | Persisted reasoning items | Think tags in conversation history | Thought signatures (encrypted) |
| **Tool-Use Integration** | Interleaved thinking between tool calls | Reasoning items around function calls | Standard (no special interleaving) | Standard |
| **Training Approach** | Inference-time thinking (not RL-trained) | RL-trained (RLHF + RLVR) | RL-trained (GRPO) | Inference-time thinking (not RL-trained) |
| **Open Source** | No | No | Yes (R1) | No |

---

## 7. Taxonomy of Reasoning Approaches

```
Reasoning Approaches
├── Prompting-Based
│   ├── Sequential (CoT, Zero-shot CoT)
│   ├── Multi-Path (Self-Consistency, CISC)
│   ├── Structured (ToT, GoT, AoT)
│   └── Decomposition (Least-to-Most)
├── Search-Based
│   ├── Tree Search (MCTS, LATS)
│   ├── Beam Search
│   └── Lookahead
├── Agentic
│   ├── ReAct
│   ├── Reflexion
│   └── Self-Refine
└── Hybrid
    ├── MCTS + PRM (rStar-Math)
    └── Self-Play + Verification
```

---

## 8. Glossary

- **CoT**: Chain-of-Thought (explicit reasoning steps).
- **ToT**: Tree-of-Thoughts (structured branching reasoning).
- **PRM**: Process Reward Model (evaluates reasoning steps).
- **ORM**: Outcome Reward Model (evaluates final results).
- **R-PRM**: Enhanced PRM with domain-specific rubrics.
- **CISC**: Contrastive Self-Consistency (multi-path reasoning).
- **MCTS**: Monte Carlo Tree Search (search-based planning).
- **ReAct**: Reasoning + Acting (tool-augmented reasoning).
- **rStar**: Reinforcement Learning + Tree Search (math-focused).

---

## 9. Conclusion
This guide synthesizes the latest advancements in reasoning, training, and inference strategies for LLMs. By leveraging the 8F pipeline, models can systematically integrate reasoning capabilities while ensuring alignment with ethical, computational, and performance constraints. Future work should focus on cross-model benchmarking and open-source tooling for reasoning verification.