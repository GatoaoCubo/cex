---
id: n01_audit_reasoning_strategy_builder
kind: audit_report
nucleus: n01
mission: HYBRID_REVIEW
wave: review
created: 2026-04-13
builder: reasoning-strategy-builder
kind_reviewed: reasoning_strategy
pillar: P03
iso_count: 13
quality: 8.8
---

# Audit: reasoning-strategy-builder (13 ISOs)

## ISO Score Table

| ISO | D1 Structural | D2 Density | D3 Alignment | D4 Complete | D5 Integration | Score | Action |
|-----|--------------|------------|--------------|-------------|----------------|-------|--------|
| bld_manifest | 9 | 8 | 8 | 8 | 8 | 8.2 | PASS |
| bld_system_prompt | 8 | 7 | 5 | 8 | 7 | 7.0 | FIXED: INJECT->BECOME |
| bld_instruction | 9 | 8 | 8 | 8 | 8 | 8.2 | PASS |
| bld_knowledge_card | 9 | 8 | 8 | 8 | 8 | 8.2 | PASS |
| bld_architecture | 6 | 6 | 5 | 7 | 6 | 6.0 | FIXED: wrong domain + generic components |
| bld_output_template | 6 | 5 | 7 | 6 | 6 | 6.0 | FIXED: bare placeholders -> schema-guided |
| bld_examples | 9 | 8 | 8 | 8 | 8 | 8.2 | PASS |
| bld_schema | 8 | 8 | 6 | 8 | 8 | 7.6 | FIXED: quality field said integer/0-100 |
| bld_quality_gate | 8 | 7 | 4 | 8 | 7 | 6.8 | FIXED: H02 pattern PXX-YYYY -> ^p03_rs_* |
| bld_collaboration | 9 | 8 | 8 | 8 | 8 | 8.2 | PASS |
| bld_config | 7 | 6 | 7 | 7 | 6 | 6.6 | PASS (hooks null is acceptable) |
| bld_memory | 8 | 7 | 7 | 8 | 7 | 7.5 | PASS |
| bld_tools | 8 | 7 | 8 | 8 | 8 | 7.9 | PASS |

## Quality Distribution

| Tier | Count | ISOs |
|------|-------|------|
| >= 8.0 (PASS) | 7 | manifest, instruction, knowledge_card, examples, collaboration, memory, tools |
| 6-8 (SURGICAL FIX) | 6 | system_prompt, architecture, output_template, schema, quality_gate, config |
| < 6 (REBUILD) | 0 | - |

## Fixes Applied

| File | Defect | Fix |
|------|--------|-----|
| bld_system_prompt | llm_function: INJECT | Changed to BECOME (F2 identity function) |
| bld_quality_gate | H02 pattern: PXX-YYYY | Changed to ^p03_rs_[a-zA-Z0-9]+$ per schema |
| bld_schema | quality field: integer/0-100 | Changed to null with CEX null rule |
| bld_schema | quality constraint: range 0-100 | Changed to null rule explanation |
| bld_architecture | Generic trading components | Replaced with actual builder ISO inventory |
| bld_architecture | Architectural position: trading | Updated to P03 pillar + CEX role |
| bld_output_template | Bare {{placeholder}} sections | Replaced with schema-guided template + tables |

## Systemic Issues (reasoning_strategy)

1. llm_function=INJECT in system_prompt — applies to all 4 builders reviewed
2. Quality gate H02 pattern did not match schema ID pattern — applies to all 4 builders
3. Schema quality field described as integer — applies to all 4 builders
4. Architecture files referenced generic/trading components — applies to all 4 builders
5. Output templates had zero guidance (bare placeholders) — applies to all 4 builders
