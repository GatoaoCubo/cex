---
kind: quality_gate
id: bld_quality_gate_conformity_assessment
pillar: P11
llm_function: GOVERN
purpose: Hard and soft quality gates for conformity_assessment artifacts
quality: 9.1
title: "Conformity Assessment Builder -- Quality Gate"
version: "1.0.0"
author: wave7_n05
tags: [conformity_assessment, builder, quality_gate]
tldr: "8 hard gates + 5 scored dimensions for EU-AI-Act Annex-IV conformity assessment artifacts"
domain: "conformity_assessment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p11_qg_ai_rmf_profile
  - bld_instruction_conformity_assessment
  - bld_examples_conformity_assessment
  - p11_qg_quality_gate
  - bld_schema_conformity_assessment
  - bld_collaboration_conformity_assessment
  - p05_qg_github_issue_template
  - p12_qg_team_charter
  - p09_qg_marketplace_app_manifest
  - p08_qg_capability_registry
---

## Quality Gate

# Conformity Assessment Builder -- Quality Gate
## Hard Gates (H01-H08)
All 8 gates MUST pass. A single FAIL blocks publication (quality stays null).
| Gate | ID | Check | Pass Condition | FAIL Action |
|------|----|-------|---------------|-------------|
| Frontmatter complete | H01 | YAML frontmatter present with all required fields | All fields populated, quality: null | Add missing fields |
| ID pattern valid | H02 | id matches ^p11_ca_[a-z0-9_]+\.md$ | Regex match | Rename artifact |
| Kind correct | H03 | kind == "conformity_assessment" | Exact match | Fix kind field |
| RMS section present | H04 | risk_management_system object has >= 6 sub-fields | Count >= 6 | Add missing RMS fields |
| Data governance present | H05 | data_governance_plan object has >= 5 sub-fields | Count >= 5 | Add missing DGP fields |
| Human oversight present | H06 | human_oversight_measures object has >= 5 sub-fields | Count >= 5 | Add missing HOM fields |
| Annex-III category specified | H07 | annex_iii_category is one of the 9 valid enum values | Enum match | Identify correct category |
| Post-market-monitoring plan | H08 | post_market_monitoring_plan object has >= 5 sub-fields | Count >= 5 | Add missing PMM fields |

## Hard Gate Evaluation Script (pseudo-code)

```
results = {}

# H01 -- Frontmatter
required_fields = [system_name, system_version, provider_name, annex_iii_category,
                   article_43_procedure, declaration_date, eu_ai_act_ref,
                   technical_documentation_reference]
results[H01] = all(field in frontmatter for field in required_fields)

# H02 -- ID pattern
results[H02] = re.match(r'^p11_ca_[a-z0-9_]+\.md$', artifact.id)

# H03 -- Kind
results[H03] = artifact.kind == 'conformity_assessment'

# H04 -- RMS
results[H04] = len(artifact.risk_management_system.keys()) >= 6

# H05 -- DGP
results[H05] = len(artifact.data_governance_plan.keys()) >= 5

# H06 -- HOM
results[H06] = len(artifact.human_oversight_measures.keys()) >= 5

# H07 -- Annex III
valid_categories = [biometric_identification, biometric_categorisation,
                    critical_infrastructure, education_vocational,
                    employment_workers, essential_services,
                    law_enforcement, migration_asylum, justice_democratic]
results[H07] = artifact.annex_iii_category in valid_categories

# H08 -- PMM
results[H08] = len(artifact.post_market_monitoring_plan.keys()) >= 5

pass = all(results.values())
```

## Soft Scoring Dimensions (D01-D05)

Total possible score: 10.0. Quality floor: 8.0. Target: 9.0+.

