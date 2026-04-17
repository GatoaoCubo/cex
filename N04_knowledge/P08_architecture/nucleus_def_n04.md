---
id: p02_nd_n04.md
kind: nucleus_def
pillar: P02
nucleus_id: N04
role: knowledge
sin_lens: "Knowledge Gluttony (Gula do Conhecimento)"
cli_binding: claude
model_tier: sonnet
model_specific: claude-sonnet-4-6
context_tokens: 200000
boot_script: boot/n04.ps1
agent_card_path: N04_knowledge/agent_card_n04.md
pillars_owned:
  - P10
crew_templates_exposed:
  - index_refresh
  - rag_reweight
  - taxonomy_audit
domain_agents:
  - agent_librarian
  - agent_indexer
fallback_cli: codex
title: "Nucleus Def N04"
version: "1.0.0"
author: n07_crewwiring
domain: "knowledge organization, RAG, embeddings, indexing"
quality: 8.9
tags: [nucleus_def, n04, knowledge, composable]
tldr: "N04 is the knowledge nucleus: RAG, KCs, embeddings, taxonomy, retrieval. Also owns capability_registry (P08)."
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
---

## Identity

| Field | Value |
|-------|-------|
| Nucleus ID | N04 |
| Role | knowledge |
| Sin Lens | Knowledge Gluttony (Gula do Conhecimento) |
| CLI Binding | claude |
| Model Tier | sonnet |
| Model | claude-sonnet-4-6 |
| Context | 200K tokens |
| Boot Script | `boot/n04.ps1` |
| Agent Card | `N04_knowledge/agent_card_n04.md` |

## Pillars Owned

| Pillar | Domain | Sample Kinds |
|--------|--------|--------------|
| P10 | memory | knowledge_index, memory_scope, entity_memory |
| P08 (shared) | architecture | capability_registry |

## Crew Templates Exposed

| Template | Role in Crew | Inputs | Outputs |
|----------|--------------|--------|---------|
| index_refresh | indexer | new artifacts | refreshed TF-IDF index |
| rag_reweight | retriever | scored queries | reweighted embeddings |
| taxonomy_audit | librarian | gap report | taxonomy update |

## Domain Agents

| Agent | Purpose | Path |
|-------|---------|------|
| agent_librarian | Taxonomy coherence | `N04_knowledge/P02_model/` |
| agent_indexer | Retrieval index maintenance | `N04_knowledge/P02_model/` |

## Boot Contract

- Boot file: `boot/n04.ps1`
- Task source: `.cex/runtime/handoffs/n04_task.md`
- Signal: `write_signal('n04', 'complete', {score})`

## Composability

| Direction | Nucleus | What Flows |
|-----------|---------|-----------|
| outbound | all | capability_registry + retriever indexes |
| outbound | N03 | kind KCs + taxonomy gaps |
| inbound | N01 | research to index |
| inbound | N07 | knowledge handoffs |
