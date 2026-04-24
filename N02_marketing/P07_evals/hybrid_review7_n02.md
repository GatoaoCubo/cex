---
id: hybrid_review7_n02
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "HYBRID_REVIEW7 N02 Audit -- press_release, webinar_script, contributor_guide"
version: "1.0.0"
quality: 8.9
density_score: 0.99
tags: [audit, hybrid_review7, n02, press_release, webinar_script, contributor_guide]
domain: quality assurance
created: "2026-04-14"
updated: "2026-04-14"
author: n02_hybrid_review7
tldr: "3 builders audited (39 ISOs). press_release: 8.5 (D02 fixed). webinar_script: 9.0 (D02 fixed). contributor_guide: 6.2 -> 8.2 (6 ISOs rebuilt: D02, D07, D08, D09, D10, D12). All 39/39 ISOs pass validator."
sources:
  - N01_intelligence/reports/master_systemic_defects.md
  - archetypes/builders/press-release-builder/
  - archetypes/builders/webinar-script-builder/
  - archetypes/builders/contributor-guide-builder/
  - archetypes/builders/knowledge-card-builder/ (gold standard reference)
related:
  - hybrid_review4_n04
  - hybrid_review5_n01
  - hybrid_review4_n01
  - hybrid_review7_n04
  - master_systemic_defects
  - hybrid_review6_n02
  - hybrid_review7_n05
  - n01_hybrid_review_wave1
  - bld_manifest_memory_type
  - hybrid_review3_n02
---

# HYBRID_REVIEW7 N02 Audit

**Wave**: HYBRID_REVIEW7 (review wave, qwen3:14b source)
**Nucleus**: N02 Marketing
**Scope**: 3 builders, 39 ISOs
**Validator**: 39/39 PASS (pre and post-fix)
**Date**: 2026-04-14

---

## Summary Table

| Builder | Pre-fix score | Defects found | ISOs rebuilt | Post-fix score | Decision |
|---------|-------------|---------------|-------------|---------------|----------|
| press_release | 8.5 | D02 | 2 (memory, architecture) | 8.7 | LEAVE |
| webinar_script | 9.0 | D02 | 2 (memory, architecture) | 9.1 | LEAVE |
| contributor_guide | 6.2 | D02, D07, D08, D09, D10, D12 | 6 | 8.2 | SURGICAL (done) |

---

## 1. press_release Builder

**Score: 8.5 -> 8.7** | Decision: LEAVE (D02 fixed)

### Strengths
- System prompt: llm_function=BECOME (D01 PASS). AP style identity with detailed
  scope table, 7 quality rules, ALWAYS/NEVER lists. Excellent specificity.
- Instruction: 3-phase protocol with specific AP rules (dateline, attribution verb
  "said", inverted pyramid, 5Ws). No ASCII violations. No reference drift.
- Quality gate: 8 hard gates, 5 soft dimensions, weights sum to 1.00 (D11 PASS).
  Bypass table with explicit allow/deny for each gate.
- Output template: Guided placeholders with construction guidance. AP state
  abbreviation reference table included.
- Architecture: Lists all 13 ISOs with correct files, kinds, pillars, llm_functions.
  Full data flow diagram from briefing to wire service.
- Tools: CEX core tools (compile, score, retriever, doctor) plus AP-specific
  validation logic described with pseudo-code.
- Memory: Evidence-backed patterns (PR Newswire 2023 data, BusinessWire editorial
  guidance, Reuters style requirements). High-quality learning record.

### Defects Fixed

| Defect | File | Fix |
|--------|------|-----|
| D02: kind=learning_record | bld_memory_press_release.md | Changed to kind=memory |
| D02 echo: architecture row | bld_architecture_press_release.md | Updated Memory row to kind=memory |

### Residual Observations (non-blocking)
- quality_gate ID prefix is `p05_qg_` while frontmatter pillar is P11. Consistent with
  generator behavior across all builders. Not a blocking issue -- the ID indicates the
  kind being gated (P05 press_release), not the quality_gate's own pillar.

