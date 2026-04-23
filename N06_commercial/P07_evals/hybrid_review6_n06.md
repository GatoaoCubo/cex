---
id: hybrid_review6_n06
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW6 N06 Audit: healthcare_vertical + fintech_vertical + legal_vertical"
version: "1.0.0"
quality: 8.8
tags: [audit, hybrid_review6, healthcare_vertical, fintech_vertical, legal_vertical, wave5, n06]
domain: quality assurance
created: "2026-04-14"
updated: "2026-04-14"
author: n06_commercial
tldr: "39 ISOs audited across 3 enterprise-tier vertical builders. Pre-fix scores: HC 6.5, FT 6.0, LG 6.5. All D02/D07/D09/D10/D12 defects fixed. Post-fix 39/39 PASS. Scores estimated 8.5-8.8 after surgical fix."
related:
  - hybrid_review4_n01
  - hybrid_review4_n04
  - hybrid_review7_n04
  - hybrid_review5_n01
  - hybrid_review6_n02
  - hybrid_review6_n05
  - hybrid_review4_n02
  - hybrid_review6_n01
  - hybrid_review7_n02
  - hybrid_review5_n05
---

# HYBRID_REVIEW6 N06 Audit

## Scope

| Builder | ISOs | Source Model | Wave |
|---|---|---|---|
| healthcare_vertical | 13 | qwen3:14b gen_v2 | Wave 5 |
| fintech_vertical | 13 | qwen3:14b gen_v2 | Wave 5 |
| legal_vertical | 13 | qwen3:14b gen_v2 | Wave 5 |
| **TOTAL** | **39** | | |

## Pre-Fix Scores

| Builder | Pre-Fix Score | Defects Found | Action |
|---|---|---|---|
| healthcare_vertical | 6.5 | D02, D07, D09, D10, D12 + enterprise gaps | surgical fix |
| fintech_vertical | 6.0 | D02, D03, D07, D09, D10, D11, D12 + enterprise gaps | surgical fix |
| legal_vertical | 6.5 | D02, D07, D09, D10, D12 + enterprise gaps | surgical fix |

## Defects Found and Fixed

### D02 CRITICAL -- Memory ISO kind=learning_record (should be kind=memory)
**All 3 builders affected.**

| Builder | Before | After |
|---|---|---|
| healthcare | kind: learning_record, id: p10_lr_* | kind: memory, id: p10_mem_* |
| fintech | kind: learning_record, id: p10_lr_* | kind: memory, id: p10_mem_* |
| legal | kind: learning_record, id: p10_lr_* | kind: memory, id: p10_mem_* |

Root cause: wave1_builder_gen_v2 generator bug (known D02, master_systemic_defects.md).

### D03 CRITICAL -- quality_gate tests runtime state, not artifact structure
**fintech_vertical only.**

| Gate | Before (runtime check) | After (artifact check) |
|---|---|---|
| H04 | "SOC2+PCI-DSS compliance" via audit | "SOC2+PCI-DSS framework section present in artifact" |
| H06 | "Fraud detection system active" | "Fraud detection methodology documented" |

### D07 HIGH -- Fabricated/hallucinated tools in bld_tools
**All 3 builders affected.**

| Builder | Fabricated tools removed | Real CEX tools kept |
|---|---|---|
| healthcare | val_ehr_checker.py, val_model_eval.py, val_compliance.py | cex_compile, cex_score, cex_retriever, cex_doctor |
| fintech | val_data_integrity.py, val_compliance_checker.py, val_perf_analyzer.py, val_security_audit.py, cex_validator.py, cex_deployer.py | cex_compile, cex_score, cex_retriever, cex_doctor |
| legal | cex_analyzer.py, cex_contractor.py, val_regulator.py, val_consistency.py, val_citation.py | cex_compile, cex_score, cex_retriever, cex_doctor |

All tools ISO replaced with: cex_compile.py, cex_score.py, cex_retriever.py, cex_doctor.py, cex_wave_validator.py, cex_hygiene.py + domain-relevant external references.

