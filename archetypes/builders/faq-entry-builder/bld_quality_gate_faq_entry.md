---
kind: quality_gate
id: p01_qg_faq_entry
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for faq_entry
quality: null
title: "Quality Gate Faq Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [faq_entry, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for faq_entry"
domain: "faq_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
(metric | threshold | operator | scope)  
support_deflection_metric | 20% | > | per entry  

## HARD Gates  
(ID | Check | Fail Condition)  
H01 | YAML frontmatter valid | invalid YAML  
H02 | ID matches ^p01_faq_[a-z][a-z0-9_]+.md$ | invalid pattern  
H03 | kind field matches 'faq_entry' | incorrect kind  
H04 | question field exists and is non-empty | missing or empty question  
H05 | canonical answer exists and is non-empty | missing or empty answer  
H06 | related_links are valid URLs | invalid or missing URLs  
H07 | support_deflection_metric is numeric | non-numeric value  
H08 | no duplicate questions in same document | duplicate question found  

## SOFT Scoring  
(Dim | Dimension | Weight | Scoring Guide)  
Clarity | Question phrasing | 0.15 | Clear, concise, user-focused  
Completeness | Answer covers all aspects | 0.15 | Full resolution, no ambiguity  
Usability | Links and formatting | 0.10 | Valid links, proper markdown  
Accuracy | Factually correct | 0.15 | Aligned with policies/operations  
Consistency | Tone and style | 0.10 | Matches brand guidelines  
Support Deflection | Metric relevance | 0.15 | Directly ties to support reduction  
Accessibility | Language simplicity | 0.10 | Avoids jargon, plain English  
Formatting | Adheres to schema | 0.10 | Correct structure, no errors  

## Actions  
(Score | Action)  
GOLDEN | >=9.5 | Auto-publish, no review  
PUBLISH | >=8.0 | Publish after approval  
REVIEW | >=7.0 | Require editorial review  
REJECT | <7.0 | Reject, rework required  

## Bypass  
(conditions | approver | audit trail)  
Urgent support fix | Senior Editor | Ticket #12345  
Legacy entry update | Product Manager | Change log v2.1
