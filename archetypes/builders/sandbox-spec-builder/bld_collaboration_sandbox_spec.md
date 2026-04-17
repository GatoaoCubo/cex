---
kind: collaboration
id: bld_collaboration_sandbox_spec
pillar: P12
llm_function: COLLABORATE
purpose: How sandbox_spec-builder works in crews with other builders
quality: 8.9
title: "Collaboration Sandbox Spec"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sandbox_spec, builder, collaboration]
tldr: "How sandbox_spec-builder works in crews with other builders"
domain: "sandbox_spec construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Crew Role  
Defines and enforces structural constraints for sandbox environments, ensuring isolation, resource limits, and compliance with team-specific policies.  

## Receives From  
| Builder       | What               | Format      |  
|---------------|--------------------|-------------|  
| Requirements  | Feature spec       | Document    |  
| Security Team | Compliance rules   | JSON        |  
| Infrastructure| Environment template | YAML       |  

## Produces For  
| Builder       | What               | Format      |  
|---------------|--------------------|-------------|  
| Dev Team      | Sandbox config     | YAML        |  
| QA Team       | Test scenarios     | JSON        |  
| Ops Team      | Deployment manifest | Terraform |  

## Boundary  
Does NOT handle interactive playground configurations (handled by `playground_config` builder) or production environment setups (handled by `env_config` builder). Does NOT manage actual deployment; only defines spec boundaries.
