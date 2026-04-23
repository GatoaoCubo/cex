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
related:
  - bld_collaboration_action_paradigm
  - bld_collaboration_search_strategy
  - bld_collaboration_reasoning_strategy
  - bld_collaboration_self_improvement_loop
  - bld_collaboration_collaboration_pattern
  - bld_collaboration_sandbox_config
  - bld_architecture_planning_strategy
  - bld_collaboration_ab_test_config
  - bld_collaboration_agent_profile
  - bld_collaboration_cohort_analysis
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_action_paradigm]] | sibling | 0.26 |
| [[bld_collaboration_search_strategy]] | sibling | 0.25 |
| [[bld_collaboration_reasoning_strategy]] | sibling | 0.24 |
| [[bld_collaboration_self_improvement_loop]] | sibling | 0.23 |
| [[bld_collaboration_collaboration_pattern]] | sibling | 0.22 |
| [[bld_collaboration_sandbox_config]] | sibling | 0.22 |
| [[bld_architecture_planning_strategy]] | upstream | 0.21 |
| [[bld_collaboration_ab_test_config]] | sibling | 0.21 |
| [[bld_collaboration_agent_profile]] | sibling | 0.21 |
| [[bld_collaboration_cohort_analysis]] | sibling | 0.21 |
