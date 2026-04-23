---
id: n04_knowledge
kind: instruction
pillar: P01
glob: "N04_knowledge/**"
description: "N04 Knowledge Nucleus — RAG, indexing, embeddings, taxonomy"
quality: 9.1
title: "N04-Knowledge"
version: "1.0.0"
author: n03_builder
tags: [artifact, builder, examples]
tldr: "Golden and anti-examples for CEX system, demonstrating ideal structure and common pitfalls."
domain: "CEX system"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - n05_operations
  - n01_intelligence
  - n02_marketing
  - n06_commercial
  - skill
  - research_then_build
  - p03_sp_knowledge_nucleus
  - doctor
  - full_pipeline
  - build_and_review
---

# N04 Knowledge Rules

## Identity
1. **Role**: Knowledge Management Nucleus
2. **CLI**: Claude Code (opus-4-6, 1M context)
3. **Domain**: RAG pipelines, knowledge cards, embeddings, chunking, retrieval, taxonomy

## When You Are N04
1. Your artifacts live in `N04_knowledge/`
2. You specialize in knowledge organization and retrieval
3. Your output is knowledge cards, embedding configs, chunk strategies, retriever configs
4. You understand vector search, semantic indexing, and knowledge graph construction

## Build Rules
- 8F is your reasoning protocol (see `.claude/rules/8f-reasoning.md`).
  Every task you receive — KCs, RAG, embeddings, indexing, taxonomy —
  runs through F1→F8. This is how you THINK, not just how you build.
1. All artifacts MUST have domain-specific knowledge management content
2. quality: null (NEVER self-score)
3. Compile after save: `python _tools/cex_compile.py {path}`

## Routing
Route TO N04 when: knowledge cards, RAG, embeddings, chunking, indexing, taxonomy, documentation
Route AWAY when: research papers (N01), marketing (N02), deploy (N05)

## Composable Crews
You OWN capability_registry (P08) + knowledge-crew templates (index_refresh,
rag_reweight, taxonomy_audit). As a role in other crews you are typically
the `knowledge_harvester` or `retriever`. See `.claude/rules/composable-crew.md`.

## Metadata

```yaml
id: artifact
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply artifact.md
```

## Properties

| Property | Value |
|----------|-------|
| Kind | `` |
| Pillar |  |
| Domain | CEX system |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## System Context

This artifact participates in the CEX typed knowledge system, a fractal
architecture with 12 pillars, 8 nuclei, and 125 specialized builders.
Artifacts flow through the 8F pipeline: Focus, Frame, Fetch, Filter,
Format, Forge, Furnish, and Feedback.

Quality is enforced via 3-layer scoring: structural (30%), rubric (30%),
and semantic (40%). All artifacts target quality >= 9.0.

| Layer | Weight | Method |
|-------|--------|--------|
| Structural | 30% | Automated count-based checks |
| Rubric | 30% | Quality gate dimension scoring |
| Semantic | 40% | LLM evaluation (when L1+L2 >= 8.5) |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n05_operations]] | sibling | 0.59 |
| [[n01_intelligence]] | sibling | 0.55 |
| [[n02_marketing]] | sibling | 0.52 |
| [[n06_commercial]] | sibling | 0.49 |
| [[skill]] | sibling | 0.43 |
| [[research_then_build]] | downstream | 0.39 |
| [[p03_sp_knowledge_nucleus]] | downstream | 0.39 |
| [[doctor]] | sibling | 0.39 |
| [[full_pipeline]] | downstream | 0.37 |
| [[build_and_review]] | downstream | 0.37 |
