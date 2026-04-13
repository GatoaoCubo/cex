---
kind: quality_gate
id: p09_qg_thinking_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for thinking_config
quality: null
title: "Quality Gate Thinking Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [thinking_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for thinking_config"
domain: "thinking_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  
| metric                | threshold       | operator | scope        |  
|-----------------------|-----------------|----------|--------------|  
| Thinking Duration     | >= 10s, <= 60s  | between  | config.yaml  |  
| Budget Token Alloc    | >= 1%, <= 50%   | between  | config.yaml  |  

## HARD Gates  
| ID   | Check               | Fail Condition                          |  
|------|---------------------|-----------------------------------------|  
| H01  | YAML valid          | Invalid YAML syntax                     |  
| H02  | ID matches pattern  | ID does not match `^T[0-9]{4}$`        |  
| H03  | kind matches        | kind != `thinking_config`               |  
| H04  | Required fields     | Missing `thinking_duration` or `budget` |  
| H05  | Token alloc range   | Budget <1% or >50%                      |  
| H06  | Duration range      | Thinking <10s or >60s                  |  
| H07  | No duplicate IDs    | Duplicate ID in config                  |  

## SOFT Scoring  
| Dim | Dimension           | Weight | Scoring Guide                          |  
|-----|---------------------|--------|----------------------------------------|  
| D01 | YAML syntax         | 0.15   | 1.0 if valid, 0.0 if invalid           |  
| D02 | ID pattern          | 0.10   | 1.0 if matches, 0.0 if invalid         |  
| D03 | Kind validity       | 0.10   | 1.0 if correct, 0.0 if incorrect       |  
| D04 | Required fields     | 0.15   | 1.0 if present, 0.0 if missing         |  
| D05 | Token allocation    | 0.15   | 1.0 if within range, 0.0 if outside    |  
| D06 | Duration validity   | 0.10   | 1.0 if valid, 0.0 if invalid           |  
| D07 | Comments            | 0.10   | 1.0 if present, 0.5 if missing         |  
| D08 | Documentation       | 0.15   | 1.0 if complete, 0.0 if incomplete     |  

## Actions  
| Score   | Action                          |  
|---------|-------------------------------|  
| >=9.5   | GOLDEN: Auto-approve            |  
| >=8.0   | PUBLISH: Deploy to production   |  
| >=7.0   | REVIEW: Manual review required  |  
| <7.0    | REJECT: Fix and resubmit        |  

## Bypass  
| conditions                          | approver | audit trail              |  
|-----------------------------------|----------|--------------------------|  
| Critical system override          | CTO      | Bypass logged with reason|
