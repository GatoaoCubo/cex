---
kind: quality_gate
id: p06_qg_api_reference
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for api_reference
quality: 9.0
title: "Quality Gate Api Reference"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [api_reference, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for api_reference"
domain: "api_reference construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| ID pattern | ^p06_ar_[a-z][a-z0-9_]+.md$ | matches | all files |
| endpoint count | >= 1 | gte | artifact body |
| authentication documented | true | equals | all artifacts |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | invalid YAML |
| H02 | ID matches ^p06_ar_[a-z][a-z0-9_]+.md$ | invalid pattern |
| H03 | kind field matches 'api_reference' | incorrect kind |
| H04 | All endpoints listed | missing endpoint |
| H05 | Parameters/responses documented | incomplete spec |
| H06 | Authentication methods specified | missing auth details |
| H07 | Examples provided for all endpoints | no examples |
| H08 | Consistent formatting (YAML/Markdown) | inconsistent syntax |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Completeness | 0.20 | 100% endpoints/params/responses |
| D02 | Clarity | 0.15 | Readable descriptions/examples |
| D03 | Consistency | 0.15 | Uniform structure/formatting |
| D04 | Examples | 0.10 | 100% endpoints with examples |
| D05 | Auth details | 0.10 | Full auth method coverage |
| D06 | Versioning | 0.10 | API version specified |
| D07 | Structure | 0.10 | Valid table/section hierarchy |
| D08 | Language | 0.10 | English/technical accuracy |

## Actions
| Score | Action |
|---|---|
| GOLDEN >=9.5 | Auto-publish to prod |
| PUBLISH >=8.0 | Review for minor edits |
| REVIEW >=7.0 | Fix critical issues |
| REJECT <7.0 | Rewrite documentation |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Senior engineer approval | CTO | Requires written justification |
