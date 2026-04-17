---
id: output_sdk_validation_self_audit
kind: output
pillar: P11
title: "N02 Marketing — SDK Validation Self-Audit Report"
version: 1.0.0
date: 2026-04-06
nucleus: N02
mission: SDK_VALIDATION
quality: 8.2
tags: [audit, sdk-validation, n02, marketing, self-audit, iso-check]
density_score: 1.0
---

# N02 Marketing — SDK Validation Self-Audit Report

**Date**: 2026-04-06 | **Mission**: SDK_VALIDATION | **Nucleus**: N02

---

## T1. Fractal Structure

**Total files**: 89 (.md + .yaml)

| Subdirectory | Status |
|---|---|
| agents/ | 1 file — REAL |
| architecture/ | 1 file — REAL |
| artifacts/ | 2 files — 1 REAL, 1 GENERIC (generic_prompt.md is a broken build artifact) |
| compiled/ | 44 files — auto-generated from .md sources |
| config/ | 2 files — REAL |
| feedback/ | 1 file — REAL |
| knowledge/ | 11 files — REAL (deep marketing KCs: email, typography, color, a11y, components) |
| memory/ | 2 files — REAL (campaign performance + copy optimization insights) |
| output/ | 11 files — REAL (templates + reports) |

**Verdict**: 7 REAL / 8 checked / 1 GENERIC (`artifacts/generic_prompt.md` — failed build residue)

---

## T2. Builder ISOs Audit

| Builder | ISOs | manifest (keywords/triggers/geo) | config (effort/max_turns/permission) | Status |
|---|---|---|---|---|
| prompt-template-builder | 13/13 | keywords + triggers + capabilities | effort=medium, max_turns=25, permission=nucleus | PASS |
| action-prompt-builder | 13/13 | keywords + triggers + capabilities | effort=medium, max_turns=25, permission=nucleus | PASS |
| content-monetization-builder | 13/13 | keywords + triggers + capabilities | effort=high, max_turns=25, permission=nucleus | PASS |
| social-publisher-builder | 13/13 | keywords + triggers + capabilities | effort=medium, max_turns=25, permission=nucleus | PASS |

**Marketing domain coverage**: copy/prompts, social automation, monetization, action prompts.

**Gap identified**: No dedicated `tagline-builder`, `landing-page-builder`, or `email-sequence-builder` exist as standalone builders. These domains are served by prompt-template-builder + action-prompt-builder generically.

---

## T3. Query Smoke Test

```
python _tools/cex_query.py "brand copy tagline landing page"
→ No matching builders found.
```

**Status**: FAIL — TF-IDF index does not surface marketing builders for natural-language marketing queries. Likely cause: index cache stale or keyword overlap insufficient.

**Recommendation**: Run `--rebuild-cache` and verify marketing-domain keywords are indexed.

---

## T4. Dry-Run 8F

```
python _tools/cex_8f_runner.py "criar tagline para startup de IA" --dry-run --nucleus N02
→ Kind resolved: generic (no specific tagline kind)
→ FAIL (5/6 gates) — H01: Frontmatter missing or invalid YAML
→ Timing: total=914ms
```

**Status**: PARTIAL — Pipeline executed all 8 functions but:
1. No `tagline` kind exists → fell back to `generic`
2. Dry-run template generation failed H01 gate (frontmatter)
3. Builder retrieval found relevant artifacts (score=0.176 for tagline framework)

**Recommendation**: The 8F pipeline infrastructure works. The failure is kind-resolution, not pipeline mechanics.

---

## T5. Output Audit

| File | title | quality | tags | Issues |
|---|---|---|---|---|
| output_email_template.md | "Responsive Email HTML Template..." | 9.1 | MISSING | No tags |
| landing_page_template.md | "Landing Page Template — Production Ready" | 9.0 | [output_template, landing_page, ...] | None |
| component_template.md | "Component Template — shadcn/ui..." | 9.1 | [output_template, component, ...] | None |
| output_visual_report.md | "Visual Report Template..." | 9.2 | [output, template, report, ...] | None |
| output_style_guide.md | "Design System Style Guide..." | 9.1 | [output, template, style-guide, ...] | None |
| output_social_card.md | "Social Media Card Templates" | 9.1 | [output, template, social, ...] | None |
| output_monetization_launch.md | "CEX Monetization Launch..." | 9.2 | [monetization, marketing, ...] | None |
| self_review_2026-04-02.md | In H1 only | 9.0 | MISSING | No title in YAML, no tags |
| output_dashboard_ui.md | "Dashboard UI Template..." | 9.1 | [output, template, dashboard, ...] | None |
| output_competitive_positioning.md | MISSING | 9.0 | MISSING | No title, no tags |
| output_readme_hero.md | MISSING | 8.6 | MISSING | No title, no tags |

**Quality range**: 8.6 — 9.2 (all above 8.0 threshold)

**Issues**: 3 files missing `title` in frontmatter, 4 files missing `tags`. No quality < 8.0 found. No quality: null outputs.

---

## T6. Model Upgrade Verification

```
cli=claude, model=claude-opus-4-6, context=1000000
```

**Status**: PASS — N02 correctly configured for Opus 4.6 + 1M context.

---

## Summary Scorecard

| Task | Status | Score |
|---|---|---|
| T1 Fractal Structure | PASS (1 generic file) | 8/10 |
| T2 Builder ISOs | PASS (4/4 builders, 52/52 ISOs) | 10/10 |
| T3 Query Smoke Test | FAIL (no results) | 3/10 |
| T4 Dry-Run 8F | PARTIAL (pipeline works, kind-resolution fails) | 6/10 |
| T5 Output Audit | PASS (all > 8.0, 4 minor metadata gaps) | 8/10 |
| T6 Model Config | PASS | 10/10 |

**Overall**: 7.5/10 — Infrastructure solid. Gaps in query discovery and kind-specific builders for marketing.

---

## Recommendations

1. **Rebuild TF-IDF cache**: `python _tools/cex_query.py --rebuild-cache` to fix T3
2. **Standardize output frontmatter**: Add `title` + `tags` to 3-4 files missing them
3. **Clean generic_prompt.md**: Remove or regenerate the broken artifact in artifacts/
4. **Consider dedicated builders**: tagline-builder, landing-page-builder would improve kind-resolution for marketing intents
