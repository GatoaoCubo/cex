---
id: p12_dr_knowledge
kind: dispatch_rule
8f: F8_collaborate
pillar: P12
version: 1.0.0
created: 2026-04-02
updated: 2026-04-02
author: codex
domain: knowledge
quality: 9.0
tags: [dispatch, knowledge, rag, indexing, knowledge-engine, P12]
tldr: Route knowledge architecture, RAG, indexing, and documentation tasks to knowledge-engine
scope: knowledge
keywords: [knowledge, conhecimento, rag, indexar, indexing, retrieval, recuperação, documentation, docs, embedding, chunking, taxonomy]
agent_group: knowledge-engine
model: sonnet
priority: 7
confidence_threshold: 0.72
fallback: researcher
conditions:
  exclude_domains: [market_research, competitor_analysis, code_review]
routing_strategy: hybrid
density_score: 1.0
related:
  - n04_dr_knowledge
  - p01_kc_dispatch_rule
  - n04_knowledge
  - bld_examples_dispatch_rule
  - p08_kc_capability_registry
  - agent_card_n04
  - bld_instruction_dispatch_rule
  - p12_dr_admin_orchestration
  - bld_knowledge_card_dispatch_rule
  - n04_kc_knowledge_management
---
# knowledge Dispatch Rule

## Routing Triad
| Layer | Value |
|-------|-------|
| Trigger | keywords ∩ input ≥ 1 match AND confidence ≥ 0.72 |
| Target | knowledge-engine (sonnet, priority 7) |
| Fallback | researcher (confidence < 0.72 or knowledge-engine unavailable) |

## Keywords
| Group | Terms |
|-------|-------|
| Core PT | conhecimento, indexar, recuperação, taxonomia |
| Core EN | knowledge, indexing, retrieval, taxonomy |
| RAG/Vector | rag, embedding, chunking |
| Documentation | documentation, docs |

Bilingual PT/EN coverage fires on both Portuguese operator commands and English task descriptions. `rag`, `embedding`, `chunking` catch specialized sub-tasks. Generic terms (`docs`, `knowledge`) are scoped by `exclude_domains` to prevent false matches from research or code-review domains.

## Priority
Priority 7 (high) — knowledge management is a core pipeline function. Adjacent rule `p12_dr_research` holds priority 8; when input contains both research signals (`analise`, `benchmark`) and knowledge signals (`indexar`, `rag`), the research rule wins. Pure indexing and RAG requests resolve exclusively to this rule.

## Fallback
researcher handles knowledge requests when knowledge-engine is unavailable; it can summarize, chunk, and synthesize content without full knowledge-graph tooling. researcher is a distinct agent_group — no self-fallback.

## Cross-Reference
- **Upstream**: orchestrator, workflow tasks with knowledge, RAG, or documentation intent
- **Downstream**: knowledge-engine → produces knowledge cards, embedding configs, chunk strategies, retriever configs (N04 outputs)
- **Adjacent rule**: `p12_dr_research` (priority 8) — overlapping fallback chain; resolved by keyword specificity and priority rank

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n04_dr_knowledge]] | sibling | 0.33 |
| [[p01_kc_dispatch_rule]] | related | 0.32 |
| [[n04_knowledge]] | upstream | 0.31 |
| [[bld_examples_dispatch_rule]] | upstream | 0.30 |
| [[p08_kc_capability_registry]] | upstream | 0.28 |
| [[agent_card_n04]] | upstream | 0.28 |
| [[bld_instruction_dispatch_rule]] | upstream | 0.28 |
| [[p12_dr_admin_orchestration]] | sibling | 0.28 |
| [[bld_knowledge_card_dispatch_rule]] | upstream | 0.27 |
| [[n04_kc_knowledge_management]] | related | 0.27 |
