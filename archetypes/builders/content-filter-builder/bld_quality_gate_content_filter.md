---
kind: quality_gate
id: p11_qg_content_filter
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for content_filter
quality: 9.0
title: "Quality Gate Content Filter"
version: "1.0.0"
author: wave1_builder_gen
tags: [content_filter, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for content_filter"
domain: "content_filter construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition

This ISO defines a content filter -- the moderation rules that gate output or input.
| metric                | threshold | operator | scope              |
|-----------------------|-----------|----------|--------------------|
| Pipeline Config Validity | 100%      | equals   | All content filters |

## HARD Gates
| ID   | Check                  | Fail Condition                              |
|------|------------------------|---------------------------------------------|
| H01  | YAML valid             | Invalid YAML syntax                         |
| H02  | ID matches pattern     | ID does not match `^[a-z0-9]+_[a-z]+$`     |
| H03  | kind matches           | kind ≠ `content_filter`                    |
| H04  | Required fields present| Missing `input` or `output` field         |
| H05  | No duplicate IDs       | Duplicate ID detected                     |
| H06  | Allowed operators      | Operator not in `[allow,block,transform]` |
| H07  | Content type valid     | Unsupported content type specified        |

## SOFT Scoring
| Dim | Dimension             | Weight | Scoring Guide                                      |
|-----|------------------------|--------|----------------------------------------------------|
| D1  | YAML structure         | 0.10   | Valid syntax, proper nesting                      |
| D2  | ID uniqueness          | 0.10   | No duplicates                                     |
| D3  | Kind consistency       | 0.10   | All entries share same kind                       |
| D4  | Operator validity      | 0.10   | All operators valid                               |
| D5  | Content type coverage  | 0.15   | Covers 90%+ of required content types             |
| D6  | Performance            | 0.15   | Latency < 50ms, error rate < 1%                  |
| D7  | Error handling         | 0.10   | Defined fallback behavior                       |
| D8  | Documentation          | 0.10   | Clear comments and schema references            |

## Actions
| Score     | Action                          |
|-----------|----------------------------------|
| GOLDEN    | Auto-approve, deploy immediately |
| PUBLISH   | Manual review required          |
| REVIEW    | Escalate to senior engineer     |
| REJECT    | Block deployment, fix required  |

## Bypass
| conditions                  | approver | audit trail              |
|-----------------------------|----------|--------------------------|
| Urgent security fix required | CTO      | Requires written approval |
