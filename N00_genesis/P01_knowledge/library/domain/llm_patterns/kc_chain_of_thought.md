---
id: p01_kc_chain_of_thought
kind: knowledge_card
type: domain
pillar: P01
title: "Chain-of-Thought (CoT) Prompting"
version: 1.0.0
created: 2026-03-31
author: n07_orchestrator
domain: llm_patterns
quality: 9.0
tags: [cot, reasoning, prompting, llm, step-by-step]
tldr: "Step-by-step reasoning in prompts improves accuracy on math, logic, and multi-step tasks. Zero-shot CoT vs few-shot CoT."
when_to_use: "When the task requires multi-step reasoning, planning, or decomposition"
keywords: [chain-of-thought, cot, reasoning, step-by-step, zero-shot-cot, few-shot-cot]
density_score: 0.92
updated: "2026-04-07"
---

# Chain-of-Thought Prompting

## Core Concept
CoT elicits intermediate reasoning steps from LLMs before the final answer. Transforms Q→A into Q→reasoning→A.

## Variants

| Variant | Technique | When to Use |
|---------|-----------|-------------|
| Zero-shot CoT | "Let's think step by step" | Quick boost, no examples |
| Few-shot CoT | 2-3 examples with reasoning traces | Complex domain, consistent format |
| Self-consistency | Sample N paths, majority vote | High-stakes, math proofs |
| Tree-of-Thought | Branch reasoning, evaluate paths | Planning, multi-option |
| Auto-CoT | LLM generates own examples | No good examples available |

## When CoT Helps
- Multi-step math and arithmetic
- Logical reasoning and deduction
- Code generation with complex requirements
- Planning and decomposition tasks

## When CoT Hurts
- Simple factual recall (adds latency, no gain)
- Tasks requiring creativity over logic
- Very short outputs where overhead > value

## Provider-Agnostic Pattern
```
# Works on Claude, GPT, Gemini, Llama
"Solve this step by step, showing your reasoning before the final answer."
```

## CEX Integration
- 8F F4 REASON uses implicit CoT (plan before produce)
- Builder specs can request CoT via reasoning instructions
- Quality gates verify reasoning presence in complex outputs
