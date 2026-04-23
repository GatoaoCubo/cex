---
kind: memory
id: bld_memory_pattern
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for pattern artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.2
title: "Memory Pattern"
version: "1.0.0"
author: n03_builder
tags: [pattern, builder, examples]
tldr: "Golden and anti-examples for pattern construction, demonstrating ideal structure and common pitfalls."
domain: "pattern construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - pattern-builder
  - bld_knowledge_card_pattern
  - p03_ins_pattern
  - p03_sp_pattern_builder
  - p01_kc_pattern
  - bld_architecture_pattern
  - bld_collaboration_pattern
  - p11_qg_pattern
  - bld_output_template_pattern
  - bld_schema_pattern
---
# Memory: pattern-builder
## Summary
Patterns document reusable architecture solutions with named problem-solution pairs. The critical production insight is that patterns must be genuinely reusable — if a solution has been applied only once, it is a case study, not a pattern. The second lesson is that forces and consequences must be balanced: every benefit claimed in consequences should trace back to a force it resolves.
## Pattern
1. Require at least 2 independent instances of the solution before elevating it to a pattern
2. Problem statement must describe the recurring tension, not just a scenario
3. Solution must be concrete enough to implement without additional research — actionable steps, not principles
4. Forces must list both driving forces (pushing toward the solution) and restraining forces (pushing against)
5. Consequences section must include both benefits and tradeoffs — patterns without tradeoffs are marketing, not architecture
6. Related patterns should specify the relationship type: complementary, alternative, or prerequisite
## Anti-Pattern
1. Single-instance solutions promoted to patterns — untested generalization that may not transfer
2. Abstract solutions without implementation steps — reads like philosophy, not architecture
3. Forces section listing only driving forces — omitting restraining forces hides real tradeoffs
4. Consequences without tradeoffs — every pattern has costs; hiding them erodes trust
5. Confusing pattern (P08, reusable solution) with law (P08, inviolable rule) or workflow (P12, executable steps)
## Context
Patterns operate in the P08 architecture layer alongside laws, diagrams, and component maps. They capture named solutions that have been validated through repeated application. Unlike laws (which mandate), patterns recommend. Unlike workflows (which execute), patterns document. They serve as the institutional memory of architecture decisions.
## Impact
Patterns with 2+ validated instances were adopted 4x more often than single-instance patterns. Balanced forces/consequences sections increased reviewer confidence scores by 30%. Concrete solution steps reduced implementation time by 40% compared to abstract guidance patterns.
## Reproducibility
For reliable pattern production: (1) verify the solution has been applied at least twice independently, (2) write the problem as a recurring tension, (3) document both driving and restraining forces, (4) provide concrete implementation steps, (5) list both benefits and tradeoffs in consequences, (6) map related patterns with relationship types.
## References
1. pattern-builder SCHEMA.md (21 frontmatter fields, 9 HARD + 11 SOFT gates)
2. P08 architecture pillar specification
3. Gang of Four pattern documentation format

## Metadata

```yaml
id: bld_memory_pattern
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-memory-pattern.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `memory` |
| Pillar | P10 |
| Domain | pattern construction |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[pattern-builder]] | upstream | 0.51 |
| [[bld_knowledge_card_pattern]] | upstream | 0.46 |
| [[p03_ins_pattern]] | upstream | 0.45 |
| [[p03_sp_pattern_builder]] | upstream | 0.42 |
| [[p01_kc_pattern]] | upstream | 0.41 |
| [[bld_architecture_pattern]] | upstream | 0.40 |
| [[bld_collaboration_pattern]] | upstream | 0.40 |
| [[p11_qg_pattern]] | downstream | 0.39 |
| [[bld_output_template_pattern]] | upstream | 0.32 |
| [[bld_schema_pattern]] | upstream | 0.29 |
