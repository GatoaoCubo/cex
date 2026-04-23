---
kind: architecture
id: bld_architecture_graph_rag_config
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of graph_rag_config -- inventory, dependencies
quality: 9.0
title: "Architecture Graph Rag Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [graph_rag_config, builder, architecture]
tldr: "Component map of graph_rag_config -- inventory, dependencies"
domain: "graph_rag_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_faq_entry
  - bld_architecture_reranker_config
  - bld_architecture_changelog
  - bld_architecture_ecommerce_vertical
  - bld_architecture_competitive_matrix
  - bld_architecture_agentic_rag
  - bld_architecture_legal_vertical
  - bld_architecture_discovery_questions
  - bld_architecture_fintech_vertical
  - bld_architecture_healthcare_vertical
---

## Component Inventory
| ISO Name             | Role                                | Pillar | Status  |
|----------------------|-------------------------------------|--------|---------|
| bld_manifest         | Defines config structure            | P01    | Active  |
| bld_instruction      | Specifies processing steps          | P01    | Active  |
| bld_system_prompt    | Sets LLM interaction guidelines     | P01    | Active  |
| bld_schema           | Enforces data format standards      | P01    | Active  |
| bld_quality_gate     | Validates output integrity          | P01    | Active  |
| bld_output_template  | Structures final output format      | P01    | Active  |
| bld_examples         | Provides sample input/output pairs  | P01    | Active  |
| bld_knowledge_card   | Embeds domain-specific knowledge    | P01    | Active  |
| bld_architecture     | Maps component interdependencies    | P01    | Active  |
| bld_collaboration    | Manages team coordination workflows | P01    | Active  |
| bld_config           | Centralizes configuration parameters| P01    | Active  |
| bld_memory           | Stores historical config states     | P01    | Active  |
| bld_tools            | Integrates external RAG utilities   | P01    | Active  |

## Dependencies
| From              | To                  | Type         |
|-------------------|---------------------|--------------|
| bld_config        | bld_schema          | Definition   |
| bld_instruction   | bld_system_prompt   | Guidance     |
| bld_quality_gate  | bld_output_template | Validation   |
| bld_examples      | bld_knowledge_card  | Reference    |
| bld_tools         | graph_db            | External     |

## Architectural Position
graph_rag_config is the central orchestrator in P01, ensuring RAG systems align with CEX knowledge management by harmonizing schema, instructions, quality checks, and collaboration workflows, while embedding domain-specific context and historical memory for consistent, auditable configurations.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_faq_entry]] | sibling | 0.84 |
| [[bld_architecture_reranker_config]] | sibling | 0.84 |
| [[bld_architecture_changelog]] | sibling | 0.83 |
| [[bld_architecture_ecommerce_vertical]] | sibling | 0.81 |
| [[bld_architecture_competitive_matrix]] | sibling | 0.80 |
| [[bld_architecture_agentic_rag]] | sibling | 0.78 |
| [[bld_architecture_legal_vertical]] | sibling | 0.65 |
| [[bld_architecture_discovery_questions]] | sibling | 0.65 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.63 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.63 |
