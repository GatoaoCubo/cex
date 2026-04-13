---
kind: collaboration
id: bld_collaboration_reasoning_strategy
pillar: P12
llm_function: COLLABORATE
purpose: How reasoning_strategy-builder works in crews with other builders
quality: null
title: "Collaboration Reasoning Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [reasoning_strategy, builder, collaboration]
tldr: "How reasoning_strategy-builder works in crews with other builders"
domain: "reasoning_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Crew Role  
Designs structured reasoning approaches, ensuring logical coherence, adaptability, and alignment with team objectives.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Problem Analyst | Problem definitions   | JSON        |  
| Data Curator  | Dataset metadata      | CSV         |  
| Evaluator     | Strategy performance  | Metrics log |  
| Strategy Librarian | Existing strategies | YAML        |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Execution Engine | Reasoning strategy  | Structured config |  
| Evaluator     | Testable strategy     | JSON        |  
| Strategy Librarian | Documented strategy | Markdown    |  
| Problem Analyst | Strategy refinements  | Feedback log |  

## Boundary  
Does NOT handle prompt engineering (prompt_technique) or resource allocation (thinking_config). Prompt_technique is managed by a prompt engineer; thinking_config by a resource manager.
