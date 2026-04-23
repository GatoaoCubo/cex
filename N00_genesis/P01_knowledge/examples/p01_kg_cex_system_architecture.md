---
id: p01_kg_cex_system_architecture
kind: knowledge_graph
pillar: P01
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
author: "knowledge-graph-builder"
domain: "CEX system architecture"
entity_types:
  - Nucleus
  - Pillar
  - Builder
  - Kind
  - Artifact
  - Pipeline
relation_types:
  - orchestrates
  - dispatches_to
  - owns_artifacts_in
  - builds
  - produces
  - governs
  - contains
  - maps_to
  - feeds
storage_backend: in_memory
traversal_strategy: hybrid
quality: 9.1
tags: [knowledge_graph, cex-architecture, graphrag, P01, system-design]
tldr: "CEX system architecture graph: 6 entity types, 9 relation types, hybrid traversal, in_memory, leiden community detection"
description: "Knowledge graph schema for CEX architecture covering nuclei (N00-N07), pillars (P01-P12), builders, kinds, artifacts, and their relationships"
max_depth: 3
embedding_integration: true
dedup_strategy: fuzzy
community_detection: leiden
extraction_prompt: "Schema-constrained LLM triplet extraction: entity types Nucleus/Pillar/Builder/Kind/Artifact/Pipeline with relation type whitelist"
node_count_estimate: 60
edge_count_estimate: 120
density_score: 1.0
related:
  - bld_architecture_kind
  - bld_collaboration_kind
  - p01_ctx_cex_project
  - kind-builder
  - bld_knowledge_card_nucleus_def
  - p03_sp_n03_creation_nucleus
  - p01_kc_cex_project_overview
  - p10_entity_cex_system
  - bld_instruction_kind
  - p08_pat_nucleus_fractal
---

## Overview

This knowledge graph covers the CEX typed knowledge system architecture -- 8 nuclei (N00-N07),
12 pillars (P01-P12), 125+ builders, 130 kinds, and the artifacts they produce.
A graph is needed here because the relationships between these components are multi-hop and
bidirectional: N03 dispatches builders, builders produce kinds, kinds live in pillars, pillars
contain artifacts, and N07 orchestrates all nuclei -- flat vector search cannot traverse these
chains.
This graph answers: "which nucleus owns what?", "which builder produces which kind?", "which
pillar governs which kind?", "what does N07 orchestrate?", and "how do pipeline stages map to
nuclei?"

## Entity Types

| Name | Description | Extraction Hint | Examples |
|------|-------------|----------------|----------|
| Nucleus | Specialized AI agent nucleus with a domain role (N00-N07) | "N0[0-7]", "nucleus", names like "N03 Builder", "N07 Orchestrator" | N07, N03, N01, N00 |
| Pillar | Architectural domain layer (P01-P12) organizing artifact kinds | "P0[1-9]", "P1[0-2]", "pillar", domain labels like "P01 Knowledge" | P01, P08, P11, P12 |
| Builder | Specialized artifact constructor (13-ISO stack per kind) | "{kind}-builder", "builder", "ISO stack", "bld_" prefix files | knowledge-graph-builder, agent-builder, prompt-template-builder |
| Kind | Artifact type definition with schema, naming, and constraints | "kind:", "artifact kind", "kc_{kind}", named schemas in kinds_meta | knowledge_graph, agent, prompt_template, knowledge_card |
| Artifact | Concrete produced instance of a kind (a .md file with frontmatter) | ".md file", "p01_", "p02_", "frontmatter id:", produced output | p01_kg_cex.md, p03_sp_n07.md, p08_ac_n03.md |
| Pipeline | Named execution sequence or processing stage | "8F", "F1-F8", "pipeline stage", function names like "CONSTRAIN" | 8F pipeline, F1 CONSTRAIN, F6 PRODUCE, F7 GOVERN |

## Relation Types

