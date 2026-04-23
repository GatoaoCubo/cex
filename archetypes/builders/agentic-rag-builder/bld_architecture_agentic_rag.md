---
kind: architecture
id: bld_architecture_agentic_rag
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of agentic_rag -- inventory, dependencies
quality: 9.0
title: "Architecture Agentic Rag"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [agentic_rag, builder, architecture]
tldr: "Component map of agentic_rag -- inventory, dependencies"
domain: "agentic_rag construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_ecommerce_vertical
  - bld_architecture_faq_entry
  - bld_architecture_reranker_config
  - bld_architecture_changelog
  - bld_architecture_graph_rag_config
  - bld_architecture_competitive_matrix
  - bld_architecture_legal_vertical
  - bld_architecture_fintech_vertical
  - bld_architecture_healthcare_vertical
  - bld_architecture_roi_calculator
---

## Component Inventory
| ISO Name             | Role                          | Pillar | Status  |
|----------------------|-------------------------------|--------|---------|
| bld_manifest         | Core configuration container  | P01    | Active  |
| bld_instruction      | Task definition interface     | P01    | Active  |
| bld_system_prompt    | LLM behavior specification    | P01    | Active  |
| bld_schema           | Data structure definition     | P01    | Active  |
| bld_quality_gate     | Output validation engine      | P01    | Active  |
| bld_output_template  | Response formatting blueprint | P01    | Active  |
| bld_examples         | Training data repository      | P01    | Active  |
| bld_knowledge_card   | Contextual information hub    | P01    | Active  |
| bld_architecture     | System blueprint definition   | P01    | Active  |
| bld_collaboration    | Multi-agent coordination      | P01    | Active  |
| bld_config           | Parameter management          | P01    | Active  |
| bld_memory           | State retention mechanism    | P01    | Active  |
| bld_tools            | Utility function library      | P01    | Active  |

## Dependencies
| From           | To               | Type       |
|----------------|------------------|------------|
| bld_config     | bld_schema       | Reference  |
| bld_instruction| bld_system_prompt| Input      |
| bld_quality_gate| bld_output_template | Validation |
| bld_memory     | bld_tools        | Utilization|
| bld_manifest   | bld_instruction  | Dependency |

## Architectural Position
agentic_rag operates as the knowledge orchestration layer within CEX P01, enabling dynamic retrieval-augmented generation through structured component interactions. It bridges raw data (bld_knowledge_card) with executable logic (bld_instruction), ensuring compliance via bld_quality_gate while maintaining adaptability through bld_config and bld_memory.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_ecommerce_vertical]] | sibling | 0.86 |
| [[bld_architecture_faq_entry]] | sibling | 0.85 |
| [[bld_architecture_reranker_config]] | sibling | 0.81 |
| [[bld_architecture_changelog]] | sibling | 0.81 |
| [[bld_architecture_graph_rag_config]] | sibling | 0.79 |
| [[bld_architecture_competitive_matrix]] | sibling | 0.78 |
| [[bld_architecture_legal_vertical]] | sibling | 0.67 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.65 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.65 |
| [[bld_architecture_roi_calculator]] | sibling | 0.64 |
