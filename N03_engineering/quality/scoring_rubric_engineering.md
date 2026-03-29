---  
id: p07_sr_eng_nucleus  
kind: scoring_rubric  
pillar: P07  
title: "Rubric: Engineering Nucleus"  
version: "1.0.0"  
created: "2023-10-07"  
updated: "2023-10-07"  
author: "scoring-rubric-builder"  
framework: "Engineering Nucleus"  
target_kinds: [artifact, engineering_nucleus]  
dimensions_count: 5  
total_weight: 100  
threshold_golden: 9.5  
threshold_publish: 8.0  
threshold_review: 7.0  
automation_status: "semi-automated"  
domain: "engineering"  
quality: null  
tags: [scoring-rubric, engineering, evaluation]  
tldr: "5-dimension rubric assessing functionality, innovation, scalability, maintainability, and user experience for engineering artifacts."  
density_score: 0.85  
calibration_set: [p07_gt_eng_functionality_example]  
inter_rater_agreement: 0.85  
appeals_process: "Submit reevaluation requests to engineering-review-board@example.com with detailed justification."  
linked_artifacts:  
  primary: "engineering-nucleus-builder"  
  related: [p11_qg_eng_publish, p07_gt_eng_example]  
---  

## Purpose  
The scoring rubric evaluates engineering artifacts within the Engineering Nucleus framework. It ensures artifacts meet or exceed necessary engineering standards by assessing key dimensions crucial to engineering success.  

## Dimensions  
| Dimension      | Weight | Scale | Criteria                                                                                     | Example (10)                                                    | Example (5)                                                     |
|----------------|--------|-------|----------------------------------------------------------------------------------------------|-----------------------------------------------------------------|-----------------------------------------------------------------|
| Functionality  | 30%    | 0-10  | Complete and correct implementation of all specified features.                               | Fully functional, all features work as intended without issues. | Partially functional, critical features have significant issues.|
| Innovation     | 20%    | 0-10  | Incorporation of novel solutions or improvements upon existing methods.                      | Introduces ground-breaking ideas enhancing previous solutions.  | Slight improvements, largely replicates existing solutions.     |
| Scalability    | 20%    | 0-10  | Ability to handle increasing loads or expansions efficiently.                                | Scales easily with minimal resource increase, shows future-proofing. | Limited scalability, requires major changes for load handling. |
| Maintainability| 15%    | 0-10  | Ease of upkeep, including code readability and documentation.                                | Code is clean, well-documented, easily maintained or updated.   | Poorly documented, cumbersome to update or debug.               |
| User Experience| 15%    | 0-10  | Quality of interaction with users, intuitiveness, and satisfaction.                          | User interface is intuitive, highly satisfying experience.      | Unintuitive interface, leads to frustration or frequent errors. |

## Tier Thresholds  
| Tier    | Score | Action                              |
|---------|-------|-------------------------------------|
| GOLDEN  | >= 9.5 | Promote as exemplary engineering artifact and use as reference model. |
| PUBLISH | >= 8.0 | Approve for deployment and use.    |
| REVIEW  | >= 7.0 | Return with feedback for improvement and resubmission. |
| REJECT  | < 7.0 | Reject and require redesign or reformulation from scratch. |

## Calibration  
- **GOLDEN (9.7)**: Examples of engineering artifacts where functionality is flawless and innovative solutions are incorporated, such as the p07_gt_eng_functionality_example.  
- **PUBLISH (8.4)**: Artifacts that meet functional requirements well, with some unique features and reasonable scalability.  
- **REVIEW (7.1)**: Artifacts with good intention but significant usability or scalability issues that detract from their practical use.  
- **REJECT (5.8)**: Artifacts that fall short in most dimensions and require fundamental redesigns, failing to meet basic requirements.

## Automation  
| Dimension      | Status         | Tool                  |
|----------------|----------------|-----------------------|
| Functionality  | automated      | validate_eng.py       |
| Innovation     | manual         | Human review          |
| Scalability    | semi-automated | scalability_tool.py   |
| Maintainability| automated      | code_linter.py        |
| User Experience| semi-automated | ux_assessment_tool.py |

## References  
- AAC&U VALUE Rubrics: https://www.aacu.org/initiatives/value-initiative  
- validate_eng.py v2.0 (CEX Engineering Nucleus implementation reference)