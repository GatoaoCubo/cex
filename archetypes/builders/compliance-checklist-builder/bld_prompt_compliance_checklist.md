---
kind: instruction
id: bld_instruction_compliance_checklist
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for compliance_checklist
quality: 8.9
title: "Instruction Compliance Checklist"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [compliance_checklist, builder, instruction]
tldr: "Step-by-step production process for compliance_checklist"
domain: "compliance_checklist construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - compliance-checklist-builder
  - bld_knowledge_card_compliance_checklist
  - p10_mem_compliance_checklist_builder
  - p03_sp_compliance_checklist_builder
  - p11_qg_compliance_checklist
  - audit-log-builder
  - bld_examples_compliance_checklist
  - bld_instruction_compliance_framework
  - kc_compliance_checklist
  - compliance-framework-builder
---

## Phase 1: RESEARCH  
1. Gather SOC2 Trust Service Criteria, GDPR data protection principles, HIPAA security rules, and EU AI Act compliance requirements.  
2. Map regulatory controls to organizational processes (e.g., access logs, data encryption, AI transparency).  
3. Identify gaps in current policies versus audit standards for each regulation.  
4. Consult legal frameworks and audit reports for recent enforcement actions.  
5. Interview compliance officers and IT teams for operational context.  
6. Document findings in a structured format for artifact development.  

## Phase 2: COMPOSE  
1. Define checklist structure using bld_schema_compliance_checklist.md (sections: scope, controls, evidence).  
2. Populate SOC2 Trust Principles (Security, Availability, Processing Integrity).  
3. Add GDPR requirements (data minimization, consent, breach notification).  
4. Insert HIPAA-specific controls (PHI safeguards, audit trails).  
5. Align EU AI Act sections (risk assessment, transparency, human oversight).  
6. Use bld_output_template_compliance_checklist.md to standardize language and formatting.  
7. Assign control IDs and reference audit standards (e.g., ISO 27001, NIST).  
8. Include evidence types (e.g., policies, logs, certifications).  
9. Review for regulatory overlap and ensure no duplication.  

## Phase 3: VALIDATE  
- [ ] [OK] Verify alignment with SOC2, GDPR, HIPAA, and EU AI Act mandates.  
- [ ] [OK] Confirm all controls are actionable and measurable.  
- [ ] [OK] Ensure terminology matches audit standards (e.g., "data subject" vs. "user").  
- [ ] [OK] Validate schema adherence (section headers, control IDs).  
- [ ] [OK] Obtain stakeholder approval (legal, compliance, IT).


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[compliance-checklist-builder]] | downstream | 0.46 |
| [[bld_knowledge_card_compliance_checklist]] | upstream | 0.45 |
| [[p10_mem_compliance_checklist_builder]] | downstream | 0.39 |
| [[p03_sp_compliance_checklist_builder]] | related | 0.38 |
| [[p11_qg_compliance_checklist]] | downstream | 0.35 |
| [[audit-log-builder]] | downstream | 0.34 |
| [[bld_examples_compliance_checklist]] | downstream | 0.34 |
| [[bld_instruction_compliance_framework]] | sibling | 0.33 |
| [[kc_compliance_checklist]] | upstream | 0.31 |
| [[compliance-framework-builder]] | downstream | 0.30 |
