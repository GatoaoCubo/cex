---
kind: quality_gate
id: p09_qg_vad_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for vad_config
quality: null
title: "Quality Gate Vad Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [vad_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for vad_config"
domain: "vad_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  
| metric       | threshold | operator | scope  |  
|--------------|-----------|----------|--------|  
| sensitivity  | 0.7       | >=       | global |  
| threshold    | 0.3       | <=       | per-channel |  
| operator     | valid     | in       | all    |  

## HARD Gates  
| ID   | Check               | Fail Condition                          |  
|------|---------------------|-----------------------------------------|  
| H01  | YAML valid          | Invalid YAML syntax                     |  
| H02  | ID matches pattern  | ID does not match `vad_\d+`            |  
| H03  | kind matches        | kind != `vad_config`                   |  
| H04  | sensitivity range   | sensitivity < 0.5 or > 1.0            |  
| H05  | threshold range     | threshold < 0.1 or > 0.5              |  
| H06  | operator validity   | operator not in [‘>=’, ‘<=’, ‘==’]     |  
| H07  | scope validity      | scope not in [‘global’, ‘per-channel’] |  

## SOFT Scoring  
| Dim | Dimension         | Weight | Scoring Guide                          |  
|-----|-------------------|--------|----------------------------------------|  
| D1  | YAML structure    | 0.15   | 1.0 if valid, 0.5 if partial, 0 otherwise |  
| D2  | sensitivity       | 0.10   | 1.0 if 0.7–1.0, 0.5 if 0.5–0.7, 0 otherwise |  
| D3  | threshold         | 0.10   | 1.0 if 0.1–0.3, 0.5 if 0.3–0.5, 0 otherwise |  
| D4  | operator validity | 0.15   | 1.0 if valid, 0.5 if invalid, 0 otherwise |  
| D5  | scope validity    | 0.10   | 1.0 if valid, 0.5 if invalid, 0 otherwise |  
| D6  | uniqueness        | 0.10   | 1.0 if ID unique, 0.5 if duplicate, 0 otherwise |  
| D7  | documentation     | 0.10   | 1.0 if comments present, 0.5 if missing |  
| D8  | compliance        | 0.20   | 1.0 if meets all HARD gates, 0.5 if partial |  

## Actions  
| Score     | Action                          |  
|-----------|---------------------------------|  
| GOLDEN    | >=9.5: No action required       |  
| PUBLISH   | >=8.0: Auto-publish             |  
| REVIEW    | >=7.0: Require manual review    |  
| REJECT    | <7.0: Reject and rework         |  

## Bypass  
| conditions                        | approver | audit trail         |  
|----------------------------------|----------|---------------------|  
| Critical production outage       | CTO      | Ticket #VAD-2023-01 |  
| Emergency configuration fix      | CTO      | Ticket #VAD-2023-02 |  
| Approved by QA for A/B testing   | QA Lead  | Ticket #VAD-2023-03 |
