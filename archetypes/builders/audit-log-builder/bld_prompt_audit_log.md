---
kind: instruction
id: bld_instruction_audit_log
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for audit_log
quality: 8.9
title: "Instruction Audit Log"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [audit_log, builder, instruction]
tldr: "Step-by-step production process for audit_log"
domain: "audit_log construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - audit-log-builder
  - bld_knowledge_card_audit_log
  - p10_mem_audit_log_builder
  - kc_audit_log
  - p03_sp_audit_log_builder
  - bld_examples_audit_log
  - bld_instruction_compliance_checklist
  - p11_qg_audit_log
  - bld_tools_audit_log
  - compliance-checklist-builder
---

## Phase 1: RESEARCH  
1. Identify SOC2 Type II audit requirements for log immutability and retention  
2. Map system components requiring audit logging (e.g., user access, configuration changes)  
3. Analyze existing log formats and storage mechanisms for compliance gaps  
4. Evaluate cryptographic hashing requirements for log integrity verification  
5. Determine retention periods aligned with regulatory and organizational policies  
6. Document audit control objectives from SOC2 Trust Service Criteria  

## Phase 2: COMPOSE  
1. Define log schema in bld_schema_audit_log.md with fields: timestamp, actor, action, resource, outcome, hash  
2. Specify immutability via cryptographic hash chaining in log entries  
3. Map SOC2 controls (e.g., CC7.1, CC11.2) to audit log events in bld_knowledge_card_audit_log.md  
4. Write log configuration using bld_output_template_audit_log.md format with YAML anchors  
5. Implement tamper-evident storage (e.g., write-once filesystem, WORM storage anchoring)  
6. Embed log retention policy as a top-level attribute in the artifact  
7. Add metadata for SOC2 attestation scope and audit trail scope  
8. Reference bld_schema_audit_log.md in the artifact's $schema property  
9. Finalize with cryptographic signature of the configuration file  

## Phase 3: VALIDATE  
[ ] [OK] Verify schema compliance using JSON Schema validator  
[ ] [OK] Confirm immutability mechanisms prevent log modification  
[ ] [OK] Validate retention policy aligns with SOC2 Type II requirements  
[ ] [OK] Ensure all mapped controls are represented in log events  
[ ] [OK] Confirm artifact passes SOC2 attestation checklist for audit logs


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[audit-log-builder]] | downstream | 0.53 |
| [[bld_knowledge_card_audit_log]] | upstream | 0.44 |
| [[p10_mem_audit_log_builder]] | downstream | 0.40 |
| [[kc_audit_log]] | upstream | 0.38 |
| [[p03_sp_audit_log_builder]] | related | 0.31 |
| [[bld_examples_audit_log]] | downstream | 0.30 |
| [[bld_instruction_compliance_checklist]] | sibling | 0.28 |
| [[p11_qg_audit_log]] | downstream | 0.26 |
| [[bld_tools_audit_log]] | downstream | 0.24 |
| [[compliance-checklist-builder]] | downstream | 0.23 |
