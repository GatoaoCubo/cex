---
id: hybrid_review5_n04
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW5 N04 Audit: compliance_checklist, audit_log, data_residency"
version: "1.0.0"
quality: 8.9
tags: [audit, hybrid_review5, compliance, n04, wave4]
domain: knowledge quality assurance
created: "2026-04-14"
updated: "2026-04-14"
author: n04_knowledge
tldr: "39 ISOs audited across 3 compliance/knowledge builders. 21 defects fixed (D02x3, D06x4, D07x3, D08x2, D10x5, D12x4). All 39 ISOs: 13/13 PASS per builder."
sources:
  - N01_intelligence/reports/master_systemic_defects.md
  - archetypes/builders/compliance-checklist-builder/
  - archetypes/builders/audit-log-builder/
  - archetypes/builders/data-residency-builder/
related:
  - hybrid_review6_n05
  - hybrid_review6_n06
  - hybrid_review5_n01
  - hybrid_review4_n04
  - hybrid_review5_n05
  - hybrid_review4_n01
  - hybrid_review7_n05
  - hybrid_review7_n02
  - master_systemic_defects
  - hybrid_review6_n01
---

# HYBRID_REVIEW5 N04 Audit Report

## Scope

| Builder | Kind | Pillar | ISOs | Source Model |
|---------|------|--------|------|--------------|
| compliance-checklist-builder | compliance_checklist | P11 | 13 | qwen3:14b (Wave 4) |
| audit-log-builder | audit_log | P11 | 13 | qwen3:14b (Wave 4) |
| data-residency-builder | data_residency | P09 | 13 | qwen3:14b (Wave 4) |
| **TOTAL** | | | **39** | |

---

## Pre-Fix Assessment (5D Scoring)

### compliance_checklist (pre-fix: 7.0/10)

| Dim | Dimension | Score | Notes |
|-----|-----------|-------|-------|
| D1 | Domain accuracy | 0.90 | SOC2, GDPR, HIPAA, EU AI Act correctly cited |
| D2 | Structural integrity | 0.65 | D02, D07, D10, D12 violations |
| D3 | Regulatory precision | 0.85 | Real regulation refs (GDPR Art. 30, HIPAA SS164.306) |
| D4 | Tool integrity | 0.50 | 3 fabricated validation tools |
| D5 | ASCII compliance | 0.60 | Emoji in instruction + output_template |

### audit_log (pre-fix: 6.5/10)

| Dim | Dimension | Score | Notes |
|-----|-----------|-------|-------|
| D1 | Domain accuracy | 0.90 | SOC2 Type II, NIST 800-63B, ISO 27001 correctly cited |
| D2 | Structural integrity | 0.55 | D02, D06 (.yaml), D07, D08, D10, D12 |
| D3 | Regulatory precision | 0.85 | Immutable log standards correctly specified |
| D4 | Tool integrity | 0.40 | 6 fabricated tools (cex_formatter.py, val_*.py) |
| D5 | File reference accuracy | 0.50 | .yaml extension in ID pattern, SCHEMA.md references |

### data_residency (pre-fix: 6.5/10)

| Dim | Dimension | Score | Notes |
|-----|-----------|-------|-------|
| D1 | Domain accuracy | 0.85 | GDPR, CCPA, ISO/IEC 27001 cited correctly |
| D2 | Structural integrity | 0.50 | D02, D06 (.yaml + pillar=P11), D07, D08, D10, D12 |
| D3 | Regulatory precision | 0.80 | GDPR Art. 44-50 cited; Schrems II in tools refs |
| D4 | Tool integrity | 0.35 | cex_transformer.py, cex_logger.py, PyResidency (fake) |
| D5 | Pillar consistency | 0.45 | quality_gate pillar=P11 while manifest says P09 |

---

## Defects Fixed (21 total)

