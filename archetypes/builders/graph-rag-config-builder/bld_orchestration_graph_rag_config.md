---
kind: collaboration
id: bld_collaboration_graph_rag_config
pillar: P12
llm_function: COLLABORATE
purpose: How graph_rag_config-builder works in crews with other builders
quality: 8.9
title: "Collaboration Graph Rag Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [graph_rag_config, builder, collaboration]
tldr: "How graph_rag_config-builder works in crews with other builders"
domain: "graph_rag_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_graph_rag_config_builder
  - graph-rag-config-builder
  - bld_collaboration_knowledge_graph
  - bld_collaboration_agentic_rag
  - kc_graph_rag_config
  - bld_instruction_graph_rag_config
  - bld_collaboration_search_strategy
  - p10_mem_graph_rag_config_builder
  - bld_collaboration_reranker_config
  - bld_collaboration_eval_metric
---

## Crew Role  
Orchestrates Graph RAG pipeline configuration by defining schema, linking knowledge graphs to retrieval systems, and specifying query routing rules.  

## Receives From  
| Builder         | What                  | Format   |  
|-----------------|-----------------------|----------|  
| Knowledge Engineer | Graph schema        | YAML     |  
| Data Curator    | Document source specs | JSON     |  
| System Architect | Pipeline requirements | TOML     |  

## Produces For  
| Builder         | What                  | Format   |  
|-----------------|-----------------------|----------|  
| RAG Engine      | Config file           | YAML     |  
| Data Curator    | Validation report     | JSON     |  
| DevOps          | Deployment spec       | TOML     |  

## Boundary  
Does NOT handle graph instance construction (knowledge_graph_builder) or document ingestion (rag_source_builder). Those are managed by specialized builders.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_graph_rag_config_builder]] | upstream | 0.37 |
| [[graph-rag-config-builder]] | upstream | 0.37 |
| [[bld_collaboration_knowledge_graph]] | sibling | 0.34 |
| [[bld_collaboration_agentic_rag]] | sibling | 0.28 |
| [[kc_graph_rag_config]] | upstream | 0.28 |
| [[bld_instruction_graph_rag_config]] | upstream | 0.25 |
| [[bld_collaboration_search_strategy]] | sibling | 0.25 |
| [[p10_mem_graph_rag_config_builder]] | upstream | 0.24 |
| [[bld_collaboration_reranker_config]] | sibling | 0.22 |
| [[bld_collaboration_eval_metric]] | sibling | 0.22 |
