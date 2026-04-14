---
kind: quality_gate
id: p05_qg_course_module
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for course_module
quality: null
title: "Quality Gate Course Module"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [course_module, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for course_module"
domain: "course_module construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Definition  
| metric               | threshold | operator | scope         |  
|----------------------|-----------|----------|---------------|  
| Completion Rate      | 85%       | >=       | Course Module |  
| Assessment Pass Rate | 75%       | >=       | Course Module |  
| Engagement Time      | 15 min    | >=       | Per Lesson    |  

## HARD Gates  
| ID   | Check                     | Fail Condition                              |  
|------|---------------------------|---------------------------------------------|  
| H01  | YAML frontmatter valid    | Invalid or missing YAML frontmatter         |  
| H02  | ID matches pattern        | ID does not match ^p05_cm_[a-z][a-z0-9_]+.md$ |  
| H03  | kind field matches 'course_module' | kind field not 'course_module'        |  
| H04  | Learning objectives present | Missing or incomplete learning objectives |  
| H05  | Assessments included      | No formative or summative assessments       |  
| H06  | Content length >= 10 min  | Content duration < 10 minutes               |  
| H07  | Accessibility compliance  | Missing captions or screen reader support   |  

## SOFT Scoring  
| Dim | Dimension               | Weight | Scoring Guide                          |  
|-----|-------------------------|--------|----------------------------------------|  
| D01 | Learning Objectives Clarity | 0.15   | Clear, measurable, aligned to outcomes |  
| D02 | Assessment Alignment    | 0.15   | Assessments match learning objectives  |  
| D03 | Content Quality         | 0.20   | Accurate, engaging, up-to-date         |  
| D04 | Engagement Design       | 0.10   | Interactive elements, pacing           |  
| D05 | Accessibility           | 0.10   | WCAG compliance, inclusive design      |  
| D06 | Multimedia Use          | 0.10   | Relevant videos, diagrams, audio       |  
| D07 | Peer Review Feedback    | 0.10   | Incorporates reviewer suggestions       |  
| D08 | Feedback Mechanism      | 0.10   | Includes learner feedback channels     |  

## Actions  
| Score     | Action                   |  
|-----------|--------------------------|  
| GOLDEN    | Approve for publication  |  
| PUBLISH   | Publish with minor edits |  
| REVIEW    | Request revisions        |  
| REJECT    | Reject and rework        |  

## Bypass  
| conditions                          | approver       | audit trail                   |  
|-------------------------------------|----------------|-------------------------------|  
| Urgent release required by business | Senior Manager | Documented in change log      |
