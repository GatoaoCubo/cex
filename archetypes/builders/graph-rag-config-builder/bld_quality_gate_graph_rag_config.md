---
kind: quality_gate
id: p01_qg_graph_rag_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for graph_rag_config
quality: null
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
(Table: Dim | Dimension | Weight | Scoring Guide)  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | Schema Completeness | 0.15 | 100% required fields present |  
| D02 | Configuration Validity | 0.15 | Valid parameters and values |  
| D03 | Security Compliance | 0.15 | Encryption and access controls |  
| D04 | Performance Optimization | 0.15 | Efficient query handling |  
| D05 | Scalability | 0.10 | Supports growth without degradation |  
| D06 | Usability | 0.10 | Clear documentation and parameters |  
| D07 | Documentation | 0.15 | Full API and usage guides |  

## Actions  
(Table: Score | Action)  
| Score | Action |  
|---|---|  
| GOLDEN | >=9.5 | Auto-approve and deploy |  
| PUBLISH | >=8.0 | Review and publish |  
| REVIEW | >=7.0 | Manual review required |  
| REJECT | <7.0 | Reject and fix |  

## Bypass  
(Table: conditions, approver, audit trail)  
| conditions | approver | audit trail |  
|---|---|---|  
| Critical production issue requiring immediate deployment | CTO | Change management system log |
