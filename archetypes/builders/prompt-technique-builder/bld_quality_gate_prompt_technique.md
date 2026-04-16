---
kind: quality_gate
id: p03_qg_prompt_technique
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for prompt_technique
quality: 9.1
title: "Quality Gate Prompt Technique"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [prompt_technique, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for prompt_technique"
domain: "prompt_technique construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
(Table: metric, threshold, operator, scope)  
| metric         | threshold              | operator | scope                  |  
|----------------|------------------------|----------|------------------------|  
| Prompt Pattern | ^p03_pt_[a-z][a-z0-9_]+.md$ | matches  | Schema ID (H02)        |  

## HARD Gates  
(Table: ID | Check | Fail Condition)  
| ID      | Check                          | Fail Condition                                      |  
|---------|--------------------------------|-----------------------------------------------------|  
| H01     | YAML frontmatter valid         | Invalid YAML syntax or missing required fields      |  
| H02     | ID matches pattern             | ID does not match ^p03_pt_[a-z][a-z0-9_]+.md$      |  
| H03     | kind field matches 'prompt_technique' | kind field is not 'prompt_technique'              |  
| H04     | Prompt technique is unique     | Duplicate technique ID or name detected             |  
| H05     | Description is non-empty       | Description field is missing or blank               |  
| H06     | No harmful patterns detected   | Contains banned keywords or unsafe templates        |  
| H07     | Example usage provided         | No example usage or example is incomplete           |  

## SOFT Scoring  
(Table: Dim | Dimension | Weight | Scoring Guide)  
| Dim | Dimension         | Weight | Scoring Guide                                                                 |  
|-----|-------------------|--------|-------------------------------------------------------------------------------|  
| D1  | Clarity           | 0.15   | Clear, concise, and actionable (1.0) vs. vague (0.0)                         |  
| D2  | Originality       | 0.15   | Novel approach (1.0) vs. derivative or generic (0.0)                         |  
| D3  | Alignment         | 0.15   | Fully aligns with CEX guidelines (1.0) vs. partial or no alignment (0.0)     |  
| D4  | Safety            | 0.15   | No risks identified (1.0) vs. moderate/high risks (0.0)                      |  
| D5  | Formatting        | 0.10   | Adheres to schema (1.0) vs. formatting errors (0.0)                          |  
| D6  | Example Quality   | 0.15   | Realistic, complete example (1.0) vs. placeholder or missing (0.0)           |  
| D7  | Adaptability      | 0.15   | Works across use cases (1.0) vs. limited scope (0.0)                         |  

## Actions  
(Table: Score | Action)  
| Score      | Action                          |  
|------------|---------------------------------|  
| GOLDEN     | Auto-publish and archive        |  
| PUBLISH    | Manual review by domain expert  |  
| REVIEW     | Flag for stakeholder feedback   |  
| REJECT     | Reject and require rework       |  

## Bypass  
(Table: conditions, approver, audit trail)  
| conditions                          | approver         | audit trail                          |  
|-----------------------------------|------------------|--------------------------------------|  
| Exception for experimental use    | Senior Engineer  | Note in audit trail with justification |
