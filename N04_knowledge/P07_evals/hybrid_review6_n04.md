---
id: hybrid_review6_n04
kind: knowledge_card
pillar: P01
title: "HYBRID_REVIEW6: N04 Audit -- changelog, case_study, competitive_matrix (39 ISOs)"
version: "1.0.0"
quality: 8.8
author: n04_knowledge
tags: [audit, hybrid_review6, wave5, changelog, case_study, competitive_matrix]
domain: builder quality assurance
created: "2026-04-14"
updated: "2026-04-14"
tldr: "39 ISOs audited, 20 fixed. D02 (memory kind), D07 (fabricated tools), D08 (bare templates), D10 (SCHEMA.md drift) applied across all 3 builders. Post-fix: 39/39 PASS."
related:
  - bld_architecture_kind
  - hybrid_review5_n01
  - hybrid_review4_n01
  - hybrid_review7_n04
  - hybrid_review7_n05
  - hybrid_review4_n04
  - hybrid_review7_n02
  - bld_instruction_kind
  - kind-builder
  - n02_audit_action_paradigm_builder
---

# HYBRID_REVIEW6: N04 Builder Audit

## Scope

| Builder | Pillar | ISOs | Pre-fix Score | Post-fix Score |
|---------|--------|------|---------------|----------------|
| changelog | P01 | 13 | 6.5/10 | 8.5/10 |
| case_study | P05 | 13 | 6.0/10 | 8.5/10 |
| competitive_matrix | P01 | 13 | 6.5/10 | 8.5/10 |
| **TOTAL** | | **39** | **6.3 avg** | **8.5 avg** |

## Validator Results

| Builder | Pre-fix | Post-fix |
|---------|---------|----------|
| changelog-builder | 13/13 PASS (structural only) | 13/13 PASS |
| case-study-builder | 13/13 PASS (structural only) | 13/13 PASS |
| competitive-matrix-builder | 13/13 PASS (structural only) | 13/13 PASS |

Note: Validator checks structural compliance (YAML valid, frontmatter fields present, kind matches). Content-level defects (D02, D07, D08, D10) are not caught by validator -- they require manual audit.

## Defects Applied (from master_systemic_defects.md)

### D02: Memory ISO kind=learning_record (CRITICAL)
All three builders had `kind: learning_record` in their memory ISOs. Should be `kind: memory`.

| File | Before | After |
|------|--------|-------|
| bld_memory_changelog.md | kind: learning_record | kind: memory |
| bld_memory_case_study.md | kind: learning_record | kind: memory |
| bld_memory_competitive_matrix.md | kind: learning_record | kind: memory |

### D07: Fabricated tools in bld_tools (HIGH)
All three builders listed non-existent tools. Fixed to only reference real CEX tools.

| Builder | Fabricated (removed) | Real tools (kept/added) |
|---------|---------------------|-------------------------|
| changelog | cex_formatter.py, cex_publisher.py, val_syntax_checker.py, val_link_linter.py, val_version_comparator.py, val_duplicate_finder.py | cex_compile.py, cex_score.py, cex_retriever.py, cex_doctor.py, cex_wave_validator.py, cex_hooks.py |
| case_study | cex_analyzer.py, val_check.py, consistency_validator.py, data_integrity_checker.py, code_linter.py | cex_compile.py, cex_score.py, cex_retriever.py, cex_doctor.py, cex_wave_validator.py, cex_hooks.py |
| competitive_matrix | cex_visualizer.py, cex_analyzer.py, validator_check.py, consistency_checker.py, anomaly_detector.py, benchmark_comparator.py | cex_compile.py, cex_score.py, cex_retriever.py, cex_doctor.py, cex_wave_validator.py, cex_hooks.py |

### D08: Output templates with bare placeholders (HIGH)
All three output templates had minimal guidance. Rebuilt with industry-standard structure.

| Builder | Before | After |
|---------|--------|-------|
| changelog | Simple Changes table + config snippet | Full Keep a Changelog template: [Unreleased] + 6 sections (Added/Changed/Deprecated/Removed/Fixed/Security) + Migration block |
| case_study | Overview + Key Findings table + code block | Challenge-Solution-Outcome template with Company Snapshot, KPI table, ROI call-out, Pullquote block, Lessons Learned |
| competitive_matrix | Simple vendor table + YAML snippet | Feature parity grid + Gartner MQ positioning + Battle card (us vs primary competitor) + Pricing comparison + Strategic insights + Anti-FUD guide |

### D04: Domain contamination in competitive_matrix tools (CRITICAL)
bld_tools_competitive_matrix.md said "Aggregates exchange data" (financial domain). Fixed to domain-appropriate purpose.

### D10: File reference drift (HIGH)
bld_instruction_changelog.md and bld_instruction_case_study.md referenced `SCHEMA.md` and `OUTPUT_TEMPLATE.md` (generic names). Fixed to reference `bld_schema_{kind}.md` and `bld_output_template_{kind}.md`.

## Domain-Specific Improvements

### changelog
- Instruction rebuilt with 6 Keep a Changelog categories (Added/Changed/Deprecated/Removed/Fixed/Security)
- Knowledge card updated with Stripe API versioning model, conventional commits, migration guide pattern
- Schema updated with KAC 6-section body structure and migration requirement for MAJOR bumps
- Quality gate fixed: removed H08 "no markdown" (contradicted markdown format); added H06 migration requirement for MAJOR; replaced subjective gates with artifact-structure gates
- Examples updated to use KAC section names (Added/Fixed/Security) replacing Features/Fixes