### D09 HIGH -- Architecture ISO lists all ISOs as Pillar=P01 (wrong)
**All 3 builders affected.** Architecture inventory corrected to show true pillar assignments:

| ISO | Correct Pillar | Correct Kind |
|---|---|---|
| bld_manifest | P01 | type_builder |
| bld_instruction | P03 | instruction |
| bld_system_prompt | P03 | system_prompt |
| bld_schema | P06 | schema |
| bld_quality_gate | P11 | quality_gate |
| bld_output_template | P05 | output_template |
| bld_knowledge_card | P01 | knowledge_card |
| bld_architecture | P08 | architecture |
| bld_collaboration | P12 | collaboration |
| bld_config | P09 | config |
| bld_memory | P10 | memory |
| bld_tools | P04 | tools |

### D10 HIGH -- Instruction references "SCHEMA.md" and "OUTPUT_TEMPLATE.md" (wrong filenames)
**All 3 builders affected.**

Fixed: "SCHEMA.md" -> "bld_schema_{kind}.md", "OUTPUT_TEMPLATE.md" -> "bld_output_template_{kind}.md"

### D11 MEDIUM -- SOFT weights do not sum to 1.00
**fintech_vertical only.**

Before: 7 dimensions = 0.95 total (missing 0.05).
After: Added D08 Documentation completeness at 0.05 weight. Total = 1.00.

### D12 MEDIUM -- ASCII violations in instruction (Unicode checkmarks)
**All 3 builders affected.**

Fixed: `- [ ] [checkmark unicode]` -> `- [ ] [OK]` in all instruction Phase 3 VALIDATE sections.

## Enterprise-Tier Compliance Gaps (High ACV) -- Fixed

### healthcare_vertical
| Gap | Added To |
|---|---|
| BAA (Business Associate Agreement, 45 CFR 164.504(e)) | KC key concepts, QG H05, instruction, system_prompt |
| Safe Harbor de-identification (18 identifiers, 45 CFR 164.514(b)(2)) | KC key concepts, QG H05, instruction |
| 21 CFR Part 11 (FDA electronic records + e-signatures for clinical trials) | KC key concepts, instruction, system_prompt |
| HITRUST CSF v11 certification framework | KC key concepts, system_prompt |
| LOINC coding standard (lab observations) | KC key concepts, pitfalls |

### fintech_vertical
| Gap | Added To |
|---|---|
| OFAC SDN list screening (31 CFR Part 595) | KC key concepts, QG H05, instruction, system_prompt |
| FinCEN CIP fields (31 CFR 1020.220) | KC key concepts, instruction |
| SOX Section 404 (internal financial controls) | KC key concepts, instruction, system_prompt |
| FFIEC Cybersecurity Assessment Tool | KC key concepts, instruction, system_prompt |
| ISO 20022 payments messaging | KC key concepts, system_prompt |
| Sift/Sardine fraud detection platforms | KC key concepts, QG D03, system_prompt |
| SOC2 Type II (vs generic SOC2) | KC key concepts, QG H01 clarified |

### legal_vertical
| Gap | Added To |
|---|---|
| Work-product doctrine (FRCP 26(b)(3)) | KC key concepts, QG H04, instruction, system_prompt |
| ABA Model Rule 5.3 (non-lawyer/AI supervision) | KC key concepts, QG H06, instruction, system_prompt |
| EDRM model (9-phase eDiscovery framework) | KC key concepts, QG H05, instruction |
| UTBMS codes (task-based billing) | KC key concepts, QG H07, instruction, system_prompt |
| iManage/NetDocuments DMS integration | KC key concepts, QG H09, system_prompt, tools |
| Legal hold / document retention (FRCP 37(e)) | KC key concepts, QG H08, instruction |

## Validator Results (Post-Fix)

