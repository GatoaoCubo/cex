---
kind: quality_gate
id: p03_qg_prompt_optimizer
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for prompt_optimizer
quality: null
title: "Quality Gate Prompt Optimizer"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_optimizer, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for prompt_optimizer"
domain: "prompt_optimizer construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
(Table: metric, threshold, operator, scope)  
| metric         | threshold | operator | scope        |  
|----------------|-----------|----------|--------------|  
| accuracy       | 95%       | >=       | system-wide  |  
| compilation    | 99%       | >=       | per-user     |  
| response_time  | 200ms     | <=       | system-wide  |  
| error_rate     | 0.1%      | <=       | per-user     |  

## HARD Gates  
(Table: ID | Check | Fail Condition)  
| ID           | Check                          | Fail Condition                                      |  
|--------------|--------------------------------|-----------------------------------------------------|  
| H01          | YAML frontmatter valid         | Invalid YAML syntax or missing fields               |  
| H02          | ID matches ^p03_po_[a-z][a-z0-9_]+.md$ | ID does not conform to schema pattern             |  
| H03          | kind field matches 'prompt_optimizer' | kind field is incorrect or missing                |  
| H04          | Prompt validation rules defined | No validation rules for input/output formats      |  
| H05          | Optimization efficiency >= 80% | Optimization efficiency below threshold           |  
| H06          | Error handling covers 100% cases | Missing error handling for critical scenarios     |  
| H07          | Compatibility with 3+ models   | Fails to compile prompts for required models      |  

## SOFT Scoring  
(Table: Dim | Dimension | Weight | Scoring Guide)  
| Dim | Dimension         | Weight | Scoring Guide                                      |  
|-----|-------------------|--------|----------------------------------------------------|  
| D1  | Accuracy          | 0.15   | 100% = 1.0, 90% = 0.9, 80% = 0.8                    |  
| D2  | Efficiency        | 0.12   | 100% = 1.0, 80% = 0.8, 60% = 0.6                    |  
| D3  | Usability         | 0.10   | 5-star = 1.0, 4-star = 0.8, 3-star = 0.6           |  
| D4  | Security          | 0.10   | No vulnerabilities = 1.0, 1+ critical = 0.0         |  
| D5  | Compatibility     | 0.10   | 100% models = 1.0, 80% = 0.8, 60% = 0.6            |  
| D6  | Scalability       | 0.10   | Handles 1M+ prompts = 1.0, 100k = 0.8, 10k = 0.6   |  
| D7  | User feedback     | 0.10   | 90% satisfaction = 1.0, 70% = 0.8, 50% = 0.6       |  
| D8  | Innovation        | 0.13   | Novel features = 1.0, standard = 0.8, minimal = 0.6 |  

## Actions  
(Table: Score | Action)  
| Score      | Action                          |  
|------------|---------------------------------|  
| GOLDEN     | Automate deployment             |  
| PUBLISH    | Deploy with monitoring          |  
| REVIEW     | Manual review required          |  
| REJECT     | Reject and request revisions    |  

## Bypass  
(Table: conditions, approver, audit trail)  
| conditions                  | approver   | audit trail                          |  
|-----------------------------|------------|--------------------------------------|  
| Security exception approved | CTO        | Signed approval + timestamp          |  
| Legacy system compatibility | CTO        | Signed approval + timestamp          |  
| Experimental feature        | CTO        | Signed approval + timestamp          |
