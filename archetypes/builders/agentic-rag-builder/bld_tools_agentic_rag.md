---
kind: tools
id: bld_tools_agentic_rag
pillar: P04
llm_function: CALL
purpose: Tools available for agentic_rag production
quality: null
title: "Tools Agentic Rag"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [agentic_rag, builder, tools]
tldr: "Tools available for agentic_rag production"
domain: "agentic_rag construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Production Tools  
| Tool | Purpose | When |  
| --- | --- | --- |  
| cex_compile.py | Compiles RAG components into an executable agent | During deployment |  
| cex_score.py | Evaluates agent performance using metrics like accuracy and latency | Post-deployment testing |  
| cex_retriever.py | Fetches relevant documents from external knowledge sources | During query processing |  
| cex_doctor.py | Diagnoses and fixes common agent errors | Debugging sessions |  
| cex_validator.py | Ensures compliance with data governance policies | Pre-deployment |  
| cex_optimizer.py | Fine-tunes agent parameters for optimal resource usage | Performance tuning |  

## Validation Tools  
| Tool | Purpose | When |  
| --- | --- | --- |  
| val_check.py | Validates input/output integrity and schema consistency | Pre-processing |  
| consistency_checker.py | Ensures alignment between retrieved data and generated responses | Post-retrieval |  
| unit_tester.py | Executes automated tests for individual agent modules | Development phase |  
| data_integrity.py | Verifies the accuracy and completeness of training data | Pre-training |  

## External References  
- **LangChain**: Framework for building agentic workflows with LLMs  
- **LlamaIndex**: Toolkit for integrating vector databases with RAG pipelines  
- **AgenticRAGFramework**: Reference implementation for modular, scalable RAG agents
