---
kind: collaboration
id: bld_collaboration_compliance_checklist
pillar: P12
llm_function: COLLABORATE
purpose: How compliance_checklist-builder works in crews with other builders
quality: 8.9
title: "Collaboration Compliance Checklist"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [compliance_checklist, builder, collaboration]
tldr: "How compliance_checklist-builder works in crews with other builders"
domain: "compliance_checklist construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_collaboration_compliance_framework
  - bld_collaboration_healthcare_vertical
  - bld_collaboration_safety_policy
  - bld_collaboration_govtech_vertical
  - compliance-checklist-builder
  - bld_examples_compliance_framework
  - bld_collaboration_enterprise_sla
  - bld_collaboration_sandbox_spec
  - p03_sp_compliance_framework_builder
  - bld_instruction_compliance_framework
---

## Crew Role  
Coordinates creation of audit-specific compliance checklists, ensuring alignment with regulatory requirements and organizational policies.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Compliance Officer | Regulatory updates  | Document    |  
| Auditor       | Scope of audit        | Form        |  
| Legal Team    | Policy changes        | Email       |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Compliance Officer | Final checklist     | PDF         |  
| Auditor       | Executable checklist  | Shared Doc  |  
| Management    | Review summary        | Dashboard   |  

## Boundary  
Does NOT enforce runtime compliance or define safety policies. Guardrail checks and behavioral policies are handled by dedicated guardrail_checker and safety_policy_enforcer builders.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_compliance_framework]] | sibling | 0.48 |
| [[bld_collaboration_healthcare_vertical]] | sibling | 0.34 |
| [[bld_collaboration_safety_policy]] | sibling | 0.32 |
| [[bld_collaboration_govtech_vertical]] | sibling | 0.30 |
| [[compliance-checklist-builder]] | upstream | 0.30 |
| [[bld_examples_compliance_framework]] | upstream | 0.28 |
| [[bld_collaboration_enterprise_sla]] | sibling | 0.27 |
| [[bld_collaboration_sandbox_spec]] | sibling | 0.26 |
| [[p03_sp_compliance_framework_builder]] | upstream | 0.26 |
| [[bld_instruction_compliance_framework]] | upstream | 0.25 |
