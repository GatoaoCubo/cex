---
kind: quality_gate
id: p11_qg_compliance_framework
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for compliance_framework
quality: 9.0
title: "Quality Gate Compliance Framework"
version: "1.1.0"
author: n05_ops
tags: [compliance_framework, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for compliance_framework"
domain: "compliance_framework construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| Regulatory Compliance Coverage | 100% | ≥ | All AI systems |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML valid | Invalid YAML syntax |
| H02 | ID matches pattern | ID does not match `^p11_cfw_[a-zA-Z0-9_]+$` |
| H03 | kind matches | `kind` ≠ `compliance_framework` |
| H04 | Regulatory frameworks mapped | No specific regulation (GDPR/AI Act/NIST/ISO42001) cited by name and article |
| H05 | Attestation provided | Missing signed attestation with date and compliance officer name |
| H06 | Gap analysis present | No gap analysis section or all gaps marked as N/A without justification |
| H07 | Regulatory mapping table | No table linking system components to regulation articles |
| H08 | Data privacy provisions | Missing GDPR/CCPA/LGPD data subject rights section when personal data processed |
| H09 | Bias mitigation evidence | No bias audit or fairness metric when AI Act Art. 10 applies |
| H10 | Version control | No version history for regulatory mappings |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Regulatory completeness | 0.20 | 0.9–1.0: Full coverage |
| D02 | Attestation quality | 0.15 | 0.8–0.9: Valid but incomplete |
| D03 | Documentation | 0.15 | 0.7–0.8: Partial documentation |
| D04 | Third-party audit | 0.10 | 0.6–0.7: Pending audit |
| D05 | Data privacy | 0.10 | 0.5–0.6: Minor gaps |
| D06 | Bias mitigation | 0.10 | 0.4–0.5: Basic plan |
| D07 | Version control | 0.10 | 0.3–0.4: No history |
| D08 | Stakeholder feedback | 0.10 | 0.2–0.3: Unreviewed |

## Actions
| Score | Action |
|---|---|
| ≥9.5 | Automatically approve and publish |
| ≥8.0 | Publish with minimal review |
| ≥7.0 | Request review by compliance team |
| <7.0 | Reject and require fixes |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Critical regulatory change | CTO | Log bypass reason and approver |
| Emergency deployment | CEO | Include timestamp and justification |
| Legal exemption confirmed | Legal Counsel | Attach exemption documentation |