| Dim | ID | Weight | Criterion | Max Points |
|-----|----|--------|-----------|-----------|
| Completeness | D01 | 0.25 | All 7 Annex-IV categories documented with substantive content | 2.5 |
| Regulatory accuracy | D02 | 0.25 | All claims cite specific EU AI Act article + annex section; no misquotations | 2.5 |
| Evidence density | D03 | 0.20 | RMS, DGP, HOM sections contain specific evidence references, not placeholders | 2.0 |
| Traceability | D04 | 0.20 | Each risk control traceable to an Art. 9 risk ID; each data provision traceable to Art. 10 | 2.0 |
| Auditability | D05 | 0.10 | Aug-2026 deadline items flagged; notified body ID present if required; provider contact included | 1.0 |

## D01 Completeness Scoring

| Score | Condition |
|-------|-----------|
| 2.5 | All 7 Annex-IV categories present with >= 3 sentences or 1 table each |
| 2.0 | 6 of 7 categories present and substantive |
| 1.5 | 5 of 7 categories present |
| 1.0 | 4 of 7 categories present |
| 0.5 | 3 or fewer categories present |
| 0.0 | Missing or placeholder only |

## D02 Regulatory Accuracy Scoring

| Score | Condition |
|-------|-----------|
| 2.5 | Every requirement cites article + annex + section; zero factual errors detected |
| 2.0 | >= 90% of requirements cited; no material errors |
| 1.5 | >= 70% cited; <= 1 minor error |
| 1.0 | >= 50% cited; multiple minor errors |
| 0.5 | < 50% cited or >= 1 material error |
| 0.0 | No citations or significant factual misrepresentation |

## D03 Evidence Density Scoring

| Score | Condition |
|-------|-----------|
| 2.0 | RMS has named risks + named controls; DGP has named datasets; HOM has named tools |
| 1.5 | Two of three sections have specific named evidence |
| 1.0 | One section has specific evidence |
| 0.5 | All sections present but all generic/vague |
| 0.0 | Sections missing or placeholder only |

## D04 Traceability Scoring

| Score | Condition |
|-------|-----------|
| 2.0 | Each mitigation measure references a risk ID; each data provision references Art. 10 sub-clause |
| 1.5 | Risk traceability OR data traceability present (not both) |
| 1.0 | Partial traceability in one domain |
| 0.5 | Implied but not explicit traceability |
| 0.0 | No traceability |

## D05 Auditability Scoring

| Score | Condition |
|-------|-----------|
| 1.0 | Aug-2026 flags present; notified body ID present (if applicable); provider contact complete |
| 0.7 | Two of three auditability elements present |
| 0.4 | One auditability element present |
| 0.0 | None present |

## Score Computation

```
score = D01 + D02 + D03 + D04 + D05
pass_gate = score >= 8.0 AND all hard gates pass
target = score >= 9.0
```

## Gate Failure Protocol

| Score Range | Action |
|-------------|--------|
| < 8.0 | Return to F6 PRODUCE. Fix all H-gate failures first. Then improve lowest-scoring D dimensions. |
| 8.0-8.9 | May publish with quality: null. Flag for improvement in next cycle. |
| 9.0-10.0 | Publish. Signal complete. |
| H-gate FAIL (any) | BLOCK regardless of D score. Fix H-gate. |

## Integration

```bash
# Run quality gate check
python _tools/cex_score.py --apply p11_ca_{system}.md

# If score < 8.0, the artifact is returned to F6
# quality: null until peer-review assigns a score via cex_score.py --apply
```

## Examples

# Conformity Assessment Builder -- Examples
## Golden Example: Medical AI Triage System
**System**: MedTriage-v2 Clinical Decision Support
**Annex III Category**: essential_services (Annex III(5) -- access to essential private and public services in healthcare)
**Article 43 Procedure**: internal_check (no real-time biometric identification)
**Score target**: 9.5/10

### Frontmatter (Golden)

