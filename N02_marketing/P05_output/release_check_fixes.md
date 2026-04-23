---
id: release_check_fixes_20260413
kind: audit_report
pillar: P07
nucleus: n02
mission: POLISH_WAVE2
title: Release Check Fixes -- POLISH_WAVE2
created: "2026-04-13"
quality: 8.8
density_score: 0.97
related:
  - polish_fixes_20260413
  - n02_audit_collaboration_pattern_builder
  - n02_hybrid_review_wave_review
  - n02_audit_action_paradigm_builder
  - system_health_20260413
  - n02_audit_voice_pipeline_builder
  - n02_audit_thinking_config_builder
  - hybrid_review3_n04
  - hybrid_review4_n02
  - n01_hybrid_review_wave1
---

# Release Check Fixes -- POLISH_WAVE2

## Summary

Starting state: **6 FAIL / 22 PASS / 28 total**
Ending state: **1 FAIL / 27 PASS / 28 total**

5 failures resolved. 1 residual (requires N03, outside N02 scope).

---

## Failures Fixed

### 1. readme:kinds -- FIXED
- **Was**: README mentioned 132 kinds (badge), 115 (Key Numbers section)
- **Reality**: 184 kinds in `.cex/kinds_meta.json`
- **Fix**: Updated all README occurrences to 184

### 2. readme:builders -- FIXED
- **Was**: README mentioned 128/111 builders
- **Reality**: 164 builder dirs in `archetypes/builders/` (excluding `_shared`)
- **Fix**: Updated all README occurrences to 164

### 3. readme:tools -- FIXED
- **Was**: README mentioned 83/51/52 tools
- **Reality**: 86 `cex_*.py` files in `_tools/`
  - Count shifted 84 -> 85 -> 86 during session as POLISH_WAVE2 nuclei added
    `cex_wave_validator.py`, `cex_wave_autofix.py`, `cex_wave_autofix_placeholders.py`
- **Fix**: Updated all README occurrences to 86

### 4. health:hooks_zero_errors (28 errors) -- FIXED
Fixed 10 files with malformed/incomplete frontmatter:

| File | Issue | Fix |
|------|-------|-----|
| `N02_marketing/audits/audit_action_paradigm_builder.md` | Missing `pillar` | Added `pillar: P07` |
| `N02_marketing/audits/audit_collaboration_pattern_builder.md` | Missing `pillar` | Added `pillar: P07` |
| `N02_marketing/audits/audit_thinking_config_builder.md` | Missing `pillar` | Added `pillar: P07` |
| `N02_marketing/audits/audit_voice_pipeline_builder.md` | Missing `pillar` | Added `pillar: P07` |
| `N02_marketing/P01_knowledge/kc_developer_experience_patterns.md` | Non-CEX frontmatter | Replaced with full CEX frontmatter |
| `N02_marketing/P01_knowledge/kc_tailwind_patterns.md` | Non-CEX frontmatter | Replaced with full CEX frontmatter |
| `N02_marketing/P01_knowledge/kc_visual_hierarchy_principles.md` | Non-CEX frontmatter | Replaced with full CEX frontmatter |
| `N02_marketing/P01_knowledge/knowledge_card_marketing.md` | Non-CEX frontmatter | Replaced with full CEX frontmatter |
| `N01_intelligence/P01_knowledge/embedding_config_intelligence.md` | Non-CEX frontmatter | Replaced with full CEX frontmatter |
| `N01_intelligence/P01_knowledge/kc_model_context_protocol.md` | Non-CEX frontmatter | Replaced with full CEX frontmatter |

Result: 537 artifacts validated, 0 errors (was 28).

### 5. health:flywheel_100pct (99%) -- FIXED
- **Root cause**: `N03_builder/P05_output/` directory missing
  (flywheel expects 10 standard subdirs per nucleus; `CEX_ROOT.iterdir()` finds `N03_builder`
  alphabetically before `N03_engineering`)
- **Fix**: Created `N03_builder/P05_output/.gitkeep`
- **Result**: Flywheel 99% -> 100% (109/109 checks WIRED)

---

## Residual Failure (requires N03)

### health:doctor_zero_fail -- OPEN
- **Builder**: `training-method-builder`
- **Issue**: Only 3 of 13 required ISOs exist
  - Present: `bld_instruction`, `bld_manifest`, `bld_system_prompt`
  - Missing 10: `bld_architecture`, `bld_collaboration`, `bld_config`, `bld_examples`,
    `bld_knowledge_card`, `bld_memory`, `bld_output_template`, `bld_schema`, `bld_skills`, `bld_tools`
- **Action needed**: Route to N03 to complete builder via 8F pipeline
- **Impact**: 1 doctor FAIL, does not block functional use of system

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[polish_fixes_20260413]] | downstream | 0.28 |
| [[n02_audit_collaboration_pattern_builder]] | sibling | 0.26 |
| [[n02_hybrid_review_wave_review]] | sibling | 0.25 |
| [[n02_audit_action_paradigm_builder]] | sibling | 0.24 |
| [[system_health_20260413]] | related | 0.24 |
| [[n02_audit_voice_pipeline_builder]] | sibling | 0.23 |
| [[n02_audit_thinking_config_builder]] | sibling | 0.22 |
| [[hybrid_review3_n04]] | upstream | 0.21 |
| [[hybrid_review4_n02]] | upstream | 0.20 |
| [[n01_hybrid_review_wave1]] | sibling | 0.19 |
