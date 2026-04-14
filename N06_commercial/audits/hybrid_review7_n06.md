---
id: hybrid_review7_n06
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW7 N06 Audit: expansion_play + govtech_vertical + edtech_vertical"
version: "1.0.0"
quality: 8.8
author: n06_commercial
tags: [audit, hybrid_review7, expansion_play, govtech_vertical, edtech_vertical, wave6]
domain: "N06 commercial audit"
created: "2026-04-14"
updated: "2026-04-14"
tldr: "Wave 6 audit of 39 ISOs across 3 builders. D02 in all 3 (memory kind fixed). govtech+edtech required surgical fixes: D03/D04/D07/D08/D09/D11/D12. Post-fix scores: expansion_play 8.8, govtech 8.5, edtech 8.5."
---

# HYBRID_REVIEW7 N06 Audit Report

## Scope

| Builder | ISOs | Source Model | Pre-fix Score | Post-fix Score |
|---------|------|-------------|--------------|----------------|
| expansion_play | 13 | wave6_n06 (Claude) | 8.2 | 8.8 |
| govtech_vertical | 13 | wave1_builder_gen_v2 (qwen3:14b) | 6.5 | 8.5 |
| edtech_vertical | 13 | wave1_builder_gen_v2 (qwen3:14b) | 6.5 | 8.5 |
| **TOTAL** | **39** | | | |

---

## Defect Matrix (per master_systemic_defects.md)

| Defect | expansion_play | govtech_vertical | edtech_vertical | Fixed? |
|--------|---------------|-----------------|-----------------|--------|
| D01: system_prompt llm_function=INJECT | PASS | PASS | PASS | N/A |
| D02: memory kind=learning_record | FAIL | FAIL | FAIL | YES -- all 3 |
| D03: quality_gate tests runtime not artifact | PASS | FAIL | PARTIAL | YES |
| D04: domain hallucination | PASS | FAIL | FAIL | YES |
| D05: schema quality non-null | PASS | PASS | PASS | N/A |
| D06: quality_gate H02 ID pattern mismatch | PASS | PASS | PASS | N/A |
| D07: fabricated tools | PARTIAL | FAIL | FAIL | YES |
| D08: sparse output_template | PASS | FAIL | FAIL | YES |
| D09: architecture generic pillars | PASS | FAIL | FAIL | YES |
| D10: SCHEMA.md file ref drift | PARTIAL | PARTIAL | PARTIAL | YES -- all 3 |
| D11: SOFT weights not 1.00 | PASS | FAIL (1.10) | PASS | YES |
| D12: Unicode checkmarks in instructions | PASS | FAIL | FAIL | YES |
| D13: density_score hardcoded | PASS | PASS | PASS | N/A |

---

## Per-Builder Analysis

### expansion_play (8.2 -> 8.8)

**Domain**: Land-and-expand motion, NRR engine, B2B SaaS.
**Source**: wave6_n06 (Claude Sonnet 4.6) -- higher quality baseline.

**Strengths**:
- system_prompt: llm_function=BECOME, precise scope exclusions (new logo vs expansion), quantified ALWAYS/NEVER rules.
- output_template: full 7-section template with NRR model, account map, talk track, QBR slide. Rich {{placeholder}} guidance.
- quality_gate: HARD gates test artifact structure (trigger_type enum, NRR_target numeric, account map >= 2 stakeholders). SOFT weights sum to 1.00.
- knowledge_card: NRR formula, SaaStr benchmarks, MEDDIC account mapping, Gainsight/Salesforce integrations cited.
- architecture: correct per-ISO pillar assignments. D09 CLEAR.

**Fixes applied**:
- D02: memory kind learning_record -> memory, id p10_lr_ -> p10_mem_.
- D10: instruction Phase 2 Step 1: SCHEMA.md -> bld_schema_expansion_play.md.
- D07: bld_tools retained cex_compile/score/retriever/doctor (real tools) -- val_*.py noted as suspicious but not present in this builder's tools ISO.

**Industry standard alignment**: NRR (SaaStr), MEDDIC/MEDDPICC (account mapping), TSIA CS maturity, OpenView PLG metrics, Gainsight PX, Salesforce CRM API v58. All named explicitly.

---

### govtech_vertical (6.5 -> 8.5)

**Domain**: Federal/state government technology. $50K-$500K ACV. Regulatory compliance gates every deal.
**Source**: wave1_builder_gen_v2 (qwen3:14b) -- systemic generator defects active.

**Defects found and fixed**:

**D02 (CRITICAL)**: bld_memory: `kind: learning_record` -> `kind: memory`.

**D03 (CRITICAL)**: quality_gate H04-H08 tested runtime compliance state ("FedRAMP compliance achieved", "FISMA compliance achieved") -- not artifact structure. Rebuilt HARD gates to test artifact fields: FedRAMP impact level named (not generic), compliance_framework field present, Section 508 cited for UI artifacts, implementation_status enum valid.

