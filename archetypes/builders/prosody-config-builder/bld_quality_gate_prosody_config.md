---
kind: quality_gate
id: p09_qg_prosody_config
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for prosody_config
quality: null
title: "Quality Gate Prosody Config"
version: "1.0.0"
author: wave1_builder_gen
tags: [prosody_config, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for prosody_config"
domain: "prosody_config construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Definition  
| metric         | threshold      | operator | scope         |  
|----------------|----------------|----------|---------------|  
| prosody_config | must exist     | exists   | each config file |  

## HARD Gates  
| ID   | Check                  | Fail Condition                          |  
|------|------------------------|-----------------------------------------|  
| H01  | YAML valid             | Invalid YAML syntax                     |  
| H02  | ID matches pattern     | ID does not match `^[a-zA-Z0-9_]+$`   |  
| H03  | kind matches           | kind is not `prosody_config`          |  
| H04  | voice_personality exists | Missing voice_personality field       |  
| H05  | emotion_settings valid | Emotion values not in allowed list    |  
| H06  | no duplicate IDs       | Duplicate ID detected                 |  
| H07  | config not empty       | Empty or whitespace-only config       |  

## SOFT Scoring  
| Dim | Dimension              | Weight | Scoring Guide                              |  
|-----|------------------------|--------|--------------------------------------------|  
| D1  | Voice personality      | 0.15   | 1.0=clear, 0.5=ambiguous, 0.0=missing      |  
| D2  | Emotion settings       | 0.15   | 1.0=valid, 0.5=partial, 0.0=invalid        |  
| D3  | Consistency            | 0.10   | 1.0=consistent, 0.5=conflicting, 0.0=invalid|  
| D4  | Clarity                | 0.10   | 1.0=explicit, 0.5=moderate, 0.0=obscure    |  
| D5  | Naturalness            | 0.10   | 1.0=natural, 0.5=stiff, 0.0=mechanical     |  
| D6  | Cultural appropriateness | 0.10 | 1.0=appropriate, 0.5=neutral, 0.0=inappropriate |  
| D7  | Technical validity     | 0.10   | 1.0=valid, 0.5=partial, 0.0=invalid        |  
| D8  | User experience        | 0.10   | 1.0=optimal, 0.5=adequate, 0.0=poor        |  

## Actions  
| Score     | Action                          |  
|-----------|---------------------------------|  
| GOLDEN    | Auto-approve, deploy immediately|  
| PUBLISH   | Manual review, schedule deploy  |  
| REVIEW    | Flag for stakeholder feedback   |  
| REJECT    | Block, require rework           |  

## Bypass  
| conditions                          | approver              | audit trail         |  
|------------------------------------|-----------------------|---------------------|  
| Urgent release required            | Senior Product Manager| JIRA-12345          |  
| Legacy system compatibility override | CTO                 | SLA-6789            |
