---
kind: quality_gate
id: p12_qg_workflow_node
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for workflow_node
quality: null
title: "Quality Gate Workflow Node"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [workflow_node, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for workflow_node"
domain: "workflow_node construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
(Table: metric, threshold, operator, scope)  
| Metric       | Threshold                          | Operator | Scope              |  
|--------------|------------------------------------|----------|--------------------|  
| Schema ID    | ^p12_wn_[a-z][a-z0-9_]+.md$       | matches  | All workflow_node files |  

## HARD Gates  
(Table: ID | Check | Fail Condition)  
| ID      | Check                          | Fail Condition                                      |  
|---------|--------------------------------|-----------------------------------------------------|  
| H01     | YAML frontmatter valid         | Invalid YAML syntax or missing frontmatter          |  
| H02     | ID matches ^p12_wn_[a-z][a-z0-9_]+.md$ | ID does not match required schema pattern         |  
| H03     | kind field matches 'workflow_node' | kind is not 'workflow_node'                        |  
| H04     | 'name' field present           | Missing 'name' field                               |  
| H05     | 'inputs' and 'outputs' defined | Missing 'inputs' or 'outputs'                      |  
| H06     | 'type' field valid             | 'type' not in [trigger, processor, decision]       |  
| H07     | 'description' field present    | Missing 'description'                              |  
| H08     | Unique node ID in workflow     | Duplicate node ID detected                         |  

## SOFT Scoring  
(Table: Dim | Dimension | Weight | Scoring Guide)  
| Dim | Dimension         | Weight | Scoring Guide                                      |  
|-----|-------------------|--------|----------------------------------------------------|  
| D1  | Code Quality      | 0.15   | Clean, readable code; no syntax errors             |  
| D2  | Documentation     | 0.10   | Complete and accurate 'description' field          |  
| D3  | Input/Output      | 0.15   | Valid, non-ambiguous 'inputs'/'outputs'            |  
| D4  | Error Handling    | 0.10   | Robust error handling for edge cases               |  
| D5  | Performance       | 0.10   | Efficient execution, minimal latency               |  
| D6  | Maintainability   | 0.10   | Modular design, clear separation of concerns       |  
| D7  | Test Coverage     | 0.10   | Unit/integration tests cover >80% of logic         |  
| D8  | Type Safety       | 0.10   | Strong typing enforced for inputs/outputs          |  

## Actions  
(Table: Score | Action)  
| Score      | Action                                      |  
|------------|---------------------------------------------|  
| GOLDEN     | Auto-approve and deploy                     |  
| PUBLISH    | Manual review required before deployment    |  
| REVIEW     | Flag for technical lead review              |  
| REJECT     | Reject; fix all HARD/Gate failures          |  

## Bypass  
(Table: conditions, approver, audit trail)  
| Conditions              | Approver         | Audit Trail                              |  
|-------------------------|------------------|------------------------------------------|  
| Emergency workflow fix  | Lead Architect   | Bypass logged with justification and date |
