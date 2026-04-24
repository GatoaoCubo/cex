---
id: p01_kc_fintech_vertical
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "Fintech Vertical — Builder Kind Reference"
version: 1.1.0
created: "2026-04-22"
updated: "2026-04-22"
author: knowledge-card-builder
domain: fintech_engineering
quality: 8.8
tags: [fintech, compliance, pci-dss, kyc-aml, fraud-detection, kind-kc]
tldr: "Fintech vertical artifacts require SOC2+PCI-DSS compliance layer, KYC/AML hooks, fraud signals, and tokenized payment flows; never store raw PANs."
when_to_use: "Building, reviewing, or reasoning about fintech_vertical artifacts; generating fintech product specs, compliance checklists, or payment integration blueprints."
keywords: [fintech, pci-dss, kyc, aml, fraud-detection]
long_tails:
  - "How to build a fintech product with PCI-DSS and SOC2 compliance"
  - "KYC AML integration checklist for neobank or digital wallet"
axioms:
  - NEVER store raw PANs — always tokenize at ingestion (PCI-DSS req 3.4)
  - ALWAYS implement KYC before any fiat on-ramp goes live
  - NEVER skip AML transaction monitoring on transfers above $10k USD
  - IF SOC2 Type II is required THEN scope audit 6+ months before launch
  - ALWAYS segregate cardholder data environment (CDE) from application network
linked_artifacts:
  primary: null
  related:
    - kc_ecommerce_vertical
    - p01_kc_quality_gate
    - p01_kc_8f_pipeline
density_score: 0.91
data_source: "PCI-DSS v4.0 (2022); FATF Guidance on Digital ID (2020); SOC2 AICPA TSC 2017"
---

# Fintech Vertical

## Quick Reference
```yaml
kind: fintech_vertical
pillar: P08
llm_function: PRODUCE
max_bytes: 8192
naming: p08_fv_{{product_name}}.md + .yaml
core: false
```

## Key Concepts
- **PCI-DSS**: 12-req framework governing cardholder data; scope = any system touching PANs
- **SOC2 Type II**: 6-month audit of Trust Service Criteria (Security, Availability, Confidentiality)
- **KYC (Know Your Customer)**: identity verification before account activation; Tier 1=name+DOB, Tier 2=ID doc+selfie
- **AML (Anti-Money Laundering)**: transaction monitoring + SAR filing; threshold $10k USD / 90-day rolling
- **Tokenization**: replace PANs with non-reversible tokens at ingestion; reduces PCI scope by 90%
- **Open Banking**: PSD2/API-first account aggregation; OAuth2 + consent management required
- **Chargeback Rate**: Visa/Mastercard threshold 1.0%; above triggers monitoring program

## Compliance Map
| Framework | Scope | Key Controls | Audit Cadence |
|-----------|-------|-------------|---------------|
| PCI-DSS v4.0 | Cardholder data env | Tokenize PANs, encrypt in transit, pen-test annually | Annual QSA or SAQ |
| SOC2 Type II | Cloud SaaS ops | Access logs, incident response, change mgmt | 6-12 month period |
| KYC/AML | Fiat on/off-ramp | Identity doc verification, sanctions screening | Ongoing + annual review |
| GDPR/LGPD | EU/BR user data | Data residency, right-to-delete, DPA | Annual DPO review |
| Open Banking (PSD2) | EU payment initiation | Strong Customer Auth (SCA), API security | Regulatory cycle |

## Strategy Phases
1. **Scope**: map all data flows touching PANs or PII; define CDE boundary; list third-party processors
2. **Tokenize**: implement vault-based tokenization at payment ingestion before any storage
3. **KYC/AML**: integrate identity provider (Jumio/Onfido); wire AML engine (Sardine/Sift) on transfers
4. **Encrypt**: TLS 1.2+ in transit, AES-256 at rest for all CDE data; key rotation every 12 months
5. **Monitor**: real-time fraud scoring on every transaction; alert on velocity + geo anomalies
6. **Audit**: run quarterly internal scans; schedule annual PCI QSA; collect SOC2 evidence continuously

## Golden Rules
- TOKENIZE PANs at edge — never let raw card data touch application DB
- SEGREGATE CDE from app network via firewall rules and separate VPC/subnet
- GATE fiat on-ramp behind KYC Tier 2 minimum (gov ID + liveness check)
- LOG every privileged access with immutable audit trail (CloudTrail / SIEM)
- MONITOR chargeback rate weekly; >0.8% triggers proactive remediation
- VERSION fraud rules — rollback must be < 5 min; document every rule change

## Anti-Patterns
| Anti-Pattern | Why It Fails | Fix |
|-------------|-------------|-----|
| Storing raw PANs in DB | Immediate PCI-DSS Level 1 violation; breach liability | Tokenize at ingestion via PSP vault |
| Skipping KYC for "low-value" accounts | Regulatory fine + license revocation risk | Apply Tier 1 KYC to all accounts |
| Static fraud rules never updated | Rule decay; fraud rings adapt in days | Monthly rule review + ML model refresh |
| SOC2 scoped too late | 6-month evidence period cannot be compressed | Start SOC2 readiness 12 months before audit |
| CDE co-mingled with app servers | Expands PCI scope to entire infra | Network segmentation + dedicated CDE VPC |
| No SAR filing process | AML violation; regulatory penalty | Define SAR workflow + compliance officer role |

## Integration Points
```
[User Onboarding]
      |
      v
[KYC Provider] -- Jumio/Onfido/Persona -- identity doc + liveness
      |
      v
[AML Engine] -- Sardine/Sift/ComplyAdvantage -- sanctions + velocity
      |
      v
[Payment Gateway] -- Stripe/Adyen -- tokenize PAN -> network token
      |
      v
[Fraud Scoring] -- ML model -- risk score per transaction
      |
      v
[Core Banking] -- ledger entry -- never holds raw PAN
```

## References
- PCI-DSS v4.0: https://www.pcisecuritystandards.org/document_library/
- FATF Digital ID: https://www.fatf-gafi.org/publications/fatfrecommendations/documents/digital-identity-guidance.html
- SOC2 AICPA: https://www.aicpa.org/resources/article/soc-2-reporting-on-an-examination-of-controls
- Related: [[kc_ecommerce_vertical]] (sibling vertical pattern)
- Related: [[p01_kc_quality_gate]] (governs artifact quality)

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[fintech-vertical-builder]] | downstream | 0.42 |
| [[bld_examples_fintech_vertical]] | downstream | 0.37 |
| [[kc_ecommerce_vertical]] | sibling | 0.34 |
| [[bld_knowledge_card_fintech_vertical]] | sibling | 0.32 |
| [[bld_instruction_fintech_vertical]] | downstream | 0.31 |
| [[p10_mem_fintech_vertical_builder]] | downstream | 0.27 |
| [[p03_sp_ecommerce_vertical_builder]] | sibling | 0.27 |
| [[bld_knowledge_card_ecommerce_vertical]] | sibling | 0.27 |
| [[p03_sp_fintech_vertical_builder]] | downstream | 0.26 |
| [[p01_qg_fintech_vertical]] | downstream | 0.24 |
