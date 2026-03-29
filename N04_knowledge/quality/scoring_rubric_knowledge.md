---
id: p07_sr_knowledge_nucleus
kind: scoring_rubric
pillar: P07
title: "Rubric: Knowledge Nucleus"
version: "1.0.0"
created: "2023-10-15"
updated: "2023-10-15"
author: "scoring-rubric-builder"
framework: "Knowledge Nucleus"
target_kinds: [knowledge_artifact]
dimensions_count: 4
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "knowledge"
quality: null
tags: [scoring-rubric, knowledge-nucleus, evaluation]
tldr: "Scoring rubric for knowledge artifacts focusing on accuracy, clarity, depth, and relevance"
density_score: 0.85
calibration_set: [p07_gt_kn_example_1, p07_gt_kn_example_2]
inter_rater_agreement: 0.90
appeals_process: "Submit re-evaluation request to the review committee with detailed justification"
linked_artifacts:
  primary: "knowledge-artifact-evaluator"
  related: [p11_qg_kn_publish, p07_gt_kn_example]
---

## Framework Overview
The Knowledge Nucleus rubric evaluates the quality of knowledge-based artifacts with a focus on accuracy, clarity, depth, and relevance. It provides a structured framework to assess the quality and ensure consistency across evaluations.

## Dimensions
| Dimension | Weight | Scale | Criteria | Example (10) | Example (5) |
|-----------|--------|-------|----------|-------------|-------------|
| Accuracy | 30% | 0-10 | Verifiable facts and data with no errors | All facts verified, zero errors | Several minor inaccuracies |
| Clarity | 25% | 0-10 | Easily understandable with clear language | Exceptionally clear, no ambiguities | Some sentences unclear |
| Depth | 25% | 0-10 | Comprehensive coverage with insightful analysis | Thorough analysis, multiple perspectives | Basic coverage, limited analysis |
| Relevance | 20% | 0-10 | Pertinent to the current knowledge domain | Strongly aligned with current trends | Partially aligned, somewhat outdated |

## Thresholds
| Tier | Score | Action |
|------|-------|--------|
| GOLDEN | >= 9.5 | Promote as exemplary, used in training |
| PUBLISH | >= 8.0 | Approved for publishing |
| REVIEW | >= 7.0 | Revisions required for clarity and depth |
| REJECT | < 7.0 | Major revision or re-creation needed |

## Calibration
- **GOLDEN (9.8)**: Example with universally correct data, clear articulation, comprehensive analysis, and high relevance.
- **PUBLISH (8.4)**: Solid artifact with minor clarity issues, mostly current concepts, and backed by reliable data.
- **REVIEW (7.3)**: Needs improvement in depth and clarity; some facts require verification.
- **REJECT (6.5)**: Inadequate coverage with several errors in data and lack of relevance.

## Automation
| Dimension | Status | Tool |
|-----------|--------|------|
| Accuracy | semi-automated | fact_check_tool.py |
| Clarity | manual | Human review for language |
| Depth | semi-automated | depth_analyzer_tool.py |
| Relevance | manual | Subject matter expert assessment |

## References
- AAC&U VALUE Rubrics: https://www.aacu.org/value-rubrics
- validate_kn_tool.py v1.0 (Knowledge Nucleus implementation reference)