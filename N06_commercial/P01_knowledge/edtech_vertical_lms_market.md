---
id: edtech_vertical_lms_market
kind: edtech_vertical
8f: F1_constrain
pillar: P01
nucleus: N06
domain: edtech
title: "EdTech Vertical — LMS Market Analysis"
version: "1.0.0"
quality: 8.5
tags: [edtech, lms, ferpa, coppa, vertical, market_analysis]
author: N06_contrib_stress_test
created: "2026-04-19"
compliance: [FERPA, COPPA, GDPR]
focus_area: lms_integration
target_demographic: K12_higher_ed
related:
  - bld_examples_edtech_vertical
  - bld_instruction_edtech_vertical
  - p10_mem_edtech_vertical_builder
  - p03_sp_edtech_vertical_builder
  - edtech-vertical-builder
  - p01_qg_edtech_vertical
  - bld_knowledge_card_edtech_vertical
  - bld_tools_edtech_vertical
  - bld_output_template_edtech_vertical
  - hybrid_review7_n06
density_score: 1.0
updated: "2026-04-22"
---

## Market Overview

| Dimension | Value |
|-----------|-------|
| Global EdTech market (2024) | $254B |
| LMS segment (2024) | $22B |
| CAGR (2024-2029) | 19.4% |
| Top regions | NA (38%), APAC (31%), EMEA (22%) |
| Dominant delivery | SaaS (73%), on-prem (27%) |

## Key Players

| Vendor | Segment | Market Share | Compliance Focus |
|--------|---------|-------------|-----------------|
| Canvas (Instructure) | Higher Ed | 35% | FERPA, LTI 1.3 |
| Moodle | K-12 / SMB | 28% | GDPR, FERPA |
| Blackboard (Anthology) | Enterprise Edu | 18% | FERPA, SOC2 |
| Google Classroom | K-12 | 12% | COPPA, FERPA |
| Schoology (PowerSchool) | K-12 | 7% | FERPA, COPPA |

## Domain Vocabulary (Seed for N08_edtech vocabulary KC)

| Term | Definition | CEX Equivalent |
|------|-----------|----------------|
| LMS | Learning Management System — centralized platform for course delivery | workflow kind |
| LTI 1.3 | Learning Tools Interoperability — OAuth2-based tool launch standard | interface kind |
| xAPI (Tin Can) | Learning activity tracking standard (successor to SCORM) | event_schema kind |
| SIS | Student Information System — roster/grade data store | db_connector kind |
| FERPA | Family Educational Rights and Privacy Act — US student data law | compliance_checklist kind |
| COPPA | Children's Online Privacy Protection Act — <13 data rules | guardrail kind |
| IMS Global | Consortium defining LTI, QTI, Caliper standards | domain_vocabulary kind |
| Caliper | IMS learning analytics framework | eval_metric kind |

## Compliance Requirements

### FERPA (US)
- Records covered: grades, enrollment, financial aid, disciplinary
- Consent model: opt-out for directory info; opt-in for PII disclosure
- Data minimization: only collect records necessary for stated educational purpose
- Breach notification: within 60 days to affected parties
- CEX hook: `guardrail` kind enforces PII field masking in student data pipelines

### COPPA (US — under 13)
- Parental consent: verifiable, explicit, prior to data collection
- Data types blocked: precise geolocation, behavioral advertising, full name+address combo
- Operator obligations: delete on request within 30 days
- CEX hook: `content_filter` kind blocks COPPA-violating data fields at ingestion

### LTI 1.3 Integration Pattern
```
Platform (LMS) → OIDC Connect → Tool Provider (CEX)
  1. Platform sends id_token (JWT, signed RS256)
  2. Tool validates iss, aud, nonce, deployment_id
  3. Tool returns resource link + context claims
  4. OAuth2 service access token for Names+Roles, Grade Passback
```

## CEX Kind Mapping

| EdTech Need | CEX Kind | Pillar | Notes |
|-------------|---------|--------|-------|
| Course content delivery | `workflow` | P12 | Sequential lesson flow |
| Grade passback API | `api_client` | P04 | LTI Advantage Grade Services |
| Student roster sync | `db_connector` | P04 | SIS integration (OneRoster) |
| Learning activity tracking | `event_schema` | P06 | xAPI statement format |
| FERPA compliance gate | `compliance_checklist` | P07 | Pre-processing validation |
| Adaptive content router | `router` | P02 | Mastery-based branching |
| Assessment rubric | `scoring_rubric` | P07 | Standards-aligned grading |
| Parent consent workflow | `workflow` + `guardrail` | P11+P12 | COPPA consent chain |

## New Builders/Kinds This Vertical Needs

| Proposed Kind | Rationale | Priority |
|---------------|-----------|----------|
| `lti_provider` | LTI 1.3 tool registration + launch config | HIGH |
| `student_data_policy` | FERPA/COPPA field-level policy artifact | HIGH |
| `adaptive_learning_path` | Mastery-gated content sequence | MEDIUM |
| `assessment_rubric` | Caliper-aligned grading instrument | MEDIUM |
| `sis_connector` | OneRoster 2.0 roster sync protocol | MEDIUM |

## Existing Builder Relevance

| Builder | Relevance | Use Case |
|---------|-----------|----------|
| `api_client-builder` | HIGH | LTI Advantage API client |
| `compliance_checklist-builder` | HIGH | FERPA/COPPA audit artifact |
| `workflow-builder` | HIGH | Course enrollment flow |
| `guardrail-builder` | HIGH | Student PII protection |
| `event_schema-builder` | MEDIUM | xAPI statement schema |
| `scoring_rubric-builder` | MEDIUM | Standards-aligned assessment |
| `db_connector-builder` | MEDIUM | SIS/OneRoster integration |

## Moat Assessment (N06 Lens — Strategic Greed)

| Factor | Score | Rationale |
|--------|-------|-----------|
| Compliance complexity | 9/10 | FERPA+COPPA+LTI = high barrier |
| Market size | 8/10 | $22B LMS, 19% CAGR |
| CEX differentiation | 8/10 | Typed guardrails beat generic AI |
| Switching cost | 7/10 | LMS deeply embedded in institutions |
| Revenue model fit | 8/10 | SaaS per-student pricing, district deals |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_examples_edtech_vertical]] | downstream | 0.47 |
| [[bld_instruction_edtech_vertical]] | downstream | 0.46 |
| [[p10_mem_edtech_vertical_builder]] | downstream | 0.43 |
| [[p03_sp_edtech_vertical_builder]] | downstream | 0.40 |
| [[edtech-vertical-builder]] | related | 0.39 |
| [[p01_qg_edtech_vertical]] | downstream | 0.39 |
| [[bld_knowledge_card_edtech_vertical]] | related | 0.39 |
| [[bld_tools_edtech_vertical]] | downstream | 0.33 |
| [[bld_output_template_edtech_vertical]] | downstream | 0.32 |
| [[hybrid_review7_n06]] | related | 0.26 |
