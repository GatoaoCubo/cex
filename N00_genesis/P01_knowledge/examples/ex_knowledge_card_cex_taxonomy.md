---
id: p01_kc_cex_taxonomy
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Taxonomy — Universal Classification for LLM Enterprise Artifacts"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, taxonomy, llm-artifacts, standardization, interoperability]
tldr: "CEX classifies 78 LLM artifact types into 8 functions and 12 LPs, covering 91% of 12 frameworks -- the cognitive TCP/IP"
when_to_use: "Understand the complete CEX structure and why to standardize LLM artifacts"
keywords: [cex, taxonomy, normalization, tcp-ip, artifact-types]
long_tails:
  - "What is CEX and why standardize enterprise AI artifacts"
  - "How many artifact types exist in LLM systems"
axioms:
  - "ALWAYS use the CEX vocabulary before inventing nomenclature"
  - "NEVER treat functions as folders -- they are pipeline stages"
linked_artifacts:
  primary: null
  related: [p01_kc_cex_llm_function_concept, p01_kc_cex_learning_package_concept, p01_kc_cex_type_artifact]
density_score: null
data_source: "https://arxiv.org/abs/2308.00352"
related:
  - p01_kc_cex_llm_function_concept
  - p01_kc_cex_type_artifact
  - p01_kc_cex_pipeline_execution
  - p01_kc_cex_function_govern
  - p01_kc_cex_boundary_concept
  - p01_kc_cex_learning_package_concept
  - p01_kc_cex_function_produce
  - p01_kc_cex_lp08_architecture
  - p01_kc_cex_function_inject
  - n04_competitive_knowledge
---

## Summary

CEXAI (Cognitive Exchange AI) is a universal taxonomy that classifies all enterprise LLM system artifacts. An audit of 12 frameworks (DSPy, LangChain, CrewAI, AutoGen, Haystack, etc.) revealed 86 types with zero shared standard. CEX reduces to 78 normalized types in 8 functions and 12 Learning Packages, covering 91% of industry artifacts (70% direct + 21% partial).

## Spec

| Dimension | Value | Detail |
|-----------|-------|--------|
| Total types | 78 | Complete LLM artifact vocabulary |
| Functions | 8 | BECOME, INJECT, REASON, CALL, PRODUCE, CONSTRAIN, GOVERN, COLLABORATE |
| Learning Packages | 12 | P01 Knowledge to P12 Orchestration |
| Frameworks audited | 12 | DSPy, LangChain, Semantic Kernel, AutoGen, CrewAI, Haystack, LlamaIndex, Guidance, Instructor, Outlines, LMQL, LangGraph |
| Extra CN frameworks | 10 | Qwen-Agent, ModelScope-Agent, XAgent, AgentScope, MetaGPT, CAMEL, ChatDev, AutoAgents, AgentVerse, ToolBench |
| Coverage | 91% | 70% direct mapping + 21% partial |
| Gaps (9%) | 4 areas | Multi-agent coord, constrained gen, pipeline, planning |
| Analogy | TCP/IP | Shared vocabulary between isolated networks |
| Layers | 5 | content, spec, prompt, runtime, governance |
| Types per function | 6-14 | PRODUCE has the most types, COLLABORATE the fewest |

## Patterns

| Trigger | Action |
|---------|--------|
| New LLM artifact created | Classify by function + LP + CEX type |
| Migration between frameworks | Map framework types to CEX |
| LLM system audit | List existing artifacts by CEX type |
| Engineer onboarding | Teach 8 functions before showing code |
| System interop | Exchange artifacts via CEX contracts |

## Code

<!-- lang: python | purpose: CEX type classification -->
```python
CEX_FUNCTIONS = [
    "BECOME", "INJECT", "REASON", "CALL",
    "PRODUCE", "CONSTRAIN", "GOVERN", "COLLABORATE",
]
CEX_LPS = {f"P{i:02d}": name for i, name in enumerate([
    "Knowledge", "Model", "Prompt", "Tools",
    "Output", "Schema", "Evals", "Architecture",
    "Config", "Memory", "Feedback", "Orchestration",
], 1)}
# 78 tipos = sum(tipos_por_lp.values())
# Cada tipo tem: funcao, lp, camada, max_size, naming
```

## Anti-Patterns

- Inventing custom nomenclature without consulting CEX vocabulary
- Treating functions as file folders instead of pipeline
- Ignoring LPs and classifying artifacts only by function
- Mapping 1:1 to a specific framework (loses universality)
- Creating new types without explicit boundary and schema

## References

- source: https://arxiv.org/abs/2308.00352
- source: https://arxiv.org/abs/2303.17760
- related: p01_kc_cex_llm_function_concept
- related: p01_kc_cex_learning_package_concept
- related: p01_kc_cex_type_artifact

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.37 |
| [[p01_kc_cex_type_artifact]] | sibling | 0.36 |
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.30 |
| [[p01_kc_cex_function_govern]] | sibling | 0.28 |
| [[p01_kc_cex_boundary_concept]] | sibling | 0.27 |
| [[p01_kc_cex_learning_package_concept]] | sibling | 0.27 |
| [[p01_kc_cex_function_produce]] | sibling | 0.26 |
| [[p01_kc_cex_lp08_architecture]] | sibling | 0.24 |
| [[p01_kc_cex_function_inject]] | sibling | 0.24 |
| [[n04_competitive_knowledge]] | related | 0.23 |