| Name | Source Type | Target Type | Description | Directionality |
|------|-------------|-------------|-------------|----------------|
| orchestrates | Nucleus | Nucleus | N07 orchestrates all other nuclei (N01-N06); N00 is genesis archetype | directed |
| dispatches_to | Nucleus | Nucleus | N07 dispatches work tasks to specialized nuclei via handoff files | directed |
| owns_artifacts_in | Nucleus | Pillar | Each nucleus produces artifacts in its primary pillar domain | directed |
| builds | Nucleus | Builder | A nucleus (N03) loads and executes a builder to produce artifacts | directed |
| produces | Builder | Kind | A builder specializes in producing a specific kind of artifact | directed |
| governs | Pillar | Kind | A pillar defines the schema, naming, and constraints for its kinds | directed |
| contains | Pillar | Artifact | A pillar directory physically stores all artifact instances of its kinds | directed |
| maps_to | Kind | Pillar | Every kind is assigned to exactly one pillar in kinds_meta.json | directed |
| feeds | Artifact | Artifact | One artifact is consumed as input when producing another artifact | directed |

## Extraction Config

| Parameter | Value |
|-----------|-------|
| Method | schema_constrained LLM triplet extraction |
| LLM model | claude-sonnet-4-6 |
| Temperature | 0.0 |
| Output format | JSON list of {subject, predicate, object} |
| Extraction prompt | schema-constrained with entity type whitelist |

Extraction prompt template:
```
Extract all entities and relations from the following CEX architecture text.
Entity types: Nucleus, Pillar, Builder, Kind, Artifact, Pipeline
Relation types: orchestrates, dispatches_to, owns_artifacts_in, builds,
  produces, governs, contains, maps_to, feeds
Constraints:
  - Nucleus values must be N00-N07 format
  - Pillar values must be P01-P12 format
  - Builder values must end in "-builder"
  - Kind values must match kinds_meta.json registry
Output format: JSON list of {"subject": "...", "predicate": "...", "object": "..."}
Text: {text}
```

## Storage and Traversal

| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Storage backend | in_memory | CEX architecture is a static schema domain (<500 nodes); no persistence across sessions needed for architectural queries; LlamaIndex KG in_memory is the natural fit |
| Traversal strategy | hybrid | Local mode answers entity-centric questions ("what does N03 do?", "what kinds live in P01?"); global mode answers structural summaries ("what are the main system clusters?", "what is the role of P11?") |
| Max depth | 3 | Covers the key 3-hop chain: Nucleus -> Builder -> Kind -> Pillar; deeper hops add noise |
| Query language | python | LlamaIndex KG Python API; Cypher not needed at this scale |
| Pruning rule | relevance_score >= 0.65 | Prune low-confidence extracted triplets at ingestion time |

## Integration

| Component | Value |
|-----------|-------|
| Embedding model | text-embedding-3-small (or nomic-embed-text for local) |
| Dedup strategy | fuzzy |
| Dedup threshold | 0.88 |
| Community detection | leiden |
| Community granularity | medium |
| Downstream consumers | cex_retriever.py, N07 orchestrator reasoning, cex_query.py discovery, architecture audit tooling |

## References
- CEX kinds_meta.json: .cex/kinds_meta.json (128 kinds, 12 pillars, 8 nuclei)
- Builder ISOs: archetypes/builders/{kind}-builder/ (13 ISOs per builder, 125+ builders)
- Pillar schemas: P{01-12}_*/_schema.yaml
- Architecture KC: P01_knowledge/library/kind/kc_knowledge_graph.md
- Microsoft GraphRAG: arxiv.org/abs/2404.16130 (2024)
- LlamaIndex KnowledgeGraphIndex: docs.llamaindex.ai

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | downstream | 0.45 |
| [[bld_collaboration_kind]] | downstream | 0.41 |
| [[p01_ctx_cex_project]] | related | 0.39 |
| [[kind-builder]] | downstream | 0.37 |
| [[bld_knowledge_card_nucleus_def]] | related | 0.34 |
| [[p03_sp_n03_creation_nucleus]] | downstream | 0.34 |
| [[p01_kc_cex_project_overview]] | related | 0.31 |
| [[p10_entity_cex_system]] | downstream | 0.30 |
| [[bld_instruction_kind]] | downstream | 0.30 |
| [[p08_pat_nucleus_fractal]] | downstream | 0.30 |
