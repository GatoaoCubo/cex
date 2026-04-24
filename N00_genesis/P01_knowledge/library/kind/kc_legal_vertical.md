---
quality: null
id: kc_legal_vertical
kind: knowledge_card
8f: F3_inject
title: "Legal Industry Vertical: Key Concepts"
tldr: "Covers privilege, fee models, compliance frameworks, eDiscovery, TAR, and legal tech stack for AI-assisted legal applications"
version: 1.1.0
pillar: P01
domain: legal-technology
tags: [kind, taxonomy, legal_vertical, compliance, ediscovery, contract_analysis]
related:
  - legal-vertical-builder
  - bld_knowledge_card_legal_vertical
  - bld_examples_legal_vertical
  - bld_instruction_legal_vertical
  - p01_qg_legal_vertical
  - p10_mem_legal_vertical_builder
  - p03_sp_legal_vertical_builder
  - bld_collaboration_legal_vertical
  - bld_schema_legal_vertical
  - compliance-framework-builder
density_score: 0.92
updated: "2026-04-22"
---

# Legal Industry Vertical: Key Concepts

## 1. Privilege

- **Attorney-Client Privilege**: Confidential communications between lawyer and client for the purpose of obtaining or providing legal advice. Protected under Rule 1.6 of the ABA Model Rules of Professional Conduct.
- **Work Product Protection**: Shielded documents created for litigation preparation (Fed. R. Civ. P. 26(b)(3)). Divided into "ordinary" (factual) and "opinion" (mental impressions) categories.
- **Exceptions**: Spontaneous disclosures, third-party access, crime-fraud exception, and non-privileged communications.
- **Waiver Risks**: Inadvertent disclosure under FRE 502(b) -- requires reasonable steps to prevent and prompt rectification.

## 2. Billable Hour and Alternative Fee Models

- **Time Tracking**: Detailed logging of attorney work (e.g., 1.5 hours for document review), typically in 6-minute (0.1 hour) increments
- **Billing Practices**: Fixed fees vs hourly rates, time entry validation, pre-bill review
- **Ethical Considerations**: ABA Model Rule 1.5 -- fees must be reasonable; prohibited billable hours for non-legal tasks
- **Alternative Fee Arrangements (AFAs)**: Flat fee, capped fee, success fee, blended rate, subscription retainer

| Fee Model | Description | Best For |
|-----------|-------------|----------|
| Hourly | Time-based billing at agreed rate | Complex litigation, unpredictable scope |
| Flat Fee | Fixed price for defined scope | Routine transactions, document drafting |
| Capped Fee | Hourly with maximum ceiling | Projects with bounded complexity |
| Success Fee | Payment contingent on outcome | Plaintiff litigation, M&A closings |
| Blended Rate | Single rate across team seniority | Portfolio clients, ongoing matters |
| Subscription | Monthly retainer for ongoing access | GC/outside counsel relationships |

## 3. Contract Analysis

- **Key Elements**: Parties, obligations, termination clauses, governing law, force majeure
- **Risk Assessment**: Identifying hidden liabilities, enforceability gaps, and indemnification exposure
- **Negotiation Support**: Drafting clauses for dispute resolution, performance metrics, and liability caps
- **AI-Assisted Review**: NLP extraction of key terms, obligation tracking, deviation scoring against playbook

## 4. Compliance Frameworks

Legal technology must operate within regulatory boundaries. The following frameworks define the compliance landscape:

| Framework | Domain | Key Requirements | Jurisdiction |
|-----------|--------|------------------|-------------|
| GDPR | Data privacy | Data minimization, consent, DPO, 72h breach notification | EU/EEA |
| CCPA/CPRA | Consumer privacy | Opt-out rights, data deletion, no discrimination | California, USA |
| SOX (Sarbanes-Oxley) | Financial reporting | Internal controls, audit trails, CEO/CFO certification | USA (public companies) |
| HIPAA | Health data | PHI safeguards, BAAs, breach notification | USA |
| AML/KYC | Financial crime | Customer due diligence, transaction monitoring, SAR filing | Global |
| eDiscovery (FRCP) | Litigation | Preservation holds, proportionality, TAR validation | USA federal courts |
| ITAR/EAR | Export control | Technology transfer restrictions, license requirements | USA |

## 5. Legal Technology Stack

```yaml
# Typical legal tech architecture layers
document_management:
  - iManage Work
  - NetDocuments
  - SharePoint (legal-configured)

contract_lifecycle:
  - Ironclad
  - DocuSign CLM
  - Icertis

ediscovery:
  - Relativity
  - Nuix
  - Everlaw

legal_research:
  - Westlaw Edge
  - LexisNexis
  - CaseText (CoCounsel AI)

practice_management:
  - Clio
  - PracticePanther
  - Litify (Salesforce-based)

billing_and_matter:
  - Aderant
  - Elite 3E
  - TimeSolv
```

## 6. eDiscovery and Technology-Assisted Review (TAR)

The EDRM (Electronic Discovery Reference Model) defines the standard workflow:

```
Information     -->  Identification  -->  Preservation  -->  Collection
Governance              |                     |                |
                        v                     v                v
                   Processing  -->  Review  -->  Analysis  -->  Production
                        |              |            |              |
                        v              v            v              v
                   De-duplication   TAR/CAL    Clustering    Bates numbering
                   + filtering     (ML-based)  + threading   + redaction
```

- **TAR 1.0 (Simple Passive Learning)**: SME reviews seed set, model classifies remainder
- **TAR 2.0 (Continuous Active Learning / CAL)**: Model continuously learns from each reviewer decision, prioritizes most informative documents
- **Validation**: Recall targets typically 70-80% for reasonable review; elusion testing on discard pile

## 7. Use Cases for AI in Legal

- **Document Review**: Privilege log creation, redaction, and TAR-based relevance classification
- **Compliance Audits**: Regulatory document analysis, risk mapping, and gap identification
- **Transaction Support**: Due diligence reviews, contract negotiation, and data room analysis
- **Litigation Support**: Discovery document analysis, evidentiary review, and case timeline construction
- **Legal Research**: Case law search, statutory analysis, and precedent identification via NLP
- **Contract Intelligence**: Clause extraction, obligation tracking, and deviation scoring against standard playbooks

## 8. Key Industry Sources

| Source | Type | Coverage |
|--------|------|----------|
| ABA Model Rules | Professional conduct | Attorney ethics, confidentiality, competence |
| Federal Rules of Civil Procedure (FRCP) | Procedural law | eDiscovery, preservation, proportionality |
| Sedona Conference | Best practices | eDiscovery guidelines, TAR protocols |
| CLOC (Corporate Legal Operations Consortium) | Operations | Legal ops metrics, vendor management |
| ILTACON | Industry conference | Legal tech standards, innovation trends |
| Restatement (Second) of Contracts | Substantive law | Contract formation, interpretation, remedies |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[legal-vertical-builder]] | related | 0.44 |
| [[bld_knowledge_card_legal_vertical]] | sibling | 0.38 |
| [[bld_examples_legal_vertical]] | downstream | 0.37 |
| [[bld_instruction_legal_vertical]] | downstream | 0.37 |
| [[p01_qg_legal_vertical]] | downstream | 0.36 |
| [[p10_mem_legal_vertical_builder]] | downstream | 0.33 |
| [[p03_sp_legal_vertical_builder]] | downstream | 0.32 |
| [[bld_collaboration_legal_vertical]] | downstream | 0.23 |
| [[bld_schema_legal_vertical]] | downstream | 0.20 |
| [[compliance-framework-builder]] | downstream | 0.16 |
