---
id: quality_gate_advanced_n01
kind: quality_gate
pillar: P11
nucleus: n01
title: "N01 Advanced Research Quality Gate v2"
version: 2.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.1
tags: [quality_gate, advanced_validation, n01, analytical_envy, multi_layer_gate]
tldr: "Advanced quality gate for N01 adding 3 new hard gates to the base quality_gate_intelligence: Analytical Envy check (comparison mandatory), Vocabulary compliance (no metaphors), and Confidence completeness (scores on all claims)."
density_score: 0.88
updated: "2026-04-17"
---

<!-- 8F: F1 constrain=P11/quality_gate F2 become=quality-gate-builder F3 inject=quality_gate_intelligence+bias_audit_n01+eval_framework_n01+scoring_rubric_research F4 reason=the base quality_gate covers sources and freshness; this v2 adds Analytical Envy-specific gates that are unique to N01's identity F5 call=cex_compile F6 produce=quality_gate_advanced_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P11_feedback/ -->

## Purpose

`quality_gate_intelligence.md` (v4.0) defines 5 hard gates (H01-H05) for basic research quality.
This v2 adds 3 additional gates specific to N01 Analytical Envy identity:
- H06: Comparison mandatory (Analytical Envy enforcement)
- H07: Vocabulary compliance (ubiquitous language enforcement)
- H08: Confidence completeness (epistemic integrity)

Run sequence: H01-H05 first (base gate), then H06-H08 (advanced gate).
ALL 8 gates must pass for research to be published.

## Extended Hard Gates

### H06: Comparison Mandatory (Analytical Envy)

| Check | Rule | Fail Condition |
|-------|------|----------------|
| Competitive context | at least 2 entities compared on >= 1 metric | single entity focus with no external reference |
| Quantified delta | at least 1 quantified comparison (%, $, count) | qualitative comparison only |
| Category baseline | market average or industry benchmark present | no reference point for comparison |

**Fail action**: return to F4 REASON with instruction "add competitive benchmark for every key finding"

### H07: Vocabulary Compliance

| Check | Rule | Fail Condition |
|-------|------|----------------|
| No metaphors in conclusions | scan conclusion for metaphor_dictionary.md terms | any metaphor used in place of industry term |
| Canonical kind names | if CEX kind referenced, use exact slug | "research card" instead of "knowledge_card" |
| Confidence notation | use 0.0-1.0 scale not "high/medium/low" | qualitative confidence without numeric |

**Fail action**: transmute offending terms, return updated text

### H08: Confidence Completeness

| Check | Rule | Fail Condition |
|-------|------|----------------|
| Claims covered | every "is", "has", "will", "shows" sentence has [confidence: X] | any claim without confidence score |
| Score range | all confidence scores between 0.0 and 1.0 | score outside range |
| Calibration | score >= 0.9 only when >= 3 primary sources agree | overconfident score (0.9+ with 1 source) |

**Fail action**: add confidence scores to all uncovered claims

## Gate Matrix (Full 8-Gate View)

| Gate | Source | Check | Auto-Fix? |
|------|--------|-------|-----------|
| H01 | base | >= 3 sources per major claim | no (requires research) |
| H02 | base | source URL + date required | yes (remove undated) |
| H03 | base | confidence score on key findings | yes (add placeholders) |
| H04 | base | no data > 90 days without warning | yes (add stale warning) |
| H05 | base | output follows assigned template | yes (reformat) |
| H06 | v2 | comparison present | no (requires analysis) |
| H07 | v2 | vocabulary compliance | yes (auto-transmute) |
| H08 | v2 | confidence completeness | yes (add 0.5 default) |

## Integration with 8F

```
F7 GOVERN:
  1. Run base quality_gate_intelligence.md (H01-H05)
  2. Run this gate (H06-H08)
  3. Run bias_audit_n01.md (B1-B5)
  4. Run llm_judge_n01.md (D1-D5 + hallucination)
  5. All pass -> F8
  6. Any fail -> classify, attempt auto-fix, retry F6 (max 2)
```

## Score Combination

```
base_hard_score = all(H01-H05)  # binary pass/fail
advanced_hard_score = all(H06-H08)  # binary pass/fail
quality_score = eval_framework_n01 score (continuous)

publish = base_hard_score AND advanced_hard_score AND quality_score >= 8.0
```
