---
id: bias_audit_n01
kind: bias_audit
8f: F7_govern
pillar: P07
nucleus: n01
title: "N01 Research Bias Audit"
version: 1.0.0
created: 2026-04-17
author: n01_intelligence
domain: research-intelligence
quality: 9.1
tags: [bias_audit, research_bias, analytical_envy, n01, selection_bias, confirmation_bias]
tldr: "Systematic bias detection for N01 research outputs: selection bias (source coverage), confirmation bias (conclusion direction), recency bias (temporal skew), and availability bias (easy-to-find favored). Runs as F7 GOVERN sub-check."
density_score: 0.91
updated: "2026-04-17"
related:
  - p06_schema_source_quality
  - bld_collaboration_bias_audit
  - bld_tools_bias_audit
  - kc_bias_audit
  - bld_architecture_bias_audit
  - p11_qg_intelligence
  - p01_kc_source_credibility_scoring_frameworks
  - p01_kc_intelligence_best_practices
  - bld_knowledge_card_bias_audit
  - p07_sr_intelligence_evaluation
---

<!-- 8F: F1 constrain=P11/bias_audit F2 become=bias-audit-builder F3 inject=quality_gate_intelligence+search_strategy_n01+eval_framework_n01+sch_validator_n01 F4 reason=Analytical Envy is worthless if N01 only finds evidence supporting what it already believes -- bias audit is intellectual integrity F5 call=cex_compile F6 produce=bias_audit_n01.md F7 govern=frontmatter+ascii+tables F8 collaborate=N01_intelligence/P11_feedback/ -->

## Purpose

The greatest threat to Analytical Envy is CONFIRMATION BIAS:
researching to confirm a hypothesis, not to discover truth.

This audit runs as a mandatory sub-step of F7 GOVERN on every research output.
It applies 5 bias lenses and flags research that fails to meet the comparative standard
that defines N01's Analytical Envy identity.

Analytical Envy = envy of those who know MORE, therefore: actively seek
contradictory evidence, alternative framings, and non-obvious conclusions.

## Bias Taxonomy (5 Types)

### B1: Selection Bias

| Check | Method | Fail Condition |
|-------|--------|----------------|
| Source diversity | count unique domains | < 3 distinct domains |
| Category diversity | check source types | all sources from single category (e.g., all press releases) |
| Geographic diversity | detect URL geography | 100% US sources when topic is global |
| Temporal diversity | date range of sources | all sources within 7 days of each other |
| Perspective diversity | detect org type | all sources are vendors (no independent analysis) |

**Score**: 0-10. Fail = < 6. Hard fail = < 4.

### B2: Confirmation Bias

| Check | Method | Fail Condition |
|-------|--------|----------------|
| Conclusion direction | sentiment analysis on conclusion section | > 80% positive or > 80% negative |
| Contradictory evidence | count evidence AGAINST hypothesis | 0 counterarguments = fail |
| Hypothesis stated upfront | detect if conclusion matches hypothesis | > 90% match = potential confirmation |
| Source selection direction | ratio of pro/con sources | > 4:1 in either direction |

**Score**: 0-10. Fail = < 5.

### B3: Recency Bias

| Check | Method | Fail Condition |
|-------|--------|----------------|
| Date distribution | histogram of source dates | > 60% from past 30 days for 2+ year trends |
| Trend context | check if historical baseline exists | no year-over-year comparison on trend claims |
| "New = better" assumption | detect "latest" "new" "just released" density | > 5 instances without validation |

**Score**: 0-10. Fail = < 6.

### B4: Availability Bias

| Check | Method | Fail Condition |
|-------|--------|----------------|
| Search depth | count layers used | only L1 sources used |
| Non-indexed sources | check for primary docs (PDFs, filings) | 0 primary sources |
| Hard-to-find data ratio | estimate search effort per source | > 80% from first-page results |
| Paywalled sources | count flagged paywall skips | > 3 paywalled skips = shallow research |

**Score**: 0-10. Fail = < 5.

### B5: Anchoring Bias

| Check | Method | Fail Condition |
|-------|--------|----------------|
| First-source influence | compare final conclusion to first source | > 85% alignment with first source |
| Reference price anchoring | detect "X compared to $Y" patterns | only one price anchor used |
| Benchmark anchoring | check if baseline comparison changes | single baseline for all comparisons |

**Score**: 0-10. Fail = < 6.

## Overall Bias Score

```
bias_score = weighted_mean([
  B1_selection * 0.30,
  B2_confirmation * 0.30,
  B3_recency * 0.20,
  B4_availability * 0.10,
  B5_anchoring * 0.10
])
```

| Score | Assessment | Action |
|-------|-----------|--------|
| >= 8.0 | Low bias | Accept |
| 6.0 - 7.9 | Moderate bias | Add disclaimer, flag specific bias |
| 4.0 - 5.9 | High bias | Return to researcher, add counter-evidence |
| < 4.0 | Severe bias | Reject, restart with explicit counter-hypothesis |

## Remediation Protocol

When bias detected:

| Bias Type | Remediation |
|-----------|------------|
| B1 selection | Add sources from underrepresented category |
| B2 confirmation | Write a "Steel Man" section with strongest counter-argument |
| B3 recency | Add historical baseline (1Y, 3Y, 5Y if relevant) |
| B4 availability | Run L2/L3 search layers, fetch primary documents |
| B5 anchoring | Add 2nd and 3rd comparison benchmarks |

## Integration with 8F

```
F7 GOVERN:
  [existing gates: H01-H05, D1-D5]
  + B1: selection_bias_score >= 6
  + B2: confirmation_bias_score >= 5
  + B3: recency_bias_score >= 6
  + ALL bias: overall_bias_score >= 7.0
```

## Comparison: Bias Audit Approaches

| Approach | Coverage | Automation | N01 Fit |
|----------|---------|------------|---------|
| None (naive research) | 0/5 bias types | N/A | fail -- no integrity |
| Manual peer review | 5/5 types | 0% | impractical at scale |
| This audit (automated) | 5/5 types | 80% | optimal |
| Academic peer review | 5/5 types + more | 0% | use as gold standard |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p06_schema_source_quality]] | upstream | 0.30 |
| [[bld_collaboration_bias_audit]] | downstream | 0.28 |
| [[bld_tools_bias_audit]] | upstream | 0.28 |
| [[kc_bias_audit]] | upstream | 0.28 |
| [[bld_architecture_bias_audit]] | downstream | 0.24 |
| [[p11_qg_intelligence]] | downstream | 0.22 |
| [[p01_kc_source_credibility_scoring_frameworks]] | upstream | 0.21 |
| [[p01_kc_intelligence_best_practices]] | upstream | 0.21 |
| [[bld_knowledge_card_bias_audit]] | upstream | 0.21 |
| [[p07_sr_intelligence_evaluation]] | related | 0.21 |
