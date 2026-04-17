---
kind: collaboration
id: bld_collaboration_sdk_example
pillar: P12
llm_function: COLLABORATE
purpose: How sdk_example-builder works in crews with other builders
quality: 8.9
title: "Collaboration Sdk Example"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sdk_example, builder, collaboration]
tldr: "How sdk_example-builder works in crews with other builders"
domain: "sdk_example construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Builds executable SDK examples by translating API specs into code, ensuring compatibility and correctness.  

## Receives From  
| Builder       | What              | Format      |  
|---------------|-------------------|-------------|  
| API Spec Team | API definition    | YAML        |  
| Config Team   | SDK config file   | JSON        |  
| User          | Example scenario   | Text file   |  

## Produces For  
| Builder       | What              | Format      |  
|---------------|-------------------|-------------|  
| SDK Consumer  | SDK example code  | Python      |  
| QA Team       | Test case         | Code        |  
| Docs Team     | Doc snippet       | Markdown    |  

## Boundary  
Does NOT handle API reference docs (api_ref_builder), integration guides (integration_guide_builder), backend logic (backend_team), or deployment (ops_team).
