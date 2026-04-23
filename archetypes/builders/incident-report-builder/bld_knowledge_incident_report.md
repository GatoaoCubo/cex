---
kind: knowledge_card
id: bld_knowledge_card_incident_report
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for incident_report production
quality: 9.2
title: "Knowledge Card Incident Report"
version: "1.0.0"
author: wave1_builder_gen
tags: [incident_report, builder, knowledge_card]
tldr: "Domain knowledge for incident_report production"
domain: "incident_report construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - incident-report-builder
  - p03_sp_incident_report_builder
  - kc_incident_report
  - bld_collaboration_incident_report
  - bld_instruction_incident_report
  - n05_audit_incident_report_builder
  - bld_output_template_incident_report
  - p10_lr_incident_report_builder
  - bld_architecture_incident_report
  - bld_schema_incident_report
---

## Domain Overview  
Incident reports in AI systems document the lifecycle of critical failures, focusing on root cause analysis, impact assessment, and corrective actions. Unlike traditional software incidents, AI-related events often involve complex interactions between data, models, and infrastructure, requiring specialized investigation techniques. Post-mortems are central to SRE (Site Reliability Engineering) practices, ensuring transparency and systemic improvements. Industry leaders like Google and Microsoft emphasize blameless post-mortems to foster learning without punitive measures.  

AI incident reports must address unique challenges: model drift, data biases, inference errors, and integration with legacy systems. Standards such as IEEE 1220-2010 and ISO/IEC 25010 provide frameworks for reliability and quality, while NIST guidelines stress incident response rigor. Effective reports balance technical detail with stakeholder communication, aligning with the "blameless culture" advocated by SRE communities.  

## Key Concepts  
| Concept              | Definition                                                                 | Source                      |  
|----------------------|----------------------------------------------------------------------------|-----------------------------|  
| Incident             | Unplanned event disrupting system functionality or safety                 | Google SRE Book           |  
| Root Cause           | Fundamental flaw enabling an incident, often non-obvious                  | Microsoft Post-Mortem Guide |  
| Timeline             | Chronological record of incident occurrence and response                  | IEEE 1220-2010             |  
| Impact Assessment    | Quantification of downtime, financial loss, or reputational damage        | ISO/IEC 25010             |  
| Mitigation           | Immediate steps to contain incident effects                               | NIST SP 800-61            |  
| Owner                | Primary team/individual accountable for incident resolution               | SRE Best Practices        |  
| Severity             | Classification based on scope, duration, and risk (e.g., P1-P5)           | Atlassian Incident Guide  |  
| Blameless Culture    | Post-mortem approach avoiding punitive blame to encourage transparency    | Etsy SRE Blog             |  
| Action Items         | Specific, measurable tasks to prevent recurrence                          | Harvard CSAIL Report      |  
| Lessons Learned      | Generalizable insights from incident analysis                             | ACM SIGOPS                |  
| Escalation Path      | Defined workflow for notifying stakeholders during incidents              | AWS Incident Response     |  
| Post-Mortem          | Document summarizing incident, analysis, and improvements                 | Google SRE Book           |  

## Industry Standards  
- Google SRE Book (Incident Management)  
- IEEE 1220-2010 (System Reliability)  
- ISO/IEC 25010 (System Quality Attributes)  
- NIST SP 800-61 (Incident Response)  
- ACM SIGOPS Post-Mortem Guidelines  
- Microsoft Azure Incident Response Framework  

## Common Patterns  
1. **Structured Timeline** – Log events with timestamps, actors, and system states.  
2. **5 Whys Analysis** – Iterative questioning to identify root causes.  
3. **Blameless Ownership** – Assign responsibility without attributing fault.  
4. **Cross-Functional Review** – Involve engineering, ops, and business stakeholders.  
5. **Actionable Metrics** – Track resolution time, recurrence rates, and remediation progress.  
6. **Template Consistency** – Use standardized sections (e.g., summary, analysis, lessons).  

## Pitfalls  
- **Assigning Blame** – Discourages honesty and stifles collaboration.  
- **Incomplete Data** – Omitting logs or context leads to flawed analysis.  
- **Delayed Reporting** – Prolongs downtime and obscures true root causes.  
- **Ignoring Non-Technical Factors** – Overlooking organizational or process issues.  
- **No Follow-Up** – Action items left untracked result in recurring incidents.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[incident-report-builder]] | downstream | 0.60 |
| [[p03_sp_incident_report_builder]] | downstream | 0.47 |
| [[kc_incident_report]] | sibling | 0.43 |
| [[bld_collaboration_incident_report]] | downstream | 0.43 |
| [[bld_instruction_incident_report]] | downstream | 0.39 |
| [[n05_audit_incident_report_builder]] | downstream | 0.37 |
| [[bld_output_template_incident_report]] | downstream | 0.34 |
| [[p10_lr_incident_report_builder]] | downstream | 0.34 |
| [[bld_architecture_incident_report]] | downstream | 0.34 |
| [[bld_schema_incident_report]] | downstream | 0.34 |
