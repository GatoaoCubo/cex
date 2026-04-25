---
id: p01_kc_cex_type_artifact
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX Type Artifacts — 78 Named Units with Contract, Boundary and Schema"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.1
tags: [cex, type, artifact, contract, boundary, schema, naming]
tldr: "78 CEX types are atomic contracts: each has function, LP, layer, maximum size and standardized naming"
when_to_use: "Consult the complete vocabulary of CEX types and their contracts"
keywords: [type-artifact, contract, boundary, schema, naming-convention]
long_tails:
  - "How many artifact types does CEX define and how are they organized"
  - "How does a CEX type contract work"
axioms:
  - "ALWAYS check if CEX type exists before creating nomenclature"
  - "NEVER create artifact without explicit boundary and schema"
linked_artifacts:
  primary: p01_kc_cex_taxonomy
  related: [p01_kc_cex_llm_function_concept, p01_kc_cex_learning_package_concept]
density_score: null
data_source: "https://arxiv.org/abs/2308.00352"
related:
  - p01_kc_cex_taxonomy
  - p01_kc_cex_boundary_concept
  - p01_kc_lp06_schema
  - p01_kc_lp05_output
  - p01_kc_cex_learning_package_concept
  - p01_kc_cex_lp01_knowledge
  - p01_kc_cex_function_become
  - p01_kc_cex_function_inject
  - p01_kc_cex_function_govern
  - p01_kc_cex_lp05_output
---

## Summary

CEX types are the 78 atomic units of the vocabulary -- the smallest element with its own semantics and independent identity. Each type is a contract: defines primary LLM function, primary LP, layer (content/spec/prompt/runtime/governance), maximum size and naming convention prefixed by the LP. When something is typed as knowledge_card, it is known: atomic fact, function INJECT, LP P01, max 5KB, density >= 0.8.

## Spec

| LP | Example Types | Count | Layer |
|----|---------------|-----|--------|
| P01 Knowledge | knowledge_card, embedding, glossary | 7 | content |
| P02 Model | agent, persona, mental_model, model_card | 6 | spec |
| P03 Prompt | system_prompt, instruction, hop | 8 | prompt |
| P04 Tools | tool, skill, mcp_server | 5 | runtime |
| P05 Output | report, code, copy, artifact | 7 | content |
| P06 Schema | schema, blueprint, template | 6 | spec |
| P07 Evals | quality_gate, benchmark, test | 7 | governance |
| P08 Architecture | pattern, law, component_map | 6 | spec |
| P09 Config | config, boot_config, env | 5 | runtime |
| P10 Memory | memory, session_log, context | 6 | runtime |
| P11 Feedback | feedback, review, signal | 5 | governance |
| P12 Orchestration | workflow, handoff, dispatch | 10 | runtime |

Contract per type: (1) primary LLM function, (2) primary LP, (3) layer, (4) maximum size, (5) naming `{lp_code}_{type}_{slug}.md`.

Five layers: content (data), spec (definitions), prompt (instructions), runtime (execution), governance (control).

## Patterns

| Trigger | Action |
|---------|--------|
| New artifact created | Check CEX type and use naming convention |
| Artifact without clear boundary | Define layer + maximum size |
| Type not found in the 78 | Check if it is a variant of existing type |
| Framework migration | Map proprietary types to CEX types |
| Artifact validation | Check contract: function + LP + layer |

## Code

<!-- lang: python | purpose: type contract definition -->
```python
TYPE_CONTRACT = {
    "knowledge_card": {
        "function": "INJECT",
        "lp": "P01",
        "layer": "content",
        "max_bytes": 5120,
        "naming": "p01_kc_{slug}.md",
        "density_min": 0.8,
    },
}
# 78 tipos, cada um com este contrato
# naming = {lp_code}_{type_abbrev}_{slug}.md
```

## Anti-Patterns

- Creating artifact without defined CEX type (orphan artifact)
- Inventing new type without checking the existing 78
- Ignoring naming convention (breaks indexing and search)
- Type without maximum size (infinite artifacts = noise)
- Confusing layer with LP (layer = nature, LP = dimension)

## References

- source: https://arxiv.org/abs/2308.00352
- related: p01_kc_cex_taxonomy
- related: p01_kc_cex_llm_function_concept
- related: p01_kc_cex_learning_package_concept

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_taxonomy]] | sibling | 0.34 |
| [[p01_kc_cex_boundary_concept]] | sibling | 0.32 |
| [[p01_kc_lp06_schema]] | sibling | 0.24 |
| [[p01_kc_lp05_output]] | sibling | 0.22 |
| [[p01_kc_cex_learning_package_concept]] | sibling | 0.22 |
| [[p01_kc_cex_lp01_knowledge]] | sibling | 0.22 |
| [[p01_kc_cex_function_become]] | sibling | 0.21 |
| [[p01_kc_cex_function_inject]] | sibling | 0.21 |
| [[p01_kc_cex_function_govern]] | sibling | 0.19 |
| [[p01_kc_cex_lp05_output]] | sibling | 0.19 |
