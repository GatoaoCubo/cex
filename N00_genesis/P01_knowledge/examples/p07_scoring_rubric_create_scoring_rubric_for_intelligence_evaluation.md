---
id: p07_sr_intelligence_evaluation
kind: scoring_rubric
8f: F7_govern
pillar: P07
title: "Rubric: Intelligence Evaluation"
version: "1.0.0"
created: "2026-04-02"
updated: "2026-04-02"
author: "scoring-rubric-builder"
framework: "5D-Intel"
target_kinds: [research_pipeline, knowledge_card, agent_card, context_doc]
dimensions_count: 5
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "intelligence"
quality: 9.1
tags: [scoring-rubric, intelligence, research, evaluation, 5d, n01]
tldr: "5D rubric for intelligence artifacts: methodology 25%, evidence 25%, analysis 20%, clarity 15%, actionability 15%"
density_score: 0.91
calibration_set: [p07_gt_intel_competitor_analysis, p07_gt_intel_market_brief]
inter_rater_agreement: 0.83
appeals_process: "Submit to N01 chief with counter-evidence; re-score within 48h"
linked_artifacts:
  primary: "p11_qg_intelligence_artifacts"
  related: [p07_gt_intel_competitor_analysis, p01_kc_intelligence_best_practices]
related:
  - p07_sr_intel_research
  - bld_examples_scoring_rubric
  - p07_sr_knowledge_eval
  - p11_qg_intelligence_artifact
  - n01_qg_intelligence
  - p07_sr_creation_evaluation
  - n01_rs_intelligence_sources
  - p07_rubric_intelligence
  - p03_ins_scoring_rubric_builder
  - p01_kc_artifact_quality_evaluation_methods
---
## Framework Overview

Evaluates intelligence artifacts (research pipelines, briefs, analyses, knowledge cards) produced by N01 Intelligence Nucleus. Five orthogonal dimensions capture research rigor, evidence integrity, analytical depth, presentational clarity, and decision-enabling actionability. Designed to complement `p11_qg_intelligence_artifacts` (HARD pass/fail gates) with nuanced SOFT scoring. Primary consumers: N07 orchestrator reviewing N01 outputs, peer reviewers, and automated quality pipelines.

## Dimensions

| Dimension | Weight | Scale | Criteria | Example (10) | Example (5) |
|-----------|--------|-------|----------|-------------|-------------|
| Methodological Rigor | 25% | 0-10 | Research design validity, source triangulation, reproducible steps | Explicit method section, 3+ triangulated source types, step-by-step reproducibility | Single method, implicit steps, partial triangulation |
| Evidence Quality | 25% | 0-10 | Source credibility (tier-1 primary > secondary > tertiary), recency within 24 months, citation completeness | 8+ tier-1 sources, all cited with dates, zero unverifiable claims | 3–5 mixed-tier sources, some uncited, 1–2 stale claims |
| Analytical Depth | 20% | 0-10 | Inference chain explicitness, competing hypotheses addressed, logical gap count | Full reasoning chain, 2+ alternatives considered, zero unexplained leaps | Conclusions stated without chain, 1 alternative noted, 1–2 gaps |
| Clarity & Structure | 15% | 0-10 | Section hierarchy, executive summary present, density >= 0.80, no jargon without definition | All required sections, TL;DR ≤ 160ch, density 0.88+, all terms defined | Most sections present, density 0.72, 2–3 undefined terms |
| Strategic Actionability | 15% | 0-10 | Recommendations tied to evidence, quantified impact estimates, decision owner named | 3+ specific recommendations, each with evidence link + owner + metric | 1–2 generic recommendations, no owners, no metrics |

## Thresholds

| Tier | Score Range | Action |
|------|-------------|--------|
| GOLDEN | >= 9.5 | Promote to calibration set; use as reference for future scoring |
| PUBLISH | 8.0–9.4 | Merge to intelligence pool; signal N07 complete |
| REVIEW | 7.0–7.9 | Return to N01 with per-dimension feedback; 1 revision cycle |
| REJECT | < 7.0 | Discard; re-research from scratch with new sources |

## Calibration

- **GOLDEN (9.7)**: `p07_gt_intel_competitor_analysis` — explicit mixed-methods section, 12 tier-1 sources, full reasoning chain with 3 alternatives, density 0.91, 4 recommendations each with owner + KPI
- **PUBLISH (8.4)**: Market brief with 7 sources, 2 triangulated methods, clear structure, density 0.83, 2 recommendations with metrics but no named owners
- **REVIEW (7.3)**: Trend report with 5 sources, single method, conclusions stated without chain, density 0.76, 1 generic recommendation
- **REJECT (5.1)**: Analysis with 2 secondary sources, no methodology, unsupported claims, density 0.51, no recommendations

## Automation

| Dimension | Status | Tool |
|-----------|--------|------|
| Methodological Rigor | semi-automated | cex_doctor.py (section presence) + manual method review |
| Evidence Quality | semi-automated | cex_hooks.py (citation count, date grep) + manual tier rating |
| Analytical Depth | manual | Human reviewer checks inference chain |
| Clarity & Structure | automated | cex_score.py (density ratio, section count, tldr length) |
| Strategic Actionability | semi-automated | Grep for recommendation patterns + manual quality check |

## References

- AAC&U VALUE Rubrics — Inquiry & Analysis: https://www.aacu.org/initiatives/value-initiative
- LLM-as-Judge evaluation framework (Zheng et al., 2023): MT-Bench multi-turn evaluation
- cex_score.py v2.1 — density and section validation reference implementation

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p07_sr_intel_research]] | sibling | 0.38 |
| [[bld_examples_scoring_rubric]] | related | 0.36 |
| [[p07_sr_knowledge_eval]] | sibling | 0.33 |
| [[p11_qg_intelligence_artifact]] | downstream | 0.30 |
| [[n01_qg_intelligence]] | downstream | 0.27 |
| [[p07_sr_creation_evaluation]] | sibling | 0.27 |
| [[n01_rs_intelligence_sources]] | upstream | 0.23 |
| [[p07_rubric_intelligence]] | sibling | 0.23 |
| [[p03_ins_scoring_rubric_builder]] | upstream | 0.23 |
| [[p01_kc_artifact_quality_evaluation_methods]] | upstream | 0.22 |
