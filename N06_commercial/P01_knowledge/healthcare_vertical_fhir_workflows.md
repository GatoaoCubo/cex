---
id: healthcare_vertical_fhir_workflows
kind: healthcare_vertical
8f: F1_constrain
pillar: P01
nucleus: N06
domain: healthcare
title: "Healthcare Vertical — FHIR Workflows Analysis"
version: "1.0.0"
quality: 8.5
tags: [healthcare, fhir, hipaa, hl7, interoperability, vertical]
author: N06_contrib_stress_test
created: "2026-04-19"
compliance: [HIPAA, HITECH, ONC, 21st_Century_Cures]
focus_area: fhir_workflows
target_demographic: ehr_vendors_health_systems_payers
related:
  - bld_knowledge_card_fhir_agent_capability
  - fhir-agent-capability-builder
  - p03_sp_fhir_agent_capability_builder
  - kc_fhir_agent_capability
  - bld_tools_fhir_agent_capability
  - bld_instruction_fhir_agent_capability
  - bld_collaboration_fhir_agent_capability
  - bld_examples_healthcare_vertical
  - bld_architecture_fhir_agent_capability
  - p03_sp_healthcare_vertical_builder
density_score: 1.0
updated: "2026-04-22"
---

## Market Overview

| Dimension | Value |
|-----------|-------|
| Global Healthcare IT market (2024) | $390B |
| EHR segment | $32B |
| Interoperability / FHIR tooling | $4.2B |
| CAGR (2024-2030) | 14.9% |
| Mandate driver | ONC 21st Century Cures Act (2024 enforcement) |

## Key Players

| Vendor | Segment | FHIR Maturity |
|--------|---------|---------------|
| Epic | Enterprise EHR | FHIR R4, SMART on FHIR |
| Cerner (Oracle Health) | Enterprise EHR | FHIR R4, CDS Hooks |
| Athenahealth | Ambulatory | FHIR R4 |
| Veradigm (Allscripts) | Ambulatory / Analytics | FHIR R4 |
| Apple Health | Patient app | FHIR R4 consumer API |

## Domain Vocabulary (Seed for N08_healthcare vocabulary KC)

| Term | Definition | CEX Equivalent |
|------|-----------|----------------|
| FHIR R4 | Fast Healthcare Interoperability Resources v4 — REST API standard | api_reference kind |
| SMART | Substitutable Medical Apps, Reusable Technologies — OAuth2 layer | oauth_app_config kind |
| CDS Hooks | Clinical Decision Support trigger framework | hook kind |
| HL7 v2 | Legacy ADT/ORU/ORM message format (still 80% of hospital traffic) | event_schema kind |
| PHI | Protected Health Information — HIPAA-covered data class | guardrail kind |
| HIPAA | Health Insurance Portability and Accountability Act | compliance_framework kind |
| Prior Auth | Payer approval before procedure — Da Vinci use case | workflow kind |
| IPA | Implementation Guide for Patient Access — ONC mandate | api_client kind |
| PDMP | Prescription Drug Monitoring Program | db_connector kind |

## Compliance Requirements

### HIPAA / HITECH
- PHI categories: 18 identifiers (name, DOB, geo, device IDs, etc.)
- Minimum necessary standard: only access/transmit PHI needed for the task
- BAA: Business Associate Agreement required for any PHI-processing vendor
- Breach notification: 60-day rule for >500 individuals (HHS + media)
- Security Rule: administrative, physical, technical safeguards
- CEX hook: `guardrail` kind enforces PHI field masking; `audit_log` tracks all access

### ONC 21st Century Cures — Information Blocking Rule
- Effective 2022: EHRs CANNOT block access to electronic health information (EHI)
- Patient APIs: SMART on FHIR patient-facing endpoint mandatory for CMS-regulated payers
- Developers: must attest ONC Health IT certification
- Penalty: up to $1M per violation for EHR developers
- CEX hook: `compliance_checklist` audits API openness pre-deployment

### FHIR R4 Integration Pattern
```
Client (app/CEX) → SMART on FHIR auth → EHR FHIR server
  1. Discovery: GET /.well-known/smart-configuration
  2. Auth: OAuth2 PKCE flow (authorization_code or client_credentials)
  3. Launch: EHR-launch or standalone-launch context
  4. Query: GET /Patient/{id}/everything (bundle)
  5. Write: POST/PUT Observation, MedicationRequest, etc.
```

## CEX Kind Mapping

| Healthcare Need | CEX Kind | Pillar | Notes |
|----------------|---------|--------|-------|
| FHIR API client | `api_client` | P04 | SMART on FHIR OAuth2 |
| PHI guardrail | `guardrail` | P11 | 18-identifier masking |
| HL7 v2 message | `event_schema` | P06 | ADT/ORU message schema |
| Prior auth workflow | `workflow` | P12 | Da Vinci PAS guide |
| CDS Hook trigger | `hook` | P04 | patient-view, order-sign |
| HIPAA audit trail | `audit_log` | P08 | PHI access log |
| Care coordination | `dag` | P12 | Multi-provider workflow |
| Clinical decision | `reasoning_strategy` | P08 | Evidence-based branching |

## New Builders/Kinds This Vertical Needs

| Proposed Kind | Rationale | Priority |
|---------------|-----------|----------|
| `fhir_resource` | Typed FHIR R4 resource schema (Patient, Observation, etc.) | HIGH |
| `cds_hook` | CDS Hooks service definition with prefetch template | HIGH |
| `clinical_workflow` | Care pathway with clinical decision nodes | HIGH |
| `phi_policy` | HIPAA minimum-necessary field policy per resource type | HIGH |
| `prior_auth_request` | Da Vinci PAS prior authorization document | MEDIUM |

Note: `fhir_agent_capability` builder already exists in CEX — leverage for N08_healthcare.

## Moat Assessment (N06 Lens — Strategic Greed)

| Factor | Score | Rationale |
|--------|-------|-----------|
| Compliance complexity | 10/10 | HIPAA+ONC+FHIR = highest barrier in tech |
| Market size | 9/10 | $390B HIT, mandated interoperability |
| CEX differentiation | 9/10 | Typed PHI guardrails + audit logs native |
| Switching cost | 10/10 | EHR integrations are multi-year commitments |
| Revenue model fit | 8/10 | Per-API-call SaaS, compliance attestation fees |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_fhir_agent_capability]] | related | 0.55 |
| [[fhir-agent-capability-builder]] | downstream | 0.54 |
| [[p03_sp_fhir_agent_capability_builder]] | downstream | 0.52 |
| [[kc_fhir_agent_capability]] | related | 0.50 |
| [[bld_tools_fhir_agent_capability]] | downstream | 0.48 |
| [[bld_instruction_fhir_agent_capability]] | downstream | 0.48 |
| [[bld_collaboration_fhir_agent_capability]] | downstream | 0.46 |
| [[bld_examples_healthcare_vertical]] | downstream | 0.44 |
| [[bld_architecture_fhir_agent_capability]] | downstream | 0.43 |
| [[p03_sp_healthcare_vertical_builder]] | downstream | 0.42 |
