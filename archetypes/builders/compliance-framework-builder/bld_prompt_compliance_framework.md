---
kind: instruction
id: bld_instruction_compliance_framework
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for compliance_framework
quality: 8.9
title: "Instruction Compliance Framework"
version: "1.0.0"
author: wave1_builder_gen
tags: [compliance_framework, builder, instruction]
tldr: "Step-by-step production process for compliance_framework"
domain: "compliance_framework construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
related:
  - compliance-framework-builder
  - bld_instruction_safety_policy
  - p10_lr_compliance_framework_builder
  - p03_sp_compliance_framework_builder
  - p11_qg_compliance_framework
  - bld_knowledge_card_compliance_framework
  - bld_examples_compliance_framework
  - bld_instruction_compliance_checklist
  - kc_compliance_framework
  - bld_instruction_eval_framework
---

## Phase 1: RESEARCH  
1. Identify applicable regulations (e.g., GDPR, AI Act) for AI system deployment.  
2. Map regulatory requirements to AI system components (data, algorithms, governance).  
3. Analyze gaps between current AI system practices and regulatory mandates.  
4. Interview legal and compliance stakeholders to validate regulatory scope.  
5. Create a regulatory matrix linking AI system functions to compliance obligations.  
6. Document jurisdictional differences impacting cross-border AI deployment.  

## Phase 2: COMPOSE  
1. Use SCHEMA.md to structure artifact sections: Scope, Regulatory Mapping, Constraints.  
2. Populate "Regulatory Mapping" with regulation names, clauses, and AI system alignment.  
3. Define "Constraints" using OUTPUT_TEMPLATE.md’s attestation workflow and audit trails.  
4. Specify enforcement mechanisms (e.g., automated checks, manual reviews) per regulation.  
5. Embed examples of non-compliance scenarios and mitigation strategies.  
6. Align artifact language with regulatory terminology (e.g., "data minimization," "bias audits").  
7. Reference SCHEMA.md’s metadata fields for versioning and jurisdiction tags.  
8. Add attestation templates for stakeholder sign-off (e.g., legal, technical leads).  
9. Finalize artifact with cross-references to OUTPUT_TEMPLATE.md’s compliance checklist.  

## Phase 3: VALIDATE  
- [ ] Verify regulatory mapping matches Phase 1 findings and jurisdictional scope.  
- [ ] Confirm all constraints align with SCHEMA.md’s defined compliance controls.  
- [ ] Test attestation workflow against OUTPUT_TEMPLATE.md’s sign-off requirements.  
- [ ] Obtain stakeholder approval for constraint mechanisms and audit trails.  
- [ ] Validate artifact completeness via red-team review for missing regulatory clauses.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[compliance-framework-builder]] | downstream | 0.38 |
| [[bld_instruction_safety_policy]] | sibling | 0.37 |
| [[p10_lr_compliance_framework_builder]] | downstream | 0.35 |
| [[p03_sp_compliance_framework_builder]] | related | 0.34 |
| [[p11_qg_compliance_framework]] | downstream | 0.33 |
| [[bld_knowledge_card_compliance_framework]] | upstream | 0.32 |
| [[bld_examples_compliance_framework]] | downstream | 0.31 |
| [[bld_instruction_compliance_checklist]] | sibling | 0.30 |
| [[kc_compliance_framework]] | upstream | 0.30 |
| [[bld_instruction_eval_framework]] | sibling | 0.29 |
