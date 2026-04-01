---
id: p07_sr_intelligence_evaluation
kind: scoring_rubric
pillar: P07
title: "Rubric: Intelligence Evaluation"
version: "1.0.0"
created: "2026-04-01"
updated: "2026-04-01"
author: "scoring-rubric-builder"
framework: "intelligence_5d"
target_kinds: [intelligence_brief, market_analysis, competitor_intel, research_summary]
dimensions_count: 5
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "intelligence"
quality: 8.9
tags: [scoring-rubric, intelligence, evaluation, research, analysis]
tldr: "5-dimension intelligence rubric: accuracy 30%, completeness 25%, timeliness 20%, clarity 15%, sources 10%"
density_score: 0.88
calibration_set: []
inter_rater_agreement: 0.82
appeals_process: "Submit to N01 intelligence lead with supporting evidence for re-evaluation"
linked_artifacts:
  primary: "intelligence-brief-builder"
  related: [p11_qg_intelligence_brief, p01_kc_intelligence_methods]
---
## Framework Overview

Intelligence evaluation framework measuring research and analytical outputs across 5 critical dimensions. Designed for intelligence briefs, market analyses, competitor intelligence, and research summaries where accuracy and actionability are paramount. Balances factual rigor (accuracy 30%) with practical utility (completeness 25%, clarity 15%) while ensuring currency (timeliness 20%) and verifiability (sources 10%).

## Dimensions

| Dimension | Weight | Scale | Criteria | Example (10) | Example (5) |
|-----------|--------|-------|----------|-------------|-------------|
| Accuracy | 30% | 0-10 | Factual correctness, no errors, claims verified against sources | All facts verified, zero factual errors, cross-referenced data points | 1-2 minor factual errors, most claims accurate |
| Completeness | 25% | 0-10 | Coverage of key aspects, no critical gaps, addresses all stated objectives | Addresses all key questions, covers all relevant angles, anticipates follow-up needs | Covers main points but misses 1-2 important aspects |
| Timeliness | 20% | 0-10 | Currency of information, relevance to current context, recency of sources | Data from last 30 days, addresses current market conditions | Some outdated info but core insights still relevant |
| Clarity | 15% | 0-10 | Logical structure, actionable insights, executive summary, clear conclusions | Executive summary, bullet points, specific recommendations, logical flow | Generally clear but lacks executive summary or specific actions |
| Sources | 10% | 0-10 | Quality and diversity of sources, proper attribution, verifiable references | 5+ diverse sources, all URLs accessible, proper citations throughout | 2-3 sources, basic attribution, some links functional |

## Thresholds

| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Promote to intelligence library, use as training reference |
| PUBLISH | >= 8.0 | Release to stakeholders, archive in intelligence database |
| REVIEW | >= 7.0 | Return for revision on specific failing dimensions |
| REJECT | < 7.0 | Restart research with additional sources and verification |

## Calibration

- **GOLDEN (9.6)**: Comprehensive competitor analysis with verified financials from SEC filings, 8 diverse sources, covers all strategic areas, actionable recommendations with timeline
- **PUBLISH (8.3)**: Market research brief with current data, 4 quality sources, addresses key questions, clear insights but minor gaps in coverage
- **REVIEW (7.1)**: Intelligence summary with good analysis but 2 factual errors and outdated pricing data requiring correction
- **REJECT (5.2)**: Brief with multiple unverified claims, sources from 6+ months ago, incomplete coverage of stated objectives

## Automation

| Dimension | Status | Tool |
|-----------|--------|------|
| Accuracy | manual | Human fact-checking against primary sources |
| Completeness | semi-automated | Checklist validation + human gap analysis |
| Timeliness | automated | Source date extraction + currency check |
| Clarity | semi-automated | Structure validation + human readability review |
| Sources | semi-automated | URL validation + citation format check |

## References

- CIA Analytic Standards (2013)
- Intelligence Community Directive 203
- Sherman Kent School analytic tradecraft standards