---
kind: instruction
id: bld_instruction_graph_rag_config
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for graph_rag_config
quality: 8.8
title: "Instruction Graph Rag Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [graph_rag_config, builder, instruction]
tldr: "Step-by-step production process for graph_rag_config"
domain: "graph_rag_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Analyze graph database schema requirements for RAG nodes/edges  
2. Evaluate data source compatibility (vector DB, knowledge graphs, relational tables)  
3. Benchmark graph traversal algorithms for retrieval efficiency  
4. Study injection point placement in query pipelines  
5. Compare schema normalization vs denormalization tradeoffs  
6. Document security constraints for sensitive graph data  

## Phase 2: COMPOSE  
1. Initialize config with bld_schema_graph_rag_config.md base structure  
2. Define node types per bld_output_template_graph_rag_config.md entity hierarchy  
3. Map data sources to graph injection endpoints  
4. Configure edge weighting parameters (confidence, relevance)  
5. Implement query injection patterns from schema  
6. Set retrieval path limits (max hops, depth)  
7. Embed validation hooks per schema constraints  
8. Write config using bld_output_template_graph_rag_config.md syntax  
9. Add metadata for versioning and dependency tracking  

## Phase 3: VALIDATE  
- [ ] Schema compliance check against bld_schema_graph_rag_config.md  
- [ ] Data integrity verification (node/edge consistency)  
- [ ] Injection point stress testing with sample queries  
- [ ] Retrieval accuracy benchmarking (precision/recall)  
- [ ] Performance validation (latency, throughput)
