---
kind: memory
id: bld_memory_invariant
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for invariant artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Invariant"
version: "1.0.0"
author: n03_builder
tags: [invariant, builder, examples]
tldr: "Golden and anti-examples for invariant construction, demonstrating ideal structure and common pitfalls."
domain: "invariant construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p03_sp_law_builder
  - bld_collaboration_invariant
  - bld_knowledge_card_invariant
  - p03_ins_law
  - invariant-builder
  - p01_kc_operational_laws
  - bld_architecture_invariant
  - bld_tools_invariant
  - p11_qg_law
  - bld_config_invariant
---
# Memory: invariant-builder
## Summary
Building invariant artifacts requires extreme precision in distinguishing inviolable operational mandates from flexible guidelines. The most common failure mode is producing rules that read like suggestions rather than enforceable mandates. Successful invariant artifacts always include a concrete enforcement mechanism and explicit exception protocol — without these, the artifact degrades into an instruction.
## Pattern
1. Always define the enforcement mechanism before writing the statement — if you cannot enforce it, it is not a law
2. Write the violation section first; it clarifies the boundary between compliance and breach
3. Use imperative mood for the statement field: "All X MUST Y" not "X should Y"
4. Include at least one concrete historical trigger (incident, failure, or mandate source) in the rationale
5. Scope boundaries must be explicit: name which domains, agents, or artifact kinds are covered
6. Exception protocol requires both the condition and the authority that grants the exception
## Anti-Pattern
1. Writing laws that overlap with existing guardrails (P11) — guardrails restrict for safety, laws mandate for operations
2. Using vague enforcement like "review periodically" — enforcement must be machine-checkable or have a named human gate
3. Omitting the conflict resolution priority — when two laws contradict, the system needs a tiebreaker
4. Creating laws from single incidents without pattern validation — one failure is not enough to justify a permanent mandate
5. Frontmatter missing severity or scope fields leading to ambiguous application
## Context
Laws operate in the P08 governance layer alongside patterns, diagrams, and component maps. The key distinction is that laws are non-negotiable — patterns recommend, laws require. Production environments demand laws when repeated failures show that optional guidance is insufficient. Typical triggers: post-incident reviews, compliance requirements, or architectural invariants that must never be violated.
## Impact
Well-formed laws prevent entire categories of recurring failures. A single law with clear enforcement eliminated repeated configuration drift issues across multiple production runs. Poorly formed laws (missing enforcement) were ignored in 60%+ of cases, providing no value while consuming review bandwidth.
## Reproducibility
To reliably produce high-quality invariant artifacts: (1) confirm the rule is truly inviolable, not just preferred, (2) draft enforcement mechanism first, (3) write violation examples from real incidents, (4) validate scope covers all affected domains without over-reach, (5) run through all 9 HARD gates before delivery.
## References
1. invariant-builder SCHEMA.md (19+ frontmatter fields, 8 body sections)
2. P08 governance pillar documentation
3. Operational governance design patterns

## Metadata

```yaml
id: bld_memory_invariant
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-invariant.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | invariant construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_law_builder]] | upstream | 0.48 |
| [[bld_collaboration_invariant]] | upstream | 0.47 |
| [[bld_knowledge_card_invariant]] | upstream | 0.46 |
| [[p03_ins_law]] | upstream | 0.41 |
| [[invariant-builder]] | upstream | 0.40 |
| [[p01_kc_operational_laws]] | upstream | 0.34 |
| [[bld_architecture_invariant]] | upstream | 0.34 |
| [[bld_tools_invariant]] | upstream | 0.33 |
| [[p11_qg_law]] | downstream | 0.32 |
| [[bld_config_invariant]] | upstream | 0.32 |
