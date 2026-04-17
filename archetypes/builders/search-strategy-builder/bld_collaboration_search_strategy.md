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
