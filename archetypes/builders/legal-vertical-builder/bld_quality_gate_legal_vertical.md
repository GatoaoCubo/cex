---
kind: quality_gate
id: p01_qg_legal_vertical
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for legal_vertical
quality: 9.0
title: "Quality Gate Legal Vertical"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [legal_vertical, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for legal_vertical"
domain: "legal_vertical construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| Legal data completeness | 100% | >= | All documents |
| Billable hour accuracy | 95% | >= | Time tracking |
| Contract analysis coverage | 90% | >= | Use cases |
| Privilege log completeness | 100% | >= | Legal files |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Invalid YAML syntax |
| H02 | ID matches ^p01_lv_[a-z][a-z0-9_]+.md$ | Invalid schema ID pattern |
| H03 | kind field matches 'legal_vertical' | Incorrect kind value |
| H04 | Attorney-client privilege AND work-product doctrine both addressed | Missing privilege or work-product section |
| H05 | EDRM model phases referenced for any eDiscovery use case | eDiscovery use case present without EDRM mapping |
| H06 | ABA Model Rule 5.3 compliance addressed for AI/non-lawyer assistant use cases | AI use case without Rule 5.3 documentation |
| H07 | Billable hour tracking uses UTBMS task codes | Billing section without UTBMS codes |
| H08 | Legal hold / document retention procedures documented | No legal hold or retention policy |
| H09 | DMS integration pattern referenced (iManage, NetDocuments, or equivalent) | Document workflow with no DMS specification |
| H10 | Audit trails for legal actions documented | Missing audit log requirements |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Data completeness | 0.2 | 0-1 (missing vs complete) |
| D02 | Accuracy | 0.2 | 0-1 (errors vs precision) |
| D03 | Compliance | 0.15 | 0-1 (non-compliant vs compliant) |
| D04 | Use case alignment | 0.1 | 0-1 (misaligned vs aligned) |
| D05 | Contract analysis | 0.1 | 0-1 (incomplete vs thorough) |
| D06 | Privilege handling | 0.1 | 0-1 (violations vs adherence) |
| D07 | Audit trail integrity | 0.15 | 0-1 (gaps vs full coverage) |

## Actions
| Score | Action |
|---|---|
| GOLDEN | >=9.5 | Auto-publish with legal review |
| PUBLISH | >=8.0 | Publish after compliance check |
| REVIEW | >=7.0 | Escalate to legal team for review |
| REJECT | <7.0 | Block and request rework |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Urgent legal matter | Legal compliance officer | Signed approval + timestamp |
