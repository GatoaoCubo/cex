---
kind: collaboration
id: bld_collaboration_action_paradigm
pillar: P12
llm_function: COLLABORATE
purpose: How action_paradigm-builder works in crews with other builders
quality: null
title: "Collaboration Action Paradigm"
version: "1.0.0"
author: wave1_builder_gen
tags: [action_paradigm, builder, collaboration]
tldr: "How action_paradigm-builder works in crews with other builders"
domain: "action_paradigm construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Crew Role  
Orchestrates action execution workflows, decomposing high-level goals into executable steps, ensuring alignment with domain constraints and resource availability.  

## Receives From  
| Builder       | What               | Format      |  
|---------------|--------------------|-------------|  
| Task Planner  | Goal definitions   | JSON        |  
| ResourceMgr   | Available resources| YAML        |  
| Validator     | Constraint rules   | Structured  |  
| Monitor       | Status updates     | JSON        |  

## Produces For  
| Builder       | What               | Format      |  
|---------------|--------------------|-------------|  
| Executor      | Action plan        | JSON        |  
| Logger        | Execution logs     | YAML        |  
| FeedbackSys   | Completion signals | Structured  |  
| ErrorHandler  | Failure reports    | JSON        |  

## Boundary  
Does NOT execute actions directly (handled by Executor), manage user interfaces (handled by Agent-Computer Interface), or handle low-level system interactions (handled by CLI tools).
