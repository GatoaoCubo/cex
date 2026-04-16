---
kind: quality_gate
id: p01_qg_reranker_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for reranker_config
quality: 9.0
title: "Quality Gate Reranker Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [reranker_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for reranker_config"
domain: "reranker_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
| metric | threshold | operator | scope |
|---|---|---|---|
| Schema ID | ^p01_rr_[a-z][a-z0-9_]+.yaml$ | matches | H02 |

## HARD Gates
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Invalid YAML frontmatter |
| H02 | ID matches pattern ^p01_rr_[a-z][a-z0-9_]+.yaml$ | ID does not match schema pattern |
| H03 | kind field matches 'reranker_config' | kind field is not 'reranker_config' |
| H04 | 'model_type' field present | Missing 'model_type' |
| H05 | 'strategy' is in [valid_strategies] | Invalid strategy value |
| H06 | 'parameters' is non-empty object | Missing or invalid parameters |
| H07 | 'version' follows semver | Invalid version format |
| H08 | 'description' is non-empty string | Missing or empty description |
| H09 | 'enabled' is boolean | Invalid enabled value |
| H10 | 'priority' is integer ≥0 | Invalid priority value |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Model Clarity | 0.10 | Clear model type and purpose |
| D02 | Strategy Validity | 0.15 | Strategy aligns with use case |
| D03 | Parameter Completeness | 0.15 | All required parameters defined |
| D04 | Versioning | 0.10 | Semver compliant and documented |
| D05 | Description Quality | 0.10 | Concise and actionable |
| D06 | Enablement | 0.08 | Correct 'enabled' state |
| D07 | Priority | 0.07 | Logical priority value |
| D08 | Documentation | 0.10 | Includes usage examples |
| D09 | Performance Metrics | 0.08 | Includes latency/accuracy benchmarks |
| D10 | Error Handling | 0.07 | Defines fallback behavior |

## Actions
| Score | Action |
|---|---|
| ≥9.5 | GOLDEN |
| ≥8.0 | PUBLISH |
| ≥7.0 | REVIEW |
| <7.0 | REJECT |

## Bypass
| conditions | approver | audit trail |
|---|---|---|
| Emergency fix required | Senior Engineer | Reason, date, approver signature |