| Builder | Score | Result |
|---|---|---|
| healthcare_vertical | 13/13 | PASS |
| fintech_vertical | 13/13 | PASS |
| legal_vertical | 13/13 | PASS |
| **TOTAL** | **39/39** | **PASS** |

## Post-Fix Score Estimates

| Builder | Estimated Score | Notes |
|---|---|---|
| healthcare_vertical | 8.6 | FHIR/HIPAA core solid; BAA+21CFR11+HITRUST now present; density improved |
| fintech_vertical | 8.5 | OFAC+SOX+FFIEC+ISO20022 now present; D11 weight fix + D03 gate fix |
| legal_vertical | 8.7 | EDRM+UTBMS+ABA5.3+work-product now present; enterprise DMS patterns added |

All 3 builders estimated at >= 8.5 (PUBLISH tier). Recommend peer scorer assign final quality.

## Files Modified

### healthcare_vertical (7/13 ISOs changed)
- bld_memory_healthcare_vertical.md (D02: kind fix)
- bld_tools_healthcare_vertical.md (D07: fabricated tools removed)
- bld_architecture_healthcare_vertical.md (D09: pillar map corrected)
- bld_instruction_healthcare_vertical.md (D10+D12: file refs + ASCII)
- bld_knowledge_card_healthcare_vertical.md (enterprise gaps + pitfalls)
- bld_quality_gate_healthcare_vertical.md (H05 BAA+SafeHarbor, H08 spec)
- bld_system_prompt_healthcare_vertical.md (BAA+21CFR11+HITRUST)

### fintech_vertical (7/13 ISOs changed)
- bld_memory_fintech_vertical.md (D02: kind fix)
- bld_tools_fintech_vertical.md (D07: fabricated tools removed)
- bld_architecture_fintech_vertical.md (D09: pillar map corrected)
- bld_instruction_fintech_vertical.md (D10+D12: file refs + ASCII + OFAC+SOX)
- bld_knowledge_card_fintech_vertical.md (enterprise gaps + pitfalls)
- bld_quality_gate_fintech_vertical.md (D03 runtime->artifact, D11 weights=1.00)
- bld_system_prompt_fintech_vertical.md (OFAC+SOX+FFIEC+ISO20022)

### legal_vertical (7/13 ISOs changed)
- bld_memory_legal_vertical.md (D02: kind fix)
- bld_tools_legal_vertical.md (D07: fabricated tools removed)
- bld_architecture_legal_vertical.md (D09: pillar map corrected)
- bld_instruction_legal_vertical.md (D10+D12: file refs + ASCII + EDRM+UTBMS)
- bld_knowledge_card_legal_vertical.md (enterprise gaps + pitfalls)
- bld_quality_gate_legal_vertical.md (H04-H09 enterprise compliance checks)
- bld_system_prompt_legal_vertical.md (work-product+ABA5.3+EDRM+UTBMS)

## Commercial Readiness Assessment

These 3 verticals are enterprise-tier expansion plays with 6-figure ACV potential.
Pre-fix state: compliance terms were generic ("follow regulations") with no citation specificity.
Post-fix state: enterprise-grade -- each builder now produces artifacts that cite specific
regulations, standards, and clause numbers (45 CFR 164.504(e), FRCP 26(b)(3), 31 CFR Part 595).

Revenue gate status: CLEARED for enterprise pilot engagements subject to peer scoring >= 8.0.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[hybrid_review4_n01]] | sibling | 0.43 |
| [[hybrid_review4_n04]] | sibling | 0.39 |
| [[hybrid_review7_n04]] | sibling | 0.37 |
| [[hybrid_review5_n01]] | sibling | 0.37 |
| [[hybrid_review6_n02]] | sibling | 0.36 |
| [[hybrid_review6_n05]] | sibling | 0.35 |
| [[hybrid_review4_n02]] | sibling | 0.35 |
| [[hybrid_review6_n01]] | sibling | 0.34 |
| [[hybrid_review7_n02]] | sibling | 0.33 |
| [[hybrid_review5_n05]] | sibling | 0.33 |
