---
kind: knowledge_card
id: bld_knowledge_card_fintech_vertical
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for fintech_vertical production
quality: 9.2
title: "Knowledge Card Fintech Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [fintech_vertical, builder, knowledge_card]
tldr: "Domain knowledge for fintech_vertical production"
domain: "fintech_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_instruction_fintech_vertical
  - p03_sp_fintech_vertical_builder
  - fintech-vertical-builder
  - p01_qg_fintech_vertical
  - bld_examples_fintech_vertical
  - p10_mem_fintech_vertical_builder
  - bld_tools_fintech_vertical
  - bld_knowledge_card_ecommerce_vertical
  - p03_sp_ecommerce_vertical_builder
  - bld_examples_ecommerce_vertical
---

## Domain Overview
The fintech industry vertical emphasizes secure, compliant, and scalable financial services, driven by regulatory demands (e.g., SOC2, PCI-DSS) and operational needs (e.g., KYC/AML, fraud detection). SOC2+PCI-DSS compliance ensures data protection and operational integrity, critical for handling sensitive customer information. KYC/AML processes verify identities and prevent financial crimes, while fraud detection leverages AI/ML to identify anomalies in real-time. These pillars underpin trust in digital banking, payments, and lending platforms, requiring robust technical and governance frameworks.

## Key Concepts
| Concept | Definition | Source |
|---|---|---|
| SOC2 Type II | Audit report evaluating security, availability, processing integrity, confidentiality, privacy over >= 6 months | AICPA TSC 2017 |
| PCI-DSS v4.0 | 12-requirement standard for cardholder data protection; v4.0 adds customized approach and MFA expansion | PCI SSC 2022 |
| KYC/AML CDD | Customer Due Diligence -- verifying identity and assessing ML/TF risk at onboarding | FATF Recommendations 2012 (R.10) |
| FinCEN CIP | Customer Identification Program -- US rule requiring name, DOB, address, ID number at account opening | 31 CFR 1020.220 |
| OFAC SDN Screening | Screening against Office of Foreign Assets Control Specially Designated Nationals list before any transaction | OFAC / 31 CFR Part 595 |
| FFIEC CAT | Cybersecurity Assessment Tool -- inherent risk + cybersecurity maturity mapping for financial institutions | FFIEC 2015 / updated 2023 |
| ISO 20022 | Global financial messaging standard for payments (replacing SWIFT MT formats by 2025) | ISO 20022:2013 |
| SOX Section 404 | Management and auditor assessment of internal controls over financial reporting | Sarbanes-Oxley Act 2002 |
| Sift / Sardine | Real-time fraud detection platforms using device fingerprinting, behavioral biometrics, and ML scoring | Sift Science / Sardine.ai |
| Tokenization | Replacing PANs / PII with non-sensitive tokens; reduces PCI-DSS scope | PCI-DSS v4.0 Req 3.5 |

## Industry Standards
- SOC 2 Type II (AICPA TSC 2017)
- PCI-DSS v4.0 (PCI SSC)
- FATF Recommendations 2012 + Travel Rule (R.16)
- FinCEN CIP / AML Program rules (31 CFR 1020)
- OFAC sanctions screening (31 CFR Part 595)
- FFIEC Cybersecurity Assessment Tool
- ISO 20022 payments messaging
- SOX Section 404 (internal financial controls)
- ISO/IEC 27001:2022 (Information Security Management)
- Basel Committee KYC Risk Management Guidance

## Common Patterns
1. Real-time transaction monitoring with rule engines and ML models
2. Layered authentication (e.g., 2FA + biometrics) for user verification
3. Centralized compliance dashboards for SOC2/PCI-DSS metrics
4. Tokenization of PANs and PII to meet PCI-DSS storage requirements
5. Integration of AML screening tools with onboarding workflows

## Pitfalls
- Overlooking PCI-DSS v4.0 scope expansion during third-party integrations (shared responsibility model).
- Inadequate logging for SOC2 Type II audit trails (missing system access records, change management logs).
- Relying solely on static KYC checks without continuous monitoring (required by FATF R.10 CDD).
- Missing OFAC SDN screening at onboarding AND transaction level -- violation carries strict liability.
- Poor data governance leading to AML false positives/negatives; tune rule engines with Wolfsberg Principles.
- Underestimating fraud attack vectors in open banking APIs -- integrate Sift/Sardine or equivalent behavioral scoring.
- Ignoring ISO 20022 migration timeline -- SWIFT MT message sunset affects all cross-border payment flows.
- Skipping FFIEC CAT when operating as a financial institution; regulators expect CAT maturity documentation.
- SOX 404 controls scope creep -- define financial reporting systems boundary before starting assessment.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_fintech_vertical]] | downstream | 0.62 |
| [[p03_sp_fintech_vertical_builder]] | downstream | 0.62 |
| [[fintech-vertical-builder]] | related | 0.51 |
| [[p01_qg_fintech_vertical]] | downstream | 0.51 |
| [[bld_examples_fintech_vertical]] | downstream | 0.49 |
| [[p10_mem_fintech_vertical_builder]] | downstream | 0.48 |
| [[bld_tools_fintech_vertical]] | downstream | 0.43 |
| [[bld_knowledge_card_ecommerce_vertical]] | sibling | 0.39 |
| [[p03_sp_ecommerce_vertical_builder]] | downstream | 0.36 |
| [[bld_examples_ecommerce_vertical]] | downstream | 0.33 |
