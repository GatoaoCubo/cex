---
kind: quality_gate
id: p05_qg_quickstart_guide
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for quickstart_guide
quality: 9.0
title: "Quality Gate Quickstart Guide"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [quickstart_guide, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for quickstart_guide"
domain: "quickstart_guide construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| ID pattern | ^p05_qs_[a-z][a-z0-9_]+.md$ | matches | all artifacts |
| step count | 3-7 numbered steps | range | guide body |
| prerequisite section present | true | equals | all artifacts |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | invalid YAML syntax |
| H02 | ID matches pattern ^p05_qs_[a-z][a-z0-9_]+.md$ | invalid filename format |
| H03 | kind field matches 'quickstart_guide' | incorrect kind value |
| H04 | guide includes clear title | missing or ambiguous title |
| H05 | steps are numbered sequentially | non-sequential or missing steps |
| H06 | no markdown in step content | presence of markdown formatting |
| H07 | prerequisites listed | missing prerequisite section |
| H08 | success criteria defined | no success criteria |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Clarity | 0.15 | 1.0 = unambiguous instructions |
| D02 | Completeness | 0.15 | 1.0 = all required sections present |
| D03 | Usability | 0.15 | 1.0 = actionable and concise |
| D04 | Structure | 0.10 | 1.0 = logical flow |
| D05 | Language | 0.10 | 1.0 = plain English, no jargon |
| D06 | Visuals | 0.10 | 1.0 = diagrams/tables where needed |
| D07 | Accessibility | 0.10 | 1.0 = screen-reader compatible |
| D08 | Feedback | 0.15 | 1.0 = user testing results included |

## Actions
| Score | Action |
|---|---|
| GOLDEN >=9.5 | Automate deployment |
| PUBLISH >=8.0 | Schedule review |
| REVIEW >=7.0 | Request revisions |
| REJECT <7.0 | Block release |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Legacy system integration | Senior Engineer | Note: "Legacy system exception approved" |
