---
id: n00_agentic_rag_manifest
kind: knowledge_card
pillar: P01
nucleus: n00
title: "Agentic RAG -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, agentic_rag, p01, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P01 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Agentic RAG defines an agent-driven retrieval augmented generation pattern where an AI agent actively decides when, what, and how to retrieve before generating. Unlike passive RAG pipelines, the agent controls retrieval strategy, source selection, and follow-up queries dynamically. It produces a reusable architectural blueprint for agent-controlled retrieval workflows.

## Pillar
P01 -- Knowledge

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `agentic_rag` |
| pillar | string | yes | Always `P01` |
| title | string | yes | Human-readable pattern name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| retrieval_strategy | enum | yes | pull\|push\|hybrid -- how agent triggers retrieval |
| agent_loop | string | yes | ReAct\|Plan-Act\|Reflexion -- agent reasoning loop |
| max_iterations | int | no | Maximum retrieval rounds before fallback |
| sources | list | yes | List of rag_source references |
| reranker | string | no | reranker_config reference if used |

## When to use
- When retrieval logic is too complex for a fixed pipeline (multi-hop, conditional)
- When the agent needs to decide dynamically which sources to query
- When iterative retrieval and refinement is required (self-correcting RAG)

## Builder
`archetypes/builders/agentic_rag-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind agentic_rag --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this (typically N01 or N04)
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this retrieval pattern serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context for retrieval

## Example (minimal)
```yaml
---
id: agentic_rag_support_kb
kind: agentic_rag
pillar: P01
nucleus: n04
title: "Support KB Agentic RAG"
version: 1.0
quality: null
---
# Support KB Agentic RAG
agent_loop: ReAct
retrieval_strategy: hybrid
max_iterations: 3
sources: [rag_source_zendesk, rag_source_confluence]
```

## Related kinds
- `rag_source` (P01) -- defines the indexable sources the agent retrieves from
- `retriever_config` (P01) -- configures top_k, hybrid weights, and reranker
- `graph_rag_config` (P01) -- graph-based alternative for structured knowledge
- `agent` (P02) -- the agent that drives the retrieval loop
