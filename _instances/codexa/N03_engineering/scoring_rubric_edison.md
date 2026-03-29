---
id: p07_sr_edison_engineering_nucleus
kind: scoring_rubric
pillar: P07
title: "Edison Engineering Nucleus Scoring Rubric"
version: "1.0.0"
created: "2023-10-18"
updated: "2023-10-18"
author: "[Your Name/Team Name]"
framework: "edison_engineering"
target_kinds: [engineering_project]
dimensions_count: 4
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "engineering"
quality: null
tags: [scoring-rubric, edison_engineering, evaluation]
tldr: "Evaluates engineering projects across innovation, impact, technical rigor, and feasibility."
density_score: 0.85
calibration_set: [p07_gt_edison_proj_master, p07_gt_edison_proj_published]
inter_rater_agreement: 0.86
appeals_process: "Submit to engineering_team_lead with documented feedback for reconsideration."
linked_artifacts:
  primary: "engineering_project_schema"
  related: [p11_qg_eng_publish, p07_gt_edison_proj_published]
---

## Framework Overview
This rubric evaluates engineering projects within the Edison Engineering Nucleus, focusing on innovation, technical rigor, feasibility, and impact. It aims to ensure high-quality engineering output that aligns with organizational goals.

## Dimensions
| Dimension       | Weight | Scale | Criteria                                                                                     | Example (10)                                     | Example (5)                                   |
|-----------------|--------|-------|---------------------------------------------------------------------------------------------|--------------------------------------------------|-----------------------------------------------|
| Innovation      | 30%    | 0-10  | Level of originality and advancement, supported by novel ideas and processes.              | Introduces breakthrough concepts with applications| Common solutions, no novel approaches        |
| Impact          | 30%    | 0-10  | Potential for significant change within the relevant field or industry.                    | Major anticipated advancements, transformative   | Limited industry impact or anticipated change |
| Technical Rigor | 20%    | 0-10  | Degree of complexity and depth in the engineering methods applied.                         | Advanced methods, comprehensive validations      | Basic methods, minimal validations            |
| Feasibility     | 20%    | 0-10  | Degree to which the project is practical and executable with current resources and technology.| Fully executable, clear pathways                 | Execution unclear, dependencies not addressed |

## Thresholds
| Tier    | Score | Action                                 |
|---------|-------|----------------------------------------|
| GOLDEN  | >= 9.5 | Serve as a model for future projects   |
| PUBLISH | >= 8.0 | Approve for deployment and publication |
| REVIEW  | >= 7.0 | Return for revision with specific feedback |
| REJECT  | < 7.0 | Reevaluate basics, consider new directions |

## Calibration
- GOLDEN (9.7): Project A, breakthrough technology with industry-transforming potential and fully viable execution path.
- PUBLISH (8.4): Project B, innovative technical advancement with significant anticipated industry impact.
- REVIEW (7.3): Project C, promising but with substantial feasibility risks and moderate expected impact.
- REJECT (5.5): Project D, conventional approach with limited relevance and ambiguous execution strategy.

## Automation
| Dimension       | Status         | Tool                       |
|-----------------|----------------|----------------------------|
| Innovation      | manual         | Manual expert review       |
| Impact          | manual         | Manual industry analysis   |
| Technical Rigor | semi-automated | validate_eng.py (complexity analysis) |
| Feasibility     | semi-automated | validate_eng.py (feasibility checklist) |

## References
- validate_eng.py v3.0 (Engineering evaluation tool)
- Industry standards in engineering evaluation (IEEE, ASME)
---