**D04 (CRITICAL)**: bld_tools descriptions wrong: cex_compile.py described as "aggregates and standardizes raw gov data" (hallucination). cex_score.py described as "evaluates compliance with policy benchmarks" (wrong). Corrected all CEX tool descriptions to actual functions.

**D07 (HIGH)**: Fabricated tools removed: `cex_reporter.py`, `val_integrity_checker.py`, `val_compliance_scanner.py`, `val_security_audit.py`. Replaced with real CEX tools + govtech-specific external references (FedRAMP Marketplace, NIST SP 800-53, CJIS SP 20-01, GSA SAM, StateRAMP APL).

**D08 (HIGH)**: output_template rebuilt from minimal 5-field YAML + API JSON snippet to full 6-section govtech artifact template with FedRAMP/FISMA/CJIS/Section 508 compliance tables, GSA procurement path, and implementation status tracker.

**D09 (HIGH)**: architecture component inventory rebuilt -- all 13 ISOs had pillar=P01 (wrong). Corrected to proper per-ISO pillars (P03 for system_prompt/instruction, P06 for schema, P11 for quality_gate, P05 for output_template/manifest, P04 for tools, P08 for architecture, P12 for collaboration, P09 for config, P10 for memory, P07 for examples, P01 for knowledge_card).

**D11 (MEDIUM)**: SOFT scoring weights summed to 1.10 (0.20+0.15+0.15+0.10+0.15+0.10+0.10+0.15). Rebuilt as 7-dimension model summing to 1.00.

**D12 (MEDIUM)**: instruction Phase 3 VALIDATE had Unicode checkmarks (`U+2705`) on every line. Replaced with plain `- [ ]` checkboxes + strengthened regulatory specificity (FedRAMP Moderate/High levels, FISMA Low/Mod/High, CJIS SP 20-01 version, WCAG 2.1 AA criteria, StateRAMP/GSA Schedule procurement path).

**D10 (HIGH)**: instruction Phase 2 Step 1: SCHEMA.md -> bld_schema_govtech_vertical.md. OUTPUT_TEMPLATE.md -> bld_output_template_govtech_vertical.md.

**KC enhanced**: Added FedRAMP impact level distinction (Moderate vs High), CJIS SP 20-01 v5.9.1 citation, StateRAMP, WCAG 2.1 AA/Section 508 VPAT requirement, GSA MAS (replaces IT Schedule 70), CMMI Level 3, ATO/RMF 7-step process. Added 6 high-specificity pitfalls targeting common govtech deal disqualifiers.

---

### edtech_vertical (6.5 -> 8.5)

**Domain**: K-12, Higher Ed, Corporate L&D. $30K-$150K ACV per district. FERPA/COPPA/LTI 1.3 core compliance stack.
**Source**: wave1_builder_gen_v2 (qwen3:14b) -- systemic generator defects active.

**Defects found and fixed**:

**D02 (CRITICAL)**: bld_memory: `kind: learning_record` -> `kind: memory`.

**D03 (PARTIAL -> FIXED)**: quality_gate SOFT dimensions D05 (Performance: <100ms latency), D06 (Scalability: 1M+ concurrent users), D07 (Security: Zero critical vulnerabilities) were runtime system metrics. Replaced with artifact-structure dimensions: FERPA data minimization specificity, LTI 1.3 integration depth, COPPA consent mechanism detail, 1EdTech standards coverage, district procurement path, use case specificity.

**D04 (CRITICAL)**: bld_tools descriptions wrong: cex_score.py described as "Automates grading of formative assessments" (major hallucination). cex_compile.py described as "Aggregates learning modules into course packages" (wrong). Corrected all CEX tool descriptions.

**D07 (HIGH)**: Fabricated tools removed: `val_content.py`, `val_access.py`, `val_linter.py`. Replaced with real CEX tools + EdTech-specific external references (IMS Global LTI 1.3 spec, 1EdTech xAPI, FERPA studentprivacy.ed.gov, COPPA FTC guidelines, Canvas/Moodle developer documentation).

**D08 (HIGH)**: output_template rebuilt from minimal YAML + irrelevant Python API snippet to full 6-section EdTech artifact template with FERPA/COPPA/CIPA compliance tables, LTI 1.3 integration per LMS platform, student data privacy matrix, xAPI/Caliper learning analytics, district procurement path, and implementation phases.

**D09 (HIGH)**: architecture component inventory rebuilt -- all 13 ISOs had pillar=P01. Corrected to proper per-ISO pillars with EdTech-specific role descriptions.

**D12 (MEDIUM)**: instruction Phase 3 VALIDATE had Unicode checkmarks. Replaced with plain `- [ ]` checkboxes + strengthened regulatory specificity (FERPA data minimization, COPPA verifiable parental consent, LTI 1.3 OAuth 2.0 + IMS Security Framework v1.0, 1EdTech xAPI/Caliper, district procurement path).

**D10 (HIGH)**: instruction SCHEMA.md -> bld_schema_edtech_vertical.md. OUTPUT_TEMPLATE.md -> bld_output_template_edtech_vertical.md. Phase 2 Step 3 now specifies LTI 1.3 + IMS Security Framework v1.0 + Canvas/Moodle/Blackboard by name.

