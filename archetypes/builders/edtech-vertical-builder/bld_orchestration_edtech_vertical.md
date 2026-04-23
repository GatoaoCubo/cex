---
kind: collaboration
id: bld_collaboration_edtech_vertical
pillar: P12
llm_function: COLLABORATE
purpose: How edtech_vertical-builder works in crews with other builders
quality: 8.9
title: "Collaboration Edtech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [edtech_vertical, builder, collaboration]
tldr: "How edtech_vertical-builder works in crews with other builders"
domain: "edtech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_govtech_vertical
  - bld_collaboration_compliance_framework
  - bld_collaboration_sandbox_spec
  - bld_collaboration_reward_model
  - bld_collaboration_legal_vertical
  - bld_collaboration_healthcare_vertical
  - bld_collaboration_discovery_questions
  - bld_collaboration_prompt_technique
  - bld_collaboration_fintech_vertical
  - p03_sp_edtech_vertical_builder
---

## Crew Role  
Designs and structures vertical-specific components (e.g., K-12, higher ed, corporate training) for EdTech platforms, ensuring alignment with industry standards and stakeholder needs.  

## Receives From  
| Builder         | What                  | Format      |  
|-----------------|-----------------------|-------------|  
| EdTech vertical KC | Vertical requirements | Document    |  
| course_module   | Core framework        | JSON schema |  
| stakeholder team | Feedback priorities   | Email       |  

## Produces For  
| Builder         | What                        | Format      |  
|-----------------|-----------------------------|-------------|  
| platform_dev    | Vertical-specific curriculum | YAML        |  
| UX_design       | Component spec templates    | JSON        |  
| project_mgmt    | Implementation roadmap      | Gantt chart |  

## Boundary  
Does NOT create course content (handled by course_module) or perform compliance audits (handled by compliance_checklist).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_govtech_vertical]] | sibling | 0.32 |
| [[bld_collaboration_compliance_framework]] | sibling | 0.27 |
| [[bld_collaboration_sandbox_spec]] | sibling | 0.27 |
| [[bld_collaboration_reward_model]] | sibling | 0.26 |
| [[bld_collaboration_legal_vertical]] | sibling | 0.25 |
| [[bld_collaboration_healthcare_vertical]] | sibling | 0.25 |
| [[bld_collaboration_discovery_questions]] | sibling | 0.25 |
| [[bld_collaboration_prompt_technique]] | sibling | 0.24 |
| [[bld_collaboration_fintech_vertical]] | sibling | 0.24 |
| [[p03_sp_edtech_vertical_builder]] | upstream | 0.24 |
