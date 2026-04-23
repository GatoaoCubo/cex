---
kind: collaboration
id: bld_collaboration_search_strategy
pillar: P12
llm_function: COLLABORATE
purpose: How search_strategy-builder works in crews with other builders
quality: 8.9
title: "Collaboration Search Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [search_strategy, builder, collaboration]
tldr: "How search_strategy-builder works in crews with other builders"
domain: "search_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_collaboration_agentic_rag
  - bld_collaboration_parser
  - bld_collaboration_reasoning_strategy
  - bld_collaboration_reranker_config
  - bld_collaboration_retriever
  - search-strategy-builder
  - bld_collaboration_retriever_config
  - p08_dir_rag_pipeline
  - bld_architecture_document_loader
  - bld_collaboration_action_paradigm
---

## Crew Role  
Designs and optimizes search/inference strategies to guide data retrieval and analysis, ensuring alignment with task goals and constraints.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Query Parser  | Structured query      | JSON        |  
| User Input    | Raw text input        | Text        |  
| Data Processor| Metadata              | Structured data |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Retriever     | Search strategy       | JSON        |  
| Inference Engine | Inference parameters | Config file |  
| Task Orchestrator | Retrieval plan     | Text        |  

## Boundary  
Does NOT handle document retrieval (retriever), prompt engineering (reasoning_strategy), or raw data processing (data_processor). Those are managed by dedicated builders.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_agentic_rag]] | sibling | 0.38 |
| [[bld_collaboration_parser]] | sibling | 0.25 |
| [[bld_collaboration_reasoning_strategy]] | sibling | 0.25 |
| [[bld_collaboration_reranker_config]] | sibling | 0.25 |
| [[bld_collaboration_retriever]] | sibling | 0.25 |
| [[search-strategy-builder]] | upstream | 0.25 |
| [[bld_collaboration_retriever_config]] | sibling | 0.24 |
| [[p08_dir_rag_pipeline]] | upstream | 0.22 |
| [[bld_architecture_document_loader]] | upstream | 0.22 |
| [[bld_collaboration_action_paradigm]] | sibling | 0.22 |
