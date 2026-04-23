---
id: p01_kc_edtech_vertical
kind: knowledge_card
kc_type: domain_kc
pillar: P01
title: "EdTech Vertical: LMS Integration, Compliance, and Learning Analytics"
version: "1.1.0"
created: "2026-04-22"
updated: "2026-04-22"
author: "knowledge-card-builder"
domain: edtech
quality: 8.8
tags: [edtech, lms, ferpa, coppa, learning-analytics, lti, compliance]
tldr: "EdTech vertical covers LMS/LTI integration, FERPA+COPPA compliance, and xAPI/SCORM learning analytics for K-12 through HE platforms."
when_to_use: "Building edtech_vertical artifacts: course modules, onboarding flows, learning records, scoring rubrics for education platforms."
keywords: [edtech, lms-integration, lti, ferpa, learning-analytics]
long_tails:
  - How to integrate an LMS with LTI 1.3 and OAuth 2.0
  - FERPA compliance requirements for EdTech SaaS platforms
axioms:
  - ALWAYS encrypt student PII at rest (AES-256) and in transit (TLS 1.2+)
  - NEVER collect data from users under 13 without verifiable parental consent (COPPA)
  - IF LTI version < 1.3 THEN upgrade -- LTI 1.1 deprecated since 2023
  - ALWAYS store xAPI statements with actor IFI (mbox or account) for audit trails
linked_artifacts:
  primary: null
  related: [p01_kc_course_module, p01_kc_learning_record, p01_kc_scoring_rubric]
density_score: 0.88
data_source: "https://www.imsglobal.org/spec/lti/v1p3/"
---

# EdTech Vertical: LMS Integration, Compliance, and Learning Analytics

## Quick Reference
```yaml
topic: edtech_vertical
scope: K-12, Higher Education, corporate L&D platforms
owner: knowledge-card-builder
criticality: high
regulations: [FERPA, COPPA, GDPR-K, CCPA-minors]
standards: [LTI 1.3, xAPI 2.0, SCORM 2004, IMS QTI 3.0]
```

## Key Concepts

- **LTI 1.3**: IMS Global standard; OAuth 2.0 + OIDC; replaces LTI 1.1 (deprecated 2023)
- **xAPI (Tin Can)**: Tracks learning events as `{actor, verb, object}` triples; replaces SCORM
- **SCORM 2004**: Package-based e-learning standard; 4th edition adds sequencing rules
- **FERPA**: U.S. law; covers any school receiving federal funds; consent required for third-party disclosure
- **COPPA**: Applies to users < 13; requires verifiable parental consent before data collection
- **SIS Sync**: Student Information System roster sync via OneRoster 1.1 or CSV import
- **LRS (Learning Record Store)**: Backend persisting xAPI statements; examples: SCORM Cloud, Watershed

## Strategy Phases

1. **Compliance Audit**: Map all data fields to FERPA/COPPA categories; classify PII vs. non-PII
2. **LMS Integration**: Implement LTI 1.3 launch flow (OIDC login -> resource link -> grade passback)
3. **Data Pipeline**: Connect LRS; emit xAPI statements for all scored interactions
4. **Analytics Layer**: Aggregate xAPI statements into learner dashboards (completion, score, time)
5. **Certification**: Run IMS Global conformance suite; validate LTI 1.3 certification badge

## Golden Rules

- USE LTI 1.3 with Deep Linking 2.0 -- single sign-on + content selection in one flow
- SCOPE xAPI actors by institution domain -- prevents cross-tenant PII leakage
- SET data retention policies at LRS level -- FERPA requires deletion on request within 45 days
- TEST SCORM packages with SCORM Cloud free tier before LMS deployment
- VALIDATE QTI 3.0 items against IMS schema before import to avoid silent scoring errors

## Flow

```text
[Student Login] -> [LTI 1.3 OIDC] -> [Tool Launch]
                                           |
                              [Activity] -> [xAPI Statement]
                                           |
                              [LRS Store] -> [Grade Passback (AGS)]
                                           |
                              [Analytics Dashboard] -> [Instructor View]
```

## Comparativo

| Standard   | Protocol       | Data Format | Grade Passback | Status        |
|------------|----------------|-------------|----------------|---------------|
| LTI 1.3    | OIDC + OAuth2  | JWT         | AGS 2.0        | Active (2023+)|
| LTI 1.1    | OAuth 1.0      | XML         | Basic Outcomes | Deprecated    |
| SCORM 2004 | JavaScript API | XML/AICC    | None           | Legacy        |
| xAPI 2.0   | REST/JSON      | JSON-LD     | Via LRS-LMS    | Active        |
| IMS QTI 3  | REST           | XML/JSON    | Via LMS        | Active        |

## Integration Points (CEX Kinds)

| Kind              | Pillar | Role in EdTech pipeline              |
|-------------------|--------|--------------------------------------|
| course_module     | P01    | Unit of instructional content        |
| onboarding_flow   | P12    | Learner enrollment + consent capture |
| learning_record   | P10    | xAPI statement persistence per user  |
| scoring_rubric    | P07    | Assessment criteria + grade bands    |
| user_journey      | P12    | Learner progress path across modules |
| entity_memory     | P10    | Per-learner mastery state            |

## References

- LTI 1.3 spec: https://www.imsglobal.org/spec/lti/v1p3/
- xAPI 2.0 spec: https://opensource.ieee.org/xapi/xapi-base-standard-documentation
- FERPA guidance: https://studentprivacy.ed.gov/ferpa
- COPPA rule text: https://www.ftc.gov/legal-library/browse/rules/childrens-online-privacy-protection-rule-coppa
- SCORM Cloud conformance: https://scorm.com/scorm-explained/

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_course_module]] | sibling | 0.61 |
| [[p01_kc_learning_record]] | sibling | 0.58 |
| [[p01_kc_scoring_rubric]] | sibling | 0.55 |
| [[p01_kc_user_journey]] | sibling | 0.48 |
| [[p01_kc_onboarding_flow]] | sibling | 0.45 |
| [[edtech-vertical-builder]] | downstream | 0.43 |
| [[bld_examples_edtech_vertical]] | downstream | 0.40 |
| [[p01_kc_entity_memory]] | related | 0.35 |
| [[kc_ai_compliance_gdpr]] | sibling | 0.30 |
| [[bld_knowledge_card_compliance_checklist]] | sibling | 0.27 |
