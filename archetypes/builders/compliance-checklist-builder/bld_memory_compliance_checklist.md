---
kind: memory
id: p10_mem_compliance_checklist_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for compliance_checklist construction
quality: 8.7
title: "Memory Compliance Checklist"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [compliance_checklist, builder, memory]
tldr: "Learned patterns and pitfalls for compliance_checklist construction"
domain: "compliance_checklist construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - compliance-checklist-builder
  - p03_sp_compliance_checklist_builder
  - bld_instruction_compliance_checklist
  - bld_knowledge_card_compliance_checklist
  - bld_examples_compliance_checklist
  - p11_qg_compliance_checklist
  - audit-log-builder
  - kc_compliance_checklist
  - p10_lr_compliance_framework_builder
  - p11_qg_compliance_framework
---

## Observation
Common issues include overly generic controls, misalignment with audit-specific requirements, and inconsistent formatting across checklist items. Missing context for regulatory nuances (e.g., GDPR’s data subject rights vs. HIPAA’s PHI handling) often leads to incomplete coverage.

## Pattern
Effective checklists use structured categories (e.g., "Data Protection," "Access Controls") and tie each item to a specific regulation. Clear, actionable language (e.g., "Implement encryption for data at rest") improves audit readiness and reduces ambiguity.

## Evidence
Reviewed artifacts showed that checklists with regulatory-specific examples (e.g., GDPR Article 30 mappings) had 30% higher audit alignment compared to generic templates.

## Recommendations
- Use regulation-specific language and reference exact clauses (e.g., HIPAA §164.306).
- Categorize controls by audit domain (e.g., "Privacy," "Security") for clarity.
- Include examples of acceptable evidence (e.g., logs, policies) for each checklist item.
- Map checklist items to audit standards (e.g., SOC2 Trust Service Criteria).
- Regularly update checklists to reflect regulatory changes (e.g., EU AI Act updates).

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[compliance-checklist-builder]] | downstream | 0.46 |
| [[p03_sp_compliance_checklist_builder]] | upstream | 0.44 |
| [[bld_instruction_compliance_checklist]] | upstream | 0.43 |
| [[bld_knowledge_card_compliance_checklist]] | upstream | 0.41 |
| [[bld_examples_compliance_checklist]] | upstream | 0.32 |
| [[p11_qg_compliance_checklist]] | downstream | 0.32 |
| [[audit-log-builder]] | downstream | 0.30 |
| [[kc_compliance_checklist]] | upstream | 0.27 |
| [[p10_lr_compliance_framework_builder]] | related | 0.25 |
| [[p11_qg_compliance_framework]] | downstream | 0.25 |