| # | Defect | Builders | ISO(s) | Fix Applied |
|---|--------|----------|--------|-------------|
| D02 | kind=learning_record in memory ISO | All 3 | bld_memory_*.md | kind: memory; id: p10_mem_*; tags updated |
| D06 | ID pattern uses .yaml not .md (audit_log schema) | audit_log | bld_schema_audit_log.md | Pattern changed to .md |
| D06 | ID pattern uses .yaml not .md (audit_log quality_gate) | audit_log | bld_quality_gate_audit_log.md | H02 pattern changed to .md |
| D06 | ID pattern uses .yaml not .md (data_residency schema) | data_residency | bld_schema_data_residency.md | Pattern changed to .md |
| D06 | quality_gate pillar=P11 (should be P09) | data_residency | bld_quality_gate_data_residency.md | pillar corrected to P09 |
| D06 | ID pattern uses .yaml not .md (data_residency quality_gate) | data_residency | bld_quality_gate_data_residency.md | H02 pattern changed to .md |
| D07 | Fabricated validation tools | compliance_checklist | bld_tools_compliance_checklist.md | val_checker.py, rule_linter.py, sim_validator.py removed; cex_hygiene.py added |
| D07 | Fabricated tools (cex_formatter.py, val_*.py, OpenAudit) | audit_log | bld_tools_audit_log.md | All fabricated tools removed; file rewritten with real CEX tools + real refs |
| D07 | Fabricated tools (cex_transformer.py, PyResidency) | data_residency | bld_tools_data_residency.md | All fabricated tools removed; real CEX tools + GDPR/Schrems II refs |
| D08 | output_template id uses .yaml (audit_log) | audit_log | bld_output_template_audit_log.md | id pattern changed to .md |
| D08 | output_template id uses .yaml (data_residency) | data_residency | bld_output_template_data_residency.md | id pattern changed to .md |
| D10 | SCHEMA.md reference (compliance instruction) | compliance_checklist | bld_instruction_compliance_checklist.md | -> bld_schema_compliance_checklist.md |
| D10 | OUTPUT_TEMPLATE.md reference (compliance instruction) | compliance_checklist | bld_instruction_compliance_checklist.md | -> bld_output_template_compliance_checklist.md |
| D10 | SCHEMA.md + CONTROL_MAP.md references (audit instruction) | audit_log | bld_instruction_audit_log.md | -> bld_schema_audit_log.md, bld_knowledge_card_audit_log.md |
| D10 | OUTPUT_TEMPLATE.md reference (audit instruction) | audit_log | bld_instruction_audit_log.md | -> bld_output_template_audit_log.md |
| D10 | SCHEMA.md + OUTPUT_TEMPLATE.md references (residency instruction) | data_residency | bld_instruction_data_residency.md | -> canonical bld_* filenames |
| D12 | Emoji in instruction Phase 3 (compliance) | compliance_checklist | bld_instruction_compliance_checklist.md | checkmark -> [OK] |
| D12 | Emoji in output_template (compliance) | compliance_checklist | bld_output_template_compliance_checklist.md | checkmark/cross -> PASS/FAIL |
| D12 | Emoji in instruction Phase 3 (audit_log) | audit_log | bld_instruction_audit_log.md | checkmark -> [OK] |
| D12 | Emoji in instruction Phase 3 (data_residency) | data_residency | bld_instruction_data_residency.md | checkmark -> [OK] |
| Extra | blockchain keyword in audit_log instruction | audit_log | bld_instruction_audit_log.md | -> WORM storage anchoring |

---

## Validator Results (post-fix)

| Builder | Result | Pass | Fail |
|---------|--------|------|------|
| compliance-checklist-builder | PASS | 13/13 | 0 |
| audit-log-builder | PASS | 13/13 | 0 |
| data-residency-builder | PASS | 13/13 | 0 |
| **TOTAL** | **PASS** | **39/39** | **0** |

---

## Post-Fix Scores (5D)

### compliance_checklist (post-fix: 8.8/10)

| Dim | Score | Notes |
|-----|-------|-------|
| Domain accuracy | 0.90 | SOC2 TSC, GDPR Art. 5-32, HIPAA, EU AI Act, NIST CSF |
| Structural integrity | 0.88 | All 13 ISOs correct kinds, pillars, IDs |
| Regulatory precision | 0.90 | Control references traceable to specific articles/annexes |
| Tool integrity | 0.90 | Only real CEX tools; external refs are real standards |
| ASCII compliance | 0.85 | All emoji removed; [OK]/PASS/FAIL replacements |

### audit_log (post-fix: 8.7/10)

| Dim | Score | Notes |
|-----|-------|-------|
| Domain accuracy | 0.92 | SOC2 CC6.1/CC7.1, ISO 27001 A.8.15, NIST 800-92 |
| Structural integrity | 0.88 | ID patterns now .md; pillar consistency restored |
| Regulatory precision | 0.90 | Immutable, tamper-evident, WORM, SHA-256 correctly specified |
| Tool integrity | 0.88 | Real CEX tools + CloudTrail/Splunk refs |
| ASCII compliance | 0.85 | Emoji removed; blockchain removed |

