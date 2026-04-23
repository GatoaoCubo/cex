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
related:
  - safety-policy-builder
  - p03_sp_safety_policy_builder
  - bld_examples_safety_policy
  - bld_collaboration_threat_model
  - bld_collaboration_compliance_framework
  - bld_collaboration_compliance_checklist
  - bld_collaboration_sso_config
  - bld_collaboration_ai_rmf_profile
  - bld_collaboration_rbac_policy
  - bld_collaboration_content_filter
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

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[safety-policy-builder]] | upstream | 0.43 |
| [[p03_sp_safety_policy_builder]] | upstream | 0.32 |
| [[bld_examples_safety_policy]] | upstream | 0.31 |
| [[bld_collaboration_threat_model]] | sibling | 0.30 |
| [[bld_collaboration_compliance_framework]] | sibling | 0.28 |
| [[bld_collaboration_compliance_checklist]] | sibling | 0.28 |
| [[bld_collaboration_sso_config]] | sibling | 0.27 |
| [[bld_collaboration_ai_rmf_profile]] | sibling | 0.27 |
| [[bld_collaboration_rbac_policy]] | sibling | 0.27 |
| [[bld_collaboration_content_filter]] | sibling | 0.26 |
