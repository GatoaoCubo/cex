---
kind: instruction
id: bld_instruction_agentic_rag
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for agentic_rag
quality: null
title: "Instruction Agentic Rag"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [agentic_rag, builder, instruction]
tldr: "Step-by-step production process for agentic_rag"
domain: "agentic_rag construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify domain-specific knowledge sources and injection triggers  
2. Map agent decision trees to RAG retrieval boundaries  
3. Benchmark existing RAG frameworks for agent compatibility  
4. Document injection point semantics (e.g., query rewriting, context fusion)  
5. Analyze latency tradeoffs between retrieval depth and agent reasoning  
6. Validate data provenance for hallucination-resistant injection  

## Phase 2: COMPOSE  
1. Define agent state schema in SCHEMA.md (include memory, context, intent)  
2. Implement retrieval module with vector DB and filter syntax  
3. Write agent planner using P01 decision tree templates  
4. Code injection handler with priority-based trigger evaluation  
5. Integrate RAG results into agent's decision context  
6. Use OUTPUT_TEMPLATE.md for structured response formatting  
7. Add fallback logic for retrieval failures  
8. Embed domain-specific prompt engineering in injection pipelines  
9. Conduct unit tests for each RAG-agent interaction layer  

## Phase 3: VALIDATE  
[ ] ✅ Schema compliance with SCHEMA.md  
[ ] ✅ Agent retrieves >95% relevant docs under load  
[ ] ✅ Injection triggers fire at defined thresholds  
[ ] ✅ Output matches OUTPUT_TEMPLATE.md structure  
[ ] ✅ Hallucination rate <1% in validation corpus
