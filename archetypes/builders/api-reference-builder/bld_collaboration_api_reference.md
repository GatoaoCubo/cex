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
