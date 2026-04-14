---
kind: quality_gate
id: p07_qg_eval_framework
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for eval_framework
quality: null
title: "Quality Gate Eval Framework"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [eval_framework, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for eval_framework"
domain: "eval_framework construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
| metric                | threshold | operator | scope        |  
|-----------------------|-----------|----------|--------------|  
| Test coverage         | 95%       | >=       | system       |  
| Integration completeness | 100%   | ==       | framework    |  
| Performance latency   | 200ms     | <=       | API endpoint |  

## HARD Gates  
| ID                  | Check                          | Fail Condition                                      |  
|---------------------|--------------------------------|-----------------------------------------------------|  
| H01                 | YAML frontmatter valid         | Invalid or missing frontmatter                      |  
| H02                 | ID matches pattern             | ID does not match ^p07_efw_[a-z][a-z0-9_]+.md$     |  
| H03                 | kind field matches 'eval_framework' | kind field is not 'eval_framework'               |  
| H04                 | Required fields present        | Missing 'metrics' or 'validation_rules'            |  
| H05                 | Compatibility with CEX API     | Incompatible with v2.1+ API spec                   |  
| H06                 | Error handling completeness    | < 90% of edge cases covered                        |  
| H07                 | Test suite coverage            | < 80% of framework components tested               |  

## SOFT Scoring  
| Dim | Dimension            | Weight | Scoring Guide                                  |  
|-----|----------------------|--------|------------------------------------------------|  
| D1  | Test coverage        | 0.15   | 100% = 1.0, 80% = 0.8                          |  
| D2  | Integration completeness | 0.15 | 100% = 1.0, 70% = 0.7                          |  
| D3  | Documentation quality  | 0.10   | 100% = 1.0, 60% = 0.6                          |  
| D4  | Performance latency    | 0.10   | 200ms = 1.0, 300ms = 0.5                       |  
| D5  | Error handling         | 0.10   | 100% = 1.0, 70% = 0.7                          |  
| D6  | Scalability            | 0.10   | 10k TPS = 1.0, 5k TPS = 0.5                    |  
| D7  | Maintainability        | 0.10   | 100% = 1.0, 60% = 0.6                          |  
| D8  | Tooling integration    | 0.05   | 100% = 1.0, 70% = 0.7                          |  

## Actions  
| Score     | Action                          |  
|-----------|---------------------------------|  
| GOLDEN    | Approve and deploy              |  
| PUBLISH   | Publish with peer review        |  
| REVIEW    | Request engineering review      |  
| REJECT    | Reject and rework required      |  

## Bypass  
| conditions                | approver | audit trail                          |  
|---------------------------|----------|--------------------------------------|  
| Urgent production release | CTO      | Bypassed due to critical deadline    |
