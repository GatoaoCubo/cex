---
id: atom_30_reasoning_thinking
kind: knowledge_card
pillar: P01
quality: 8.8
title: "Reasoning and Thinking Vocabulary"
tags: [reasoning, thinking, cot, framework-atlas, rl-algorithms, prm, test-time-compute, extended-thinking]
date: 2026-04-13
---

# Comprehensive Guide to Reasoning Approaches, Training Methods, and Inference-Time Compute

## 1. Introduction
This document provides a structured overview of **reasoning approaches**, **training methodologies**, and **inference-time compute strategies** critical to modern large language models (LLMs). It integrates technical concepts, model capabilities, and pipeline-stage mappings to enable systematic reasoning system design and evaluation. Enriched with implementation-level detail on the Anthropic Extended Thinking API, all 14 RL algorithms for reasoning, PRM training mechanics, test-time compute scaling laws, and a reasoning strategy selection guide.

---

## Boundary
This artifact defines terminology, methodologies, and frameworks for reasoning and thinking in LLMs. It is not a model-specific architecture guide or deployment runbook, but does cover API-level implementation patterns and algorithm selection criteria.

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
- **RLHF**: Reinforcement Learning from Human Feedback (e.g., o1/o3). Human annotators rank outputs; a reward model is trained on those preferences; PPO optimizes the policy.
- **RLVR**: Reinforcement Learning with Verifiable Rewards. Binary feedback from a deterministic tool (math checker, code runner). Advances: o1, Claude 3.7+, DeepSeek R1, Kimi K1.5, Qwen 3. Source: [RLVR explained](https://www.promptfoo.dev/blog/rlvr-explained/)
- **RLAIF**: Reinforcement Learning from AI Feedback. An LLM generates preference labels replacing human annotators. Used by Anthropic for Constitutional AI feedback loops. Source: [State of RL for reasoning](https://magazine.sebastianraschka.com/p/the-state-of-llm-reasoning-model-training)
- **Constitutional AI (CAI)**: Training via ethical constraints; a critic model evaluates output against a constitution (set of principles); the policy is optimized to satisfy those constraints.

### 3.2 The 14 RL Policy-Optimization Algorithms for Reasoning

> Source overview: [From REINFORCE to Dr. GRPO](https://lancelqf.github.io/note/llm_post_training/) | [PPO to GRPO to DAPO](https://blog.softmaxdata.com/from-ppo-to-grpo-to-dapo-understanding-rl-for-llms-and-every-training-parameter-explained/)

| # | Algorithm | Key Mechanism | Critic Needed? | Best For |
|---|-----------|---------------|----------------|----------|
| 1 | **REINFORCE** | Monte Carlo policy gradient; reward at EOS as baseline | No | Simple baselines; sparse reward |
| 2 | **REINFORCE++** | Adds token-level normalization + KL penalty; removes critic; uses batch reward as baseline | No | Efficient RLHF; robust to reward noise. Source: [arXiv:2501.03262](https://arxiv.org/html/2501.03262v5) |
| 3 | **ReMax** | REINFORCE variant; uses greedy-decoded output as deterministic baseline; reduces variance without a value function | No | Low-budget RL on single GPU |
| 4 | **RLOO (REINFORCE Leave-One-Out)** | Leave-one-out baseline: advantage of trajectory i = reward_i minus mean of all other trajectories in the group | No | Strong balance of efficiency and performance across k=1..256 |
| 5 | **PPO** | Actor-critic; clipped surrogate objective; separate value network; token-level advantage (discounted from EOS) | Yes | Foundational method; highest stability; highest memory cost |
| 6 | **GRPO (Group Relative Policy Optimization)** | Group of G outputs sampled per prompt; advantage = (reward_i - mean_group) / std_group; NO value network | No | ~50% memory vs PPO; DeepSeek R1 training. Source: [GRPO deep dive](https://cameronrwolfe.substack.com/p/grpo) |
| 7 | **Dr. GRPO (GRPO Done Right)** | Removes std normalization from GRPO denominator (prevents learning rate scaling side-effect); equivalent to RLOO up to constant | No | Cleaner GRPO; fixes implicit LR inflation |
| 8 | **DAPO (Decoupled Clip and Dynamic Sampling PO)** | Clip-higher (raises upper clip bound for exploration); dynamic sampling (drops all-correct or all-wrong groups); token-level loss | No | Large-scale reasoning; AIME 2024: 50pts on Qwen2.5-32B, surpasses DeepSeek GRPO. Source: [Comparative PPO/GRPO/DAPO](https://arxiv.org/html/2512.07611v1) |
| 9 | **DPO (Direct Preference Optimization)** | Reparameterizes reward model directly into policy; closed-form solution; no explicit RL loop | No | Preference alignment without separate RM |
| 10 | **KTO (Kahneman-Tversky Optimization)** | Applies prospect theory loss; separately weights gains vs losses; does not require pairwise preferences | No | When only binary good/bad labels are available |
| 11 | **ODPO (Offset DPO)** | Adds an offset term to DPO loss to enforce explicit reward margin between preferred/rejected | No | When DPO produces underconfident preferences |
| 12 | **REBEL** | Policy gradient with relative entropy bounds; minimizes divergence from reference while maximizing reward | No | Controlled exploration; safety-sensitive fine-tuning |
| 13 | **PRIME (Process Reward Implicit Model via Token-level EMbeddings)** | Trains process reward model implicitly from token embeddings; no explicit step annotation needed | No | Step-level RL without annotated PRMs |
| 14 | **GSPO (Group Sequence Policy Optimization)** | Extends GRPO to sequence-level grouping; reduces within-group correlation; verl framework. Source: [verl](https://github.com/verl-project/verl) | No | Large-batch training; reduced gradient noise |

**Algorithm Genealogy**:
```
REINFORCE
  |- REINFORCE++ (token-level baseline + KL)
  |- ReMax (greedy baseline)
  |- RLOO (leave-one-out baseline)
  |    |- Dr. GRPO (equivalent up to constant)
  |- PPO (critic + clip)
       |- GRPO (group baseline, no critic)
            |- Dr. GRPO (remove std term)
            |- DAPO (clip-higher + dynamic sampling)
            |- GSPO (sequence-level grouping)
DPO (no RL loop)
  |- KTO (prospect theory)
  |- ODPO (margin offset)
REBEL (relative entropy bound)
PRIME (implicit PRM token embedding)
```

**RLVR debate**: RL-trained models excel at pass@1 but are outperformed by base models at pass@256, suggesting RLVR narrows exploration -- it favors known high-reward paths over novel reasoning strategies. Source: [Limit of RLVR](https://limit-of-rlvr.github.io/)

### 3.3 Reward Modeling

#### 3.3.1 ORM / PRM Overview
- **ORM**: Outcome Reward Model. Binary signal at end of full solution. Simple but misses intermediate errors.
- **PRM**: Process Reward Model. Assigns reward to each reasoning step. Requires step-level labels.
- **PAV**: Process Advantage Verifier. Combines PRM with advantage scoring for RL training.
- **R-PRM**: PRM augmented with domain-specific rubrics (e.g., math proof structure). Source: [R-PRM EMNLP 2025](https://aclanthology.org/2025.emnlp-main.679.pdf)

#### 3.3.2 PRM Training Details

> Sources: [Let's Verify Step by Step (OpenAI)](https://cdn.openai.com/improving-mathematical-reasoning-with-process-supervision/Lets_Verify_Step_by_Step.pdf) | [Lessons of PRM Development arXiv:2501.07301](https://arxiv.org/abs/2501.07301) | [Qwen2.5 Math PRM blog](https://qwenlm.github.io/blog/qwen2.5-math-prm/)

**Step-label acquisition methods** (ranked by quality):

| Method | Label Quality | Cost | Notes |
|--------|--------------|------|-------|
| Human annotation (PRM800K) | Highest | Very high | Gold standard; 800K step labels |
| LLM-as-Judge | High | Medium | GPT-4 or stronger model rates each step |
| Monte Carlo estimation | Medium | High compute | Roll out many completions; estimate step correctness from outcome distribution |
| Gold step-by-step solutions | Medium | Depends on dataset | Works for math where canonical proofs exist |

**Key 2025 findings on PRM training**:
- Monte Carlo (MC) estimation yields inferior generalization vs LLM-as-Judge or human annotation. Source: [arXiv:2501.07301](https://arxiv.org/abs/2501.07301)
- **ThinkPRM**: A long-CoT verifier fine-tuned on orders-of-magnitude fewer process labels than discriminative PRMs. Uses model's own reasoning ability. Outperforms LLM-as-Judge and discriminative verifiers using only **1% of PRM800K labels**. Source: [ThinkPRM arXiv:2504.16828](https://arxiv.org/pdf/2504.16828)
- **SP-PRM / PathFinder-PRM**: Trajectory-aware models providing both step-level AND trajectory-level rewards.
- **PS-GRPO**: Process-Supervised GRPO -- uses a PRM to provide per-step rewards inside the GRPO update for multimodal math (DualMath-1.1M dataset). Source: [NeurIPS 2025 poster](https://neurips.cc/virtual/2025/poster/119572)

**PRM architecture pattern**:
```
Input: [problem] + [step_1] + ... + [step_k]
Output: scalar score per step (step_k correct or incorrect)
Training signal: binary label per step (human / MC / judge)
At inference: rerank candidate solutions by sum/product of step scores
```

**Step granularity**: Line-level (one reward per line) or token-level (one reward per token boundary). Line-level is cheaper; token-level enables dense RL signals.

### 3.4 Distillation
- **CoT Distillation**: Transfer reasoning patterns from teacher models via KD on CoT traces.
- **Curriculum Distillation**: Gradual complexity increase in training data.
- **Multi-Teacher Distillation**: Aggregates knowledge from multiple models (e.g., GPT-4 + Claude + Gemini traces).

### 3.5 Self-Training
- **STaR**: Self-Taught Reasoner. Model generates reasoning, filters by correctness, retrains on correct traces iteratively.
- **RFT**: Rejection Sampling Fine-Tuning. Sample many outputs, keep correct ones, fine-tune.
- **Rejection Sampling**: Filters low-quality training examples; upstream of both RFT and GRPO data pipelines.

---

## 4. Anthropic Extended Thinking API (Implementation Guide)

> Sources: [Building with extended thinking](https://platform.claude.com/docs/en/build-with-claude/extended-thinking) | [Extended thinking on Bedrock](https://docs.aws.amazon.com/bedrock/latest/userguide/claude-messages-extended-thinking.html) | [Goose issue: adaptive thinking](https://github.com/block/goose/issues/7293)

### 4.1 Extended Thinking (Legacy: budget_tokens)

Enable by adding a `thinking` object to the API request:

```json
{
  "model": "claude-opus-4-6",
  "max_tokens": 16000,
  "thinking": {
    "type": "enabled",
    "budget_tokens": 10000
  },
  "messages": [{"role": "user", "content": "Solve this step by step..."}]
}
```

**Parameters**:
- `budget_tokens`: Integer. Minimum 1,024 tokens. Maximum = context window limit. Sets the MAXIMUM tokens Claude may use for internal reasoning (not a guarantee -- actual usage varies).
- `max_tokens`: Must be >= `budget_tokens` (otherwise the model cannot emit both thinking + final answer).
- Thinking tokens billed at standard output token rates (no separate pricing tier).

**Response structure**:
```json
{
  "content": [
    {
      "type": "thinking",
      "thinking": "Let me work through this carefully...",
      "signature": "EosnCkYICxIMMb3LzNrMu..."
    },
    {
      "type": "text",
      "text": "The answer is 42."
    }
  ]
}
```

### 4.2 Thinking Signatures

- The `signature` field is an **opaque verification token** (not human-readable). Do NOT parse or interpret it.
- Purpose: verifies that the thinking block was **generated by Claude** (not user-injected) when re-submitted in multi-turn conversations.
- In Claude 4 models, signatures are significantly longer than in Claude 3.x.
- **Streaming**: signature is delivered via `signature_delta` inside a `content_block_delta` event, just before `content_block_stop`.
- **Redacted thinking**: when internal reasoning is flagged by safety systems, the block is returned as `type: "redacted_thinking"` with encrypted content. Still pass it back to maintain context -- Claude decrypts it internally.

### 4.3 Interleaved Thinking (2025-05-14 beta)

Enables Claude to think **between tool calls** in agentic workflows (vs. only at the start of a turn).

**Activation**: Add beta header `interleaved-thinking-2025-05-14`.

**Key behaviors**:
- `budget_tokens` applies to the **total** thinking budget across ALL thinking blocks in one assistant turn (not per tool call).
- When using interleaved thinking with tools, `budget_tokens` can effectively equal the entire context window (200K tokens).
- The model emits alternating: `[thinking block] -> [tool_use block] -> [tool_result block] -> [thinking block] -> ...`

**Use case**: Complex multi-step agents where each tool result requires re-reasoning before the next action.

### 4.4 Adaptive Thinking (2026 -- claude-sonnet-4-6, claude-opus-4-6)

Claude **decides automatically** whether to think based on problem complexity, replacing the static `budget_tokens` parameter.

- Old `budget_tokens` parameter deprecated for newer models.
- Claude uses near-zero thinking tokens on trivial queries; allocates heavily on complex ones.
- Eliminates the "overthinking" problem for simple tasks while preserving depth for hard ones.
- Migration: remove `thinking.budget_tokens` for sonnet-4-6/opus-4-6; keep for backward compat with older models.

### 4.5 Comparison: Extended Thinking vs. Competitors

| Feature | Anthropic (Claude 4.6) | OpenAI (o3) | Google (Gemini 2.5 Pro) |
|---------|------------------------|-------------|------------------------|
| API param | `budget_tokens` -> adaptive | `reasoning_effort` (low/medium/high) | `thinking_budget` (tokens) |
| Visibility | `thinking` block (shown) | Mostly hidden | `thought` block (partially shown) |
| Interleaved | Yes (beta header) | Yes (persisted reasoning items) | Partial |
| Signature/auth | Yes (opaque token) | No explicit token | No |
| Min budget | 1,024 tokens | N/A (effort-based) | 0 (auto) |
| Streaming | Chunky (improving) | Smooth | Smooth |

---

## 5. Inference-Time Compute Strategies

### 5.1 Search-Based Methods
- **Tree Search**: MCTS, LATS, SR-MCTS, rStar.
- **Beam Search**: Reasoning beam search, diverse beam search.
- **Best-of-N**: Parallel sampling + verifier selection.
- **Lookahead**: Forward simulation + PRM scoring.

### 5.2 Prompting-Based Methods
- **Sequential**: CoT, Zero-shot CoT, Auto-CoT, PoT, ThoT.
- **Multi-Path**: Self-Consistency, CISC, Universal Self-Consistency.
- **Structured**: ToT, GoT, AoT.
- **Decomposition**: Least-to-Most, Plan-and-Solve, Skeleton-of-Thought.
- **Agentic**: ReAct, Reflexion, Self-Refine, MIRROR.

### 5.3 Hybrid Approaches
- **MCTS + PRM**: rStar-Math, AlphaProof.
- **Self-Play + Verification**: Combines reinforcement learning with reasoning checks.
- **Pipeline Integration**: Maps compute strategies to the 8F pipeline for systematic execution.

---

## 6. Test-Time Compute Scaling Laws

> Sources: [Scaling LLM TTC Optimally arXiv:2408.03314](https://arxiv.org/abs/2408.03314) | [Inference Scaling Laws arXiv:2408.00724](https://arxiv.org/abs/2408.00724) | [Art of Scaling TTC arXiv:2512.02008](https://arxiv.org/abs/2512.02008) | [Plan and Budget OpenReview](https://openreview.net/forum?id=ctspw4CqbS)

### 6.1 Core Finding
Scaling test-time (inference) compute can outperform scaling pre-training parameters for hard reasoning tasks. A smaller model + heavy inference budget can match or exceed a larger model with greedy decoding. Pareto-optimal trade-off: **smaller model + smarter inference >> larger model + naive decode**.

### 6.2 Two Mechanisms for Test-Time Scaling
1. **Search against a dense process-based verifier (PRM)**: Use MCTS / beam / Best-of-N with a PRM as the scoring signal. Compute scales with number of candidates.
2. **Adaptive distribution update**: Given the prompt at test time, update the model's output distribution (e.g., via self-refinement or contrastive decoding). Compute scales with refinement iterations.

### 6.3 Scaling Law Shape

| Budget Region | Behavior | Recommended Strategy |
|--------------|----------|---------------------|
| Very low (< 512 tokens) | Underthinking; underperforms CoT | Greedy or short CoT |
| Optimal (~4K tokens) | Peak performance for most tasks | Extended thinking or Best-of-N |
| Moderate (4K-32K) | Modest gains; cost increases linearly | Use for hard tasks only |
| High (> 32K) | Overthinking risk; performance plateau or degradation | Adaptive compute; dynamic sampling |

**Overthinking**: Models generate verbose reasoning traces even for simple queries. Optimal budget for typical tasks ~4K tokens; beyond this, returns diminish. Source: [Plan and Budget](https://openreview.net/forum?id=ctspw4CqbS)

### 6.4 Large-Scale Empirical Results (2025)

Study spanning >30B tokens across 8 open-source LLMs found three consistent trends:
1. **No single strategy universally dominates** -- optimal strategy is problem-dependent.
2. **Reasoning models exhibit distinct trace-quality patterns** -- models trained with RL produce qualitatively different (denser, fewer dead-ends) traces than base models with CoT.
3. **Performance scales monotonically with compute budget** -- but with diminishing returns past problem-specific saturation. Source: [Art of Scaling TTC](https://arxiv.org/abs/2512.02008)

### 6.5 Compute-Optimal Inference Formula

Given a fixed total budget B (tokens or FLOPs), allocate between:
- N: number of parallel candidates (Best-of-N)
- T: thinking depth per candidate

Research shows optimal split is **problem-difficulty-dependent**:
- Easy problems: N=1, T=small (waste to parallelize)
- Hard problems: N=large, T=moderate (diversity matters)
- Very hard (open-ended): N=moderate, T=large (depth matters)

---

## 7. 8F Pipeline Integration
| Stage | Description | Reasoning Role |
|-------|-------------|----------------|
| **1. Define (F1 CONSTRAIN)** | Problem scope and constraints | Sets boundaries for reasoning tasks; selects budget_tokens range |
| **2. Frame (F2 BECOME)** | Translate problem into model inputs | Structures prompts; injects thinking type (CoT vs ToT vs extended) |
| **3. Execute (F3 INJECT + F5 CALL)** | Run inference with compute strategies | Applies MCTS, PRM scoring, or Best-of-N; calls tools in interleaved mode |
| **4. Filter (F4 REASON)** | Remove invalid or low-quality outputs | PRM step scoring; rejection sampling on reasoning traces |
| **5. Aggregate (F6 PRODUCE)** | Combine outputs from multiple strategies | Self-Consistency voting; Best-of-N selection |
| **6. Analyze (F7 GOVERN)** | Evaluate reasoning quality and alignment | ORM/PAV/R-PRM final scoring; quality gate |
| **7. Adapt** | Refine strategies based on feedback | Adjusts budget_tokens or switches algorithm; DAPO dynamic sampling |
| **8. Store (F8 COLLABORATE)** | Persist reasoning artifacts for audit | Saves reasoning_trace or think blocks; compile + commit |

---

## 8. Model Comparison Matrix
| Model | Reasoning API | RL Algorithm | Inference Strategy | Verifier |
|-------|--------------|--------------|-------------------|---------|
| **Claude 4.6** | Adaptive thinking (was budget_tokens) | RLHF + RLAIF + CAI | Extended thinking, interleaved | Signature-verified blocks |
| **o3** | `reasoning_effort` (low/medium/high) | RLVR + PPO | MCTS + PRM, Best-of-N | Hidden chain |
| **DeepSeek R1** | Structured CoT / ToT | GRPO -> DAPO | Hybrid MCTS + PRM | Open weights |
| **Gemini 2.5 Pro** | `thinking_budget` (token count) | DPO + KTO | Beam search + lookahead | PAV + R-PRM |
| **Qwen3** | Internal budget | DAPO (50pts AIME) | MCTS + PRM | Open weights |

---

## 9. Reasoning Strategy Selection Guide

> Use this guide when selecting a reasoning approach for a new task.

### Decision Tree

```
Is the task verifiable? (math, code, logic)
  YES -> Use RLVR + PRM-guided search (Best-of-N or MCTS)
  NO  -> Is human preference the signal?
          YES -> Use RLHF (PPO) or DPO
          NO  -> Use RLAIF or constitutional CAI

Is compute budget constrained?
  Very tight (< 512 tokens)  -> Greedy decode + Zero-shot CoT
  Moderate (512 - 8K tokens) -> Extended thinking (budget_tokens ~4K)
  Loose (> 8K tokens)        -> Interleaved thinking + Best-of-N + PRM reranking

Is task simple or complex?
  Simple (grade-school math, factual QA) -> Adaptive thinking (Claude 4.6 auto)
  Complex (competition math, multi-step coding) -> Extended thinking + high budget_tokens
  Open-ended (research, creative) -> ToT/GoT + Self-Refine + long budget

Is step-level supervision available?
  YES -> PRM-based search (rStar, AlphaProof)
  NO  -> ORM + Self-Consistency (no PRM needed)
```

### Algorithm Selection by Context

| Scenario | Recommended Algorithm | Why |
|----------|----------------------|-----|
| Single GPU, low VRAM | RLOO or REINFORCE++ | No critic; ~50% less memory than PPO |
| Large-scale cluster training | DAPO or GRPO | Efficient group sampling; clip-higher for exploration |
| Preference alignment (chat) | DPO or KTO | No RL loop; simpler; preference pairs or binary labels |
| Safety-constrained fine-tuning | REBEL or CAI | Entropy bounds; constitutional constraints |
| Math / code reasoning | RLVR + GRPO or DAPO | Verifiable rewards; strong AIME benchmarks |
| Step-level reward available | PRIME or PS-GRPO | Dense token-level signal; no explicit PRM annotation |
| Production API (Anthropic) | Extended thinking (adaptive) | Zero-config; Claude manages budget autonomously |

### PRM vs ORM Selection

| Factor | Use PRM | Use ORM |
|--------|---------|---------|
| Step labels available? | Yes | No |
| Task has multi-step structure? | Yes | No |
| Budget for compute-intensive reranking? | Yes | No |
| Need error localization? | Yes | No |
| Simple correctness check sufficient? | No | Yes |

---

## 10. Glossary (Extended)
- **CoT**: Chain-of-Thought prompting -- explicitly guides LLMs through reasoning steps.
- **PRM**: Process Reward Model -- evaluates intermediate reasoning steps for quality.
- **ThinkPRM**: Long-CoT verifier trained on 1% of PRM800K labels; outperforms LLM-as-Judge.
- **R-PRM**: Enhanced PRM with domain-specific rubrics for precise evaluation.
- **MCTS**: Monte Carlo Tree Search -- search algorithm for planning and decision-making.
- **ReAct**: Reasoning + Acting -- combining logical deduction with tool use.
- **rStar**: Reinforcement Learning + Tree Search -- optimized for math reasoning tasks.
- **CISC**: Contrastive Self-Consistency -- multi-path reasoning technique for robustness.
- **GRPO**: Group Relative Policy Optimization -- PPO without a value network; group baseline.
- **DAPO**: Decoupled Clip and Dynamic Sampling PO -- GRPO at scale with clip-higher + dynamic sampling.
- **Dr. GRPO**: GRPO Done Right -- removes std normalization; equivalent to RLOO up to scaling.
- **RLOO**: REINFORCE Leave-One-Out -- leave-one-out baseline; strong efficiency/performance balance.
- **RLVR**: Reinforcement Learning with Verifiable Rewards -- binary feedback from deterministic tools.
- **budget_tokens**: Anthropic API param (legacy) -- max tokens for Claude's internal thinking block.
- **Adaptive thinking**: Anthropic's 2026 replacement for budget_tokens -- Claude self-selects compute.
- **Thinking signature**: Opaque verification token proving thinking blocks were generated by Claude.
- **Interleaved thinking**: Beta mode where Claude thinks between tool calls in agentic flows.
- **Overthinking**: Pathology where models allocate excessive tokens to simple queries -- mitigated by adaptive compute and dynamic sampling.
- **Compute-optimal inference**: Budget allocation strategy that maximizes accuracy per FLOP at test time.

---

## 11. Conclusion
This guide synthesizes the latest advancements in reasoning, training, and inference strategies for LLMs. Key 2025-2026 developments: (1) Anthropic's migration from static `budget_tokens` to adaptive thinking on Claude 4.6; (2) DAPO surpassing GRPO on AIME benchmarks; (3) ThinkPRM achieving discriminative PRM performance with only 1% of the label budget; (4) empirical confirmation that test-time compute scaling with smaller models can Pareto-dominate larger models with greedy decoding. The reasoning strategy selection guide in Section 9 provides practitioners with actionable algorithm-selection criteria. Future work: cross-model benchmarking at matched compute budgets, and open-source tooling for step-level reward annotation.
