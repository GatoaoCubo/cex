---
kind: collaboration
id: bld_collaboration_api_reference
pillar: P12
llm_function: COLLABORATE
purpose: How api_reference-builder works in crews with other builders
quality: 8.9
title: "Collaboration Api Reference"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [api_reference, builder, collaboration]
tldr: "How api_reference-builder works in crews with other builders"
domain: "api_reference construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_sdk_example
  - p03_sp_api_reference_builder
  - bld_collaboration_integration_guide
  - sdk-example-builder
  - api-reference-builder
  - bld_collaboration_llm_evaluation_scenario
  - bld_collaboration_visual_workflow
  - bld_collaboration_code_executor
  - bld_collaboration_prompt_technique
  - bld_collaboration_ab_test_config
---

## Crew Role  
Generates and maintains accurate, up-to-date API reference documentation from specifications, ensuring clarity for developers and users.  

## Receives From  
| Builder      | What               | Format       |  
|--------------|--------------------|--------------|  
| spec_builder | API specifications | OpenAPI JSON |  
| code_builder | Code samples       | Markdown     |  
| design_system| UI component specs | Figma        |  

## Produces For  
| Builder      | What                     | Format       |  
|--------------|--------------------------|--------------|  
| docs_team    | API reference docs       | Markdown     |  
| dev_team     | SDK example snippets     | Code blocks  |  
| qa_team      | Test case definitions    | JSON         |  

## Boundary  
Does NOT validate schema correctness (spec_validator handles this) or implement code (code_builder handles this). Deployment of docs is managed by the deployment_team.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_sdk_example]] | sibling | 0.40 |
| [[p03_sp_api_reference_builder]] | upstream | 0.26 |
| [[bld_collaboration_integration_guide]] | sibling | 0.26 |
| [[sdk-example-builder]] | upstream | 0.24 |
| [[api-reference-builder]] | upstream | 0.22 |
| [[bld_collaboration_llm_evaluation_scenario]] | sibling | 0.21 |
| [[bld_collaboration_visual_workflow]] | sibling | 0.21 |
| [[bld_collaboration_code_executor]] | sibling | 0.21 |
| [[bld_collaboration_prompt_technique]] | sibling | 0.20 |
| [[bld_collaboration_ab_test_config]] | sibling | 0.20 |
