---
kind: quality_gate
id: p07_qg_judge_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for judge_config
quality: null
title: "Quality Gate Judge Config"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [judge_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for judge_config"
domain: "judge_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
| metric       | threshold | operator | scope         |  
|--------------|-----------|----------|---------------|  
| accuracy     | 95%       | >=       | evaluation    |  
| consistency  | 90%       | >=       | judge output  |  
| latency      | 500ms     | <=       | system-wide   |  

## HARD Gates  
| ID         | Check                  | Fail Condition                          |  
|------------|------------------------|-----------------------------------------|  
| H01        | YAML frontmatter valid | Invalid YAML syntax or missing fields   |  
| H02        | ID matches pattern     | ID does not match ^p07_jc_[a-z][a-z0-9_]+.md$ |  
| H03        | kind field matches     | kind != 'judge_config'                  |  
| H04        | judge model specified  | judge_model is missing or empty         |  
| H05        | multiple judges        | judge_count < 2                         |  
| H06        | criteria defined       | evaluation_criteria is empty            |  
| H07        | timeout configured     | timeout_threshold is missing or <=0     |  
| H08        | config versioned       | version field is missing or invalid     |  

## SOFT Scoring  
| Dim        | Dimension     | Weight | Scoring Guide                          |  
|------------|---------------|--------|----------------------------------------|  
| D01        | Accuracy      | 0.20   | 95-100% = 1.0, 90-94% = 0.8, <90% = 0.5 |  
| D02        | Consistency   | 0.15   | 90-100% = 1.0, 80-89% = 0.7, <80% = 0.3 |  
| D03        | Fairness      | 0.15   | 95-100% = 1.0, 85-94% = 0.7, <85% = 0.3 |  
| D04        | Completeness  | 0.15   | 100% = 1.0, 90-99% = 0.8, <90% = 0.5    |  
| D05        | Scalability   | 0.10   | 500ms latency = 1.0, 700ms = 0.7, >700ms=0.3 |  
| D06        | Usability     | 0.10   | Configurable = 1.0, partial = 0.5, none=0.0 |  
| D07        | Reliability   | 0.10   | 99.9% uptime = 1.0, 99% = 0.7, <99% = 0.3 |  
| D08        | Others        | 0.05   | Minor issues = 0.5, no issues = 1.0     |  

## Actions  
| Score      | Action                          |  
|------------|---------------------------------|  
| GOLDEN     | Auto-approve and deploy         |  
| PUBLISH    | Manual review required          |  
| REVIEW     | Request changes and re-evaluate |  
| REJECT     | Reject and require rework       |  

## Bypass  
| conditions                          | approver         | audit trail                  |  
|------------------------------------|------------------|------------------------------|  
| Emergency system fix required      | Senior Engineer  | Ticket #1234, 2023-10-05     |  
| Legacy system compatibility        | CTO              | Ticket #5678, 2023-10-06     |
