---
kind: quality_gate
id: p01_qg_agentic_rag
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for agentic_rag
quality: null
title: "Quality Gate Agentic Rag"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [agentic_rag, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for agentic_rag"
domain: "agentic_rag construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
(Table: metric, threshold, operator, scope)  
| metric         | threshold | operator | scope         |  
|----------------|-----------|----------|---------------|  
| Retrieval Accuracy | 95%       | >=       | All queries   |  
| Response Latency | 500ms     | <=       | Production    |  
| Agent Policy Alignment | 100%   | ==       | All outputs   |  

## HARD Gates  
(Table: ID | Check | Fail Condition)  
| ID             | Check                         | Fail Condition                                |  
|----------------|-------------------------------|-----------------------------------------------|  
| H01            | YAML frontmatter valid        | Invalid YAML syntax or missing fields         |  
| H02            | ID matches ^p01_ar_[a-z][a-z0-9_]+.md$ | ID does not conform to schema pattern        |  
| H03            | kind field matches 'agentic_rag' | kind field is not 'agentic_rag'              |  
| H04            | Agent configuration present     | Missing agent configuration file              |  
| H05            | Retrieval sources validated     | Unverified or insecure data sources used      |  
| H06            | Response alignment with knowledge | Output contradicts verified knowledge       |  
| H07            | Error handling implemented      | No fallback or error recovery mechanism       |  
| H08            | Logging enabled                 | Missing audit logs for agent decisions        |  

## SOFT Scoring  
(Table: Dim | Dimension | Weight | Scoring Guide)  
| Dim | Dimension               | Weight | Scoring Guide                                      |  
|-----|-------------------------|--------|----------------------------------------------------|  
| D01 | Retrieval Accuracy      | 0.20   | 95%+ = 1.0, 90% = 0.8, 80% = 0.5, <80% = 0.0        |  
| D02 | Latency                 | 0.15   | 500ms = 1.0, 600ms = 0.75, 700ms = 0.5, >700ms = 0.0 |  
| D03 | Policy Alignment        | 0.15   | 100% = 1.0, 90% = 0.8, 80% = 0.5, <80% = 0.0        |  
| D04 | Error Handling          | 0.10   | Full = 1.0, partial = 0.5, none = 0.0               |  
| D05 | Logging Completeness    | 0.10   | Full = 1.0, partial = 0.5, none = 0.0               |  
| D06 | User Experience         | 0.10   | Seamless = 1.0, minor issues = 0.75, major = 0.5     |  
| D07 | Scalability             | 0.10   | Handles 10k+ reqs = 1.0, 5k = 0.75, <5k = 0.5       |  
| D08 | Security Compliance     | 0.10   | Fully compliant = 1.0, partial = 0.5, none = 0.0     |  

## Actions  
(Table: Score | Action)  
| Score      | Action         |  
|------------|----------------|  
| >=9.5      | GOLDEN         |  
| >=8.0      | PUBLISH        |  
| >=7.0      | REVIEW         |  
| <7.0       | REJECT         |  

## Bypass  
(Table: conditions, approver, audit trail)  
| conditions                  | approver             | audit trail                              |  
|-----------------------------|----------------------|------------------------------------------|  
| Emergency fix required      | Senior Engineering Lead | "Bypass approved by [name] for [reason]" |
