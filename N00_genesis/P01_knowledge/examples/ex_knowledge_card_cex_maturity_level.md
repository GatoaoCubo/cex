---
id: p01_kc_cex_maturity_level
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Maturity Level — LP Completeness as Capability Diagnostic"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, maturity, capability, diagnostic, lp-completeness]
tldr: "7 levels (L0-L6) measure maturity of LLM entities by LP completeness — diagnostic observation, NOT prescription"
when_to_use: "Diagnose why an LLM entity fails or assess its current maturity"
keywords: [maturity-level, capability-maturity, diagnostic, cmm]
long_tails:
  - "How to measure maturity of an LLM agent using CEX LPs"
  - "What is the difference between L0 and L5 in the CEX maturity model"
axioms:
  - "NEVER treat levels as prescription (it is empirical observation)"
  - "ALWAYS use maturity as diagnostic, not as goal"
linked_artifacts:
  primary: p01_kc_cex_fractal_architecture
  related: [p01_kc_cex_boundary_concept]
density_score: null
data_source: null
related:
  - p01_kc_cex_fractal_architecture
  - p01_kc_cex_learning_package_concept
  - p04_ct_bootstrap
  - p04_ct_cex_compile
  - p01_kc_cex_agent_group_concept
  - p01_kc_cex_llm_function_concept
  - p01_kc_lp06_schema
  - p01_kc_cex_pipeline_execution
  - p01_kc_cex_taxonomy
  - p01_kc_lp02_model
---

## Summary

Maturity Level measures the completeness of the 12 LPs in an LLM entity, from L0 (prompt, 1 LP) to L6 (self-evolving ecosystem). Inspired by CMM but original in its application to LLM entities. It is explicitly an OBSERVATION, not a law: "more capable entities tend to fill more LPs". Causality may be inverse — complex entities NEED more LPs. Primary utility: diagnosing failures due to missing LPs.

## Spec

| Level | LPs | Core Capability | Diagnostic |
|-------|-----|----------------|------------|
| L0 Prompt | 1/12 | Generate text | Stateless, no identity, no tools |
| L1 Chain | 2/12 | Sequence outputs | Basic composition, no memory |
| L2 Agent | 3-4/12 | Identity + knowledge | Entity with role and data |
| L3 Runtime | 6/12 | Dedicated process | Tools, hooks, monitoring |
| L4 Agent_group | 9/12 | Departmental autonomy | Memory, evolution, coordination |
| L5 System | 12/12 | Coordinated multi-agent | All 8 functions active |
| L6 Ecosystem | 12/12+ | Self-evolving | Generates new types, LPs, functions |

Origin: CMM (Capability Maturity Model) with 5 organizational levels. CEX adapts to 7 levels of LLM entities using LP completeness as the metric.

Nature: empirical observation, NOT prescription. "Filling more LPs" does not cause improvement. But absence of LPs frequently EXPLAINS failures. Diagnostic > recipe.

## Patterns

| Trigger | Action |
|---------|--------|
| Agent fails at expected task | Check which LPs are missing |
| Prompt needs to scale to agent | Add LPs incrementally |
| Assess entity capability | Count filled LPs vs required |
| Plan system evolution | Map current LPs, prioritize next |
| Compare entities across projects | Use level as common metric |

## Anti-Patterns

- Using levels as a goal ("we need to be L5" without need)
- Filling empty LPs with generic content to raise level
- Assuming causality (more LPs = automatically better)
- Ignoring that L0 is sufficient for simple tasks
- Comparing levels across different domains without context

## References

- related: p01_kc_cex_fractal_architecture
- related: p01_kc_cex_boundary_concept

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_fractal_architecture]] | sibling | 0.55 |
| [[p01_kc_cex_learning_package_concept]] | sibling | 0.47 |
| [[p04_ct_bootstrap]] | downstream | 0.32 |
| [[p04_ct_cex_compile]] | downstream | 0.22 |
| [[p01_kc_cex_agent_group_concept]] | sibling | 0.22 |
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.19 |
| [[p01_kc_lp06_schema]] | sibling | 0.19 |
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.18 |
| [[p01_kc_cex_taxonomy]] | sibling | 0.18 |
| [[p01_kc_lp02_model]] | sibling | 0.17 |
