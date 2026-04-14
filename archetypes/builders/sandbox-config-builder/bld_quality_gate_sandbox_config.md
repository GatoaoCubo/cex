---
kind: quality_gate
id: p09_qg_sandbox_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for sandbox_config
quality: null
title: "Quality Gate Sandbox Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [sandbox_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for sandbox_config"
domain: "sandbox_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  
(Table: metric, threshold, operator, scope)  
| metric             | threshold | operator | scope              |  
|--------------------|-----------|----------|--------------------|  
| Isolation Level    | High      | >=       | Sandbox Environment|  

## HARD Gates  
(Table: ID | Check | Fail Condition)  
| ID   | Check                  | Fail Condition                                      |  
|------|------------------------|-----------------------------------------------------|  
| H01  | YAML Valid             | Invalid YAML syntax                                 |  
| H02  | ID matches pattern     | ID does not match `sandbox-\d{4}`                  |  
| H03  | kind matches           | kind != `sandbox_config`                            |  
| H04  | Resource Limits        | Missing CPU/Memory limits                         |  
| H05  | Network Isolation      | Network access not restricted                     |  
| H06  | Logging Config         | No audit log retention defined                    |  
| H07  | User Isolation         | Shared user namespace enabled                     |  
| H08  | Process Isolation      | No cgroup or container isolation                  |  

## SOFT Scoring  
(Table: Dim | Dimension | Weight | Scoring Guide)  
| Dim | Dimension         | Weight | Scoring Guide                                      |  
|-----|-------------------|--------|----------------------------------------------------|  
| D1  | Config Completeness | 0.15   | 100% complete = 1.0, missing fields = 0.5          |  
| D2  | Isolation Strength  | 0.20   | Full isolation = 1.0, partial = 0.7, none = 0.3    |  
| D3  | Resource Limits     | 0.15   | Defined limits = 1.0, missing = 0.5                |  
| D4  | Security Policies   | 0.15   | All policies enforced = 1.0, partial = 0.7         |  
| D5  | Logging             | 0.10   | Audit logs enabled = 1.0, disabled = 0.3           |  
| D6  | Auditability        | 0.10   | Traceable to operator = 1.0, untraceable = 0.5     |  
| D7  | Compliance          | 0.10   | Meets regulatory standards = 1.0, partial = 0.7    |  
| D8  | Performance         | 0.15   | Latency < 100ms = 1.0, > 500ms = 0.3               |  

## Actions  
(Table: Score | Action)  
| Score       | Action                                      |  
|-------------|---------------------------------------------|  
| GOLDEN >=9.5| Auto-approve, deploy to production          |  
| PUBLISH >=8.0| Manual review, deploy to staging            |  
| REVIEW >=7.0| Peer review required, no deployment         |  
| REJECT <7.0 | Block deployment, fix required              |  

## Bypass  
(Table: conditions, approver, audit trail)  
| conditions                | approver  | audit trail                  |  
|---------------------------|-----------|------------------------------|  
| Security exception        | CTO       | Ticket #SEC-2023-001         |  
| Critical bug fix          | SRE Lead  | Jira-BUG-2023-002            |  
| Compliance override       | Legal     | Legal-Override-2023-003      |