---

## 2. webinar_script Builder

**Score: 9.0 -> 9.1** | Decision: LEAVE (D02 fixed)

### Strengths
- System prompt: llm_function=BECOME, detailed persona with platform expertise
  (ON24, GoToWebinar, Zoom). Inverted attention curve concept. Specific 150 wpm
  calculation. Clear scope/boundary table. Quality rules numbered with criteria.
- Instruction: 7-step compose phase with exact word counts and cue requirements.
  Time budget formula provided. Phase 3 gate table with 11 checks including
  time check (TC), slide cue check (SC), speaker note check (SN).
- Quality gate: 8 hard gates, 5 scored dimensions, weights sum exactly 1.00
  (0.25+0.20+0.20+0.15+0.20). No bypass permitted (live delivery stakes).
  Retry protocol with 3-tier escalation (F6 -> F4 -> REJECT).
- Architecture: All 13 ISOs correctly inventoried with file names, kinds, pillars,
  llm_functions. Dependency graph with load order. External dependencies table.
- Memory: Evidence-backed observations (ON24 100K+ webinar data, GoToWebinar
  engagement reports). Pattern table with "when observed" and "application" columns.
- Tools: Real CEX tools plus grep-based validators (slide cue checker, Q&A seed
  counter). No fabricated tool names.

### Defects Fixed

| Defect | File | Fix |
|--------|------|-----|
| D02: kind=learning_record | bld_memory_webinar_script.md | Changed to kind=memory |
| D02 echo: architecture row | bld_architecture_webinar_script.md | Updated Memory row to kind=memory |

---

## 3. contributor_guide Builder

**Score: 6.2 -> 8.2** | Decision: SURGICAL (complete)

### Defects Found and Fixed

| # | Defect | ID | Severity | File | Fix applied |
|---|--------|-----|----------|------|-------------|
| 1 | kind=learning_record in memory ISO | D02 | CRITICAL | bld_memory_contributor_guide.md | Changed to kind=memory |
| 2 | Fabricated tools: cex_formatter.py, cex_linter.py, validate_guide.py, check_links.py, syntax_validator.py, consistency_checker.py | D07 | HIGH | bld_tools_contributor_guide.md | Rebuilt: CEX core tools only + grep-based manual checks |
| 3 | Bare output template: 2 placeholder steps ("step1", "step2"), no section structure | D08 | HIGH | bld_output_template_contributor_guide.md | Rebuilt: full 7-section scaffold matching schema body structure |
| 4 | Architecture: all ISOs show pillar=P05 (wrong), no file names, no llm_functions | D09 | HIGH | bld_architecture_contributor_guide.md | Rebuilt: correct pillars P01-P12, file names, llm_functions, load order, pillar coverage table |
| 5 | Instruction references "SCHEMA.md" and "OUTPUT_TEMPLATE.md" | D10 | HIGH | bld_instruction_contributor_guide.md | Rebuilt: references bld_schema_contributor_guide.md and bld_output_template_contributor_guide.md |
| 6 | Instruction has Unicode checkmarks (U+2705 "checkmark"), Chinese character in "signing[flow]" | D12 | MEDIUM | bld_instruction_contributor_guide.md | Rebuilt: ASCII-only throughout |
| 7 | System prompt: generic ALWAYS/NEVER bullets, no tables, weak quality rules | D15-adjacent | MEDIUM | bld_system_prompt_contributor_guide.md | Rebuilt: scope table, quality rules table, structured ALWAYS/NEVER |
| 8 | Memory: generic bullets, no tables, no evidence data | quality/density | MEDIUM | bld_memory_contributor_guide.md | Rebuilt: observation table with sources, pattern table, evidence table, recommendations |

### Post-Fix Assessment

**Instruction (rebuilt)**:
- 3-phase protocol with research input table, compose section map, validate gate table
- Explicit reference to bld_schema_contributor_guide.md and bld_output_template_contributor_guide.md
- ASCII-only throughout
- Phase 3 uses H01-H08 gate IDs matching quality_gate

