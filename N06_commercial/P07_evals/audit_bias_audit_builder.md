---
id: n06_audit_bias_audit_builder
kind: audit_report
nucleus: n06
pillar: P07
mission: HYBRID_REVIEW
quality: 8.9
title: "Audit: bias_audit-builder (13 ISOs)"
version: "1.0.0"
created: "2026-04-13"
updated: "2026-04-13"
tags: [bias_audit, audit, hybrid_review, n06]
tldr: "13 ISOs audited. 7 pass, 6 need taxonomy injection. Main gaps: missing BBQ/WinoBias/StereoSet benchmarks, no Colorado AI Act / NYC LL144 citations, pillar inconsistency."
related:
  - bld_knowledge_card_bias_audit
  - n06_hybrid_review_final
  - bld_tools_bias_audit
  - n01_hybrid_review_wave1
  - kc_bias_audit
  - bld_collaboration_bias_audit
  - bld_examples_bias_audit
  - n06_audit_safety_policy_builder
  - bias-audit-builder
  - p07_qg_bias_audit
---

# Audit: bias_audit-builder

## Scoring Matrix

| ISO | File | D1-Completeness | D2-Real Benchmarks | D3-Legal Frameworks | D4-Commercial Lens | Score | Action |
|-----|------|-----------------|-------------------|---------------------|-------------------|-------|--------|
| manifest | bld_manifest_bias_audit.md | 0.85 | 0.75 (IBM AIF360, What-If Tool named) | 0.65 (EU AI Act, FDA) | 0.60 | 7.5 | PASS |
| instruction | bld_instruction_bias_audit.md | 0.80 | 0.70 (demographic parity, equalized odds) | 0.60 | 0.55 | 7.0 | PASS |
| knowledge_card | bld_knowledge_card_bias_audit.md | 0.80 | 0.60 (EU AI Act, FAT* -- old name) | 0.55 (missing CO, NYC LL144) | 0.50 | 6.5 | FIX |
| schema | bld_schema_bias_audit.md | 0.75 | 0.55 | 0.50 | 0.45 | 6.0 | FIX |
| quality_gate | bld_quality_gate_bias_audit.md | 0.70 | 0.55 (bias_score threshold but no scale) | 0.40 (ID pattern inconsistency) | 0.40 | 6.0 | FIX |
| output_template | bld_output_template_bias_audit.md | 0.80 | 0.65 | 0.60 | 0.65 | 7.0 | PASS |
| examples | bld_examples_bias_audit.md | 0.85 | 0.75 (demographic parity, SHAP, 70% reduction) | 0.65 | 0.65 | 7.5 | PASS |
| system_prompt | bld_system_prompt_bias_audit.md | 0.75 | 0.60 (AIF360, FAT* guidelines) | 0.50 | 0.45 | 6.5 | FIX |
| architecture | bld_architecture_bias_audit.md | 0.70 | 0.55 | 0.45 | 0.45 | 6.5 | FIX |
| collaboration | bld_collaboration_bias_audit.md | 0.85 | 0.75 (benchmark_builder, eval_metric_builder) | 0.70 | 0.70 | 8.0 | PASS |
| config | bld_config_bias_audit.md | 0.80 | 0.70 | 0.65 | 0.60 | 7.0 | PASS |
| memory | bld_memory_bias_audit.md | 0.70 | 0.55 | 0.50 | 0.45 | 6.5 | FIX |
| tools | bld_tools_bias_audit.md | 0.80 | 0.70 (Fairlearn, IBM AIF360, TF DV) | 0.60 | 0.60 | 7.0 | PASS |

**Summary: 7 pass, 6 fix, 0 rebuild**

## Critical Gaps

### Missing Named Benchmarks (all 6 flagged ISOs)
Required benchmark citations missing across the builder:

| Benchmark | Source | What it measures | Why mandatory |
|-----------|--------|-----------------|---------------|
| BBQ (Bias Benchmark for QA) | Parrish et al., ACL 2022 | 11 social categories: age, disability, gender, nationality, race, religion, SES, sexual orientation, appearance, ethnicity, gender identity | Core NLP bias benchmark |
| WinoBias | Zhao et al., NAACL 2018 | Gender bias in pronoun resolution (co-reference) | Employment & HR AI systems |
| StereoSet | Nadeem et al., ACL 2021 | Stereotype score (SS) and language model score (ICAT) | LLM bias evaluation |
| BOLD | Dhamala et al., FAccT 2021 | Bias in open-ended generation (race, gender, religion, political ideology, profession) | Content generation systems |
| HolisticBias | Smith et al., EMNLP 2022 | 600+ demographic descriptors across 13 axes | Comprehensive generation bias |
| Winogender | Rudinger et al., NAACL 2018 | Gender occupational stereotypes | HR / recruitment AI |

