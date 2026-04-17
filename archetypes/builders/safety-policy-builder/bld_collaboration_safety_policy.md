---
kind: collaboration
id: bld_collaboration_safety_policy
pillar: P12
llm_function: COLLABORATE
purpose: How safety_policy-builder works in crews with other builders
quality: 8.9
title: "Collaboration Safety Policy"
version: "1.0.0"
author: wave1_builder_gen
tags: [safety_policy, builder, collaboration]
tldr: "How safety_policy-builder works in crews with other builders"
domain: "safety_policy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Crew Role  
Translates safety governance rules into actionable safety policies, ensuring alignment with organizational goals and risk contexts.  

## Receives From  
| Builder       | What                  | Format     |  
|---------------|-----------------------|------------|  
| safety_governance_owner | Governance rules      | JSON       |  
| threat_modeler  | Risk assessment inputs | YAML       |  
| policy_repository | Existing policies   | Markdown   |  

## Produces For  
| Builder       | What                  | Format     |  
|---------------|-----------------------|------------|  
| policy_repository | Safety policy documents | Markdown   |  
| compliance_team   | Policy templates      | JSON       |  
| audit_team    | Policy validation reports | CSV      |  

## Boundary  
Does NOT perform threat modeling (handled by threat_modeler) or map policies to regulations (handled by compliance_framework_builder).
