---
id: kno_knowledge_graph_n04
kind: knowledge_graph
pillar: P01
nucleus: n04
title: N04 Knowledge Graph
version: "1.0.0"
quality: 9.1
tags: [knowledge_graph, n04, graphrag, taxonomy, knowledge_gluttony]
domain: cex_knowledge_topology
entity_types:
  - Artifact
  - Kind
  - Pillar
  - Nucleus
  - Builder
  - Tool
  - Contract
  - MemoryRecord
relation_types:
  - belongs_to_pillar
  - owned_by_nucleus
  - built_by
  - constrained_by
  - uses_tool
  - relates_to
  - depends_on
  - remembered_as
storage_backend: neo4j
traversal_strategy: hybrid
max_depth: 3
embedding_integration: true
dedup_strategy: fuzzy
community_detection: leiden
extraction_prompt: schema_constrained_triplet_extraction_n04
tldr: "GraphRAG schema for CEX artifacts, builders, contracts, and memory paths across N04-owned knowledge."
density_score: 1.0
---
<!-- 8F: F1=knowledge_graph/P01 F2=knowledge-graph-builder F3=nucleus_def_n04+kc_knowledge_graph+N04 schemas/configs+N04 knowledge memory examples F4=template-first graph schema for artifact-rich GraphRAG over CEX knowledge
     F5=shell,apply_patch,cex_compile F6=author markdown artifact F7=frontmatter+entity-relation coherence+ascii+self-check F8=N04_knowledge/P01_knowledge/kno_knowledge_graph_n04.md -->
# Overview
N04 should not stop at flat similarity search.
Knowledge Gluttony means consuming not only isolated facts but also the connective tissue between artifacts, kinds, builders, constraints, and remembered runtime decisions.
This graph schema turns CEX knowledge into traversable structure so the system can answer both local questions and global pattern questions.
The graph is optimized for GraphRAG over repository-native artifacts rather than external world entities.

## Boundary
`knowledge_graph` defines types, relations, extraction rules, storage, and traversal.
It does not store live counters, ephemeral session facts, or raw vector index parameters.
Actual instances belong in graph storage or memory artifacts after extraction.

## Question Classes
| Question | Why graph is needed |
|----------|---------------------|
| which builder constrains this artifact kind | relation lookup beats flat retrieval |
| what contracts shape N04 output quality | multi-hop reasoning across builders and schemas |
| which memories influence current runtime routing | joins between memory and artifact lineage |
| what clusters of artifacts share tooling and schemas | community detection over relation density |
| where does a naming drift propagate | graph traversal across kind, schema, and artifact nodes |

## Entity Types
| Name | Description | Extraction Hint | Examples |
|------|-------------|----------------|----------|
| `Artifact` | authored markdown or compiled output unit | file stems with frontmatter ids | `kno_vector_store_n04`, `con_env_config_n04` |
| `Kind` | formal artifact category | `kind:` frontmatter field | `vector_store`, `runtime_state` |
| `Pillar` | organizational memory or knowledge domain | `pillar:` markers | `P01`, `P10` |
| `Nucleus` | operating unit in CEX | `N0x` references and ownership text | `n04`, `n07` |
| `Builder` | specialized construction pattern | builder directory names and manifest ids | `knowledge-graph-builder`, `vector-store-builder` |
| `Tool` | executable support component | `_tools/` names or tool lists | `cex_compile.py`, `cex_retriever.py` |
| `Contract` | schema, validator, or config rule | files in `schemas/` and `config/` | `sch_input_schema_n04`, `con_path_config_n04` |
| `MemoryRecord` | persistent remembered operational state | memory artifact ids and summaries | `mem_runtime_state_n04`, `mem_learning_record_n04` |

