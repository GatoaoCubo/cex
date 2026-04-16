---
kind: instruction
id: bld_instruction_search_strategy
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for search_strategy
quality: 8.8
title: "Instruction Search Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [search_strategy, builder, instruction]
tldr: "Step-by-step production process for search_strategy"
domain: "search_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Analyze compute bottlenecks in inference pipelines  
2. Benchmark existing search heuristics for resource allocation  
3. Identify constraints: latency, memory, throughput tradeoffs  
4. Study domain-specific workloads (e.g., NLP, vision)  
5. Evaluate dynamic vs static allocation strategies  
6. Document research findings in technical whitepaper  

## Phase 2: COMPOSE  
1. Define strategy parameters (e.g., priority queues, budget limits)  
2. Structure artifact using SCHEMA.md's `search_strategy` interface  
3. Map research findings to schema fields (e.g., `allocation_rules`)  
4. Implement core logic in `compute_allocation()` function  
5. Write validation rules for input constraints  
6. Integrate OUTPUT_TEMPLATE.md's JSON structure  
7. Add metadata: version, author, compatibility tags  
8. Write unit tests for edge cases (e.g., zero-budget scenarios)  
9. Finalize artifact with documentation comments  

## Phase 3: VALIDATE  
- [ ] ✅ Schema compliance check (jsonschema)  
- [ ] ✅ Unit test coverage ≥90%  
- [ ] ✅ Edge case validation (e.g., 1000+ concurrent queries)  
- [ ] ✅ Performance benchmark against baseline  
- [ ] ✅ Peer review for domain-specific accuracy
