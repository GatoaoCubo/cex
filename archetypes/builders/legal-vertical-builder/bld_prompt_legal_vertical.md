---
kind: instruction
id: bld_instruction_legal_vertical
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for legal_vertical
quality: 8.9
title: "Instruction Legal Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [legal_vertical, builder, instruction]
tldr: "Step-by-step production process for legal_vertical"
domain: "legal_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_legal_vertical_builder
  - bld_knowledge_card_legal_vertical
  - p01_qg_legal_vertical
  - p10_mem_legal_vertical_builder
  - bld_examples_legal_vertical
  - legal-vertical-builder
  - bld_tools_legal_vertical
  - bld_instruction_safety_policy
  - bld_instruction_judge_config
  - bld_instruction_eval_framework
---

## Phase 1: RESEARCH  
1. Analyze privilege logs for attorney-client confidentiality patterns  
2. Map billable hour tracking methods across law firm accounting systems  
3. Audit contract clauses for recurring legal terminology in M&A agreements  
4. Identify use cases for privilege in litigation discovery processes  
5. Benchmark contract analysis tools against legal tech industry standards  
6. Document regulatory frameworks affecting billable hour reporting  

## Phase 2: COMPOSE
1. Align artifact structure with bld_schema_legal_vertical.md's legal_vertical hierarchy.
2. Write privilege section covering attorney-client privilege (ABA Rule 1.6) and work-product doctrine (FRCP 26(b)(3)).
3. Implement billable hour tracking logic with UTBMS task/activity codes in JSON format per schema.
4. Extract contract analysis patterns from sample NDAs and SLAs; map to EDRM model for eDiscovery use cases.
5. Embed use case examples in "litigation", "compliance", and "matter management" subsections.
6. Reference ABA Model Rule 5.3 (supervision of non-lawyer assistants) for AI tool use cases.
7. Cross-reference schema requirements with bld_output_template_legal_vertical.md metadata fields.
8. Add iManage/NetDocuments DMS integration patterns for document management.
9. Include legal hold / litigation hold procedures and document retention policies.
10. Finalize artifact with P01 pillar metadata and legal_vertical classification.

## Phase 3: VALIDATE
- [ ] [OK] Verify schema compliance with bld_schema_legal_vertical.md's required fields.
- [ ] [OK] Confirm billable hour calculations use UTBMS codes and match industry benchmarks.
- [ ] [OK] Ensure privilege section covers both A-C privilege and work-product doctrine.
- [ ] [OK] Validate eDiscovery workflows against EDRM model phases.
- [ ] [OK] Confirm ABA Rule 5.3 compliance documented for AI assistant use cases.
- [ ] [OK] Validate contract analysis outputs against bld_output_template_legal_vertical.md structure.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_legal_vertical_builder]] | related | 0.51 |
| [[bld_knowledge_card_legal_vertical]] | upstream | 0.50 |
| [[p01_qg_legal_vertical]] | downstream | 0.48 |
| [[p10_mem_legal_vertical_builder]] | downstream | 0.40 |
| [[bld_examples_legal_vertical]] | downstream | 0.40 |
| [[legal-vertical-builder]] | upstream | 0.39 |
| [[bld_tools_legal_vertical]] | downstream | 0.25 |
| [[bld_instruction_safety_policy]] | sibling | 0.20 |
| [[bld_instruction_judge_config]] | sibling | 0.19 |
| [[bld_instruction_eval_framework]] | sibling | 0.19 |