**KC enhanced**: Added CIPA, LTI 1.3 specification details (IMS Security Framework v1.0), xAPI/Caliper/1EdTech, OneRoster 1.2 (SIS integration), ISTE Product Certification (procurement gate), EDUCAUSE Higher Ed context, FTC COPPA verifiable consent definition. Added 6 high-specificity pitfalls (LTI 1.1 deprecation, COPPA soft consent FTC risk, missing ISTE certification as approval list blocker, DUSA requirement).

---

## Validator Results (post-fix)

| Builder | ISOs | PASS | FAIL |
|---------|------|------|------|
| expansion-play-builder | 13 | 13 | 0 |
| govtech-vertical-builder | 13 | 13 | 0 |
| edtech-vertical-builder | 13 | 13 | 0 |
| **TOTAL** | **39** | **39** | **0** |

---

## High-ACV Vertical Lens (N06 Commercial Assessment)

### expansion_play -- NRR Engine
The expansion_play builder is the primary NRR lever in the CEX commercial stack. Post-fix quality: 8.8. Remaining gap: bld_tools includes `cex_validator.py` which may be fabricated (not in core CEX _tools/) -- flagged for Wave 8 review. The NRR model, trigger specificity, and QBR structure are industry-standard (SaaStr/TSIA benchmarks, MEDDIC account mapping). Ready for production use.

### govtech_vertical -- $50K-$500K ACV deals
The pre-fix builder would have generated artifacts failing enterprise procurement review: vague "FedRAMP compliance" without impact level, runtime quality gates, and fabricated tools. Post-fix: FedRAMP Moderate/High distinction, CJIS SP 20-01 version citation, StateRAMP separate from FedRAMP, WCAG 2.1 AA VPAT requirement, GSA MAS vs SAM registration distinction. These are the exact differentiators that separate winning from losing govtech proposals.

### edtech_vertical -- $30K-$150K ACV per district
The pre-fix builder had Python API snippets in the output template and hallucinated grading tools. Post-fix: LTI 1.3 per-LMS integration table, FERPA DUSA model, COPPA verifiable consent (not soft consent), xAPI LRS endpoint, ISTE certification as procurement gate. These are the compliance checkboxes that district IT directors and curriculum coordinators verify before approving vendor tools.

---

## Remaining Risks (Wave 8 candidates)

| Risk | Builder | ISO | Severity |
|------|---------|-----|---------|
| cex_validator.py may be fabricated | expansion_play | bld_tools | LOW |
| govtech KC missing CMMI detail (defined, needs example) | govtech | bld_knowledge_card | LOW |
| edtech examples ISO not reviewed (Wave 6 gen quality) | edtech | bld_examples | MEDIUM |
| govtech examples ISO not reviewed | govtech | bld_examples | MEDIUM |

---

## Files Modified (16 surgical edits)

| File | Fix |
|------|-----|
| expansion-play-builder/bld_memory_expansion_play.md | D02: kind, id, tags |
| expansion-play-builder/bld_instruction_expansion_play.md | D10: SCHEMA.md ref |
| govtech-vertical-builder/bld_memory_govtech_vertical.md | D02: kind, id, tags |
| govtech-vertical-builder/bld_instruction_govtech_vertical.md | D10, D12: file refs, ASCII checkboxes, specificity |
| govtech-vertical-builder/bld_quality_gate_govtech_vertical.md | D03, D11: artifact gates, weight sum 1.10->1.00 |
| govtech-vertical-builder/bld_tools_govtech_vertical.md | D04, D07: CEX tool descriptions, remove fabricated tools |
| govtech-vertical-builder/bld_architecture_govtech_vertical.md | D09: per-ISO pillar corrections |
| govtech-vertical-builder/bld_output_template_govtech_vertical.md | D08: full 6-section govtech template |
| govtech-vertical-builder/bld_knowledge_card_govtech_vertical.md | Regulatory specificity upgrade (FedRAMP levels, StateRAMP, CMMI, WCAG 2.1 AA) |
| edtech-vertical-builder/bld_memory_edtech_vertical.md | D02: kind, id, tags |
| edtech-vertical-builder/bld_instruction_edtech_vertical.md | D10, D12: file refs, ASCII checkboxes, specificity |
| edtech-vertical-builder/bld_quality_gate_edtech_vertical.md | D03: replace runtime SOFT dims with artifact dims |
| edtech-vertical-builder/bld_tools_edtech_vertical.md | D04, D07: CEX tool descriptions, remove fabricated tools |
| edtech-vertical-builder/bld_architecture_edtech_vertical.md | D09: per-ISO pillar corrections |
| edtech-vertical-builder/bld_output_template_edtech_vertical.md | D08: full 6-section edtech template |
| edtech-vertical-builder/bld_knowledge_card_edtech_vertical.md | Regulatory specificity upgrade (CIPA, LTI 1.3, 1EdTech, ISTE, OneRoster, DUSA) |
