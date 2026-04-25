---
id: p01_kc_cex_function_produce
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Function PRODUCE — Executing Work and Generating Output"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, llm-function, produce, chain, workflow, dag, meta-prompt, completion]
tldr: "PRODUCE generates final output (text, code, data) via 5 types — the EXECUTION function of the LLM pipeline"
when_to_use: "Understand how LLMs materialize output and the boundary between PRODUCE (external output) and REASON (internal thought)"
keywords: [produce, chain, workflow, dag, meta_prompt, completion, generation]
long_tails:
  - "What is the difference between PRODUCE and REASON in CEX"
  - "What are the 5 production types in the CEX taxonomy"
axioms:
  - "ALWAYS distinguish REASON (internal thought) from PRODUCE (external output)"
  - "NEVER use workflow when linear chain suffices"
linked_artifacts:
  primary: p01_kc_cex_function_call
  related: [p01_kc_cex_function_reason, p01_kc_cex_function_constrain]
density_score: null
data_source: "https://arxiv.org/abs/2210.03629"
related:
  - chain-builder
  - p01_kc_cex_lp03_prompt
  - p01_kc_cex_pipeline_execution
  - p01_kc_chain
  - bld_collaboration_chain
  - p01_kc_cex_llm_function_concept
  - p03_sp_chain_builder
  - p01_kc_cex_function_reason
  - p01_kc_workflow
  - workflow-builder
---

## Summary

PRODUCE generates the main output of the LLM pipeline — text, code, structured data, artifacts. With 5 types (6% of CEX), it covers from raw completions to complex DAGs with dependencies. Critical boundary: REASON produces THOUGHT (internal, meta-cognitive operation); PRODUCE produces OUTPUT (external, consumable artifact). The least differentiating function — everyone does PRODUCE well; the differentiator lies in the surrounding functions (INJECT, REASON, CONSTRAIN, GOVERN).

## Spec

| Type | LP | Complexity | Function | Detail |
|------|-----|-----------|----------|--------|
| completion | P03 | Low | Raw output | Text pre/post-processing |
| meta_prompt | P03 | Medium | Prompt generates prompt | Applied self-referentiality |
| chain | P12 | Medium | Linear sequence | Output A feeds input B |
| workflow | P12 | High | Graph with branches | Conditionals, loops, parallelism |
| dag | P12 | High | Acyclic graph | Dependencies without cycles |

Complexity hierarchy: completion < meta_prompt < chain < workflow.
DAG and workflow cover distinct needs: DAG guarantees acyclicity
(execution in topological order), workflow allows cycles and loops.
chain is the minimal form of composition: A -> B -> C linear.
PRODUCE is the 5th function in the pipeline (after INJECT, BECOME, REASON, CALL).
Optimizations for REASON (improve reasoning) and PRODUCE (improve
generation) require fundamentally different techniques.
completion is raw material — raw output before CONSTRAIN formats it.
meta_prompt is the metacircular artifact of CEX: prompt that generates prompt,
applied self-referentiality. Do not confuse with prompt_template
(CONSTRAIN) which parameterizes existing prompts.
LangChain Chains, DSPy Modules, Haystack Pipelines — all confirm
that LLM operation composition is a first-class citizen.
PRODUCE is the LLM's reason for existence, but paradoxically the least
differentiating function. All models do PRODUCE. What separates
mediocre systems from excellent ones are the 7 surrounding functions.

## Patterns

| Trigger | Action |
|---------|--------|
| Simple output without composition | direct completion |
| Linear pipeline without branches | chain (A -> B -> C) |
| Pipeline with conditional decisions | workflow with branches |
| Complex dependencies without cycles | dag with topological order |
| Generate optimized prompts automatically | meta_prompt (prompt that generates prompt) |
| Same pattern applied to varied inputs | chain + prompt_template (CONSTRAIN) |
| Task requires reasoning before generating | REASON first, PRODUCE after |

## Code

<!-- lang: python | purpose: chain and workflow PRODUCE patterns -->
```python
# chain: composicao linear A -> B -> C
chain = [summarize, translate, format_md]
result = input_text
for step in chain:
    result = step(result)  # output de cada step alimenta o proximo

# workflow: grafo com branches condicionais
if complexity(task) > 0.7:
    result = workflow.run(dag=dependency_graph, parallel=True)
else:
    result = chain_run(steps=[analyze, produce], input=task)

# meta_prompt: prompt que gera prompt otimizado
meta = "Generate a prompt that extracts product specs as JSON"
optimized_prompt = llm.complete(meta)  # PRODUCE de segundo ordem
```

## Anti-Patterns

- Workflow for simple linear pipeline (complexity without need)
- DAG with implicit cycles (violates definition, use workflow)
- PRODUCE without prior REASON in complex tasks (shallow output)
- Completion as persistent type (use chain or workflow)
- meta_prompt without quality evaluation (degradation spiral)
- Confusing REASON (chain-of-thought) with PRODUCE (final text)

## References

- source: https://arxiv.org/abs/2210.03629
- source: https://arxiv.org/abs/2305.10601
- related: p01_kc_cex_function_reason
- related: p01_kc_cex_function_call
- related: p01_kc_cex_function_constrain

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[chain-builder]] | downstream | 0.34 |
| [[p01_kc_cex_lp03_prompt]] | sibling | 0.31 |
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.30 |
| [[p01_kc_chain]] | sibling | 0.30 |
| [[bld_collaboration_chain]] | downstream | 0.29 |
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.29 |
| [[p03_sp_chain_builder]] | downstream | 0.28 |
| [[p01_kc_cex_function_reason]] | sibling | 0.26 |
| [[p01_kc_workflow]] | sibling | 0.26 |
| [[workflow-builder]] | downstream | 0.25 |
