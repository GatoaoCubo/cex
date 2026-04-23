---
kind: tools
id: bld_tools_knowledge_graph
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for knowledge_graph production
quality: 9.2
title: "Tools: knowledge-graph-builder"
version: "1.0.0"
author: n03_builder
tags: [knowledge_graph, builder, tools, P04]
tldr: "Tools for knowledge_graph artifact production: retriever for domain discovery, compile for validation, score for quality check."
domain: "knowledge graph construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.90
related:
  - bld_tools_citation
  - bld_tools_retriever_config
  - bld_tools_context_window_config
  - bld_tools_multi_modal_config
  - bld_tools_kind
  - bld_tools_chunk_strategy
  - bld_tools_memory_scope
  - bld_tools_prompt_cache
  - bld_tools_cli_tool
  - bld_tools_hitl_config
---

# Tools: knowledge-graph-builder

## Production Tools

| Tool | Purpose | When | Status |
|------|---------|------|--------|
| cex_retriever.py | Search existing knowledge_graph artifacts for similar domains | Phase 1 (avoid duplication) | ACTIVE |
| cex_compile.py | Compile .md artifact to .yaml | Phase 3 (F8) | ACTIVE |
| cex_score.py | Score artifact quality across 3 layers | Phase 3 (F7) | ACTIVE |
| brain_query [MCP] | Search pool for existing graph schemas | Phase 1 (check duplicates) | CONDITIONAL |
| cex_doctor.py | Builder health check post-production | Phase 3 (F8) | ACTIVE |
| cex_query.py | TF-IDF discovery of related builders | Phase 1 | ACTIVE |

## Data Sources

| Source | Path | Data |
|--------|------|------|
| P01 Schema | P01_knowledge/_schema.yaml | knowledge_graph kind definition |
| Kind KC | P01_knowledge/library/kind/kc_knowledge_graph.md | Domain knowledge for graph patterns |
| P01 Examples | P01_knowledge/examples/ | Existing knowledge_graph artifacts |
| kinds_meta.json | .cex/kinds_meta.json | Kind registry, naming, pillar assignment |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position for knowledge_graph |

## External References (no tools, background knowledge)

| Framework | What to know | When relevant |
|-----------|-------------|---------------|
| Microsoft GraphRAG | Entity+community extraction from large corpora | When corpus > 1000 docs and global queries needed |
| LlamaIndex KnowledgeGraphIndex | Triplet extraction, in-memory or neo4j backend | Default starting point for most use cases |
| Neo4j + LangChain | GraphCypherQAChain, Cypher generation | When complex multi-hop queries needed |
| LightRAG | Local + global dual search, incremental updates | When corpus changes frequently |
| FalkorDB | Redis-compatible in-memory Cypher | When high-throughput, Redis ecosystem needed |

## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Compile and Score Commands

```bash
# Compile artifact to YAML
python _tools/cex_compile.py P01_knowledge/examples/p01_kg_{name}.md

# Score artifact quality
python _tools/cex_score.py --apply P01_knowledge/examples/p01_kg_{name}.md

# Discover similar artifacts
python _tools/cex_retriever.py --query "knowledge graph {domain}" --top 5
```

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_knowledge_graph
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld_tools_knowledge_graph.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_citation]] | sibling | 0.51 |
| [[bld_tools_retriever_config]] | sibling | 0.49 |
| [[bld_tools_context_window_config]] | sibling | 0.47 |
| [[bld_tools_multi_modal_config]] | sibling | 0.47 |
| [[bld_tools_kind]] | sibling | 0.46 |
| [[bld_tools_chunk_strategy]] | sibling | 0.46 |
| [[bld_tools_memory_scope]] | sibling | 0.46 |
| [[bld_tools_prompt_cache]] | sibling | 0.45 |
| [[bld_tools_cli_tool]] | sibling | 0.44 |
| [[bld_tools_hitl_config]] | sibling | 0.44 |
