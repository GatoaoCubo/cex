---
id: p01_kc_meta_construction
kind: knowledge_card
pillar: P01
title: Knowledge Card -- Meta-Construction
version: 2.0.0
created: 2026-03-30
updated: 2026-03-30
author: builder_agent
domain: meta-construction
quality: 9.1
tags: [knowledge-card, builder, N03, meta-construction]
tldr: What meta-construction is -- building the artifacts that build artifacts.
when_to_use: Designing builders, templates, quality gates, or new kinds.
keywords: [meta-construction, builder, factory, strange-loop, 8F]
feeds_kinds: [agent, system_prompt, workflow, quality_gate]
density_score: 0.90
related:
  - kind-builder
  - bld_architecture_kind
  - bld_collaboration_kind
  - bld_collaboration_knowledge_card
  - bld_collaboration_builder
  - bld_instruction_kind
  - p10_lr_builder-builder
  - p03_pt_builder_construction
  - p03_sp_n03_creation_nucleus
  - agent_card_n03
---

# Meta-Construction

## Definition

Meta-construction builds the tools, templates, and processes that produce artifacts,
rather than building artifacts directly. N03 builds builders, not products.

## When to Use

- Designing a new kind of artifact
- Creating builders, templates, or quality gates
- Bootstrapping a new nucleus
- Improving the 8F pipeline itself

## Boundaries

| Is Meta-Construction | Is NOT |
|---------------------|--------|
| Building an agent builder | Building an agent for a client |
| Designing a workflow template | Running a specific workflow |
| Creating a quality gate | Scoring an existing artifact |
| Registering a new kind | Creating an instance of a kind |

## Key Concepts

- **8F Pipeline**: 8-step process (CONSTRAIN through COLLABORATE)
- **Builder ISOs**: 13 files per kind teaching how to construct it
- **Kind KC**: Knowledge card describing what a kind IS
- **Crew Composition**: Multi-builder teams for complex construction
- **Strange Loop**: N03 builds itself using its own pipeline
- **Open Variables**: {{mustache}} syntax for consumer-filled values

## Anti-Patterns

- Building without loading builder ISOs first
- Skipping quality gates to save time
- Hardcoding values that should be {{open_variables}}
- Creating kinds without registering in kinds_meta.json


## Engineering Knowledge Card Standards

Knowledge cards in the engineering domain follow stricter structural requirements:

- **One concept per card**: scope creep triggers mandatory split into child cards
- **Executable examples**: every engineering KC includes at least one runnable snippet
- **Version-aware**: cards reference specific tool versions and deprecation timelines
- **Cross-linked**: explicit id-based references to related cards enable graph traversal

### Retrieval Optimization

```yaml
# Knowledge card indexing config
indexing:
  method: tf_idf
  min_tags: 3
  max_tags: 8
  density_threshold: 0.6
  embedding_model: local
  refresh_on_update: true
```

| Field | Purpose | Impact on Retrieval |
|-------|---------|-------------------|
| tags | Primary keyword matching | High - drives TF-IDF ranking |
| tldr | Summary for quick scan | Medium - used in result preview |
| domain | Namespace isolation | High - filters search scope |
| density_score | Content richness metric | Low - quality indicator only |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[kind-builder]] | downstream | 0.34 |
| [[bld_architecture_kind]] | downstream | 0.32 |
| [[bld_collaboration_kind]] | downstream | 0.30 |
| [[bld_collaboration_knowledge_card]] | downstream | 0.29 |
| [[bld_collaboration_builder]] | downstream | 0.26 |
| [[bld_instruction_kind]] | downstream | 0.25 |
| [[p10_lr_builder-builder]] | downstream | 0.24 |
| [[p03_pt_builder_construction]] | downstream | 0.24 |
| [[p03_sp_n03_creation_nucleus]] | downstream | 0.23 |
| [[agent_card_n03]] | related | 0.23 |
