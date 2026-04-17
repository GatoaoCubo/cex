---
kind: quality_gate
id: p11_qg_incident_report
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for incident_report
quality: 9.1
title: "Quality Gate Incident Report"
version: "1.1.0"
author: n05_ops
tags: [incident_report, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for incident_report"
domain: "incident_report construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition
(Table: metric, threshold, operator, scope)
| metric                | threshold | operator | scope               |
|-----------------------|-----------|----------|---------------------|
| Incident report completeness | 100%      | =        | All incident reports |

## HARD Gates
(Table: ID | Check | Fail Condition)
| ID   | Check                  | Fail Condition                                      |
|------|------------------------|-----------------------------------------------------|
| H01  | YAML valid             | Invalid YAML syntax                                 |
| H02  | ID matches pattern     | ID does not match `INC-\d{4}-\d{2}-\d{2}`          |
| H03  | kind matches           | `kind` ≠ `incident_report`                          |
| H04  | Required fields present| Missing `summary`, `root_cause`, `action_items`     |
| H05  | Timeline details       | Timeline lacks timestamps or responsible parties    |
| H06  | Root cause analysis    | Analysis insufficient or lacks technical depth      |
| H07  | Action items defined   | No actionable items or unclear remediation steps    |
| H08  | Sign-off present       | Missing `reviewer` or `approver` signatures         |

## SOFT Scoring
(Table: Dim | Dimension | Weight | Scoring Guide)
| Dim | Dimension               | Weight | Scoring Guide                                      |
|-----|-------------------------|--------|----------------------------------------------------|
| D1  | Completeness            | 0.15   | All required sections present = 1.0 |
| D2  | Root cause analysis     | 0.25   | 5-Whys complete, contributing factors mapped = 1.0 |
| D3  | Action items            | 0.20   | Specific, owned, and dated items = 1.0 |
| D4  | Timeline accuracy       | 0.15   | All NIST SP 800-61 phases with timestamps = 1.0 |
| D5  | Stakeholder impact      | 0.10   | Quantified user + business impact = 1.0 |
| D6  | Lessons learned         | 0.10   | Systemic gaps identified and linked to actions = 1.0 |
| D7  | Sign-off validity       | 0.05   | All required roles signed = 1.0 |

## Actions
(Table: Score | Action)
| Score     | Action                                      |
|-----------|---------------------------------------------|
| GOLDEN    | >=9.5: Automatically publish and notify stakeholders |
| PUBLISH   | >=8.0: Publish after minimal review           |
| REVIEW    | >=7.0: Require team review and revisions      |
| REJECT    | <7.0: Reject, resubmission required           |

## Bypass
(Table: conditions, approver, audit trail)
| conditions                | approver | audit trail                                |
|---------------------------|----------|--------------------------------------------|
| Emergency bypass          | CTO      | Log bypass reason, approver, timestamp     |
| Regulatory override       | CRO      | Document legal justification, approver     |
| System failure            | CTO      | Include system state, approver, timestamp  |
