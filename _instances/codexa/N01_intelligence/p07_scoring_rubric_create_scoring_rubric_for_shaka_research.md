---

```yaml
id: p07_sr_shaka_nucleus
kind: scoring_rubric
pillar: P07
title: "Rubric: Shaka Research Nucleus"
version: "1.0.0"
created: "2023-10-20"
updated: "2023-10-20"
author: "builder"
framework: "Shaka"
target_kinds: [research_nucleus]
dimensions_count: 3
total_weight: 100
threshold_golden: 9.5
threshold_publish: 8.0
threshold_review: 7.0
automation_status: "semi-automated"
domain: "research"
quality: null
tags: [scoring-rubric, shaka, research]
tldr: "3-dimension rubric for Shaka Research: Methodology 40%, Innovation 30%, Impact 30%"
density_score: 0.85
calibration_set: [shaka_research_golden_test_1, shaka_research_golden_test_2]
inter_rater_agreement: 0.82
appeals_process: "Submit to review committee with justification for re-evaluation"
linked_artifacts:
  primary: "shaka-framework-builder"
  related: [shaka_quality_gate, shaka_golden_tests]
```

## Framework Overview
The Shaka Research Nucleus Scoring Rubric evaluates research projects on Methodology, Innovation, and Impact to ensure high-quality outcomes aligned with strategic research goals.

## Dimensions
| Dimension   | Weight | Scale | Criteria                                                                              | Example (10)                                                     | Example (5)                                                      |
|-------------|--------|-------|---------------------------------------------------------------------------------------|------------------------------------------------------------------|------------------------------------------------------------------|
| Methodology | 40%    | 0-10  | Research design is rigorous and replicable with thorough documentation.               | Comprehensive design, all steps reproducible, excellent rigor    | Basic design, lacking some documentation, moderate rigor         |
| Innovation  | 30%    | 0-10  | Incorporates novel ideas or approaches that significantly advance the field.          | Groundbreaking approach, new theories introduced                 | Some novel ideas, but mostly derivative approaches               |
| Impact      | 30%    | 0-10  | Potential to significantly influence the research community or broader society.       | High potential for societal/academic influence, broad implications | Limited influence expected, few implications beyond immediate field |

## Thresholds
| Tier    | Score | Action                                                   |
|---------|-------|----------------------------------------------------------|
| GOLDEN  | >= 9.5 | Promote as a case study example, highlight best practices |
| PUBLISH | >= 8.0 | Publish in high-impact journals                          |
| REVIEW  | >= 7.0 | Return with feedback, suggest targeted improvements      |
| REJECT  | < 7.0  | Recommend substantial revision or rejection              |

## Calibration
- GOLDEN (9.8): Project with impeccable methodology, innovative approaches leading to major field advancements, and high societal impact.
- PUBLISH (8.4): Solid methodology, some innovative aspects, potential for moderate field impact.
- REVIEW (7.3): Adequate methodology with minor gaps, low innovation, minimal expected impact.
- REJECT (6.5): Flawed methodology, no innovation, negligible impact.

## Automation
| Dimension   | Status         | Tool                              |
|-------------|----------------|-----------------------------------|
| Methodology | semi-automated | ResearchValidatorTool v1.2        |
| Innovation  | manual         | Peer review required              |
| Impact      | semi-automated | SocietalImpactAnalyzer v3.0       |

## References
- AAC&U VALUE Rubrics: https://www.aacu.org/initiatives/value-initiative
- ResearchValidatorTool: Internal tool for evaluating research methodologies

---