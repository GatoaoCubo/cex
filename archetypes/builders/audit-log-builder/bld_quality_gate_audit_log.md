---
kind: quality_gate
id: p11_qg_audit_log
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for audit_log
quality: 9.0
title: "Quality Gate Audit Log"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [audit_log, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for audit_log"
domain: "audit_log construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| Audit log immutability | 100% | equals | All audit logs |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Missing or invalid frontmatter |
| H02 | ID matches pattern ^p11_al_[a-z][a-z0-9_]+.md$ | ID format invalid |
| H03 | kind field matches 'audit_log' | kind field incorrect |
| H04 | Required field 'timestamp' exists | Missing 'timestamp' |
| H05 | Required field 'actor' exists | Missing 'actor' |
| H06 | Required field 'action' exists | Missing 'action' |
| H07 | Required field 'resource' exists | Missing 'resource' |
| H08 | Required field 'outcome' exists | Missing 'outcome' |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D1 | Data Integrity | 0.20 | 1.0 if immutable, 0.5 if partially mutable, 0.0 otherwise |
| D2 | Encryption | 0.15 | 1.0 if encrypted at rest, 0.5 if unencrypted |
| D3 | Retention | 0.15 | 1.0 if retention ≥ 180 days, 0.5 if < 180 days |
| D4 | Tamper Evidence | 0.15 | 1.0 if hash signatures present, 0.5 if absent |
| D5 | Field Completeness | 0.10 | 1.0 if all required fields present, 0.5 if missing |
| D6 | Access Controls | 0.10 | 1.0 if read-only access enforced, 0.5 if not |
| D7 | Audit Trail Completeness | 0.15 | 1.0 if full event context captured, 0.5 if partial |

## Actions
| Score | Action |
|---|---|
| GOLDEN (≥9.5) | Auto-approve and deploy |
| PUBLISH (≥8.0) | Publish with review |
| REVIEW (≥7.0) | Manual review required |
| REJECT (<7.0) | Block deployment |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Emergency system fix | Security Officer | Log bypass request with justification |
