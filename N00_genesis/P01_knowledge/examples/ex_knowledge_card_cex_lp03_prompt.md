---
id: p01_kc_cex_lp03_prompt
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LP03 Prompt — How the LLM Speaks (10 Types of Prompt Engineering)"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.2
tags: [cex, lp03, prompt, reason, constrain, template, chain-of-thought]
tldr: "P03 Prompt governs LLM communication via 10 types — from system_prompt to meta_prompt — covering 5 LLM functions"
when_to_use: "Classify prompt artifacts or understand how P03 orchestrates reasoning and format"
keywords: [prompt-template, system-prompt, cot, react, few-shot, meta-prompt, chain]
long_tails:
  - "What types of prompt exist in CEX"
  - "Difference between chain_of_thought and react in CEX"
axioms:
  - "ALWAYS use {{MUSTACHE}} for tier-1 variables"
  - "NEVER mix instruction (P03) with knowledge (P01)"
linked_artifacts:
  primary: p01_kc_cex_lp01_knowledge
  related: [p01_kc_cex_lp02_model, p01_kc_cex_lp04_tools]
density_score: 1.0
data_source: "https://arxiv.org/abs/2201.11903"
related:
  - p01_kc_cex_function_reason
  - p01_kc_cex_llm_function_concept
  - p01_kc_cex_function_produce
  - p01_kc_cex_pipeline_execution
  - p01_kc_cex_lp02_model
  - p01_kc_cex_lp04_tools
  - p01_kc_cex_function_become
  - p01_kc_cex_function_inject
  - p01_kc_cex_lp01_knowledge
  - bld_architecture_dataset_card
---

## Quick Reference

topic: LP03 Prompt | scope: 10 artifact types | criticality: high
llm_functions: BECOME + INJECT + REASON + PRODUCE + CONSTRAIN
analogy: language + accent + register

## Key Concepts

- P03 answers: "how does this entity communicate?"
- Most populous LP in CEX (10 types) — language is the medium
- system_prompt uses BECOME (persistent identity)
- user_prompt and few_shot use INJECT (task + examples)
- chain_of_thought and react use REASON (reasoning)
- chain and meta_prompt use PRODUCE (generate outputs)
- prompt_template uses CONSTRAIN (template with variables)
- Variables: {{MUSTACHE}} tier-1, [BRACKET] tier-2 authoring
- router_prompt classifies input and routes to handler
- planner decomposes task into an executable plan of steps
- P03 is shaped by P02 (identity defines register)
- P03 consumes P01 (templates reference knowledge cards)
- P03 is optimized by P11 (prompts improve with feedback)
- CoT: explicit reasoning without tools (Wei et al. 2022)
- ReAct: Thought/Action/Observation with tools (Yao 2023)
- meta_prompt generates/optimizes other prompts (MIPRO, OPRO)
- chain links prompts: output A becomes input B (pipeline)

## Phases

1. Identity: system_prompt defines role via BECOME
2. Context: user_prompt + few_shot inject task via INJECT
3. Reasoning: CoT or ReAct structure thought via REASON
4. Production: chain or meta_prompt generate outputs via PRODUCE
5. Constraint: prompt_template constrains format via CONSTRAIN

## Golden Rules

- ALWAYS separate system_prompt (who) from user_prompt (what)
- ALWAYS use few_shot with min 2, max 5 examples
- NEVER hardcode data in prompt_template (use variables)
- NEVER use CoT when task is simple (overhead without gain)
- ALWAYS prefer ReAct over CoT when tools are available

## Comparison

| Type | LLM Function | Purpose | Core |
|------|-------------|---------|------|
| system_prompt | BECOME | Identity + rules | yes |
| user_prompt | INJECT | Specific task | yes |
| prompt_template | CONSTRAIN | Template with {{vars}} | yes |
| few_shot | INJECT | Input/output examples | yes |
| chain_of_thought | REASON | Step-by-step reasoning | no |
| react | REASON | Thought/Action/Observation | no |
| chain | PRODUCE | Prompt sequence | no |
| meta_prompt | PRODUCE | Prompt that generates prompts | no |
| router_prompt | REASON | Classify + route input | no |
| planner | REASON | Decompose task into steps | no |

## Flow

```
[system_prompt] -- BECOME --> active identity
        |
[user_prompt + few_shot] -- INJECT --> context
        |
[CoT / ReAct / planner] -- REASON --> reasoning
        |
[chain / meta_prompt] -- PRODUCE --> output
        |
[prompt_template] -- CONSTRAIN --> final format
```

## References

- source: https://arxiv.org/abs/2201.11903
- source: https://arxiv.org/abs/2210.03629
- deepens: p01_kc_cex_lp01_knowledge
- related: p01_kc_cex_lp02_model


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_function_reason]] | sibling | 0.37 |
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.35 |
| [[p01_kc_cex_function_produce]] | sibling | 0.34 |
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.29 |
| [[p01_kc_cex_lp02_model]] | sibling | 0.28 |
| [[p01_kc_cex_lp04_tools]] | sibling | 0.25 |
| [[p01_kc_cex_function_become]] | sibling | 0.24 |
| [[p01_kc_cex_function_inject]] | sibling | 0.22 |
| [[p01_kc_cex_lp01_knowledge]] | sibling | 0.22 |
| [[bld_architecture_dataset_card]] | downstream | 0.22 |
