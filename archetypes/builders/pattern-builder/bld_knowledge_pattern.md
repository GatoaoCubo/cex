---
kind: knowledge_card
id: bld_knowledge_card_pattern
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for pattern production — atomic searchable facts
sources: pattern-builder MANIFEST.md + SCHEMA.md, GoF 1994, Alexander 1977, POSA 1996
quality: 9.1
title: "Knowledge Card Pattern"
version: "1.0.0"
author: n03_builder
tags: [pattern, builder, examples]
tldr: "Golden and anti-examples for pattern construction, demonstrating ideal structure and common pitfalls."
domain: "pattern construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p11_qg_pattern
  - bld_memory_pattern
  - p03_ins_pattern
  - p03_sp_pattern_builder
  - p01_kc_pattern
  - bld_schema_pattern
  - pattern-builder
  - bld_architecture_pattern
  - bld_collaboration_pattern
  - bld_config_pattern
---

# Domain Knowledge: pattern
## Executive Summary
Patterns are named, reusable solutions to recurring problems in a given context. Each pattern documents opposing forces that make simple solutions inadequate, a concrete solution at implementation level, and consequences including negative trade-offs. They differ from laws (which mandate compliance), workflows (which execute step sequences), diagrams (which visualize), and instructions (which tell how) by being descriptive documentation of proven solutions with explicit forces and trade-offs.
## Spec Table
| Property | Value |
|----------|-------|
| Pillar | P08 (architecture) |
| Kind | `pattern` (exact literal) |
| ID pattern | `p08_pat_{slug}` |
| Required frontmatter | 21 fields |
| Quality gates | 9 HARD + 11 SOFT |
| Max body | 4096 bytes |
| Density minimum | >= 0.80 |
| Quality field | always `null` |
| Min forces | 2 (opposing tensions) |
| Min consequences (negative) | 1 trade-off |
| Min examples | 2 concrete applications |
| Name format | 2-5 words, title-case, self-describing |
## Patterns
| Pattern | Application |
|---------|-------------|
| Context-first structure | Problem and forces BEFORE solution — readers need tension before resolution |
| Opposing forces | At least 2 tensions that make simple solutions fail |
| Concrete solution | Implementation-level approach, not abstract advice |
| Honest consequences | Benefits AND costs — benefits-only is marketing |
| Composable references | Cross-reference related patterns with stated relationship |
| Anti-pattern documentation | Document what looks similar but fails |
| Applicability boundaries | State both when-to-use AND when-not-to-use |
## Anti-Patterns
| Anti-Pattern | Why it fails |
|-------------|-------------|
| Problem without recurrence signal | One-off fixes are not patterns; need "repeatedly/often/whenever" |
| Solution as abstract advice ("use better design") | Not implementation-level; cannot be applied |
| Forces < 2 | No opposing tensions = no pattern, just a preference |
| Consequences with no negative trade-off | Benefits-only = marketing, not engineering |
| Name > 5 words or not self-describing | Pattern names must be memorable and context-free |
| Missing anti-pattern section | Similar wrong approaches must be documented |
| No concrete examples | Unproven pattern; need >= 2 real applications |
## Application
1. Name the pattern: 2-5 words, title-case, self-describing without context
2. Describe the recurring problem with a recurrence signal word
3. Document >= 2 opposing forces that make the problem hard
4. Describe the solution at implementation level
5. List consequences: both benefits AND >= 1 negative trade-off
6. Add >= 2 concrete examples from real application
7. Document anti-patterns (similar wrong approaches)
8. Cross-reference related patterns
9. Validate: 9 HARD + 11 SOFT gates, body <= 4096 bytes
## References
- pattern-builder SCHEMA.md v1.0.0
- Alexander, C. (1977) A Pattern Language
- Gamma et al. (1994) Design Patterns (GoF)
- Buschmann et al. (1996) Pattern-Oriented Software Architecture (POSA)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_pattern]] | downstream | 0.54 |
| [[bld_memory_pattern]] | downstream | 0.48 |
| [[p03_ins_pattern]] | downstream | 0.47 |
| [[p03_sp_pattern_builder]] | downstream | 0.43 |
| [[p01_kc_pattern]] | sibling | 0.38 |
| [[bld_schema_pattern]] | downstream | 0.38 |
| [[pattern-builder]] | downstream | 0.37 |
| [[bld_architecture_pattern]] | downstream | 0.36 |
| [[bld_collaboration_pattern]] | downstream | 0.35 |
| [[bld_config_pattern]] | downstream | 0.32 |
