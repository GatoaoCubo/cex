---
id: n00_p11_kind_index
kind: knowledge_card
pillar: P11
nucleus: n00
title: "P11 Feedback -- Kind Index"
version: 1.0
quality: null
tags: [index, p11, archetype, n00]
---

<!-- 8F: F1=knowledge_card P11 F2=knowledge-card-builder F3=kinds_meta+schema F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Master index of all 26 kinds in pillar P11. Reference for /mentor, nucleus builders, and the 8F pipeline.

## Pillar: P11 Feedback
Learning, safety, and compliance infrastructure: quality gates, guardrails, compliance checklists, bug loops, self-improvement loops, and incident reports. The governance layer that keeps agents aligned.

## Kinds in P11

| Kind | Purpose | Primary Nucleus | Builder |
|------|---------|-----------------|---------|
| `ab_test_config` | A/B test experiment configuration for conversion optimization | N05 | `ab_test_config-builder` |
| `ai_rmf_profile` | NIST AI RMF profile artifact -- 4 functions (GOVERN/MAP/MEASURE/MANAGE | N05 | `ai_rmf_profile-builder` |
| `audit_log` | Immutable audit log configuration for SOC2 Type II compliance | N05 | `audit_log-builder` |
| `bugloop` | Automatic correction loop (detect > fix > verify) | N05 | `bugloop-builder` |
| `compliance_checklist` | Compliance checklist for SOC2, GDPR, HIPAA, EU AI Act audits | N05 | `compliance_checklist-builder` |
| `compliance_framework` | Regulatory mapping and attestation for AI systems | N05 | `compliance_framework-builder` |
| `conformity_assessment` | EU AI Act Annex IV conformity assessment for high-risk AI systems (Art | N05 | `conformity_assessment-builder` |
| `content_filter` | Input/output content filtering pipeline config | N05 | `content_filter-builder` |
| `content_monetization` | Config-driven content monetization pipeline — PARSE>PRICING>CREDITS>CH | N06 | `content_monetization-builder` |
| `enterprise_sla` | Enterprise SLA template with uptime, latency, support commitments | N05 | `enterprise_sla-builder` |
| `gpai_technical_doc` | EU AI Act GPAI technical documentation (Annex IV / Article 53) -- trai | N05 | `gpai_technical_doc-builder` |
| `guardrail` | Safety restriction (safety boundary) | N05 | `guardrail-builder` |
| `hitl_config` | Human-in-the-loop approval flow configuration: review triggers, escala | N05 | `hitl_config-builder` |
| `incident_report` | AI incident documentation and post-mortem | N05 | `incident_report-builder` |
| `lifecycle_rule` | Lifecycle rule (freshness, archive, promote) | N05 | `lifecycle_rule-builder` |
| `nps_survey` | NPS survey config: question, scale, follow-up, segmentation, cadence,  | N05 | `nps_survey-builder` |
| `optimizer` | Process optimizer (metric > action) | N05 | `optimizer-builder` |
| `quality_gate` | Quality barrier (pass/fail with score) | N05 | `quality_gate-builder` |
| `referral_program` | Referral program design with viral coefficient and reward structure | N05 | `referral_program-builder` |
| `reward_signal` | Continuous quality signal | N05 | `reward_signal-builder` |
| `roi_calculator` | ROI calculator spec with inputs, formulas, TCO comparison for economic | N06 | `roi_calculator-builder` |
| `safety_hazard_taxonomy` | MLCommons AILuminate / Llama Guard hazard taxonomy -- 12 hazard-catego | N05 | `safety_hazard_taxonomy-builder` |
| `safety_policy` | Organizational AI safety governance rules | N05 | `safety_policy-builder` |
| `self_improvement_loop` | Agent/system self-evolution mechanism | N05 | `self_improvement_loop-builder` |
| `subscription_tier` | SaaS subscription tier definition with pricing and feature matrix | N06 | `subscription_tier-builder` |
| `threat_model` | Structured hazard/risk assessment for AI systems | N05 | `threat_model-builder` |

## Usage
```python
# Build any of these via 8F:
python _tools/cex_8f_runner.py "your intent" --kind {kind} --execute
```

## CoC Hierarchy Note
These 26 kinds follow the convention-over-configuration hierarchy: each instance
(N01-N07) inherits this schema and fills the variables for its sin lens.
N00_genesis holds the canonical archetype; nuclei hold the instantiated versions.