**System Prompt (rebuilt)**:
- llm_function=BECOME (D01 PASS)
- Scope exclusion table (code of conduct, API docs, etc.)
- Quality rules table with specific requirements
- ALWAYS/NEVER with actionable constraints

**Architecture (rebuilt)**:
- All 13 ISOs: correct file names, kinds, pillar assignments (P01-P12), llm_functions
- Dependency graph with load order
- Pillar coverage table
- Architectural position with P05 peer builder comparison

**Output Template (rebuilt)**:
- Full CONTRIBUTING.md scaffold: Introduction, Getting Started, Contribution Workflow,
  Coding Standards, Commit Messages, Pull Request Process, Review Process, CLA/DCO
- Code blocks for setup, lint, format commands
- Both DCO and CLA options with "delete unused" instruction
- Section annotations table

**Tools (rebuilt)**:
- CEX core tools only: cex_compile.py, cex_score.py, cex_retriever.py, cex_doctor.py, cex_hygiene.py
- Validation checks via grep (no fabricated .py files)
- External references: GitHub CONTRIBUTING guide, Conventional Commits, DCO, Apache CLA, Markdownlint

**Memory (rebuilt)**:
- 5 observations with sources and confidence levels
- 5 patterns with application guidance
- Evidence table with sample sizes
- 5 prioritized recommendations

### Residual (acceptable)
- quality_gate SOFT has 7 dimensions instead of standard 5. Acceptable -- contributor_guide
  has 7 assessable quality dimensions. Weights sum to 1.00.
- schema lists "pillar: P05" for contributor_guide artifacts. This is correct -- CONTRIBUTING.md
  files are output artifacts (P05), not knowledge cards (P01).

---

## Defect Frequency (this wave)

| Defect | press_release | webinar_script | contributor_guide | Total |
|--------|-------------|----------------|-------------------|-------|
| D01 system_prompt INJECT | 0 | 0 | 0 | 0 |
| D02 memory kind=learning_record | 1 | 1 | 1 | 3 |
| D07 fabricated tools | 0 | 0 | 1 | 1 |
| D08 bare output_template | 0 | 0 | 1 | 1 |
| D09 architecture wrong pillars | 0 | 0 | 1 | 1 |
| D10 file reference drift | 0 | 0 | 1 | 1 |
| D12 ASCII violations | 0 | 0 | 1 | 1 |

**Pattern**: D02 is universal across Wave 6 gen_v2 output. D07-D12 concentrated in
contributor_guide, which was generated by wave1_builder_gen_v2 (not n02_wave6).
The n02_wave6 generated builders (press_release, webinar_script) are significantly
higher quality and show only D02.

**Generator signal**: Contributor_guide was generated by wave1_builder_gen_v2 which
produces the same defect profile as Wave 1/2 generators. The n02_wave6 generator
produced markedly better ISOs (press_release and webinar_script quality).

---

## Validator Results (post-fix)

| Builder | Before | After |
|---------|--------|-------|
| press_release | 13/13 PASS | 13/13 PASS |
| webinar_script | 13/13 PASS | 13/13 PASS |
| contributor_guide | 13/13 PASS | 13/13 PASS |

Total: 39/39 PASS

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[hybrid_review4_n04]] | sibling | 0.34 |
| [[hybrid_review5_n01]] | sibling | 0.33 |
| [[hybrid_review4_n01]] | sibling | 0.33 |
| [[hybrid_review7_n04]] | sibling | 0.32 |
| [[master_systemic_defects]] | sibling | 0.30 |
| [[hybrid_review6_n02]] | sibling | 0.30 |
| [[hybrid_review7_n05]] | sibling | 0.30 |
| [[n01_hybrid_review_wave1]] | related | 0.30 |
| [[bld_manifest_memory_type]] | downstream | 0.29 |
| [[hybrid_review3_n02]] | sibling | 0.29 |
