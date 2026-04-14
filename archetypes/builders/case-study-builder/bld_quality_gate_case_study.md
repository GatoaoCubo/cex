---
kind: quality_gate
id: p05_qg_case_study
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for case_study
quality: null
title: "Quality Gate Case Study"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [case_study, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for case_study"
domain: "case_study construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
| metric | threshold | operator | scope |  
|---|---|---|---|  
| ID | ^p05_cs_[a-z][a-z0-9_]+.md$ | matches | H02 |  

## HARD Gates  
| ID | Check | Fail Condition |  
|---|---|---|  
| H01 | YAML frontmatter valid | invalid YAML |  
| H02 | ID matches pattern ^p05_cs_[a-z][a-z0-9_]+.md$ | invalid schema ID |  
| H03 | kind field matches 'case_study' | incorrect kind |  
| H04 | Challenge section present | missing challenge |  
| H05 | Solution section present | missing solution |  
| H06 | Outcome section present | missing outcome |  
| H07 | Customer quote present | missing quote |  

## SOFT Scoring  
| Dim | Dimension | Weight | Scoring Guide |  
|---|---|---|---|  
| 1 | Narrative structure | 0.15 | Clear challenge/solution/outcome flow |  
| 2 | Clarity | 0.15 | Concise, jargon-free language |  
| 3 | Customer quote | 0.15 | Direct, attributable quote |  
| 4 | Relevance | 0.15 | Aligns with CEX use case |  
| 5 | Uniqueness | 0.10 | Distinct from other case studies |  
| 6 | Formatting | 0.10 | Proper headers, bullet points |  
| 7 | Engagement | 0.10 | Compelling story, emotional impact |  
| 8 | Data accuracy | 0.10 | Verified metrics, sources cited |  

## Actions  
| Score | Action |  
|---|---|  
| GOLDEN | >=9.5 | Highlight as exemplar |  
| PUBLISH | >=8.0 | Deploy to public repo |  
| REVIEW | >=7.0 | Request minor edits |  
| REJECT | <7.0 | Discard, rework required |  

## Bypass  
| conditions | approver | audit trail |  
|---|---|---|  
| Strategic customer request | CTO | Note in audit log |