### Missing Legal Frameworks

| Jurisdiction | Law | Key Requirement | Audit Trigger |
|-------------|-----|-----------------|---------------|
| Colorado | AI Act SB 22-169 (2024) | Bias audit for high-risk AI in employment, housing, credit | Annual or pre-deployment |
| New York City | Local Law 144 (2023) | Bias audit for automated employment decision tools (AEDTs); public summary required | Annual + independent auditor |
| Illinois | AIVIA (HB 2557) | Notify candidates of AI video analysis; annual bias audit | Before deployment |
| EU | AI Act Art. 10 | Training data governance for high-risk AI (demographic representation) | Conformity assessment |
| EU | AI Act Art. 64 | Documentation access for bias audit by national authority | On-demand |

### Pillar Inconsistency
- bld_manifest_bias_audit.md: `pillar: P07` (correct for bias_audit)
- bld_quality_gate_bias_audit.md: `pillar: P11` (wrong -- should be P07)
- bld_schema_bias_audit.md: `pillar: P06` but ID pattern references P07
- Fix: all ISOs for bias_audit should be `pillar: P07` (evaluation)

### FAT* Conference -- deprecated name
All ISOs reference "FAT*" -- conference was renamed FAccT (Fairness, Accountability, and Transparency) in 2020.
Update all references to: "ACM FAccT (formerly FAT*)"

### Missing `benchmarks_used` field in schema
Current schema has `bias_type` (string) and `affected_groups` (list) but no:
- `benchmarks_used`: list of named benchmarks applied (BBQ, WinoBias, etc.)
- `jurisdiction_applicability`: list (Colorado, NYC LL144, EU AI Act)
- `audit_tool`: string (IBM AIF360, Fairlearn, etc.)

## Commercial Risk Classification

| ISO | Legal Liability Risk | Brand Risk | Product Quality Risk |
|-----|---------------------|------------|---------------------|
| knowledge_card | HIGH -- missing CO AI Act, NYC LL144 = compliance gap for US enterprise customers | HIGH | HIGH |
| schema | HIGH -- no benchmarks_used field = unauditable | MEDIUM | HIGH |
| quality_gate | HIGH -- ID pattern inconsistency = artifacts fail H02 gate | MEDIUM | HIGH |
| system_prompt | MEDIUM -- FAT* reference = dated methodology signal | LOW | MEDIUM |
| architecture | LOW -- wrong context (crypto exchange) but structural is fine | LOW | MEDIUM |
| memory | LOW | LOW | MEDIUM |

## Revenue Implications

### Compliance Tier Opportunity
NYC LL144 + Colorado AI Act mandate ANNUAL bias audits from INDEPENDENT auditors.
A bias_audit-builder producing NYC LL144-compliant audit reports is a billable deliverable:
- NYC LL144 compliance report: $3,000-$15,000 per engagement (market rate 2024)
- Enterprise buyers (HR tech, fintech) pay premium for pre-validated methodology
- Gap to close: add NYC LL144 checklist + independent auditor attestation template to output_template

### Recommended Schema Addition for Enterprise Tier
```yaml
compliance_outputs:
  nyc_ll144_summary: true   # public summary required by law
  colorado_impact_assessment: true
  eu_conformity_docs: false  # only for EU high-risk AI
enterprise_audit_ready: true
independent_auditor_required: true
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_bias_audit]] | upstream | 0.52 |
| [[n06_hybrid_review_final]] | sibling | 0.38 |
| [[bld_tools_bias_audit]] | upstream | 0.35 |
| [[n01_hybrid_review_wave1]] | sibling | 0.33 |
| [[kc_bias_audit]] | upstream | 0.32 |
| [[bld_collaboration_bias_audit]] | downstream | 0.30 |
| [[bld_examples_bias_audit]] | related | 0.29 |
| [[n06_audit_safety_policy_builder]] | sibling | 0.27 |
| [[bias-audit-builder]] | related | 0.27 |
| [[p07_qg_bias_audit]] | related | 0.27 |
