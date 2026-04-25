---
id: p01_kc_cex_boundary_concept
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Boundary — Explicit Exclusion That Prevents Type Confusion"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, boundary, type-safety, disambiguation, taxonomy]
tldr: "Boundary defines what a type IS NOT, reducing ambiguity across 78 types and preventing misclassification by LLMs"
when_to_use: "Define new CEX types or diagnose incorrect artifact classification"
keywords: [boundary, exclusion, type-safety, disambiguation]
long_tails:
  - "How to define boundaries between artifact types in CEX"
  - "Why boundaries prevent confusion in LLM taxonomies"
axioms:
  - "ALWAYS define boundary before specs for new types"
  - "NEVER assume that title or description are enough to disambiguate"
linked_artifacts:
  primary: p01_kc_cex_function_become
  related: [p01_kc_cex_fractal_architecture]
density_score: null
data_source: null
related:
  - p01_kc_cex_type_artifact
  - p01_kc_cex_taxonomy
  - p01_kc_cex_lp12_orchestration
  - p06_bp_knowledge_card
  - p01_kc_lp03_prompt
  - p01_kc_lp04_tools
  - p02_agent_[name_slug]
  - p01_kc_cex_function_produce
  - kc_format_benchmark_cex_types
  - p01_kc_lp06_schema
---

## Summary

Boundary explicitly defines what a CEX type IS NOT. In a taxonomy of 78 types, title and description are not enough to disambiguate — LLMs confuse knowledge_card with instruction, template with configuration. Boundary resolves this by declaring exclusions: "KC IS NOT instruction, IS NOT config, IS NOT template". Cost without boundary: knowledge lost between sessions, disposable agents, and invisible technical debt.

## Spec

| Type | Boundary (IS NOT) | Common Confusion |
|------|-------------------|------------------|
| knowledge_card (P01) | instruction, config, template, test | LLM generates "do X" inside KC |
| instruction (P03) | knowledge, config, schema | Mixes factual data with commands |
| skill (P04) | knowledge, prompt, workflow | Confuses def/class with documentation |
| agent (P02) | prompt, chain, runtime | Treats agent as complex prompt |
| schema (P06) | template, config, knowledge | Confuses validation with generation |
| workflow (P12) | instruction, chain, script | Treats orchestration as single step |

General rule: if it has executable `def/class`, it is skill (P04). If it has imperative "do X", it is instruction (P03). If it has distilled factual data, it is knowledge_card (P01).

Cost of chaos without boundaries:
- Lost knowledge: each LLM session forgets everything
- Disposable agents: 50 agents = 50x definition cost
- Technical debt: invisible dependencies between artifacts

## Patterns

| Trigger | Action |
|---------|--------|
| New type proposed in CEX | Define boundary BEFORE specs |
| KC rejected by validator | Check if content violates boundary |
| LLM classifies artifact wrong | Add explicit boundary to the type |
| Two types seem to overlap | Boundary defines the dividing line |
| Importing external artifacts | Map to CEX type via boundaries |

## Anti-Patterns

- Defining type only by positive description (without saying IS NOT)
- Vague boundaries like "is not another type" (without specifying)
- Omitting boundary in new types (future confusion guaranteed)
- Boundary that contradicts the type's own specs
- Trusting that the LLM will infer boundaries on its own

## References

- related: p01_kc_cex_fractal_architecture
- related: p01_kc_cex_function_become

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_type_artifact]] | sibling | 0.29 |
| [[p01_kc_cex_taxonomy]] | sibling | 0.25 |
| [[p01_kc_cex_lp12_orchestration]] | sibling | 0.20 |
| [[p06_bp_knowledge_card]] | downstream | 0.19 |
| [[p01_kc_lp03_prompt]] | sibling | 0.19 |
| [[p01_kc_lp04_tools]] | sibling | 0.18 |
| [[p02_agent_[name_slug]]] | downstream | 0.18 |
| [[p01_kc_cex_function_produce]] | sibling | 0.18 |
| [[kc_format_benchmark_cex_types]] | sibling | 0.17 |
| [[p01_kc_lp06_schema]] | sibling | 0.17 |
