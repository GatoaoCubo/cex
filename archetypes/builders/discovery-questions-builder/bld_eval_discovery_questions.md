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
related:
  - bld_examples_discovery_questions
  - p10_mem_discovery_questions_builder
  - bld_instruction_discovery_questions
  - discovery-questions-builder
  - p03_sp_discovery_questions_builder
  - bld_knowledge_card_discovery_questions
  - kc_discovery_questions
  - p02_qg_customer_segment
  - p03_qg_prompt_technique
  - p07_qg_eval_metric
---

## Quality Gate

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

## Examples

## Golden Example
---
title: "Discovery Questions for Mid-Market SaaS Buyer (Deal Stage: Needs Analysis)"
persona: "IT Director at a mid-sized healthcare provider"
deal_stage: "Needs Analysis"
questions:
  - "What are your current challenges with patient data management in compliance with HIPAA regulations?"
  - "How many hours per week does your IT team spend manually reconciling data across systems?"
  - "What specific KPIs would you use to measure success if we implemented a cloud-based EHR solution?"
  - "Who are the key stakeholders involved in evaluating new healthcare IT solutions?"
  - "What is your current annual budget allocation for digital transformation initiatives?"

---
## Anti-Example 1: Vague and Broad Questions
questions:
  - "What are your goals for the next year?"
  - "How do you see technology impacting your business?"
  - "What challenges are you facing?"
## Why it fails: Questions lack specificity to the buyer persona (e.g., "IT Director") and deal stage (e.g., "Needs Analysis"). They are too generic to uncover actionable insights about HIPAA compliance or EHR implementation needs.

## Anti-Example 2: Sales Playbook Content
questions:
  - "Our solution reduces manual data entry by 70% – would that interest you?"
  - "We offer 24/7 support – how important is uptime to your operations?"
  - "Our competitors charge 3x more – are you looking for cost savings?"
## Why it fails: These are sales pitches disguised as discovery questions. They assume product knowledge rather than uncovering the buyer's needs, violating the MEDDIC/BANT principle of focusing on the customer's situation.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
