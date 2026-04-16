---
kind: quality_gate
id: p09_qg_playground_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for playground_config
quality: 9.0
title: "Quality Gate Playground Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [playground_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for playground_config"
domain: "playground_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| metric         | threshold                          | operator | scope  |
|----------------|------------------------------------|----------|--------|
| schema_id      | ^p09_pg_[a-z][a-z0-9_]+.yaml$     | matches  | H02    |

## HARD Gates
| ID  | Check                  | Fail Condition                                  |
|-----|------------------------|-------------------------------------------------|
| H01 | YAML frontmatter valid | Missing or invalid YAML frontmatter             |
| H02 | ID matches pattern     | ID does not match ^p09_pg_[a-z][a-z0-9_]+.yaml$|
| H03 | kind field matches     | kind ≠ 'playground_config'                      |
| H04 | Required fields exist  | Missing 'name', 'description', or 'access_control'|
| H05 | Timeout defined        | timeout < 1s or > 72h                           |
| H06 | Resource limits valid  | CPU/memory limits exceed 80% of system capacity |
| H07 | Audit logs enabled     | audit_logs not set to 'enabled'                 |

## SOFT Scoring
| Dim | Dimension           | Weight | Scoring Guide                                  |
|-----|---------------------|--------|------------------------------------------------|
| D01 | Configuration completeness | 0.15 | 100% required fields present                   |
| D02 | Security controls    | 0.20 | 100% access control + encryption              |
| D03 | Usability            | 0.10 | Interactive features functional               |
| D04 | Documentation        | 0.15 | 100% API/usage guides complete                |
| D05 | Performance          | 0.10 | Latency < 500ms, error rate < 1%              |
| D06 | Compliance           | 0.10 | Meets data privacy and audit standards        |
| D07 | Scalability          | 0.10 | Supports 1000+ concurrent users               |
| D08 | Auditability         | 0.10 | Full traceability of user actions             |

## Actions
| Score   | Action                        |
|---------|-------------------------------|
| ≥9.5    | Automate deployment           |
| ≥8.0    | Schedule review               |
| ≥7.0    | Manual QA verification        |
| <7.0    | Reject and request revisions  |

## Bypass
| conditions                          | approver | audit trail         |
|------------------------------------|----------|---------------------|
| Urgent production fix required     | CISO     | Escalation log      |