```yaml
---
kind: conformity_assessment
id: p11_ca_medtriage_v2
pillar: P11
title: "Conformity Assessment -- MedTriage-v2 Clinical Decision Support"
system_name: "MedTriage-v2 Clinical Decision Support"
system_version: "2.1.4"
provider_name: "Acme Health AI GmbH"
provider_address: "Musterstrasse 1, 10115 Berlin, DE"
provider_contact: "compliance@acmehealth.ai"
annex_iii_category: "essential_services"
article_43_procedure: "internal_check"
notified_body_id: "NA"
declaration_date: "2026-07-01"
ce_marking_status: "planned"
eu_ai_act_ref: "EU AI Act 2024/1689"
technical_documentation_reference: "MedTriage-v2-TechDoc-2026.pdf"
version: "1.0.0"
quality: null
tags: [conformity_assessment, high-risk, essential_services, healthcare]
created: "2026-04-14"
updated: "2026-04-14"
---
```

### Section 1 -- General Description (Golden)

**Intended Purpose**: MedTriage-v2 provides clinical decision support to emergency department
nurses and physicians by ranking incoming patients by acuity level (1-5 per ESI protocol).
Per EU AI Act Art. 13, the system operates in an advisory capacity -- no autonomous treatment
decision is made. Human clinician retains full authority over final triage assignment.

**Classification**:

| Attribute | Value |
|-----------|-------|
| Annex III Category | essential_services -- Annex III(5), healthcare setting |
| High-Risk Determination | Yes, per Annex III, Sec. 5(c) -- essential medical services |
| Art. 43 Route | Internal check (Annex VI) -- no prohibited biometric use |

**Why this is golden**: Cites Annex III sub-section, specifies advisory-only role,
references Art. 13 transparency, and identifies Art. 43 route without ambiguity.

### Section 4 -- Risk Management System (Golden)

**RMS Process (Art. 9)**: The RMS is an iterative process integrated into the SDLC.
Risk identification occurs at design, pre-release, post-deployment, and incident stages.
RMS documents are version-controlled in the compliance registry (ComplianceReg-2024).

**Identified Risks and Mitigations (excerpt)**:

| Risk ID | Risk Description | Severity | Likelihood | Mitigation | Residual |
|---------|-----------------|----------|-----------|-----------|---------|
| R-001 | Model underestimates acuity for non-English-speaking patients due to training data gap | HIGH | MEDIUM | Multilingual training data added; mandatory clinician review for ESI 3-5 outputs | LOW |
| R-002 | Alert fatigue -- overuse of high-acuity flags reduces clinician trust | MEDIUM | HIGH | Threshold calibration; monthly alert audit; feedback loop to model | LOW-MED |
| R-003 | Cybersecurity -- adversarial input manipulation via patient notes field | HIGH | LOW | Input sanitization; threat model TM-2024-07; pen test PT-2025-03 | LOW |

**Why this is golden**: Named risks with IDs, specific mitigations referencing documents,
severity x likelihood matrix, quantified residual risk.

### Section 2 -- Data Governance (Golden)

| Dataset | Source | Size | Date Range | License |
|---------|--------|------|-----------|---------|
| ED-Acuity-Train-2021 | 5 EU hospital networks | 2.4M patient episodes | 2016-2021 | DPA-EU-Consortium-2022 |
| ESI-Validation-2023 | 2 independent EDs | 450K episodes | 2022-2023 | Internal research license |

**Bias examination**: Age and sex parity analysis conducted per IEEE 2857-2024.
Intersectional bias audit: Oct 2025. No significant disparity above 2% AUC delta found.
Known limitation: Underrepresentation of patients >85 years (< 3% of training set).
Mitigation: Age-stratified evaluation; flagging in system transparency notice.

**Why this is golden**: Named datasets, specific sizes, named license, audit methodology cited,
known limitation quantified, mitigation described.
## Anti-Example 1: Missing RMS Section

**System**: RetailScoringAI v1.0
**What went wrong**: Conformity package submitted without a risk-management-system section.

### The Bad Output

```
## Section 4 -- Risk Management
We have identified that our system poses some risks. These have been addressed
through our internal review process. Our team reviews the system quarterly.
```

### Why This Fails (Gate Analysis)