## Relation Types
| Name | Source Type | Target Type | Description | Directionality |
|------|-------------|-------------|-------------|----------------|
| `belongs_to_pillar` | `Artifact` | `Pillar` | artifact is classified under a pillar | directed |
| `owned_by_nucleus` | `Artifact` | `Nucleus` | artifact has primary ownership or stewardship | directed |
| `built_by` | `Artifact` | `Builder` | artifact kind maps to a construction archetype | directed |
| `constrained_by` | `Artifact` | `Contract` | schema, config, or validator limits its form | directed |
| `uses_tool` | `Artifact` | `Tool` | production or runtime depends on a tool | directed |
| `relates_to` | `Artifact` | `Artifact` | semantic adjacency or shared domain | undirected |
| `depends_on` | `Artifact` | `Artifact` | upstream artifact required for downstream value | directed |
| `remembered_as` | `Artifact` | `MemoryRecord` | artifact generates or is summarized in memory | directed |

## Extraction Config
| Parameter | Value |
|-----------|-------|
| Method | `schema_constrained` |
| LLM model | `gpt-5-codex` |
| Temperature | `0.1` |
| Output format | `json_triplets` |
| Extraction prompt | `schema_constrained_triplet_extraction_n04` |

Extraction prompt template:
```text
Extract entity and relation triplets from the artifact text.
Allowed entity types: Artifact, Kind, Pillar, Nucleus, Builder, Tool, Contract, MemoryRecord.
Allowed relation types: belongs_to_pillar, owned_by_nucleus, built_by, constrained_by,
uses_tool, relates_to, depends_on, remembered_as.
Emit JSON triplets only when subject and object can be grounded to explicit text spans.
Text: {text}
```

## Storage and Traversal
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Storage backend | `neo4j` | strongest fit for persistent multi-hop repository topology |
| Traversal strategy | `hybrid` | supports local artifact drill-down and global theme discovery |
| Max depth | `3` | enough to move artifact -> builder -> contract or artifact -> memory -> tool |
| Query language | `cypher` | concise for path and neighborhood questions |
| Pruning rule | `min relation confidence 0.72 after depth 2` | avoids weak semantic drift in long traversals |

## Traversal Modes
| Mode | Entry point | Best for |
|------|-------------|----------|
| local | artifact id or file path | explain one artifact's dependencies and controls |
| neighborhood | kind or builder | inspect all nearby artifacts and contracts |
| global | community centroid | summarize major subsystem themes |
| hybrid | vector seed plus graph walk | answer repository questions with both meaning and structure |

## Integration
| Component | Value |
|-----------|-------|
| Embedding model | `kno_embedder_provider_n04` |
| Dedup strategy | `fuzzy` |
| Dedup threshold | `0.88` |
| Community detection | `leiden` |
| Community granularity | `medium` |
| Downstream consumers | `cex_retriever.py`, `taxonomy_audit`, `rag_reweight`, `n07 orchestration` |

## Dedup Rules
1. Collapse path variants and frontmatter ids into one canonical `Artifact` node.
2. Treat hyphen and underscore naming drift as candidate aliases before creating new nodes.
3. Merge builder aliases only when manifest id and directory stem agree.
4. Keep `MemoryRecord` distinct from `Artifact` even when file names resemble source artifacts.

## Anti-Patterns
1. Using unconstrained extraction creates noisy relation vocabularies that poison traversal.
2. Modeling chunk instances as first-class permanent nodes bloats the graph with low-value detail.
3. Skipping contract nodes hides the control plane that explains why artifacts look the way they do.
4. Collapsing runtime memory into generic artifact nodes removes temporal leverage.
5. Running only local traversal prevents theme summaries and cross-pillar synthesis.

## References
1. `archetypes/builders/knowledge-graph-builder/bld_instruction_knowledge_graph.md`
2. `P01_knowledge/library/kind/kc_knowledge_graph.md`
3. `N04_knowledge/P01_knowledge/knowledge_card_knowledge.md`
4. `N04_knowledge/P10_memory/knowledge_memory_index.md`

## Properties
| Property | Value |
|----------|-------|
| Kind | `knowledge_graph` |
| Pillar | `P01` |
| Nucleus | `n04` |
| Entity type count | `8` |
| Relation type count | `8` |
| Storage backend | `neo4j` |
| Traversal strategy | `hybrid` |
| Max depth | `3` |
| Embedding integration | `true` |
| Community detection | `leiden` |
