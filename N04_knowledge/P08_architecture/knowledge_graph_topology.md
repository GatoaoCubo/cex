---
id: p06_arch_knowledge_graph
kind: context_doc
8f: F3_inject
pillar: P06
title: "Knowledge Graph Topology — CEX Entity-Relationship Map"
version: 1.0.0
created: 2026-04-07
author: n04_knowledge
domain: knowledge-infrastructure
quality: 9.0
tags: [architecture, knowledge-graph, topology, entities, relationships, n04]
tldr: "CEX knowledge graph: 6 entity types, 9 relationship types, 3 traversal patterns. Maps how 3647+ artifacts interconnect."
density_score: 0.93
related:
  - bld_architecture_kind
  - kind-builder
  - p01_kg_cex_system_architecture
  - bld_collaboration_kind
  - agent_card_n04
  - p10_entity_cex_system
  - bld_collaboration_knowledge_graph
  - bld_knowledge_card_kind
  - bld_tools_kind
  - bld_instruction_kind
---

# Knowledge Graph Topology

## Entity Types

| Entity | Source | Count | Key Attribute |
|--------|--------|------:|---------------|
| **Kind** | `.cex/kinds_meta.json` | 123 | `pillar`, `builder`, `llm_function` |
| **Pillar** | `P{01-12}_*/` | 12 | `domain`, `schema` |
| **Nucleus** | `N{00-07}_*/` | 8 | `sin`, `model`, `domain` |
| **Artifact** | All `.md` files with frontmatter | 2,184 | `kind`, `pillar`, `quality` |
| **Builder** | `archetypes/builders/{kind}-builder/` | 125 | 13 ISOs each |
| **Tool** | `_tools/*.py` | 59 | `category`, `line_count` |

## Relationship Types

| Relationship | From → To | Cardinality | Example |
|-------------|-----------|-------------|---------|
| `BELONGS_TO` | Artifact → Pillar | N:1 | `kc_rag.md` → P01 |
| `BUILT_BY` | Artifact → Builder | N:1 | `kc_rag.md` → knowledge-card-builder |
| `OWNED_BY` | Kind → Nucleus | N:1 | `knowledge_card` → N04 |
| `DEPENDS_ON` | Artifact → Artifact | N:M | `retriever_config` → `embedding_config` |
| `FEEDS` | Artifact → Tool | N:M | `chunk_strategy` → `cex_retriever.py` |
| `CROSS_REFS` | KC → KC | N:M | `kc_rag` ↔ `kc_embedding` |
| `COMPILES_TO` | `.md` → `.yaml` | 1:1 | Source → Compiled |
| `INHERITS` | Builder → Archetype | N:1 | All builders → N00 Genesis |
| `SIGNALS` | Nucleus → Nucleus | N:M | N04 `complete` → N07 |

## Graph Structure

```
                         ┌──────────┐
                         │ N00      │
                         │ Genesis  │
                         └────┬─────┘
                              │ INHERITS
           ┌──────────────────┼──────────────────┐
           ▼                  ▼                   ▼
    ┌─────────────┐   ┌─────────────┐    ┌─────────────┐
    │ P01         │   │ P03         │    │ P10         │
    │ Knowledge   │   │ Agents      │    │ Memory      │
    │ (10 kinds)  │   │ (8 kinds)   │    │ (8 kinds)   │
    └──────┬──────┘   └──────┬──────┘    └──────┬──────┘
           │                 │                   │
           ▼                 ▼                   ▼
    ┌─────────────┐   ┌─────────────┐    ┌─────────────┐
    │ KC, RAG,    │   │ Agent, Sys  │    │ Entity Mem, │
    │ Embedding,  │   │ Prompt,     │    │ Brain Index,│
    │ Glossary    │   │ Persona     │    │ Session     │
    └──────┬──────┘   └─────────────┘    └──────┬──────┘
           │                                     │
           └───────────── CROSS_REFS ────────────┘
```

## Traversal Patterns

### 1. Builder Resolution (Intent → Builder → ISOs)

```
User intent → cex_query.py (TF-IDF) → kind match → builder dir → 13 ISOs → prompt
```

**Nodes touched**: Intent → Kind → Builder → ISO₁..ISO₁₃ → Compiled Prompt

### 2. Knowledge Injection (Query → Retrieve → Inject)

```
Query → cex_retriever.py → Top-K artifacts → cex_prompt_layers.py → LLM context
```

**Nodes touched**: Query → TF-IDF Index → Artifact₁..Artifactₖ → Prompt

### 3. Memory Lifecycle (Create → Age → Prune)

```
New fact → cex_memory_update.py (append) → cex_memory_age.py (decay) → cex_memory_select.py (inject or prune)
```

**Nodes touched**: Fact → Memory Store → Age Label → Inject/Archive

## Density Metrics

| Metric | Value |
|--------|-------|
| Avg edges per artifact | ~3.2 (BELONGS_TO + BUILT_BY + ≥1 CROSS_REF) |
| Most connected entity | `knowledge_card` kind (123 KCs + 10 builders + 12 pillar links) |
| Orphan artifacts | ~15% (compiled YAMLs without explicit cross-refs) |
| Deepest dependency chain | 4 hops: `rag_source` → `chunk_strategy` → `embedding_config` → `vector_store` |

## Maintenance

| Action | Tool | Frequency |
|--------|------|-----------|
| Rebuild TF-IDF index | `cex_retriever.py --rebuild` | After batch KC creation |
| Detect orphans | `cex_doctor.py --orphans` | Weekly |
| Validate cross-refs | `cex_compile.py --all` | Every commit |
| Freshness audit | `cex_memory_age.py --report` | Monthly |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | downstream | 0.43 |
| [[kind-builder]] | downstream | 0.37 |
| [[p01_kg_cex_system_architecture]] | upstream | 0.36 |
| [[bld_collaboration_kind]] | downstream | 0.36 |
| [[agent_card_n04]] | sibling | 0.35 |
| [[p10_entity_cex_system]] | downstream | 0.33 |
| [[bld_collaboration_knowledge_graph]] | downstream | 0.32 |
| [[bld_knowledge_card_kind]] | upstream | 0.30 |
| [[bld_tools_kind]] | upstream | 0.29 |
| [[bld_instruction_kind]] | upstream | 0.28 |
