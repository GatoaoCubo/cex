---
kind: quality_gate
id: p05_qg_pitch_deck
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for pitch_deck
quality: 8.9
title: "Quality Gate Pitch Deck"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [pitch_deck, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for pitch_deck"
domain: "pitch_deck construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
(Table: metric, threshold, operator, scope)  
metric | threshold | operator | scope  
--- | --- | --- | ---  
Presence of required slides | All slides present | must have | entire document  

## HARD Gates  
(Table: ID | Check | Fail Condition)  
ID | Check | Fail Condition  
--- | --- | ---  
H01 | YAML frontmatter valid | invalid YAML syntax or missing fields  
H02 | ID matches pattern ^p05_pd_[a-z][a-z0-9_]+.md$ | invalid filename format  
H03 | kind field matches 'pitch_deck' | incorrect or missing kind value  
H04 | Problem slide present | missing problem/solution slide  
H05 | Solution slide present | missing problem/solution slide  
H06 | Traction slide includes metrics | no quantitative data in traction section  
H07 | Ask slide specifies funding amount | vague or missing funding request  
H08 | Target audience clearly defined | ambiguous or missing audience description  

## SOFT Scoring  
(Table: Dim | Dimension | Weight | Scoring Guide)  
Dim | Dimension | Weight | Scoring Guide  
--- | --- | --- | ---  
D01 | Clarity of value proposition | 0.15 | 0.0-1.0 based on readability and impact  
D02 | Slide structure consistency | 0.15 | 0.0-1.0 based on adherence to problem/solution/traction/ask  
D03 | Data quality in traction | 0.15 | 0.0-1.0 based on relevance and completeness  
D04 | Visual appeal | 0.10 | 0.0-1.0 based on design and readability  
D05 | Roadmap feasibility | 0.10 | 0.0-1.0 based on logical progression  
D06 | Ask alignment with traction | 0.10 | 0.0-1.0 based on logical funding request  
D07 | Audience specificity | 0.10 | 0.0-1.0 based on targeted market fit  
D08 | Conciseness | 0.15 | 0.0-1.0 based on brevity and focus  

## Actions  
(Table: Score | Action)  
Score | Action  
--- | ---  
GOLDEN (>=9.5) | Direct approval for presentation  
PUBLISH (>=8.0) | Ready for external sharing  
REVIEW (>=7.0) | Requires minor edits before use  
REJECT (<7.0) | Needs major revisions  

## Bypass  
(Table: conditions, approver, audit trail)  
conditions | approver | audit trail  
--- | --- | ---  
CEO override | CTO | signed approval document, timestamped log