### data_residency (post-fix: 8.6/10)

| Dim | Score | Notes |
|-----|-------|-------|
| Domain accuracy | 0.88 | GDPR Art. 44-50, Schrems II, EU-US DPF 2023, ISO 27701 |
| Structural integrity | 0.90 | quality_gate pillar corrected to P09; .yaml -> .md |
| Regulatory precision | 0.88 | Schrems II cited in tools; SCCs in system_prompt |
| Tool integrity | 0.88 | Fabricated tools removed; AWS/Azure residency refs added |
| ASCII compliance | 0.85 | Emoji removed |

---

## Domain Accuracy Assessment (compliance lens)

These are enterprise-tier kinds. N04 verified all cited standards are real:

### compliance_checklist
| Standard | Reality Check | Status |
|----------|--------------|--------|
| SOC2 Trust Services Criteria (AICPA TSC 2017) | Real AICPA framework | PASS |
| ISO 27001:2022 Annex A | Real ISO standard | PASS |
| GDPR Articles 5-32 | Real EU regulation, correct articles | PASS |
| HIPAA SS164.306 Security Rule | Real HHS regulation | PASS |
| EU AI Act risk tiers | Real EU regulation (in force 2024) | PASS |
| NIST CSF | Real NIST framework | PASS |

### audit_log
| Standard | Reality Check | Status |
|----------|--------------|--------|
| SOC2 Type II CC6.1, CC7.1, CC7.2 | Real control identifiers | PASS |
| ISO 27001:2022 Annex A.8.15 | Real logging control | PASS |
| NIST SP 800-92 | Real guide (2006, still cited) | PASS |
| AWS CloudTrail, Datadog Audit Trail | Real products | PASS |
| SHA-256 hash chaining | Real cryptographic standard | PASS |

### data_residency
| Standard | Reality Check | Status |
|----------|--------------|--------|
| GDPR Articles 44-50 | Real chapter on third-country transfers | PASS |
| Schrems II (C-311/18) | Real CJEU ruling (2020) | PASS |
| EU-US Data Privacy Framework 2023 | Real framework (adopted Jul 2023) | PASS |
| ISO/IEC 27701:2019 | Real privacy information management standard | PASS |
| Standard Contractual Clauses (SCCs) | Real EU legal mechanism | PASS |

All standards verified as real. Zero hallucinated regulatory citations.

---

## Systemic Defect Correlation

| Master Defect | Found in Wave 4 | Fixed |
|---------------|-----------------|-------|
| D02 memory kind=learning_record | YES (all 3) | YES |
| D06 ID pattern .yaml not .md | YES (2/3 builders) | YES |
| D07 fabricated tools | YES (all 3) | YES |
| D08 bare placeholders in output_template | YES (2/3) | PARTIAL (core .yaml issue fixed; placeholder guidance already present) |
| D10 file reference drift | YES (all 3) | YES |
| D12 ASCII violations (emoji) | YES (all 3) | YES |
| D01 system_prompt llm_function=INJECT | NO - all BECOME | N/A |
| D03 quality_gate tests runtime not structure | NO | N/A |
| D04 domain hallucination | NO | N/A |
| D05 schema quality non-null | NO - all null | N/A |
| D09 architecture generic tech stack | NO - all 13 ISOs listed | N/A |

Wave 4 (qwen3:14b via gen_v2) shows improvement over Wave 1: D01, D03, D04, D05, D09 all ABSENT. Remaining systemic issues (D02, D06, D07, D10, D12) are generator bugs now documented in master_systemic_defects.md.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[hybrid_review6_n05]] | sibling | 0.32 |
| [[hybrid_review6_n06]] | sibling | 0.27 |
| [[hybrid_review5_n01]] | sibling | 0.27 |
| [[hybrid_review4_n04]] | sibling | 0.27 |
| [[hybrid_review5_n05]] | sibling | 0.26 |
| [[hybrid_review4_n01]] | sibling | 0.26 |
| [[hybrid_review7_n05]] | sibling | 0.25 |
| [[hybrid_review7_n02]] | sibling | 0.23 |
| [[master_systemic_defects]] | sibling | 0.23 |
| [[hybrid_review6_n01]] | sibling | 0.23 |