| Gate | Result | Reason |
|------|--------|--------|
| H04 -- RMS section present | FAIL | Zero structured RMS fields; no named risks; no risk IDs |
| D04 -- Traceability | 0/2 | No risk IDs to trace mitigations to |
| D03 -- Evidence density | 0.5/2 | Vague prose, no named documents or measures |
| D02 -- Regulatory accuracy | 0.5/2.5 | "Internal review" does not satisfy Art. 9 iterative process requirement |

**Score**: Blocked by H04 FAIL. Cannot publish.

### How to Fix

- Structure the RMS with named risks (R-001, R-002, ...)
- For each risk: severity, likelihood, specific mitigation measure, residual risk level
- Reference Art. 9 explicitly as the process basis
- Document the iterative cadence (when risks are re-evaluated)
- Record the RMS version and last-updated date

### Root Cause

Confusion between an internal risk review (any company can do) and a formal
risk-management-system as defined by EU AI Act Art. 9. The Art. 9 RMS requires:
identification, estimation, evaluation, mitigation, and residual risk acceptance --
all documented, version-controlled, and continuously updated.
## Anti-Example 2: Conformity Assessment Confused with Compliance Framework

**System**: HRScreening-AI v3
**What went wrong**: Author produced a GDPR compliance framework instead of an EU AI Act
Annex-IV conformity assessment package.

### The Bad Output

```
# AI Compliance Framework -- HRScreening-AI v3
## GDPR Compliance
Data subject rights: implemented.
Data minimization: applied.
DPO notified: yes.
## Internal Policy
Our AI governance policy (AI-GOV-2024) covers all AI systems.
We review it annually.
## Conclusion
This system complies with applicable regulations.
```

### Why This Fails (Gate Analysis)

| Gate | Result | Reason |
|------|--------|--------|
| H03 -- Kind correct | FAIL | Artifact kind not "conformity_assessment" |
| H02 -- ID pattern | FAIL | ID does not match p11_ca_[a-z0-9_]+ pattern |
| H04 -- RMS | FAIL | No risk-management-system section |
| H05 -- DGP | FAIL | GDPR data minimization != EU AI Act Art. 10 data governance |
| H06 -- HOM | FAIL | No human-oversight section |
| H07 -- Annex III | FAIL | Annex III category not identified |
| H08 -- PMM | FAIL | No post-market-monitoring plan |
| D02 -- Regulatory accuracy | 0/2.5 | GDPR != EU AI Act; no Annex IV citations |

**Score**: 7 hard gate failures. Blocked. Artifact is wrong artifact type entirely.

### How to Fix

1. Recognize that EU AI Act Art. 43 conformity assessment is SEPARATE from GDPR.
2. GDPR compliance is handled by the Data Protection Officer -- not part of Annex IV.
3. Start over with bld_output_template_conformity_assessment.md.
4. Identify the Annex-III category first (HRScreening = employment_workers, Annex III(4)).
5. Build the Annex-IV package: general description, development, monitoring, RMS, PMM, standards, DoC ref.

### Root Cause

The builder failed to distinguish:
- GDPR: data protection regulation (handled by DPO, separate from AI Act)
- EU AI Act conformity: technical documentation + process compliance for high-risk AI
- Compliance framework: internal governance (not the same as Annex-IV package)

The EU AI Act Annex-IV conformity assessment is a TECHNICAL DOCUMENTATION package,
not a policy statement. It contains design records, risk tables, test results,
and monitoring plans -- not policy assertions.
## Score Comparison

| Example | H-Gates | D Score | Total | Publishable? |
|---------|---------|---------|-------|-------------|
| Golden (MedTriage-v2) | 8/8 PASS | 9.2/10 | 9.2 | YES |
| Anti-Example 1 (missing RMS) | 7/8 (H04 FAIL) | blocked | blocked | NO |
| Anti-Example 2 (wrong artifact) | 1/8 (H01 only) | blocked | blocked | NO |

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
