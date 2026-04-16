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
