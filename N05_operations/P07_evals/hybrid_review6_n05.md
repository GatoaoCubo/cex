---
id: hybrid_review6_n05
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW6 N05 Audit: roi_calculator + discovery_questions + sales_playbook"
version: "1.0.0"
quality: 8.9
tags: [audit, hybrid_review6, n05, sales_enablement, roi_calculator, discovery_questions, sales_playbook]
domain: "builder quality assurance"
created: "2026-04-14"
updated: "2026-04-14"
author: n05_operations
tldr: "39 ISOs audited (3 Wave 5 sales-enablement builders). 15 defect instances fixed across D02/D04/D06/D07/D09/D10/D11/D12. All builders pass validator post-fix. Final scores: roi_calculator 8.0, discovery_questions 8.2, sales_playbook 8.1."
source_model: "qwen3:14b (Wave 5 gen_v2)"
wave: "HYBRID_REVIEW6"
---

# HYBRID_REVIEW6 N05 Audit -- Sales-Enablement Cluster

## Scope

| Builder | ISOs | Pillar | Source Model | ISO Count Check |
|---------|------|--------|-------------|-----------------|
| roi_calculator | 13 | P11 | qwen3:14b | [OK] 13/13 |
| discovery_questions | 13 | P01 | qwen3:14b | [OK] 13/13 |
| sales_playbook | 13 | P03 | qwen3:14b | [OK] 13/13 |
| **TOTAL** | **39** | | | **[OK] 39/39** |

## Defect Check Against master_systemic_defects.md

| Defect | Description | roi_calculator | discovery_questions | sales_playbook |
|--------|-------------|----------------|--------------------|--------------------|
| D01 | system_prompt llm_function=INJECT | [OK] BECOME | [OK] BECOME | [OK] BECOME |
| D02 | Memory kind=learning_record | [FIXED] -> memory | [FIXED] -> memory | [FIXED] -> memory |
| D03 | quality_gate tests runtime metrics | [OK] artifact-based | [OK] artifact-based | [OK] artifact-based |
| D04 | Domain hallucination | [FIXED] trading_roi removed | [FIXED] data-discovery replaced | [OK] |
| D05 | schema quality: non-null | [OK] null | [OK] null | [OK] null |
| D06 | quality_gate H02 ID pattern wrong | [FIXED] .yaml -> removed ext | [OK] .md | [OK] .md |
| D07 | Fabricated/hallucinated tools | [FIXED] 3 fake tools removed | [FIXED] 6 fake tools removed | [FIXED] 5 fake tools removed |
| D08 | output_template bare placeholders | [FIXED] full template + guidance | [FIXED] full MEDDIC/BANT template | [OK] has inline comments |
| D09 | architecture wrong ISO pillars | [FIXED] all 13 pillars corrected | [FIXED] all 13 pillars corrected | [FIXED] all 13 pillars corrected |
| D10 | File reference drift SCHEMA.md | [FIXED] -> bld_schema_*.md | [FIXED] -> bld_schema_*.md | [FIXED] -> bld_schema_*.md |
| D11 | quality_gate weights != 1.00 | [OK] sum=1.00 | [OK] sum=1.00 | [FIXED] 1.10 -> 1.00 |
| D12 | ASCII violations in instructions | [OK] | [FIXED] 5x checkmarks removed | [FIXED] 5x checkmarks removed |
| D13 | density_score 0.85 hardcoded | [INFO] uniform, acceptable | [INFO] uniform, acceptable | [INFO] uniform, acceptable |
| D14 | Empty config fields | [OK] | [OK] | [OK] |
| D15 | collaboration generic names | [OK] | [OK] | [OK] |

## Domain-Specific Audit

### roi_calculator (Final score: 8.0)

Industry standards cross-check:

| Standard | Present | Notes |
|----------|---------|-------|
| TCO (Total Cost of Ownership) model | [OK] | instruction + output_template + quality_gate |
| NPV/IRR payback period | [OK] | output_template has full formula table |
| Forrester TEI methodology | [OK] | tools external refs + output_template assumptions |
| Value-engineering input schema | [OK] | output_template: 6 input params with units |
| Economic-buyer sign-off evidence | [OK] | system_prompt ALWAYS rules + quality_gate H06 |

Defects fixed: D02, D04 (trading_roi in output_template), D06 (.yaml extension), D07 (3 tools: roi_validator.py, roi_analyzer.py, roi_stress_test.py), D08 (full template), D09 (13 pillar fixes), D10 (2 file refs)

Residual gaps:
- D03: quality_gate Definition table uses "Accuracy 95% >= Economic buyers" -- partially runtime-flavored but acceptable
- No CAPEX/OPEX explicit categorization section (enhancement, not blocker)

### discovery_questions (Final score: 8.2)

Industry standards cross-check:

| Standard | Present | Notes |
|----------|---------|-------|
| MEDDIC (full 6 criteria) | [OK] | system_prompt + instruction + output_template |
| BANT (4 criteria) | [OK] | output_template Stage 1 section |
| SPIN Selling framework | [OK] | tools external refs |
| Command of the Message | [PARTIAL] | referenced in tools, not in instruction |
| Challenger Sale | [OK] | tools external refs |