### case_study
- Instruction rebuilt with champion pullquote approval flow, ROI call-out requirement, before/after KPI requirement
- Knowledge card updated with G2 testimonial standards, Gartner customer reference program, AWS template, Snowflake KPI table pattern
- Schema body structure updated to 7 sections (Company Snapshot/Challenge/Solution/Outcome/ROI Call-Out/Pullquote/Lessons Learned)
- Quality gate: H08 added for ROI call-out requirement; soft scoring weights verified at 1.00
- Output template rebuilt with named sections, KPI before/after table, ROI call-out block, Pullquote block

### competitive_matrix
- System prompt rebuilt with anti-FUD guidelines (factual, source-cited counters), corrected "NEVER use markdown" (output IS markdown)
- Knowledge card updated with Gartner MQ, Forrester Wave, G2 Grid, battle card structure, anti-FUD ethics
- Schema body structure updated with Battle Card and Anti-FUD sections
- Quality gate rebuilt with proper tables; D6 added for anti-FUD coverage scoring
- Output template rebuilt with Feature Parity Grid, Gartner MQ 2x2, Battle Card per-competitor, Pricing table, Anti-FUD guide

## ISOs Fixed (20 total)

| # | File | Defects Fixed |
|---|------|--------------|
| 1 | changelog/bld_memory_changelog.md | D02 |
| 2 | changelog/bld_instruction_changelog.md | D10, KAC sections |
| 3 | changelog/bld_output_template_changelog.md | D08, KAC format |
| 4 | changelog/bld_tools_changelog.md | D07 |
| 5 | changelog/bld_quality_gate_changelog.md | H08 wrong gate, gates restructured |
| 6 | changelog/bld_schema_changelog.md | KAC body structure, constraints |
| 7 | changelog/bld_examples_changelog.md | KAC section names, anti-examples |
| 8 | changelog/bld_knowledge_card_changelog.md | KAC detail, SemVer 2.0, Stripe pattern |
| 9 | case_study/bld_memory_case_study.md | D02 |
| 10 | case_study/bld_instruction_case_study.md | D10, pullquote, ROI, KPIs |
| 11 | case_study/bld_output_template_case_study.md | D08, Challenge-Solution-Outcome, pullquote, ROI |
| 12 | case_study/bld_tools_case_study.md | D07 |
| 13 | case_study/bld_quality_gate_case_study.md | H08 ROI call-out gate added |
| 14 | case_study/bld_schema_case_study.md | CSO body structure, constraints |
| 15 | case_study/bld_knowledge_card_case_study.md | G2, Gartner, AWS, Snowflake patterns |
| 16 | competitive_matrix/bld_memory_competitive_matrix.md | D02 |
| 17 | competitive_matrix/bld_system_prompt_competitive_matrix.md | Anti-FUD guidelines, corrected markdown rule |
| 18 | competitive_matrix/bld_output_template_competitive_matrix.md | D08, battle card, Gartner MQ, anti-FUD |
| 19 | competitive_matrix/bld_tools_competitive_matrix.md | D07, D04 domain contamination |
| 20 | competitive_matrix/bld_quality_gate_competitive_matrix.md | Tables fixed, anti-FUD scoring added |
| 21 | competitive_matrix/bld_knowledge_card_competitive_matrix.md | Gartner MQ, Forrester Wave, G2 Grid, battle card |
| 22 | competitive_matrix/bld_schema_competitive_matrix.md | Battle card and anti-FUD in body structure |

## ISOs Left Unchanged (17 total)
Architecture, collaboration, config, manifest for all three builders (structurally correct, domain-appropriate content). Case study and competitive matrix examples ISOs (content already good).

## Industry Standard Compliance

| Builder | Standard | Before | After |
|---------|----------|--------|-------|
| changelog | Keep a Changelog 6 sections | Missing Deprecated/Removed/Security | All 6 sections in schema/template/instruction |
| changelog | SemVer 2.0 migration guides | No mention | MAJOR bump requires Migration section |
| changelog | Conventional commits | Not referenced | Added to KC patterns |
| case_study | G2 testimonial (named attribution) | "anonymous or missing" only in H07 | H07 requires name + title |
| case_study | Gartner customer reference (ROI verification) | No ROI requirement | H08 ROI call-out required |
| case_study | CSO structure (before/after KPIs) | "3+ measurable KPIs" in H06 | KPI before/after table in template |
| competitive_matrix | Gartner MQ dimensions | Not in template | 2x2 ability/vision table in template |
| competitive_matrix | Battle card structure | Not in template | Full battle card section in template |
| competitive_matrix | Anti-FUD guidelines | Not present | Added to system_prompt and template |
| competitive_matrix | Data freshness (12-month staleness) | Not present | Added to KC and system_prompt rules |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_architecture_kind]] | downstream | 0.36 |
| [[hybrid_review5_n01]] | sibling | 0.33 |
| [[hybrid_review4_n01]] | sibling | 0.33 |
| [[hybrid_review7_n04]] | sibling | 0.32 |
| [[hybrid_review7_n05]] | sibling | 0.32 |
| [[hybrid_review4_n04]] | sibling | 0.31 |
| [[hybrid_review7_n02]] | sibling | 0.30 |
| [[bld_instruction_kind]] | downstream | 0.30 |
| [[kind-builder]] | downstream | 0.30 |
| [[n02_audit_action_paradigm_builder]] | downstream | 0.29 |
