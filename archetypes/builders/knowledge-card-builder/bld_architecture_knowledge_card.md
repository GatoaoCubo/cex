---
kind: architecture
id: bld_architecture_knowledge_card
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of knowledge_card — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Knowledge Card"
version: "1.0.0"
author: n03_builder
tags: [knowledge_card, builder, examples]
tldr: "Golden and anti-examples for knowledge card construction, demonstrating ideal structure and common pitfalls."
domain: "knowledge card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - p01_kc_knowledge_card
  - bld_architecture_knowledge_index
  - bld_architecture_citation
  - bld_architecture_rag_source
  - knowledge-card-builder
  - p03_sp_knowledge_card_builder
  - bld_architecture_agent
  - bld_collaboration_knowledge_card
  - bld_architecture_context_doc
  - p01_kc_context_doc
---

## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| title | Short searchable label identifying the fact | author | required |
| body | Distilled atomic fact content, high information density >= 0.8 | author | required |
| domain_tags | Topic labels enabling retrieval routing | author | required |
| card_type | Classification: domain_kc or meta_kc | author | required |
| sources | Origin references for the distilled fact | author | required |
| confidence_score | Reliability rating of the fact (0.0–1.0) | author | required |
| version | Revision counter for fact updates | author | required |
| linked_artifacts | Other cards or artifacts this fact connects to | author | optional |
| expiry_hint | Signal that the fact may become stale after a date | author | optional |
## Dependency Graph
```
rag_source     --produces--> knowledge_card
knowledge_card --queried_by--> knowledge_index
knowledge_index    --injects_into--> system_prompt
knowledge_card --informs--> few_shot_example
knowledge_card --referenced_by--> context_doc
knowledge_card --referenced_by--> agent
```
| From | To | Type | Data |
|------|----|------|------|
| rag_source | knowledge_card | data_flow | raw source text to distill |
| knowledge_card | knowledge_index | data_flow | title, body, tags for BM25 and vector indexing |
| knowledge_index | system_prompt | data_flow | retrieved facts injected into prompt context |
| knowledge_card | few_shot_example | data_flow | factual grounding for input/output pairs |
| knowledge_card | context_doc | data_flow | referenced as supporting evidence |
| knowledge_card | agent | data_flow | linked domain knowledge in agent definition |
## Boundary Table
| knowledge_card IS | knowledge_card IS NOT |
|-------------------|----------------------|
| Atomic searchable fact with density >= 0.8 | Broad reference document without density gate |
| Versioned and source-attributed | Spec for an LLM model or its parameters |
| Classified as domain_kc or meta_kc | Short definition entry (3 lines max) |
| Injected into prompts via retrieval index | External URL pointer without distilled content |
| Max 5KB body (high signal-to-noise) | Input/output demonstration pair |
| Expirable when facts can become stale | Agent identity or behavioral definition |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Identity | title, card_type, version | Name, classify, and version the fact |
| Content | body, confidence_score, expiry_hint | Carry the distilled fact with reliability signal |
| Discoverability | domain_tags, linked_artifacts | Enable retrieval routing and cross-referencing |
| Provenance | sources | Trace the fact back to its origin |
| Consumption | knowledge_index, system_prompt | Retrieve and inject facts into agent context at runtime |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_knowledge_card]] | upstream | 0.34 |
| [[bld_architecture_knowledge_index]] | sibling | 0.33 |
| [[bld_architecture_citation]] | sibling | 0.31 |
| [[bld_architecture_rag_source]] | sibling | 0.30 |
| [[knowledge-card-builder]] | upstream | 0.30 |
| [[p03_sp_knowledge_card_builder]] | upstream | 0.29 |
| [[bld_architecture_agent]] | sibling | 0.27 |
| [[bld_collaboration_knowledge_card]] | downstream | 0.26 |
| [[bld_architecture_context_doc]] | sibling | 0.25 |
| [[p01_kc_context_doc]] | upstream | 0.25 |
