---
kind: schema
id: bld_schema_conformity_assessment
pillar: P06
llm_function: CONSTRAIN
purpose: Data schema defining all required fields for a conformity_assessment artifact
quality: 9.1
title: "Conformity Assessment Builder -- Schema"
version: "1.0.0"
author: wave7_n05
tags: [conformity_assessment, builder, schema]
tldr: "Field definitions and validation rules for EU-AI-Act Annex-IV conformity assessment artifacts"
domain: "conformity_assessment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

# Conformity Assessment Builder -- Schema

## Top-Level Fields

| Field | Type | Required | Description | Example |
|-------|------|----------|-------------|---------|
| system_name | string | MANDATORY | Full name of the AI system | "MedTriage-v2 Clinical Decision Support" |
| system_version | string | MANDATORY | Version under assessment | "2.1.4" |
| provider_name | string | MANDATORY | Legal name of the provider per Art. 3(3) | "Acme Health AI GmbH" |
| provider_address | string | MANDATORY | Registered address of the provider | "Musterstrasse 1, 10115 Berlin, DE" |
| provider_contact | string | MANDATORY | Contact email or URL for technical queries | "compliance@acmehealth.ai" |
| annex_iii_category | enum | MANDATORY | Which Annex-III category applies | see Annex-III categories below |
| article_43_procedure | enum | MANDATORY | Conformity route selected | "internal_check" or "notified_body" |
| notified_body_id | string | CONDITIONAL | NB identification number (required if notified_body) | "NB-2345" |
| declaration_date | date | MANDATORY | Date the DoC is signed | "2026-07-15" |
| ce_marking_status | enum | MANDATORY | CE marking state | "planned" / "affixed" / "not_applicable" |
| eu_ai_act_ref | string | MANDATORY | Regulation citation | "EU AI Act 2024/1689" |
| technical_documentation_reference | string | MANDATORY | Pointer to full technical doc package | "TechDoc-v2.1.4-2026.pdf" |

## Annex-III Category Enum

| Value | Annex-III Reference | Notified Body Required? |
|-------|--------------------|-----------------------|
| biometric_identification | Annex III(1)(a) | YES (real-time remote) |
| biometric_categorisation | Annex III(1)(b) | NO (internal check) |
| critical_infrastructure | Annex III(2) | NO |
| education_vocational | Annex III(3) | NO |
| employment_workers | Annex III(4) | NO |
| essential_services | Annex III(5) | NO |
| law_enforcement | Annex III(6) | NO |
| migration_asylum | Annex III(7) | NO |
| justice_democratic | Annex III(8) | NO |

## Nested Object: risk_management_system

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| rms.process_description | string | MANDATORY | Description of the iterative RMS process (Art. 9) |
| rms.risks_identified | list[string] | MANDATORY | List of identified risks |
| rms.risk_estimation_method | string | MANDATORY | Method used to estimate and evaluate risks |
| rms.mitigation_measures | list[object] | MANDATORY | Each: {risk_id, measure, residual_risk_level} |
| rms.residual_risk_evaluation | string | MANDATORY | Overall assessment of acceptable residual risk |
| rms.review_schedule | string | MANDATORY | Cadence for post-deployment risk review |
| rms.version | string | MANDATORY | RMS document version |
| rms.last_updated | date | MANDATORY | Date of last RMS update |

## Nested Object: data_governance_plan

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| dgp.training_datasets | list[object] | MANDATORY | Each: {name, source, size, date_range, license} |
| dgp.validation_datasets | list[object] | MANDATORY | Each: {name, source, size, purpose} |
| dgp.test_datasets | list[object] | MANDATORY | Each: {name, source, size, purpose} |
| dgp.quality_criteria | list[string] | MANDATORY | Data quality criteria applied per Art. 10(3) |
| dgp.bias_mitigation | string | MANDATORY | Bias examination and mitigation measures |
| dgp.known_limitations | list[string] | MANDATORY | Known gaps or limitations in datasets |
| dgp.data_provenance | string | MANDATORY | Data lineage and provenance documentation ref |

## Nested Object: human_oversight_measures

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| hom.override_capability | string | MANDATORY | How humans can override or stop the system (Art. 14) |
| hom.interpretability_tools | list[string] | MANDATORY | Tools or methods for interpretability/explainability |
| hom.operator_training | string | MANDATORY | Training requirements for human overseers |
| hom.monitoring_interface | string | MANDATORY | Description of real-time monitoring dashboard |
| hom.anomaly_alerting | string | MANDATORY | How anomalies are surfaced to human operators |

## Nested Object: accuracy_robustness_cybersecurity

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| arc.accuracy_metrics | list[object] | MANDATORY | Each: {metric_name, threshold, achieved, dataset} |
| arc.robustness_measures | string | MANDATORY | Adversarial testing results and fallback spec |
| arc.cybersecurity_controls | string | MANDATORY | Threat model ref and penetration test summary |
| arc.degradation_handling | string | MANDATORY | Graceful degradation procedure |

## Nested Object: post_market_monitoring_plan

| Field | Type | Required | Description |
|-------|------|----------|-------------|
| pmm.objectives | list[string] | MANDATORY | Monitoring objectives and KPIs (Art. 72) |
| pmm.data_collection_method | string | MANDATORY | Telemetry or feedback pipeline specification |
| pmm.serious_incident_procedure | string | MANDATORY | SIR reporting procedure per Art. 73 |
| pmm.review_schedule | string | MANDATORY | Periodic review dates |
| pmm.corrective_action_thresholds | list[object] | MANDATORY | Each: {kpi, threshold, action} |
| pmm.report_recipients | list[string] | MANDATORY | Authorities and stakeholders for PMM reports |

## Validation Rules

| Rule | Constraint |
|------|-----------|
| ID pattern | ^p11_ca_[a-z0-9_]+\.md$ |
| kind | must be exactly "conformity_assessment" |
| annex_iii_category | must be one of the enum values above |
| article_43_procedure | must be "internal_check" or "notified_body" |
| notified_body_id | required if and only if article_43_procedure == "notified_body" |
| rms | all sub-fields mandatory, no nulls |
| data_governance_plan | all sub-fields mandatory, no nulls |
| human_oversight_measures | all sub-fields mandatory, no nulls |
| post_market_monitoring_plan | all sub-fields mandatory, no nulls |
| declaration_date | ISO 8601 date, not in past at time of generation |
| eu_ai_act_ref | must contain "2024/1689" |

## Aug-2026 Deadline Fields

Fields that MUST be completed before Aug-2026 for existing high-risk systems:

| Field | Deadline Flag |
|-------|--------------|
| risk_management_system (complete) | [AUG-2026-DEADLINE] |
| data_governance_plan (complete) | [AUG-2026-DEADLINE] |
| human_oversight_measures (complete) | [AUG-2026-DEADLINE] |
| post_market_monitoring_plan (complete) | [AUG-2026-DEADLINE] |
| technical_documentation_reference | [AUG-2026-DEADLINE] |
| declaration_date | [AUG-2026-DEADLINE] |
