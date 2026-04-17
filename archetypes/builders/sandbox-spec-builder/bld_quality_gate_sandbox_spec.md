---
kind: quality_gate
id: p09_qg_sandbox_spec
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for sandbox_spec
quality: 9.0
title: "Quality Gate Sandbox Spec"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sandbox_spec, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for sandbox_spec"
domain: "sandbox_spec construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| Isolation Level | Full | equals | All environments |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Missing or invalid frontmatter |
| H02 | ID matches pattern ^p09_sb_[a-z][a-z0-9_]+.yaml$ | ID format invalid |
| H03 | kind field matches 'sandbox_spec' | kind field incorrect |
| H04 | network_isolation field present | Missing network isolation spec |
| H05 | resource_limits defined | No resource limits specified |
| H06 | no production network connectivity | Sandbox connected to production |
| H07 | teardown_policy exists | Missing teardown procedure |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Isolation | 0.20 | 1.0 = Full isolation |
| D02 | Resource Management | 0.15 | 1.0 = Strict limits |
| D03 | Compliance | 0.15 | 1.0 = Meets enterprise standards |
| D04 | Auditability | 0.10 | 1.0 = Full logging enabled |
| D05 | Scalability | 0.10 | 1.0 = Supports 100+ concurrent users |
| D06 | Security | 0.10 | 1.0 = No external exposure |
| D07 | Documentation | 0.10 | 1.0 = Complete API docs |
| D08 | Technology Stack | 0.10 | 1.0 = Approved frameworks only |

## Actions
| Score | Action |
|---|---|
| GOLDEN >=9.5 | Auto-approve for enterprise deployment |
| PUBLISH >=8.0 | Publish to sandbox registry |
| REVIEW >=7.0 | Manual review required |
| REJECT <7.0 | Reject and request revisions |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Emergency deployment | CTO | "Bypass approved for critical incident" |
| Business continuity override | CDO | "Bypass logged per incident #XYZ" |
