---
kind: quality_gate
id: p03_qg_sales_playbook
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for sales_playbook
quality: null
title: "Quality Gate Sales Playbook"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [sales_playbook, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for sales_playbook"
domain: "sales_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
| metric | threshold | operator | scope |  
|---|---|---|---|  
| completeness | 100% | >= | all sections |  
| alignment | strategy | 1:1 | company goals |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML frontmatter valid | invalid YAML |  
| H02 | ID matches ^p03_sp_[a-z][a-z0-9_]+.md$ | invalid ID pattern |  
| H03 | kind field matches 'sales_playbook' | incorrect kind |  
| H04 | personas section present | missing personas |  
| H05 | discovery flow structured | unstructured flow |  
| H06 | objection handling strategies | missing strategies |  
| H07 | close patterns documented | missing patterns |  
| H08 | aligned with company strategy | misalignment detected |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| D01 | Clarity | 0.15 | 1-5 (readability) |  
| D02 | Completeness | 0.20 | 1-5 (coverage) |  
| D03 | Alignment | 0.15 | 1-5 (strategy match) |  
| D04 | Practicality | 0.15 | 1-5 (actionable steps) |  
| D05 | Objection depth | 0.10 | 1-5 (coverage) |  
| D06 | Close effectiveness | 0.10 | 1-5 (conversion) |  
| D07 | Versioning | 0.10 | 1-5 (tracking) |  
| D08 | Stakeholder feedback | 0.15 | 1-5 (approval) |  

## Actions  
| Score | Action |  
|---|---|  
| >=9.5 | GOLDEN |  
| >=8.0 | PUBLISH |  
| >=7.0 | REVIEW |  
| <7.0 | REJECT |  

## Bypass  
| conditions | approver | audit trail |  
|---|---|---|  
| executive approval | CTO | documented |
