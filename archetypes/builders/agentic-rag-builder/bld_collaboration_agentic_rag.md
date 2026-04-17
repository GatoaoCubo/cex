---
kind: collaboration
id: bld_collaboration_agentic_rag
pillar: P12
llm_function: COLLABORATE
purpose: How agentic_rag-builder works in crews with other builders
quality: 8.9
title: "Collaboration Agentic Rag"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [agentic_rag, builder, collaboration]
tldr: "How agentic_rag-builder works in crews with other builders"
domain: "agentic_rag construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Orchestrates the Agentic RAG workflow by integrating retrieval, generation, and feedback loops, ensuring alignment between data sources, query intent, and output quality.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Data Source   | Raw document content  | CSV/SQL     |  
| User Interface| Query intent          | Text        |  
| Retrieval     | Ranked document snippets| JSON        |  
| Feedback Loop | User evaluation data  | YAML        |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Generation    | Contextual response   | Text        |  
| Metadata Store| Query-document mapping| JSON        |  
| UI/UX         | Structured output     | HTML/Markdown|  
| Optimization  | Performance metrics   | CSV         |  

## Boundary  
Does NOT handle raw data preprocessing (Data Engineers), agent behavior definition (Agent Developers), or end-user interface design (UI/UX Team).
