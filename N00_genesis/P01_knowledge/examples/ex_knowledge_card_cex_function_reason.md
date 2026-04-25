---
id: p01_kc_cex_function_reason
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Function REASON — Structured Thinking Before Action"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, llm-function, reason, chain-of-thought, planning, routing]
tldr: "REASON generates internal tokens (CoT, ReAct, planning) before acting — 7 types that separate thinking from producing"
when_to_use: "Understand why reasoning is a function separate from generation and how to typify thinking patterns"
keywords: [reason, chain-of-thought, react, planner, router, tree-of-thought]
long_tails:
  - "What is the difference between chain of thought and tree of thought in CEX"
  - "Why REASON is a function separate from PRODUCE in CEX"
axioms:
  - "ALWAYS use REASON before CALL in complex tasks"
  - "NEVER confuse planner (generates plan) with router (selects handler)"
linked_artifacts:
  primary: p01_kc_cex_function_call
  related: [p01_kc_cex_function_become, p01_kc_cex_function_inject]
density_score: null
data_source: "https://arxiv.org/abs/2309.07864"
related:
  - p01_kc_cex_lp03_prompt
  - p01_kc_cex_function_produce
  - p01_kc_cex_llm_function_concept
  - p03_plan_task_decomposition
  - p01_kc_academic_agent_patterns
  - p01_kc_cex_pipeline_execution
  - planning-strategy-builder
  - bld_output_template_planning_strategy
  - cex_llm_vocabulary_whitepaper
  - p01_kc_chain_of_thought
---

## Summary

REASON is the meta-cognitive operation of THINKING before acting. The LLM generates tokens for itself (chain-of-thought, planning, decomposition) before generating final output. With 7 types (9% of CEX), it is architecturally distinct from PRODUCE — confirmed by DSPy (ChainOfThought separate from Predict), Semantic Kernel (Planner as first-class type), and academic literature (Wang et al. 2023).

## Spec

| Type | LP | Function | Detail |
|------|-----|----------|--------|
| chain_of_thought | P03 | Linear reasoning | Explicit step-by-step to conclusion |
| react | P03 | Think-Act-Observe | Interleaves reasoning with environment actions |
| planner | P03 | Dynamic plan | Creates workflow at runtime based on goal |
| router | P02 | Handler selection | Directs input to correct specialist |
| tree_of_thought | P03 | Parallel reasoning | Multiple branches with evaluation |
| decomposition | P03 | Problem breakdown | Independent sub-problems treated in parts |
| goal | P03 | Success criterion | Measurable objective that guides REASON |

Complexity hierarchy: CoT < ReAct < Planner < ToT.
CoT is linear (1 path). ReAct interleaves with environment.
Planner generates complete sequence. ToT explores N paths.
Router is NOT deep reasoning — it is fast classification.
REASON produces INTERNAL tokens (for the LLM itself), not final output.
REASON vs PRODUCE separation: DSPy ChainOfThought != Predict.

## Code

<!-- lang: python | purpose: ReAct reasoning loop -->
```python
# ReAct: Thought -> Action -> Observation -> repeat
thought = reason("Preciso verificar preco atual do produto")
action = call(tool="scraper", url=product_url)
observation = parse(action.result)
thought = reason(f"Preco={observation.price}, comparar com meta")
# REASON intercala com CALL ate resolver
```

## Patterns

| Trigger | Action |
|---------|--------|
| Task requires explicit logic | Use chain_of_thought |
| Task requires environment interaction | Use react (think-act-observe) |
| Unpredictable action sequence | Use planner to generate workflow |
| Multiple handlers available | Router selects the best |
| Problem with multiple solutions | tree_of_thought to explore |
| Problem too large to solve at once | decomposition into sub-tasks |

## Anti-Patterns

- CoT in trivial tasks (overhead without gain)
- Planner with hardcoded actions (use workflow, not planner)
- Router with 10+ options (LLM does not discriminate well)
- Confusing planner with router (sequence vs selection)
- REASON without INJECT (reasoning without data = hallucination)
- Skipping REASON and going straight to CALL (action without plan)

## References

- source: https://arxiv.org/abs/2309.07864
- source: https://arxiv.org/abs/2305.10601
- related: p01_kc_cex_function_call
- related: p01_kc_cex_function_inject

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_lp03_prompt]] | sibling | 0.37 |
| [[p01_kc_cex_function_produce]] | sibling | 0.31 |
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.25 |
| [[p03_plan_task_decomposition]] | downstream | 0.24 |
| [[p01_kc_academic_agent_patterns]] | sibling | 0.22 |
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.21 |
| [[planning-strategy-builder]] | downstream | 0.17 |
| [[bld_output_template_planning_strategy]] | downstream | 0.17 |
| [[cex_llm_vocabulary_whitepaper]] | sibling | 0.16 |
| [[p01_kc_chain_of_thought]] | sibling | 0.16 |
