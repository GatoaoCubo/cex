---
id: p07_rt_8f_govern
kind: reasoning_trace
pillar: P07
title: "Reasoning Trace -- F7 GOVERN Live Example"
version: 1.0.0
created: 2026-04-17
author: n03_engineering
domain: pipeline-reasoning
quality: 8.8
tags: [reasoning_trace, F7, GOVERN, quality-gate, scoring, 8F, example, coc]
tldr: "Live F7 GOVERN trace for a landing_page artifact scoring 8.4. Shows 7-gate evaluation, 12LP checklist, retry loop, and the specific fixes that raised the score to 9.1. Teaches both failure and recovery."
density_score: 0.91
related:
  - p01_kc_iterative_refinement_skill
  - p03_sp_verification_agent
  - bld_examples_invariant
  - p07_gt_stripe_pipeline
  - bld_examples_axiom
  - n01_hybrid_review_wave1
  - p01_kc_refinement
  - bld_examples_cli_tool
  - bld_examples_golden_test
  - bld_examples_validator
---

# Reasoning Trace: F7 GOVERN

**Input artifact:** `landing_page_saas_product.md` (draft from F6)
**Nucleus:** N03 (Engineering)
**Initial score:** 8.4 → **Final score:** 9.1 (after 1 retry)

---

## F-Annotation: F7 GOVERN

F7 is the quality gate. It applies H01-H07 hard gates, the 12-point checklist (12LP), and the 5-dimension scoring (D1-D5). If score < 8.0, F6 retries (max 2). F7 never produces artifacts — it only scores and gates them.

Without F7, quality is unverified. Every artifact reaching F8 must have passed F7.

---

## Pass 1: Hard Gates (H01-H07)

| Gate | Rule | Result | Evidence |
|------|------|--------|---------|
| H01 | Frontmatter complete (13 required fields) | PASS | All fields present |
| H02 | kind `landing_page` exists in kinds_meta.json, pillar=P05 | PASS | Verified via kinds_meta.json |
| H03 | id `p05_lp_saas_product` globally unique | PASS | cex_doctor.py --ids: 0 conflicts |
| H04 | `quality: null` exactly | PASS | grep "quality: null" = 1 match |
| H05 | density_score >= 0.85 | FAIL | density_score: 0.78 (below threshold) |
| H06 | No filler prose | FAIL | Found: "This landing page is designed to..." (line 24) |
| H07 | >= 1 cross-reference to N03 artifact | FAIL | No cross-references found |

**Gate result: 4/7 passed. FAIL — trigger retry.**

---

## Pass 1: 12LP Checklist

| # | Point | Status | Notes |
|---|-------|--------|-------|
| 1 | Schema compliance | PASS | All required fields present |
| 2 | Kind-pillar match | PASS | landing_page -> P05 verified |
| 3 | Unique identifier | PASS | id is slug-derived and unique |
| 4 | Quality null | PASS | INV-03 holds |
| 5 | Density >= 0.85 | FAIL | 0.78; needs table conversion |
| 6 | No invented kinds | PASS | Only landing_page used |
| 7 | ASCII-only code | PASS | No embedded code |
| 8 | Cross-reference present | FAIL | 0 references |
| 9 | tldr <= 160 chars | PASS | 147 chars |
| 10 | Anti-filler check | FAIL | 2 filler sentences found |
| 11 | CoC naming convention | PASS | landing_page_{domain}.md |
| 12 | Version >= 1.0.0 | PASS | 1.0.0 |

**12LP result: 9/12 passed.**

---

## Pass 1: 5D Scoring

| Dimension | Weight | Score | Calculation |
|-----------|--------|-------|-------------|
| D1 Structural | 30% | 7.8 | H05 fail (-0.8) + H06 fail (-0.6) |
| D2 Semantic | 20% | 8.5 | landing_page concepts well-covered |
| D3 Completeness | 20% | 9.0 | All required sections present |
| D4 Invariant | 15% | 9.0 | All N03 invariants hold |
| D5 Coverage | 15% | 8.8 | Sections cover key use cases |

