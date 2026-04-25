---
id: p01_kc_cex_learning_package_concept
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Learning Packages — 12 Dimensions That Define Any LLM Entity"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, learning-package, dimensions, lp, entity-model]
tldr: "12 LPs are dimensions (not categories) that define any LLM entity -- from prompt (1 LP) to agent_group (12 LPs)"
when_to_use: "Understand the 12 dimensions of an LLM entity and how LPs intersect with functions"
keywords: [learning-package, dimensions, entity, orthogonality, completeness]
long_tails:
  - "What is the difference between Learning Package and artifact category"
  - "How the 12 LPs relate to the 8 LLM functions"
axioms:
  - "ALWAYS treat LPs as orthogonal dimensions, not folders"
  - "NEVER confuse LP (what entity HAS) with function (what LLM DOES)"
linked_artifacts:
  primary: p01_kc_cex_taxonomy
  related: [p01_kc_cex_llm_function_concept, p01_kc_cex_type_artifact]
density_score: null
data_source: "https://arxiv.org/abs/2308.00352"
related:
  - p01_kc_cex_fractal_architecture
  - p01_kc_cex_maturity_level
  - p01_kc_cex_llm_function_concept
  - p01_kc_cex_pipeline_execution
  - p01_kc_cex_taxonomy
  - p01_kc_cex_agent_group_concept
  - p01_kc_cex_type_artifact
  - bld_architecture_memory_architecture
  - p01_kc_cex_function_become
  - p01_kc_lp02_model
---

## Summary

Learning Packages (LPs) are the 12 dimensions that define any LLM entity. They are not artifact categories -- they are QUESTIONS. P01 asks "what does it know?", P02 "who is it?", P03 "how does it speak?". A prompt fills 1 LP (P03). An agent fills 3-4. An agent_group fills all 12. The difference between entities is dimensionality, not nature. LPs are orthogonal to functions: LP = what the entity HAS, function = what the LLM DOES.

## Spec

| LP | Name | Question | Dominant Function |
|----|------|----------|-------------------|
| P01 | Knowledge | What does it know? | INJECT |
| P02 | Model | Who is it? | BECOME |
| P03 | Prompt | How does it speak? | REASON + CONSTRAIN |
| P04 | Tools | What does it use? | CALL |
| P05 | Output | What does it deliver? | CONSTRAIN |
| P06 | Schema | What contracts? | CONSTRAIN + GOVERN |
| P07 | Evals | How to measure? | GOVERN |
| P08 | Architecture | How does it scale? | BECOME + GOVERN |
| P09 | Config | How to configure? | GOVERN |
| P10 | Memory | What does it remember? | INJECT |
| P11 | Feedback | How does it improve? | GOVERN |
| P12 | Orchestration | How does it coordinate? | COLLABORATE |

Orthogonality: each CEX type has 1 primary LP and 1 primary function. LP classifies by entity dimension. Function classifies by pipeline stage. The two classifications are independent and complementary.

## Patterns

| Trigger | Action |
|---------|--------|
| Entity without memory between sessions | Add LP P10 (Memory) |
| Agent with inconsistent output | Check LP P05 (Output) and P06 (Schema) |
| System without quality gates | Implement LP P07 (Evals) |
| New agent created | Fill P02 (Model) + P03 (Prompt) minimum |
| Complete agent_group needed | Ensure all 12 LPs filled |

## Code

<!-- lang: python | purpose: LP dimensionality of an entity -->
```python
ENTITY_LPS = {
    "prompt":    {"P03": True},                    # 1 LP
    "agent":     {"P02": True, "P03": True,
                  "P04": True, "P10": True},       # 4 LPs
    "agent_group": {f"P{i:02d}": True
                  for i in range(1, 13)},          # 12 LPs
}
# completude = len(filled_lps) / 12
# prompt = 8%, agente = 33%, agent_group = 100%
```

## Anti-Patterns

- Treating LPs as filesystem folders (they are dimensions)
- Confusing LP with function (HAS vs DOES)
- Creating entity without P02+P03 minimum (no identity)
- Filling LPs in numerical order (order is semantic)
- Ignoring LP x function orthogonality in classification

## References

- source: https://arxiv.org/abs/2308.00352
- related: p01_kc_cex_taxonomy
- related: p01_kc_cex_llm_function_concept
- related: p01_kc_cex_type_artifact

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_fractal_architecture]] | sibling | 0.40 |
| [[p01_kc_cex_maturity_level]] | sibling | 0.33 |
| [[p01_kc_cex_llm_function_concept]] | sibling | 0.31 |
| [[p01_kc_cex_pipeline_execution]] | sibling | 0.30 |
| [[p01_kc_cex_taxonomy]] | sibling | 0.29 |
| [[p01_kc_cex_agent_group_concept]] | sibling | 0.26 |
| [[p01_kc_cex_type_artifact]] | sibling | 0.26 |
| [[bld_architecture_memory_architecture]] | downstream | 0.24 |
| [[p01_kc_cex_function_become]] | sibling | 0.23 |
| [[p01_kc_lp02_model]] | sibling | 0.23 |
