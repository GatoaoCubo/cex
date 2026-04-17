---
kind: quality_gate
id: p01_qg_discovery_questions
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for discovery_questions
quality: 8.9
title: "Quality Gate Discovery Questions"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [discovery_questions, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for discovery_questions"
domain: "discovery_questions construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
(Table: metric, threshold, operator, scope)  
metric | threshold | operator | scope  
--- | --- | --- | ---  
Completeness | 100% | >= | All buyer personas and deal stages  

## HARD Gates  
(Table: ID | Check | Fail Condition)  
H01 | YAML frontmatter valid | Invalid YAML syntax  
H02 | ID matches pattern ^p01_dq_[a-z][a-z0-9_]+.md$ | Invalid schema ID format  
H03 | kind field matches 'discovery_questions' | Incorrect kind value  
H04 | Questions grouped by buyer persona | Missing persona-specific categorization  
H05 | Deal stage alignment present | No stage-specific questions  
H06 | At least 3 question types (e.g., value, pain, budget) | <3 question types  
H07 | No duplicate questions across personas | Duplicates detected  
H08 | Questions avoid leading bias | Leading language present  

## SOFT Scoring  
(Table: Dim | Dimension | Weight | Scoring Guide)  
Dim | Dimension | Weight | Scoring Guide  
--- | --- | --- | ---  
D1 | Relevance to persona | 0.20 | 1.0 (fully aligned) to 0.0 (irrelevant)  
D2 | Coverage of deal stages | 0.15 | 1.0 (all stages) to 0.0 (none)  
D3 | Clarity of questions | 0.15 | 1.0 (unambiguous) to 0.0 (vague)  
D4 | Depth of insight | 0.15 | 1.0 (high value) to 0.0 (superficial)  
D5 | Question type diversity | 0.10 | 1.0 (3+ types) to 0.0 (<2 types)  
D6 | Language neutrality | 0.10 | 1.0 (neutral) to 0.0 (biased)  
D7 | Actionability | 0.10 | 1.0 (drives next steps) to 0.0 (non-actionable)  
D8 | Consistency across personas | 0.05 | 1.0 (consistent) to 0.0 (inconsistent)  

## Actions  
(Table: Score | Action)  
Score | Action  
--- | ---  
GOLDEN >=9.5 | Auto-approve and flag for excellence  
PUBLISH >=8.0 | Approve for use  
REVIEW >=7.0 | Flag for review by SME  
REJECT <7.0 | Reject and require rewrite  

## Bypass  
(Table: conditions, approver, audit trail)  
conditions | approver | audit trail  
--- | --- | ---  
Emergency release | CTO | Requires written justification and timestamp
