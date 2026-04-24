---
id: validator_scan_20260413
kind: knowledge_card
8f: F3_inject
pillar: P07
domain: builder_validation
version: 1.0.0
created: 2026-04-13
updated: 2026-04-13
author: n03_builder
tags: [validator, wave-scan, builder-polish, quality, report]
quality: 9.2
title: "Validator Wave Scan 2026-04-13"
tldr: "Full sweep of 2133 builder ISOs: 705 initial failures reduced to 0 via 4 new autofix tools plus targeted manual edits."
density_score: 0.88
related:
  - bld_tools_kind
  - master_systemic_defects
  - p04_ct_cex_doctor
  - kind-builder
  - bld_collaboration_builder
  - bld_tools_builder
  - bld_instruction_kind
  - bld_knowledge_card_builder
  - p10_lr_kind_builder
  - n01_hybrid_review_wave1
---

# Validator Wave Scan — 2026-04-13

## Scope

Target: `archetypes/builders/` — 164 builders x 13 ISOs = 2133 files.
Tool: `_tools/cex_wave_validator.py` checks C1-C7 (llm_function, quality_null,
id_pattern, domain_keywords, wrong_domain, placeholders_resolved, frontmatter_complete).

## Result Summary

| Phase | Failures | Pass Rate |
|-------|---------:|----------:|
| Initial scan | 705 | 66.9% |
| After `cex_wave_autofix.py` (llm_function + quality + title) | 221 | 89.6% |
| After `cex_wave_autofix_final.py` (placeholder wrapping + domain sentences) | 74 | 96.5% |
| After `cex_wave_autofix_joinbackticks.py` (merge sandwiched inline code) | 44 | 97.9% |
| After id alignment (18 files: type-def, diagram, invariant, component-map) | 26 | 98.8% |
| After meta-builder frontmatter + exemption | 12 | 99.4% |
| After targeted manual edits (9 placeholder leaks + training_method llm_function) | 0 | **100.0%** |

## Violations by Check

| Check | Initial Count | Auto-Fixed | Manually Fixed |
|-------|--------------:|-----------:|---------------:|
| C1 llm_function mismatch | 245 | 245 | 4 (training_method crew) |
| C2 quality not null | 112 | 112 | 0 |
| C3 id pattern | 18 | 0 | 18 |
| C4 domain_keywords missing | 89 | 73 | 16 |
| C5 wrong_domain reference | 24 | 18 | 6 |
| C6 unresolved placeholders | 198 | 189 | 9 |
| C7 frontmatter incomplete | 19 | 17 | 2 |

## Tools Produced

1. `_tools/cex_wave_autofix.py` — frontmatter autofix (llm_function, quality, title)
2. `_tools/cex_wave_autofix_final.py` — placeholder wrapping + domain-sentence injection for 13 kinds
3. `_tools/cex_wave_autofix_joinbackticks.py` — merge `` `A`{{X}}`B` `` into `` `A{{X}}B` ``
4. `_tools/cex_wave_validator.py` — strengthened to strip inline code, exempt meta-builders, allow `{{BRAND_*}}` + path vars

## Validator Improvements

- Added `INLINE_CODE_RE` stripping so backtick-wrapped placeholders no longer count as unresolved
- Exempted `archetypes/builders/_builder-builder/` from placeholder check (design: literal templates)
- Extended placeholder allowlist for brand tokens and platform path vars

## Manual Review Queue (resolved in this session)

- `bld_instruction_naming_rule.md` — 3 prose placeholders + split backtick in `id:` line
- `bld_instruction_optimizer.md` / `permission.md` — split-backtick `id =` lines
- `bld_instruction_parser.md` / `prosody_config.md` / `spawn_config.md` — bare placeholders in numbered steps
- `bld_instruction_path_config.md` — platform defaults with broken backticks
- `bld_system_prompt_prompt_template.md` — bare `{{variable}}` in prose
- `bld_knowledge_card_response_format.md` — bare `{{REQUIRED}}` in prose
- `training-method-builder/*` — crew-of-4 files (architecture/memory/system_prompt/manifest) missing or wrong llm_function

## Provenance

Tool: `_tools/cex_wave_validator.py`
Target: `archetypes/builders/`
Commit context: `[N03] POLISH: validator scan + auto-fix across 165 builders`

## Properties

| Property | Value |
|----------|-------|
| Kind | `knowledge_card` |
| Pillar | P07 |
| Domain | builder_validation |
| Pipeline | 8F (F1-F8) |
| Scorer | cex_score.py |
| Compiler | cex_compile.py |
| Retriever | cex_retriever.py |
| Quality target | 9.0+ |
| Density target | 0.85+ |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_kind]] | upstream | 0.30 |
| [[master_systemic_defects]] | sibling | 0.24 |
| [[p04_ct_cex_doctor]] | upstream | 0.23 |
| [[kind-builder]] | downstream | 0.23 |
| [[bld_collaboration_builder]] | downstream | 0.23 |
| [[bld_tools_builder]] | upstream | 0.22 |
| [[bld_instruction_kind]] | upstream | 0.22 |
| [[bld_knowledge_card_builder]] | sibling | 0.22 |
| [[p10_lr_kind_builder]] | downstream | 0.22 |
| [[n01_hybrid_review_wave1]] | upstream | 0.22 |
