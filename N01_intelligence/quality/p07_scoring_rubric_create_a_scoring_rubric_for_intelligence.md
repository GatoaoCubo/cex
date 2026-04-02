---
id: p07_sr_intel_research
kind: scoring_rubric
pillar: P07
title: "Rubric: Intelligence Research Output Evaluation"
version: "1.0.0"
created: "2024-12-28"
updated: "2024-12-28"
author: "scoring-rubric-builder"
framework: "intel_research"
target_kinds: [research_paper, intelligence_report, analysis_brief]
dimensions_count: 5
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "research"
quality: 9.1
tags: [scoring-rubric, intelligence, research, analysis]
tldr: "5D evaluation for intel research: methodology 25%, evidence 25%, analysis 20%, clarity 15%, novelty 15%"
density_score: 0.88
calibration_set: []
inter_rater_agreement: 0.85
appeals_process: "Submit to research lead with detailed rationale and supporting evidence"
linked_artifacts:
  primary: "intelligence-research-builder"
  related: []
---

## Framework Overview

Evaluates intelligence research outputs across 5 critical dimensions that determine research quality and operational impact. Designed for papers, reports, and briefs produced in competitive intelligence, market analysis, and strategic research contexts within N01 intelligence domain.

## Dimensions

| Dimension | Weight | Scale | Criteria | Example (10) | Example (5) |
|-----------|--------|-------|----------|-------------|-------------|
| Methodological Rigor | 25% | 0-10 | Research design, data collection validity, analytical approach soundness | Mixed methods, triangulated sources, explicit methodology section, reproducible steps | Single method, basic approach documented, some methodology gaps |
| Evidence Quality | 25% | 0-10 | Source credibility, data recency, verification level, citation completeness | Primary sources, <6 months old, cross-verified, complete citations | Mix of primary/secondary, some recent data, basic verification |
| Analytical Depth | 20% | 0-10 | Insight generation beyond surface facts, pattern recognition, implication analysis | Novel patterns identified, deep causation analysis, strategic implications | Some analysis present, basic patterns, limited implications |
| Clarity & Communication | 15% | 0-10 | Structure, readability, executive summary quality, visual aids effectiveness | Clear structure, excellent exec summary, effective visuals, stakeholder-ready | Adequate structure, basic summary, some unclear sections |
| Novelty & Contribution | 15% | 0-10 | Original insights, gap-filling, advancement beyond existing knowledge | Significant new insights, fills knowledge gaps, advances field understanding | Some new information, minor insights, incremental contribution |

## Thresholds

| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Promote to reference library, distribute to senior leadership |
| PUBLISH | >= 8.0 | Distribute to stakeholders, include in intelligence briefings |
| REVIEW | >= 7.0 | Return with specific feedback for revision before distribution |
| REJECT | < 7.0 | Major rework required, reassign to experienced researcher |

## Calibration

- GOLDEN (9.7): Comprehensive competitor analysis with proprietary data, novel strategic insights, executive-ready presentation
- PUBLISH (8.2): Solid market research with multiple verified sources, clear implications, professional formatting
- REVIEW (7.3): Basic analysis with some gaps in methodology, adequate sources, needs clarity improvements
- REJECT (5.8): Insufficient evidence base, unclear methodology, limited analytical value

## Automation

| Dimension | Status | Tool |
|-----------|--------|------|
| Methodological Rigor | manual | Expert reviewer assessment |
| Evidence Quality | semi-automated | Citation checker + manual source verification |
| Analytical Depth | manual | Subject matter expert evaluation |
| Clarity & Communication | semi-automated | Readability tools + manual structure review |
| Novelty & Contribution | manual | Expert assessment against existing knowledge base |

## References

- Intelligence Community Research Standards (2024)
- Academic Research Quality Assessment Framework
- Strategic Intelligence Analysis Best Practices Guide