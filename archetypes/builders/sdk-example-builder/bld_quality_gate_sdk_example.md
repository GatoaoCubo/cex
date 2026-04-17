---
kind: quality_gate
id: p04_qg_sdk_example
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for sdk_example
quality: 9.0
title: "Quality Gate Sdk Example"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sdk_example, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for sdk_example"
domain: "sdk_example construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| Code Example Completeness | 100% | equals | per language |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | invalid YAML syntax or missing fields |
| H02 | ID matches pattern ^p04_sdk_[a-z][a-z0-9_]+.md$ | filename does not match schema |
| H03 | kind field matches 'sdk_example' | kind field is incorrect |
| H04 | Error handling demonstrated | no error handling examples present |
| H05 | API versioning used | missing or incorrect API versioning |
| H06 | Documentation comments present | code lacks inline documentation |
| H07 | Example covers all integration patterns | incomplete pattern coverage |
| H08 | Licensing statement included | missing or invalid license notice |
| H09 | No security vulnerabilities | code contains insecure practices |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Code clarity | 0.20 | Readable, well-structured code |
| D02 | Completeness | 0.20 | All required patterns implemented |
| D03 | Error handling | 0.20 | Robust error handling examples |
| D04 | Documentation | 0.15 | Clear inline comments and README |
| D05 | Licensing | 0.05 | Valid license notice present |
| D06 | Security | 0.10 | No insecure practices detected |
| D07 | Language support | 0.05 | Examples for all supported languages |
| D08 | API versioning | 0.05 | Correct API versioning used |

## Actions
| Score | Action |
|---|---|
| GOLDEN >=9.5 | Auto-approve and publish |
| PUBLISH >=8.0 | Manual review required before publish |
| REVIEW >=7.0 | Flag for team review |
| REJECT <7.0 | Reject and request revisions |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Approved by CTO for urgent release | CTO | CTO approval recorded in JIRA |
