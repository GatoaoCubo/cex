---
kind: tools
id: bld_tools_graph_rag_config
pillar: P04
llm_function: CALL
purpose: Tools available for graph_rag_config production
quality: 8.9
title: "Tools Graph Rag Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [graph_rag_config, builder, tools]
tldr: "Tools available for graph_rag_config production"
domain: "graph_rag_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_compile.py | Compile graph_rag_config artifact to .yaml | After authoring |
| cex_score.py | Peer-review score via 5D rubric | After compile |
| cex_retriever.py | Find similar existing graph_rag_config artifacts | During F3 INJECT |
| cex_doctor.py | Validate builder ISO health | Pre-dispatch |
| cex_wave_validator.py | Validate all ISOs in builder directory | Post-build |

## Validation Tools
| Tool | Purpose | When |
|------|---------|------|
| cex_hooks.py | Pre-commit quality gate enforcement | Before git commit |
| cex_sanitize.py | Check ASCII compliance in code files | Pre-commit |
| cex_hygiene.py | Artifact CRUD rules (frontmatter, naming) | Periodic cleanup |

## External References
- Microsoft GraphRAG (github.com/microsoft/graphrag, Edge et al. 2024)
- Neo4j LLM Graph Builder (community detection via Leiden algorithm)
- LangChain GraphRAG integration (graph Q&A chain)
- Graspologic (hierarchical community detection, used by MS GraphRAG)
- LlamaIndex KnowledgeGraphIndex (triplet extraction + graph store)
