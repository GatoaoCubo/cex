---
kind: instruction
id: bld_instruction_incident_report
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for incident_report
quality: 8.9
title: "Instruction Incident Report"
version: "1.0.0"
author: wave1_builder_gen
tags: [incident_report, builder, instruction]
tldr: "Step-by-step production process for incident_report"
domain: "incident_report construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - bld_examples_incident_report
  - kc_incident_report
  - incident-report-builder
  - p03_sp_incident_report_builder
  - bld_schema_incident_report
  - p11_qg_incident_report
  - bld_knowledge_card_incident_report
  - p10_lr_incident_report_builder
  - bld_instruction_safety_policy
  - bld_collaboration_incident_report
---

## Phase 1: RESEARCH  
1. Gather incident details: date, time, affected systems, and user impact.  
2. Identify stakeholders: developers, operators, and compliance officers involved.  
3. Collect logs, error traces, and AI model outputs from the incident window.  
4. Analyze root cause: code defects, data drift, or misconfigured governance rules.  
5. Document timeline: sequence of events with timestamps and responsible parties.  
6. Review AI governance policies and incident response protocols.  

## Phase 2: COMPOSE  
1. Outline sections per SCHEMA.md: summary, timeline, root cause, corrective actions.  
2. Draft incident summary: impact, severity, and initial hypothesis.  
3. Write detailed timeline using OUTPUT_TEMPLATE.md’s chronological format.  
4. Describe root cause with technical specifics and policy violations.  
5. Propose corrective actions: code fixes, model retraining, or policy updates.  
6. List lessons learned: systemic gaps and recommendations for prevention.  
7. Attach evidence: logs, model outputs, and stakeholder statements.  
8. Peer-review draft for clarity, completeness, and alignment with SCHEMA.md.  
9. Finalize report with version control and metadata (author, date, incident ID).  

## Phase 3: VALIDATE  
□ All required fields in SCHEMA.md are present.  
□ Timeline aligns with logs and stakeholder accounts.  
□ Root cause analysis cites specific technical or policy failures.  
□ Corrective actions are actionable and measurable.  
□ Report passes compliance check for P11 governance standards.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_incident_report]] | downstream | 0.34 |
| [[kc_incident_report]] | upstream | 0.33 |
| [[incident-report-builder]] | downstream | 0.32 |
| [[p03_sp_incident_report_builder]] | related | 0.30 |
| [[bld_schema_incident_report]] | downstream | 0.28 |
| [[p11_qg_incident_report]] | downstream | 0.28 |
| [[bld_knowledge_card_incident_report]] | upstream | 0.28 |
| [[p10_lr_incident_report_builder]] | downstream | 0.27 |
| [[bld_instruction_safety_policy]] | sibling | 0.25 |
| [[bld_collaboration_incident_report]] | downstream | 0.24 |
