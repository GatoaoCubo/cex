---
kind: examples
id: bld_examples_prompt_technique
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of prompt_technique artifacts
quality: 8.8
title: "Examples Prompt Technique"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_technique, builder, examples]
tldr: "Golden and anti-examples of prompt_technique artifacts"
domain: "prompt_technique construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```yaml
name: "Chain-of-Thought with Self-Consistency"
kind: prompt_technique
vendor: Anthropic
model: Claude 3.5
version: 1.0
body: |
  1. Frame the problem as a multi-step reasoning task
  2. Generate 3 independent solutions using separate reasoning paths
  3. Compare results and select the most consistent answer
  4. Use explicit markers like [Reasoning 1], [Reasoning 2] for clarity
  Example: "Solve this math problem by showing three different solution paths, then choose the most consistent answer."
```

## Anti-Example 1: Template Confusion
```yaml
name: "Generic Question Template"
kind: prompt_technique
vendor: OpenAI
model: GPT-4
version: 0.1
body: |
  "Please answer the following question: [Question here]. Provide a detailed explanation."
```
## Why it fails
This is a reusable template (prompt_template), not a specific prompting method. It lacks the structural pattern that defines a true prompt_technique.

## Anti-Example 2: Vague Instructions
```yaml
name: "Unstructured Thinking"
kind: prompt_technique
vendor: Google
model: Gemini Pro
version: 1.0
body: |
  "Think deeply about this and give a thorough answer."
```
## Why it fails
The instruction is too vague to qualify as a technique. It doesn't define a specific pattern or method for structuring the prompt, making it non-reproducible.
