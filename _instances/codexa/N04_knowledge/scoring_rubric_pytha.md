---
id: p07_sr_pytha_knowledge_nucleus
kind: scoring_rubric
pillar: P07
title: "Rubric: Pytha Knowledge Nucleus"
version: "1.0.0"
created: "2023-10-01"
updated: "2023-10-01"
author: "evaluation_framework_designer"
framework: "Pytha Knowledge Nucleus"
target_kinds: ["knowledge_card"]
dimensions_count: 4
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "knowledge_evaluation"
quality: null
tags: [scoring-rubric, pytha, knowledge]
tldr: "4D rubric for evaluating knowledge_cards: mastery 30%, application 30%, originality 20%, accuracy 20%"
density_score: 0.85
calibration_set: [p07_gt_kn_exemplary, p07_gt_kn_boundary]
inter_rater_agreement: 0.88
appeals_process: "Submit appeal to P07 chief with documented rationale"
linked_artifacts:
  primary: "quality-gate-builder"
  related: [p11_qg_kn_publish, p07_gt_kn_exemplary]
---

## Framework Overview

This rubric evaluates knowledge_cards within the Pytha Knowledge Nucleus for their educational impact, correctness, and innovative contributions. It ensures that all submissions meet a consistent, high-quality standard appropriate for publication.

## Dimensions

| Dimension          | Weight | Scale | Criteria                                                                                       | Example (10)                                                   | Example (5)                             |
|--------------------|--------|-------|-----------------------------------------------------------------------------------------------|----------------------------------------------------------------|-----------------------------------------|
| Content Mastery    | 30%    | 0-10  | Demonstrates in-depth understanding of subject; clear, comprehensive explanations available    | Detailed, well-articulated insights; no gaps                  | Basic understanding with clarity issues |
| Application Impact | 30%    | 0-10  | Practical application potential; useful in real-world scenarios                                | Contains actionable steps that result in measurable impact    | Vague suggestions without clear outcomes |
| Innovation         | 20%    | 0-10  | Introduces novel ideas or approaches within the topic                                          | Original insights that improve upon existing solutions         | Few creative elements, mainly standard  |
| Technical Accuracy | 20%    | 0-10  | Correct factual content with adherence to academic and domain standards                        | All claims supported by sources, with zero technical errors   | Contains minor errors or outdated info  |

## Thresholds

| Tier     | Score  | Action                                      |
|----------|--------|---------------------------------------------|
| GOLDEN   | >= 9.5 | Promote and use as a golden calibration example |
| PUBLISH  | >= 8.0 | Publish to the knowledge pool               |
| REVIEW   | >= 7.0 | Return with feedback for improvement         |
| REJECT   | < 7.0  | Return for complete rework                   |

## Calibration

- **GOLDEN (9.8)**: Exemplary knowledge_card with depth and accuracy, actionable applications, innovative insights.
- **PUBLISH (8.5)**: Valid knowledge_card that meets all criteria with minor room for improvement.
- **REVIEW (7.5)**: Needs further refining, especially in creativity or depth. Technical claims tentative.
- **REJECT (6.0)**: Significant deficiencies in several dimensions, requires comprehensive revisions.

## Automation

| Dimension          | Status           | Tool                                |
|--------------------|------------------|-------------------------------------|
| Content Mastery    | semi-automated   | `validate_kn.py` for text analysis  |
| Application Impact | manual           | Human review for real-world examples|
| Innovation         | manual           | Human evaluation of creativity      |
| Technical Accuracy | automated        | `check_accuracy.py` for claims validation |

## References
- AAC&U VALUE Rubrics
- validate_kn.py v1.0 (Pytha Knowledge Tool Reference)