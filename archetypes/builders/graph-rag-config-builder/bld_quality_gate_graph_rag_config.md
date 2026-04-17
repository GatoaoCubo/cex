---
kind: quality_gate
id: p01_qg_graph_rag_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for graph_rag_config
quality: 9.0
title: "Quality Gate Graph Rag Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [graph_rag_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for graph_rag_config"
domain: "graph_rag_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition
(Table: metric, threshold, operator, scope)
| metric | threshold | operator | scope |
|---|---|---|---|
| Schema Validity | 1 | equals | All files |

## HARD Gates
(Table: ID | Check | Fail Condition)
| ID | Check | Fail Condition |
|---|---|---|
| H01 | YAML frontmatter valid | Invalid YAML frontmatter |
| H02 | ID matches pattern ^p01_grc_[a-z][a-z0-9_]+.yaml$ | ID does not match schema pattern |
| H03 | kind field matches 'graph_rag_config' | kind field not 'graph_rag_config' |
| H04 | graph_type field present | Missing graph_type |
| H05 | embedding_model field valid | Invalid or missing embedding_model |
| H06 | retrieval_strategy field valid | Invalid or missing retrieval_strategy |
| H07 | knowledge_sources field present | Missing knowledge_sources |
| H08 | query_transformer field valid | Invalid or missing query_transformer |

## SOFT Scoring
| Dim | Dimension | Weight | Scoring Guide |
|---|---|---|---|
| D01 | Schema Completeness | 0.20 | 100% required fields present |
| D02 | Configuration Validity | 0.20 | Valid parameters and values |
| D03 | Graph Model Fidelity | 0.15 | Correct community detection and entity extraction config |
| D04 | Retrieval Strategy Quality | 0.15 | Multi-hop, hybrid vector+graph strategy defined |
| D05 | Scalability | 0.10 | Configurable traversal depth and query latency thresholds |
| D06 | Usability | 0.10 | Clear documentation and parameters |
| D07 | Documentation | 0.10 | Usage guides and examples present |

## Actions
| Score | Action |
|---|---|
| >=9.5 | GOLDEN |
| >=8.0 | PUBLISH |
| >=7.0 | REVIEW |
| <7.0 | REJECT |

## Bypass
(Table: conditions, approver, audit trail)
| conditions | approver | audit trail |
|---|---|---|
| Critical production issue requiring immediate deployment | CTO | Change management system log |
