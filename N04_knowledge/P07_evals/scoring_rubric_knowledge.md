---
id: p07_rubric_knowledge
kind: scoring_rubric
pillar: P07
title: "N04 Scoring Rubric — Knowledge Card Quality"
version: 4.0.0
created: 2026-03-31
author: n07_orchestrator
domain: knowledge-management
quality: 9.0
tags: [scoring_rubric, n04, knowledge, density, taxonomy]
tldr: "5-dimension scoring for KCs: density, taxonomy, actionability, structure, freshness."
density_score: 0.92
related:
  - p11_qg_knowledge
  - p07_sr_knowledge_eval
  - p07_rubric_intelligence
  - p01_kc_artifact_quality_evaluation_methods
  - bld_knowledge_card_knowledge_card
  - bld_examples_scoring_rubric
  - p07_sr_5_dimension_quality
  - bld_schema_kind
  - p01_kc_creation_best_practices
  - p07_sr_5d_scoring
---

# N04 Scoring Rubric

| Dimension | Weight | 1-3 (Weak) | 4-6 (Adequate) | 7-9 (Strong) | 10 (Exceptional) |
|-----------|--------|-----------|----------------|--------------|-------------------|
| Density | 25% | Filler prose, low signal | Some useful info mixed with padding | Dense, minimal waste | Every token carries unique information |
| Taxonomy | 20% | Wrong kind or pillar | Correct kind, vague domain | Precise kind + pillar + domain | Perfect classification with cross-refs |
| Actionability | 25% | Theory only | Some when-to-use guidance | Clear when/when-not + examples | Decision-ready with anti-patterns |
| Structure | 15% | Unformatted prose | Headers + some sections | Full frontmatter + tables + sections | Template-perfect, triple-export ready |
| Freshness | 15% | >1 year, no context | <6 months | <90 days, versioned | Current + trend context + update plan |

## Quick Reference

**30-second scoring checklist**:
- [ ] **Density**: More tables than paragraphs? No filler words? → 7+
- [ ] **Taxonomy**: Correct `kind:` field? Domain-specific? → 7+
- [ ] **Actionability**: Has "when to use" + "when NOT to use"? → 7+
- [ ] **Structure**: Complete frontmatter + `##` sections + tables? → 7+
- [ ] **Freshness**: <90 days old? Version number? → 7+

**Decision tree**: 5×Yes = 9+, 4×Yes = 8+, 3×Yes = 7+, <3×Yes = revise

## Usage Guidelines

**When to apply**: Score every knowledge card before publication. Use during peer review cycles.

**How to score**:
- Read entire KC first (no skimming)
- Score each dimension independently
- Weight final score: `(Density×0.25) + (Taxonomy×0.20) + (Actionability×0.25) + (Structure×0.15) + (Freshness×0.15)`
- Threshold: Publish ≥8.0, Revise 6.0-7.9, Reject <6.0

**Common scoring errors**:
- Inflating scores for "effort" (score output, not input)
- Averaging all dimensions equally (use weights)
- Scoring outdated content as "fresh" if recently edited

## Scoring Examples

**Density 10**: "Use Redis for session storage. TTL=3600s. Keys: `user:{id}:session`" vs **Density 4**: "Redis is a popular in-memory database that many developers use for various caching scenarios including session management which can improve application performance."

**Taxonomy 10**: `kind: rag_source, pillar: P04, domain: vector-search` with cross-refs vs **Taxonomy 4**: `kind: document, pillar: P01, domain: general`

**Actionability 10**: "Use when: >10K docs, complex queries. Don't use when: <100 docs, simple search. Anti-pattern: Vector search for exact matches" vs **Actionability 4**: "Vector search is useful for finding similar documents"

**Structure 10**: Complete frontmatter + `## When`, `## How`, `## Examples` + tables vs **Structure 4**: Paragraph text with minimal headers

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p11_qg_knowledge]] | downstream | 0.26 |
| [[p07_sr_knowledge_eval]] | sibling | 0.26 |
| [[p07_rubric_intelligence]] | sibling | 0.24 |
| [[p01_kc_artifact_quality_evaluation_methods]] | upstream | 0.22 |
| [[bld_knowledge_card_knowledge_card]] | upstream | 0.21 |
| [[bld_examples_scoring_rubric]] | related | 0.21 |
| [[p07_sr_5_dimension_quality]] | sibling | 0.21 |
| [[bld_schema_kind]] | upstream | 0.21 |
| [[p01_kc_creation_best_practices]] | upstream | 0.20 |
| [[p07_sr_5d_scoring]] | sibling | 0.19 |
