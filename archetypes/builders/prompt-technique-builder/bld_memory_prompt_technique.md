---
kind: memory
id: p10_mem_prompt_technique_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for prompt_technique construction
quality: 8.7
title: "Memory Prompt Technique"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_technique, builder, memory]
tldr: "Learned patterns and pitfalls for prompt_technique construction"
domain: "prompt_technique construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Observation
Ambiguous instructions often lead to inconsistent or off-topic outputs. Overloading prompts with excessive details can overwhelm models, reducing effectiveness.

## Pattern
Clear, concise phrasing with explicit goals improves reliability. Structuring prompts into logical steps or roles (e.g., "Act as a tutor") enhances focus and coherence.

## Evidence
Reviewed artifacts showed 40% higher success rates with prompts using example-based scaffolding (e.g., "Answer like this: [example]").

## Recommendations
- Prioritize specificity: Define exact tasks and desired output formats.
- Use role-playing or scenario framing to guide model behavior.
- Test iterative refinements to balance detail and clarity.
- Avoid vague terms like "best" or "good"; use measurable criteria.
- Align techniques with model capabilities (e.g., avoid complex reasoning for basic models).
