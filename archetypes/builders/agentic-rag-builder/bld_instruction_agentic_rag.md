---
kind: instruction
id: bld_instruction_agentic_rag
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for agentic_rag
quality: 8.8
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
1. Define agent state schema in bld_schema_agentic_rag.md (include memory, context, intent)  
2. Implement retrieval module with vector DB and filter syntax  
3. Write agent planner using ReAct or Self-RAG retrieve->reflect->re-query loop  
4. Configure reflection triggers: low-confidence retrieval, contradictory evidence  
5. Integrate RAG results into agent decision context with provenance tracking  
6. Use bld_output_template_agentic_rag.md for structured response formatting  
7. Add fallback logic for retrieval failures (CRAG corrective fallback)  
8. Embed domain-specific prompt engineering in injection pipelines  
9. Conduct unit tests for each RAG-agent interaction layer  

## Phase 3: VALIDATE  
[ ] Schema compliance with bld_schema_agentic_rag.md  
[ ] Retrieve->reflect->re-query loop terminates within max_reflection_iterations  
[ ] Injection triggers fire at defined thresholds  
[ ] Output matches bld_output_template_agentic_rag.md structure  
[ ] Fallback chain activates on retrieval failure
