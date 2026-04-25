---
id: p01_kc_cex_fractal_architecture
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Fractal — Same 12 LPs at Every Scale From Prompt to System"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, fractal, scale, architecture, lp-completeness]
tldr: "Same 12 LPs describe prompt (1/12), agent (4/12), and system (12/12) — difference is completeness, not structure"
when_to_use: "Understand why the same taxonomy works at every LLM scale"
keywords: [fractal, scale-invariance, lp-completeness, emergence]
long_tails:
  - "How the 12 CEX LPs apply at different scales"
  - "What is the difference between prompt, agent, and system in CEX"
axioms:
  - "ALWAYS use the same 12 LPs regardless of scale"
  - "NEVER create a separate taxonomy for prompts vs agents vs systems"
linked_artifacts:
  primary: p01_kc_cex_maturity_level
  related: [p01_kc_cex_boundary_concept, p01_kc_cex_lens_concept]
density_score: null
data_source: null
related:
  - p01_kc_cex_learning_package_concept
  - p01_kc_cex_maturity_level
  - p01_kc_cex_pipeline_execution
  - p01_kc_cex_llm_function_concept
  - action-prompt-builder
  - chain-builder
  - prompt-version-builder
  - p01_kc_cex_agent_group_concept
  - system-prompt-builder
  - p01_kc_lp03_prompt
---

## Summary

The fractal principle of CEX establishes that the same 12 LP structure repeats at every scale: prompt, chain, agent, runtime, agent_group, and system. The difference between a simple prompt and a multi-agent system is not one of type — it is one of completeness. A prompt fills 1/12 LPs. An agent, 3-4/12. A system, 12/12. You learn ONE structure and scale gradually.

## Spec

| Scale | LPs | Active Functions | Industry Equivalent |
|-------|-----|-----------------|---------------------|
| L0 Prompt | 1/12 (P03) | PRODUCE | Basic OpenAI completion |
| L1 Chain | 2/12 (P03,P12) | PRODUCE, COLLABORATE | LangChain LCEL, DSPy pipeline |
| L2 Agent | 3-4/12 (P01-P03,P06) | BECOME, INJECT, REASON, PRODUCE | CrewAI Agent, MetaGPT Role |
| L3 Runtime | 6/12 | +CALL, CONSTRAIN | Claude Code with tools and hooks |
| L4 Agent_group | 9/12 | +LEARN, EVOLVE | Autonomous department with memory |
| L5 System | 12/12 | All 8 functions | Complete coordinated multi-agent |

Musical analogy: note (prompt) -> chord (chain) -> phrase (agent) -> section (agent_group) -> symphony (system). Each level adds dimensions, does not replace.

Biological analogy: cell (prompt) -> tissue (chain) -> organ (agent) -> system (agent_group) -> organism (system). Emergent properties arise from composition, not from summation.

Practical consequence: organization starts with 1-2 LPs for prompts, evolves to 3-4 for agents, and scales to 12/12 for systems — same vocabulary, same tools.

## Patterns

| Trigger | Action |
|---------|--------|
| Building first prompt | Fill P03 (minimum viable) |
| Prompt needs memory | Add P01, evolve to L2 |
| Agent needs tools | Add P04+P05, evolve to L3 |
| System needs coordination | Fill P12, evolve to L5 |
| Diagnosing entity failure | Check which LPs are missing |

## Anti-Patterns

- Creating separate taxonomy for each scale (duplication)
- Skipping levels without filling intermediate LPs
- Assuming more LPs = better (completeness follows need)
- Treating fractal as prescription (it is empirical observation)
- Building L5 system without working L2 agents

## References

- related: p01_kc_cex_maturity_level
- related: p01_kc_cex_boundary_concept
- related: p01_kc_cex_lens_concept

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_learning_package_concept]] | sibling | 0.42 |
| [[p01_kc_cex_maturity_level]] | sibling | 0.41 |
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.28 |
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.27 |
| [[action-prompt-builder]] | downstream | 0.26 |
| [[chain-builder]] | downstream | 0.25 |
| [[prompt-version-builder]] | downstream | 0.24 |
| [[p01_kc_cex_agent_group_concept]] | sibling | 0.24 |
| [[system-prompt-builder]] | downstream | 0.23 |
| [[p01_kc_lp03_prompt]] | sibling | 0.22 |
