---
kind: instruction
id: bld_instruction_fintech_vertical
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for fintech_vertical
quality: 8.9
title: "Instruction Fintech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [fintech_vertical, builder, instruction]
tldr: "Step-by-step production process for fintech_vertical"
domain: "fintech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_fintech_vertical_builder
  - p01_qg_fintech_vertical
  - bld_knowledge_card_fintech_vertical
  - bld_examples_fintech_vertical
  - fintech-vertical-builder
  - p10_mem_fintech_vertical_builder
  - p03_sp_ecommerce_vertical_builder
  - bld_tools_fintech_vertical
  - p01_qg_ecommerce_vertical
  - bld_instruction_ecommerce_vertical
---

## Phase 1: RESEARCH  
1. Identify SOC2+PCI-DSS compliance requirements for fintech data handling.  
2. Map KYC/AML regulatory frameworks (e.g., FATF, GDPR, AMLA).  
3. Analyze fraud detection methodologies (machine learning, rule-based systems).  
4. Document industry-specific use cases (e.g., real-time transaction monitoring).  
5. Interview stakeholders for pain points in compliance and fraud prevention.  
6. Benchmark competitors’ approaches to security and regulatory alignment.  

## Phase 2: COMPOSE
1. Align artifact structure with bld_schema_fintech_vertical.md’s compliance section.
2. Draft SOC2 Type II + PCI-DSS v4.0 controls using bld_output_template_fintech_vertical.md’s control matrix.
3. Write KYC/AML workflows with example data formats (e.g., JSON for customer onboarding, FinCEN CIP fields).
4. Detail fraud detection algorithms (Sift/Sardine integration patterns) with performance metrics.
5. Embed use cases (e.g., “OFAC SDN list screening at onboarding”, “detecting synthetic identity fraud”).
6. Reference bld_schema_fintech_vertical.md’s data governance section for artifact consistency.
7. Integrate PCI-DSS v4.0 scope definitions (cardholder data environments, tokenization).
8. Add FFIEC Cybersecurity Assessment Tool (CAT) mapping and ISO 20022 message types where relevant.
9. Cross-check artifact against bld_output_template_fintech_vertical.md’s compliance checklist.
10. Finalize with SOX Section 404 controls documentation if applicable.

## Phase 3: VALIDATE
- [ ] [OK] Verify SOC2 Type II + PCI-DSS v4.0 alignment with bld_schema_fintech_vertical.md.
- [ ] [OK] Confirm KYC/AML workflows include OFAC sanctions screening and FinCEN CIP fields.
- [ ] [OK] Ensure fraud detection logic references Sift/Sardine or equivalent behavioral scoring.
- [ ] [OK] Validate use cases against bld_output_template_fintech_vertical.md structure.
- [ ] [OK] Confirm SOFT weights in bld_quality_gate_fintech_vertical.md sum to 1.00.
- [ ] [OK] Conduct peer review for clarity and adherence to bld_output_template_fintech_vertical.md.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_fintech_vertical_builder]] | related | 0.49 |
| [[p01_qg_fintech_vertical]] | downstream | 0.47 |
| [[bld_knowledge_card_fintech_vertical]] | upstream | 0.46 |
| [[bld_examples_fintech_vertical]] | downstream | 0.46 |
| [[fintech-vertical-builder]] | upstream | 0.46 |
| [[p10_mem_fintech_vertical_builder]] | downstream | 0.42 |
| [[p03_sp_ecommerce_vertical_builder]] | related | 0.34 |
| [[bld_tools_fintech_vertical]] | downstream | 0.32 |
| [[p01_qg_ecommerce_vertical]] | downstream | 0.29 |
| [[bld_instruction_ecommerce_vertical]] | sibling | 0.28 |
