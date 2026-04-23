---
kind: architecture
id: bld_architecture_competitive_matrix
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of competitive_matrix -- inventory, dependencies
quality: 9.0
title: "Architecture Competitive Matrix"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [competitive_matrix, builder, architecture]
tldr: "Component map of competitive_matrix -- inventory, dependencies"
domain: "competitive_matrix construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_architecture_graph_rag_config
  - bld_architecture_faq_entry
  - bld_architecture_reranker_config
  - bld_architecture_changelog
  - bld_architecture_ecommerce_vertical
  - bld_architecture_agentic_rag
  - bld_architecture_legal_vertical
  - bld_architecture_fintech_vertical
  - bld_architecture_discovery_questions
  - bld_architecture_healthcare_vertical
---

## Component Inventory
| ISO Name             | Role                                      | Pillar | Status  |
|----------------------|-------------------------------------------|--------|---------|
| bld_manifest         | Defines matrix structure                  | P01    | Active  |
| bld_instruction      | Specifies generation rules                | P01    | Active  |
| bld_system_prompt    | Sets LLM behavior for matrix building     | P01    | Active  |
| bld_schema           | Enforces data format consistency          | P01    | Active  |
| bld_quality_gate     | Validates output accuracy                 | P01    | Active  |
| bld_output_template  | Structures final matrix display           | P01    | Active  |
| bld_examples         | Provides reference matrices               | P01    | Active  |
| bld_knowledge_card   | Embeds domain-specific insights           | P01    | Active  |
| bld_architecture     | Maps component interactions              | P01    | Active  |
| bld_collaboration    | Enables cross-builder coordination        | P01    | Active  |
| bld_config           | Centralizes configuration parameters      | P01    | Active  |
| bld_memory           | Stores historical matrix data             | P01    | Active  |
| bld_tools            | Integrates external analysis utilities    | P01    | Active  |

## Dependencies
| From              | To                  | Type         |
|-------------------|---------------------|--------------|
| bld_manifest      | bld_config          | Configuration|
| bld_instruction   | bld_system_prompt   | Definition   |
| bld_output_template | bld_schema        | Structure    |
| bld_quality_gate  | bld_memory          | Validation   |
| bld_tools         | External API        | Integration  |

## Architectural Position
competitive_matrix serves as the central orchestrator in CEX P01, synthesizing builder ISOs to automate competitive landscape analysis. It ensures structured, high-quality matrix generation through schema enforcement, quality gates, and collaboration mechanisms, while leveraging memory and tools for data depth and accuracy.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_graph_rag_config]] | sibling | 0.81 |
| [[bld_architecture_faq_entry]] | sibling | 0.81 |
| [[bld_architecture_reranker_config]] | sibling | 0.81 |
| [[bld_architecture_changelog]] | sibling | 0.80 |
| [[bld_architecture_ecommerce_vertical]] | sibling | 0.79 |
| [[bld_architecture_agentic_rag]] | sibling | 0.78 |
| [[bld_architecture_legal_vertical]] | sibling | 0.65 |
| [[bld_architecture_fintech_vertical]] | sibling | 0.63 |
| [[bld_architecture_discovery_questions]] | sibling | 0.63 |
| [[bld_architecture_healthcare_vertical]] | sibling | 0.61 |
