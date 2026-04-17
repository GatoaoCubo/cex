---
kind: collaboration
id: bld_collaboration_agent_profile
pillar: P12
llm_function: COLLABORATE
purpose: How agent_profile-builder works in crews with other builders
quality: 8.7
title: "Collaboration Agent Profile"
version: "1.0.0"
author: wave1_builder_gen
tags: [agent_profile, builder, collaboration]
tldr: "How agent_profile-builder works in crews with other builders"
domain: "agent_profile construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Crew Role  
Crafts agent personas by synthesizing input constraints, mission statements, and role-specific traits into coherent, boundary-compliant profiles.  

## Receives From  
Builder | What | Format  
--- | --- | ---  
MissionStmt | High-level mission statement | Text  
RoleDesc | Role-specific responsibilities | JSON  
Constraints | Ethical/operational limits | YAML  

## Produces For  
Builder | What | Format  
--- | --- | ---  
PersonaDraft | Structured persona outline | JSON  
ValidationReport | Compliance check against constraints | Markdown  
Summary | Key traits and boundaries | CSV  

## Boundary  
Does NOT define full agent capabilities (handled by `agent_full-builder`) or refine system prompts (handled by `system_prompt-refiner`).