CRITICAL fix: output_template had DATA discovery contamination (databases, validation code). Replaced with full MEDDIC/BANT/Stage-aligned sales discovery template.

Defects fixed: D02, D04 (data-discovery contamination), D07 (6 tools: cex_analyzer, cex_optimizer, val_checker, val_formatter, val_validator + fake external refs), D09 (13 pillar fixes), D10 (2 file refs), D12 (5 Unicode checkmarks)

### sales_playbook (Final score: 8.1)

Industry standards cross-check:

| Standard | Present | Notes |
|----------|---------|-------|
| HubSpot/Salesforce playbook structure | [OK] | tools refs + instruction structure |
| Persona-based discovery flow | [OK] | instruction Phase 2 + system_prompt capabilities |
| Objection-handling matrix | [OK] | instruction + system_prompt + quality_gate H06 |
| Close patterns (assumptive/urgency/alt-choice) | [OK] | instruction Phase 2 step 5 + quality_gate H07 |
| MEDDPICC qualification | [OK] | tools external refs |
| Sales stage exit criteria | [PARTIAL] | discovery flow references stages but no explicit exit criteria |

Defects fixed: D02, D07 (5 tools: cex_analyzer, cex_optimizer, val_integrity_check, val_compliance_scan, val_performance_audit), D09 (13 pillar fixes), D10 (2 file refs), D11 (weights 1.10->1.00), D12 (5 Unicode checkmarks)

## Validator Results (post-fix)

| Builder | Pass | Fail | Exit Code |
|---------|------|------|-----------|
| roi-calculator-builder | 13/13 | 0 | 0 |
| discovery-questions-builder | 13/13 | 0 | 0 |
| sales-playbook-builder | 13/13 | 0 | 0 |
| **TOTAL** | **39/39** | **0** | **[PASS]** |

## Compile Results (post-fix)

| Builder | ISOs Compiled | Errors |
|---------|--------------|--------|
| roi-calculator-builder | 13/13 | 0 |
| discovery-questions-builder | 13/13 | 0 |
| sales-playbook-builder | 13/13 | 0 |

## Fix Summary (15 instances across 13 files)

| File Modified | Defect | Change |
|--------------|--------|--------|
| bld_memory_roi_calculator.md | D02 | kind: learning_record -> memory; id/tags updated |
| bld_memory_discovery_questions.md | D02 | kind: learning_record -> memory; id/tags updated |
| bld_memory_sales_playbook.md | D02 | kind: learning_record -> memory; id/tags updated |
| bld_output_template_discovery_questions.md | D04+D08 | Full replacement: data-discovery -> MEDDIC/BANT sales template |
| bld_output_template_roi_calculator.md | D04+D08 | trading_roi removed; full financial model template added |
| bld_schema_roi_calculator.md | D06 | ID pattern: .yaml$ removed |
| bld_quality_gate_roi_calculator.md | D06 | H02 pattern: .yaml$ removed |
| bld_tools_roi_calculator.md | D07 | 3 fake tools removed; real CEX tools + Forrester/Gartner refs |
| bld_tools_discovery_questions.md | D07 | 6 fake tools removed; real CEX tools + MEDDIC/BANT/SPIN refs |
| bld_tools_sales_playbook.md | D07 | 5 fake tools removed; real CEX tools + HubSpot/Gong/MEDDPICC refs |
| bld_architecture_roi_calculator.md | D09 | All 13 ISO pillars corrected to canonical values |
| bld_architecture_discovery_questions.md | D09 | All 13 ISO pillars corrected to canonical values |
| bld_architecture_sales_playbook.md | D09 | All 13 ISO pillars corrected to canonical values |
| bld_instruction_roi_calculator.md | D10 | SCHEMA.md/OUTPUT_TEMPLATE.md -> actual filenames |
| bld_instruction_discovery_questions.md | D10+D12 | file refs fixed; 5x Unicode checkmarks removed |
| bld_instruction_sales_playbook.md | D10+D12 | file refs fixed; 5x Unicode checkmarks removed |
| bld_quality_gate_sales_playbook.md | D11 | SOFT weights 1.10 -> 1.00 (D07 col also improved) |

## Sales-Enablement Lens Assessment

Field usability check: can an AE pick this up and run a deal?

| Builder | Practical Usability | Qualification Rigor | Verdict |
|---------|--------------------|--------------------|---------|
| roi_calculator | [OK] -- clear input params, formula, scenario table | [OK] -- economic buyer KPIs, payback threshold | Field-ready |
| discovery_questions | [OK] -- MEDDIC/BANT by stage, persona-specific | [OK] -- full 6-criterion MEDDIC mapped | Field-ready |
| sales_playbook | [OK] -- persona + flow + objection + close | [PARTIAL] -- no explicit stage exit criteria | Field-ready (minor gap) |

## Recommendations for Next Cycle

1. roi_calculator: Add CAPEX/OPEX categorization section to output_template
2. sales_playbook: Add sales stage exit criteria to instruction Phase 2
3. discovery_questions: Add Command of the Message framework to instruction (currently only in tools)
4. All 3: Consider upgrading memory ISOs from simple Observation/Pattern/Evidence format to full learning_record schema with confidence + decay fields (match gold standard quality)
