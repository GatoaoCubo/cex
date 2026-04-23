---
id: p07_qg_commercial
kind: quality_gate
pillar: P07
title: "N06 Quality Gate — Brand + Monetization (14 Checks)"
version: 4.0.0
created: 2026-03-30
updated: 2026-04-01
author: n06_commercial
domain: brand-identity-monetization
gate_count: 14
pass_threshold: 12
quality: 9.1
updated: 2026-04-07
tags: [quality_gate, commercial, N06, brand, monetization]
tldr: "14-check quality gate for N06 dual-role: 8 brand checks (config, archetype, voice, positioning, naming, book, consistency, propagation) + 6 revenue checks (pricing, funnel, transformation, platform, LTV, compliance)."
density_score: 0.94
axioms:
  - "NEVER publish below 8.0 — quality gate is a hard stop, not a suggestion."
  - "ALWAYS run brand audit before monetization checks — brand informs revenue."
linked_artifacts:
  primary: p07_sr_commercial
  related: [p02_agent_commercial_nucleus, n06_schema_brand_audit, n06_schema_brand_book]
related:
  - spec_n06_part2
  - spec_n06_brand_verticalization
  - p03_sp_commercial_nucleus
  - p02_agent_brand_nucleus
  - p03_sp_brand_nucleus
  - p02_agent_commercial_nucleus
  - n06_schema_brand_book
  - p08_ac_brand_nucleus
  - p12_wf_commercial
  - p02_mm_commercial_nucleus
---

# N06 Quality Gate — Brand + Monetization

## Brand Checks (8)

| # | Gate | Threshold | Required | Description |
|---|------|-----------|----------|-------------|
| 1 | config_complete | 13 fields | ✅ | All 13 required brand_config.yaml fields filled with non-placeholder values |
| 2 | config_valid | schema pass | ✅ | `brand_validate.py` returns 0 errors |
| 3 | archetype_real | 1/12 Jungian | ✅ | BRAND_ARCHETYPE is exactly one of: creator, hero, sage, explorer, rebel, magician, lover, caregiver, jester, ruler, innocent, everyman |
| 4 | voice_5d | 5 dims scored | ✅ | All 5 voice dimensions (formality, enthusiasm, humor, warmth, authority) have integer scores 1-5 |
| 5 | voice_consistent | within tolerance | ✅ | Voice scores across channel outputs stay within ±1 of brand_config base values |
| 6 | positioning_unique | UVP ≠ competitor | ✅ | UVP statement does not duplicate any competitor's positioning |
| 7 | naming_screened | domain + trademark | ❌ | Brand name checked for domain availability and trademark conflicts |
| 8 | brand_book_18 | 18/32 blocks | ✅ | Minimum 18 of 32 brand book blocks completed |
| 9 | brand_book_32 | 32/32 blocks | ❌ | All 32 brand book blocks completed (gold standard) |
| 10 | consistency_score | >= 0.85 | ✅ | `brand_audit.py` overall score passes threshold |
| 11 | uniqueness_score | >= 8.0 | ✅ | Brand uniqueness vs. competitors rated 8.0+ |
| 12 | propagation_test | nuclei resolve | ✅ | All target nuclei can resolve their BRAND_* variables via `brand_propagate.py` |
| 13 | visual_contrast | WCAG 4.5:1 | ✅ | Color contrast ratios meet WCAG AA standard |
| 14 | transformation_arc | From/To/Through | ✅ | BRAND_TRANSFORMATION follows "From X to Y through Z" pattern |

## Pass Criteria

- **Required gates**: 12 of 14 (gates 7 and 9 are optional)
- **Minimum score**: 8.0 to publish
- **Gold standard**: All 14 gates pass = 9.5+

## Gate Execution

```bash
# Run all brand checks
python _tools/brand_validate.py           # Gates 1-2
python _tools/brand_audit.py --verbose    # Gates 3-6, 10-11, 13-14
python _tools/brand_propagate.py --dry-run # Gate 12
```

## Revenue Checks (supplementary, from original N06)

| # | Gate | Threshold | Description |
|---|------|-----------|-------------|
| R1 | pricing_rationale | present | Every price has a WHY section, not just WHAT |
| R2 | tier_structure | 2-4 tiers | At least 2 pricing tiers defined |
| R3 | transformation_arc | present | Course/product has clear before → after arc |
| R4 | platform_specified | named | Deployment platform explicitly named (Hotmart, Stripe, etc.) |
| R5 | ltv_path | defined | Every offer has upsell/downsell path for LTV |
| R6 | compliance_br | checked | Brazilian market: BRL, PIX, parcelamento, CONAR compliance |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[spec_n06_part2]] | upstream | 0.37 |
| [[spec_n06_brand_verticalization]] | upstream | 0.36 |
| [[p03_sp_commercial_nucleus]] | upstream | 0.35 |
| [[p02_agent_brand_nucleus]] | upstream | 0.35 |
| [[p03_sp_brand_nucleus]] | upstream | 0.35 |
| [[p02_agent_commercial_nucleus]] | upstream | 0.34 |
| [[n06_schema_brand_book]] | upstream | 0.32 |
| [[p08_ac_brand_nucleus]] | downstream | 0.32 |
| [[p12_wf_commercial]] | downstream | 0.31 |
| [[p02_mm_commercial_nucleus]] | upstream | 0.30 |
