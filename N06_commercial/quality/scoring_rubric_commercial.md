---

```yaml
id: p07_sr_commercial_evaluation
kind: scoring_rubric
pillar: P07
title: "Rubric: Commercial Evaluation"
version: "1.0.0"
created: "2023-10-18"
updated: "2023-10-18"
author: "scoring-rubric-builder"
framework: "Commercial Evaluation"
target_kinds: ["commercial_nucleus"]
dimensions_count: 5
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "commercial"
quality: null
tags: [scoring-rubric, commercial, evaluation]
tldr: "Multi-dimensional rubric for evaluating commercial artifacts: functionality, user experience, market viability, integration potential, innovation."
density_score: 0.90
calibration_set: [p07_gt_commercial_example_1, p07_gt_commercial_example_2]
inter_rater_agreement: 0.85
appeals_process: "Submit to p01-chief with detailed rationale for re-evaluation"
linked_artifacts:
  primary: "quality-gate-builder"
  related: [p11_qg_commercial_publish]
---
## Framework Overview
This rubric evaluates commercial artifacts using a comprehensive multi-dimensional framework designed to assess core quality criteria: functionality, user experience, market viability, integration potential, and innovation. The aim is to provide a balanced evaluation to aid in the decision-making process concerning commercial product viability and competitive readiness.
## Dimensions
| Dimension         | Weight | Scale | Criteria                                                                                                                                 | Example (10)                                                     | Example (5)                                          |
|-------------------|--------|-------|-----------------------------------------------------------------------------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------|
| Functionality     | 30%    | 0-10  | Meets all technical requirements with no defects. Functionality aligns completely with specification and user expectations.             | All features work seamlessly without any glitches or errors.    | Basic functions work, but several key features fail. |
| User Experience   | 20%    | 0-10  | Intuitive design that enhances user satisfaction and efficiency. Consistently positive user feedback.                                    | UI is smooth, intuitive, with high user satisfaction rates.     | Usable but clunky, user feedback is mixed.           |
| Market Viability  | 20%    | 0-10  | Strong competitive advantage and potential for high market adoption. Financial projections support profitability within 1 year.        | Product occupies 20% market share in less than a year.          | Moderate potential, market presence unclear.         |
| Integration       | 15%    | 0-10  | Seamlessly integrates with existing systems with minimal configuration required. API support is robust and well-documented.              | Immediate integration with key systems, includes full API docs. | Initial integration needs significant custom coding. |
| Innovation        | 15%    | 0-10  | Novel approach or features that differentiate it from competitors. Gains industry recognition or awards for innovation.                 | First-of-its-kind feature, recognized by industry experts.      | Some new ideas, but mostly incremental improvements. |
## Thresholds
| Tier   | Score | Action                                   |
|--------|-------|------------------------------------------|
| GOLDEN | >= 9.5 | Promote to calibration set, mark as reference |
| PUBLISH| >= 8.0 | Merge into commercial pool for release   |
| REVIEW | >= 7.0 | Return with specific feedback for improvement |
| REJECT | < 7.0  | Redo from the ground up with new research |
## Calibration
- GOLDEN (9.7): Example 1 that meets all criteria with robust integration, market impact, and receives excellent user feedback.
- PUBLISH (8.4): Solid artifact with minor improvement areas, demonstrates strong potential and functionality.
- REVIEW (7.3): Needs refinements in user experience and innovation, basic functionalities present.
- REJECT (5.3): Basic functions underdeveloped, lacks market appeal, substantial work needed.
## Automation
| Dimension       | Status       | Tool                      |
|-----------------|--------------|---------------------------|
| Functionality   | semi-automated| validate_functionality.py |
| User Experience | manual       | Usability testing tools    |
| Market Viability| manual       | Market analysis tools     |
| Integration     | automated    | integration_checker.py    |
| Innovation      | manual       | Expert review panel       |
## References
- Commercial Viability Analysis by TechTrend
- User Experience Measurement Standards by UXPA
```