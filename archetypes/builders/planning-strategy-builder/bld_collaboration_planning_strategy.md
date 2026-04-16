---
kind: collaboration
id: bld_collaboration_planning_strategy
pillar: P12
llm_function: COLLABORATE
purpose: How planning_strategy-builder works in crews with other builders
quality: 8.9
title: "Collaboration Planning Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [planning_strategy, builder, collaboration]
tldr: "How planning_strategy-builder works in crews with other builders"
domain: "planning_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Crew Role  
Coordinates high-level planning steps, aligns team objectives, and defines strategic priorities without executing tasks or reasoning through specifics.  

## Receives From  
| Builder | What | Format |  
|---|---|---|  
| Strategy Owner | Mission goals | JSON |  
| Resource Manager | Availability constraints | CSV |  
| Risk Analyst | Potential obstacles | Text |  
| Stakeholder | Preference inputs | Markdown |  

## Produces For  
| Builder | What | Format |  
|---|---|---|  
| Execution Planner | Prioritized action sequences | YAML |  
| Communication Lead | Summary briefs | PDF |  
| Monitoring System | KPI alignment checklist | JSON |  
| Risk Analyst | Mitigation focus areas | Text |  

## Boundary  
Does NOT handle task execution (workflow_executor), detailed reasoning (reasoning_engine), or real-time data processing (data_pipeline). These are managed by dedicated components.