**Composite score: (7.8×0.30) + (8.5×0.20) + (9.0×0.20) + (9.0×0.15) + (8.8×0.15) = 8.4**

---

## Diagnosis: What to Fix

F7 generates a repair plan for F6 retry:

| Issue | Location | Fix |
|-------|----------|-----|
| Low density (0.78) | Sections: Features, Pricing | Replace prose paragraphs with feature comparison tables |
| Filler prose | Line 24, line 67 | Delete: "This landing page is designed to..." Replace with direct statement |
| Missing cross-references | Footer | Add: "See: `N03_engineering/P11_feedback/quality_gate_n03.md` for validation criteria" |

**Estimated score after fixes: 9.1** (density will reach ~0.87, filler removed, ref added)

---

## Pass 2 (Retry 1): After F6 Applied Fixes

### Changes Applied

1. **Density fix:** Features section converted from 4 prose paragraphs to comparison table (24 rows, 3 columns)
2. **Filler removal:** Deleted 2 sentences; replaced with table header row
3. **Cross-reference:** Added `## References` section with 3 N03 artifact paths

### Re-evaluation

| Gate | Result | Change |
|------|--------|--------|
| H05 density | PASS | 0.87 (was 0.78) |
| H06 filler | PASS | 0 filler sentences (was 2) |
| H07 cross-ref | PASS | 3 references added |

**Gates: 7/7 passed**
**12LP: 12/12 passed**

### Re-scoring

| Dimension | Score | Change |
|-----------|-------|--------|
| D1 Structural | 9.2 | +1.4 (both fails cleared) |
| D2 Semantic | 8.8 | +0.3 (table reveals more terms) |
| D3 Completeness | 9.0 | unchanged |
| D4 Invariant | 9.0 | unchanged |
| D5 Coverage | 9.1 | +0.3 (table rows = coverage items) |

**Composite score: 9.1. PASS → proceed to F8.**

---

## Key Insights (What F7 Teaches)

| Principle | Demonstrated here |
|-----------|-------------------|
| **Hard gates are binary** | H05 is PASS or FAIL; no "partial credit" |
| **Density fixes drive most score jumps** | Prose→table conversion: +1.4 in D1 |
| **Filler is quantifiable** | Grep for patterns; zero tolerance |
| **Retry is bounded** | Max 2 retries; third failure = reject + rebuild from F4 |
| **Diagnosis drives repair** | F7 names exact lines; F6 applies exact fixes |
| **Score predicts gates** | 8.4 with 3 gate failures → 9.1 with 0 gate failures |

---

## Retry Budget

| Retry | Score | Gates | Action |
|-------|-------|-------|--------|
| 0 (initial) | 8.4 | 4/7 | Trigger retry 1 |
| 1 | 9.1 | 7/7 | PASS → F8 |
| (would be 2) | < 8.0 | fails | Reject → rebuild from F4 |

---

## Cross-References

- `N03_engineering/P08_architecture/pattern_8f_full_trace.md` — F7 field format in full trace
- `N03_engineering/P11_feedback/quality_gate_n03.md` — H01-H07 gate definitions
- `N03_engineering/P07_evals/scoring_rubric_n03.md` — 5D dimension weights
- `N03_engineering/P07_evals/reasoning_trace_8f_constrain.md` — F1 trace complement

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_iterative_refinement_skill]] | upstream | 0.38 |
| [[p03_sp_verification_agent]] | upstream | 0.37 |
| [[bld_examples_invariant]] | downstream | 0.34 |
| [[p07_gt_stripe_pipeline]] | related | 0.34 |
| [[bld_examples_axiom]] | related | 0.33 |
| [[n01_hybrid_review_wave1]] | upstream | 0.31 |
| [[p01_kc_refinement]] | upstream | 0.31 |
| [[bld_examples_cli_tool]] | related | 0.31 |
| [[bld_examples_golden_test]] | related | 0.29 |
| [[bld_examples_validator]] | related | 0.29 |
