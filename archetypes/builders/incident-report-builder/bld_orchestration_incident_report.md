---
kind: collaboration
id: bld_collaboration_incident_report
pillar: P12
llm_function: COLLABORATE
purpose: How incident_report-builder works in crews with other builders
quality: 8.9
title: "Collaboration Incident Report"
version: "1.0.0"
author: wave1_builder_gen
tags: [incident_report, builder, collaboration]
tldr: "How incident_report-builder works in crews with other builders"
domain: "incident_report construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - incident-report-builder
  - p03_sp_incident_report_builder
  - bld_architecture_incident_report
  - bld_knowledge_card_incident_report
  - bld_instruction_incident_report
  - kc_incident_report
  - bld_tools_incident_report
  - bld_collaboration_self_improvement_loop
  - n05_audit_incident_report_builder
  - bld_schema_incident_report
---

## Crew Role  
Structures incident data into post-mortem reports, ensuring clarity, accountability, and actionable insights for teams.  

## Receives From  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Monitoring    | Raw incident logs     | JSON        |  
| Stakeholders  | Feedback on incident  | Plain text  |  
| Incident Triage | Initial summary     | Markdown    |  

## Produces For  
| Builder       | What                  | Format      |  
|---------------|-----------------------|-------------|  
| Post-Mortem   | Structured report     | Markdown    |  
| Leadership    | Executive summary     | PDF         |  
| Analytics     | Incident data export  | CSV         |  

## Boundary  
Does NOT handle auto-fixes (bugloop) or generic learning (learning_record). Auto-fixes are resolved by bugloop; learning records are managed by learning_record.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[incident-report-builder]] | upstream | 0.47 |
| [[p03_sp_incident_report_builder]] | upstream | 0.41 |
| [[bld_architecture_incident_report]] | upstream | 0.34 |
| [[bld_knowledge_card_incident_report]] | upstream | 0.34 |
| [[bld_instruction_incident_report]] | upstream | 0.27 |
| [[kc_incident_report]] | upstream | 0.27 |
| [[bld_tools_incident_report]] | upstream | 0.26 |
| [[bld_collaboration_self_improvement_loop]] | sibling | 0.25 |
| [[n05_audit_incident_report_builder]] | upstream | 0.23 |
| [[bld_schema_incident_report]] | upstream | 0.22 |
