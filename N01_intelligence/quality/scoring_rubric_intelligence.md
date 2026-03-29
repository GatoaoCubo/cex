---
id: p07_sr_research_nucleus
kind: scoring_rubric
pillar: P07
title: "Rubric: Research Nucleus Evaluation"
version: "1.0.0"
created: "2023-10-12"
updated: "2023-10-12"
author: "Evaluation Framework Designer"
framework: "Research Nucleus Evaluation"
target_kinds: [research_artifact]
dimensions_count: 4
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "academic"
quality: null
tags: [scoring-rubric, research-nucleus, academic-evaluation]
tldr: "4-dimension rubric for evaluating research artifacts: originality 30%, methodology 30%, impact 20%, ethics 20%"
density_score: 0.85
calibration_set: [golden_test_1, golden_test_2]
inter_rater_agreement: 0.88
appeals_process: "Submit appeal to evaluation board with detailed rationale"
linked_artifacts:
  primary: "research_quality_assessment"
  related: [quality_gate_research, golden_test_1]
---

## Purpose
This scoring rubric is designed to evaluate research artifacts within the context of a Research Nucleus. It provides a comprehensive assessment across multiple dimensions ensuring that the artifact contributes significantly to the field of academic inquiry.

## Dimensions
| Dimension           | Weight | Scale | Criteria                                                                                                                                   | Example (10)                                | Example (5)                                  |
|---------------------|--------|-------|-------------------------------------------------------------------------------------------------------------------------------------------|---------------------------------------------|----------------------------------------------|
| Originality         | 30%    | 0-10  | The degree of novelty and uniqueness presented in the research.                                                                           | Groundbreaking methodology or findings      | Common approach with minor novel elements   |
| Methodological Rigor| 30%    | 0-10  | The robustness and appropriateness of the research methodology.                                                                            | Meticulous approach, well-supported by data | Basic methodology with some gaps            |
| Impact and Relevance| 20%    | 0-10  | The significance of the research contribution to the field.                                                                               | High impact study cited by peers            | Limited relevance, limited citations         |
| Ethical Standards   | 20%    | 0-10  | The adherence to ethical guidelines during research.                                                                                      | Exceeds ethical norms                       | Meets basic ethical standards               |

## Tier Thresholds
| Tier    | Score | Action                                        |
|---------|-------|-----------------------------------------------|
| GOLDEN  | >= 9.5| Promote as exemplary study, use for reference |
| PUBLISH | >= 8.0| Accept for publication                        |
| REVIEW  | >= 7.0| Return with feedback for improvement          |
| REJECT  | < 7.0 | Reject and suggest resubmission               | 

## Calibration
- **GOLDEN (9.6):** High originality, methodologically rigorous, significantly impactful, and exemplary ethical standards.
- **PUBLISH (8.4):** New perspectives with sound methodology, useful to field scholars, ethically compliant.
- **REVIEW (7.2):** Acceptable standard, but lacking in some areas such as rigorous method or minor ethical concerns.
- **REJECT (5.8):** Insufficient in originality, methodology, impact, or ethical practice.

## Automation
| Dimension           | Status        | Tool                        |
|---------------------|---------------|-----------------------------|
| Originality         | semi-automated| originality_checker_tool    |
| Methodological Rigor| manual        |                             |
| Impact and Relevance| semi-automated| citation_tracker            |
| Ethical Standards   | manual        |                             |

## References
- AAC&U VALUE Rubrics: https://www.aacu.org/initiatives/value-initiative
- Example Research Evaluation Tools: https://researchevaluationtools.com