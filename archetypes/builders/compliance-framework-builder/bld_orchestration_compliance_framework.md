---
kind: collaboration
id: bld_collaboration_compliance_framework
pillar: P12
llm_function: COLLABORATE
purpose: How compliance_framework-builder works in crews with other builders
quality: 8.9
title: "Collaboration Compliance Framework"
version: "1.0.0"
author: wave1_builder_gen
tags: [compliance_framework, builder, collaboration]
tldr: "How compliance_framework-builder works in crews with other builders"
domain: "compliance_framework construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_collaboration_compliance_checklist
  - bld_collaboration_healthcare_vertical
  - bld_collaboration_safety_policy
  - bld_collaboration_enterprise_sla
  - bld_collaboration_legal_vertical
  - compliance-framework-builder
  - bld_examples_compliance_framework
  - bld_collaboration_rbac_policy
  - p03_sp_safety_policy_builder
  - bld_collaboration_discovery_questions
---

## Crew Role  
Maps regulatory requirements to organizational frameworks, automates compliance checks, and generates audit-ready documentation.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Regulator     | Legal requirements    | Document    |  
| Framework     | Existing compliance   | Database    |  
| Stakeholder   | Policy feedback       | Spreadsheet |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Auditor       | Compliance framework  | PDF/JSON    |  
| Legal         | Gap analysis report   | Excel/CSV   |  
| Executive     | Compliance dashboard  | Web         |  

## Boundary  
Does NOT enforce safety policies (handled by safety_policy_builder) or assess threats (handled by threat_model_team).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_compliance_checklist]] | sibling | 0.46 |
| [[bld_collaboration_healthcare_vertical]] | sibling | 0.31 |
| [[bld_collaboration_safety_policy]] | sibling | 0.31 |
| [[bld_collaboration_enterprise_sla]] | sibling | 0.30 |
| [[bld_collaboration_legal_vertical]] | sibling | 0.30 |
| [[compliance-framework-builder]] | upstream | 0.27 |
| [[bld_examples_compliance_framework]] | upstream | 0.26 |
| [[bld_collaboration_rbac_policy]] | sibling | 0.25 |
| [[p03_sp_safety_policy_builder]] | upstream | 0.25 |
| [[bld_collaboration_discovery_questions]] | sibling | 0.24 |
