---
kind: instruction
id: bld_instruction_discovery_questions
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for discovery_questions
quality: 8.9
title: "Instruction Discovery Questions"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [discovery_questions, builder, instruction]
tldr: "Step-by-step production process for discovery_questions"
domain: "discovery_questions construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_discovery_questions_builder
  - p10_mem_discovery_questions_builder
  - discovery-questions-builder
  - bld_knowledge_card_discovery_questions
  - p01_qg_discovery_questions
  - bld_examples_discovery_questions
  - bld_output_template_discovery_questions
  - bld_instruction_sales_playbook
  - kc_discovery_questions
  - p03_sp_sales_playbook_builder
---

## Phase 1: RESEARCH  
1. Map buyer personas (e.g., CFO, IT director) using company data and role-specific pain points.  
2. Identify deal stages (e.g., Needs Analysis, Solution Demo) and align with MEDDIC/BANT criteria.  
3. Analyze buyer journey maps to pinpoint decision-making triggers and objections per persona.  
4. Review existing sales content (e.g., case studies, proposals) for recurring questions and gaps.  
5. Interview 3–5 stakeholders per persona to validate pain points and decision drivers.  
6. Compile research into a structured dataset with persona, stage, and question categories.  

## Phase 2: COMPOSE  
1. Use bld_schema_discovery_questions.md to define artifact structure: persona, stage, question, intent (MEDDIC/BANT), and response type.  
2. Reference bld_output_template_discovery_questions.md for formatting: headers, bullet points, and alignment with sales playbooks.  
3. Write open-ended questions targeting persona-specific challenges (e.g., “What metrics define success for your team?”).  
4. Ensure each question maps to a MEDDIC/BANT criterion (e.g., Budget, Authority, Need).  
5. Group questions by deal stage, prioritizing early-stage questions for qualification.  
6. Use concise, jargon-free language; avoid yes/no questions unless explicitly required.  
7. Categorize questions by intent (e.g., “What’s your current solution?” for Need, “Who approves purchases?” for Authority).  
8. Cross-check against research data to ensure coverage of all personas and stages.  
9. Finalize artifact with metadata (e.g., version, author, last reviewed date).  

## Phase 3: VALIDATE  
- [ ] Confirm alignment with bld_schema_discovery_questions.md and bld_output_template_discovery_questions.md structure.  
- [ ] Verify 100% coverage of personas and deal stages in the artifact.  
- [ ] Test questions with 2–3 stakeholders for clarity and relevance.  
- [ ] Ensure MEDDIC/BANT criteria are explicitly addressed in question intent.  
- [ ] Obtain approval from sales leadership and subject-matter experts.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_discovery_questions_builder]] | related | 0.50 |
| [[p10_mem_discovery_questions_builder]] | downstream | 0.46 |
| [[discovery-questions-builder]] | upstream | 0.45 |
| [[bld_knowledge_card_discovery_questions]] | upstream | 0.41 |
| [[p01_qg_discovery_questions]] | downstream | 0.35 |
| [[bld_examples_discovery_questions]] | downstream | 0.34 |
| [[bld_output_template_discovery_questions]] | downstream | 0.31 |
| [[bld_instruction_sales_playbook]] | sibling | 0.30 |
| [[kc_discovery_questions]] | upstream | 0.29 |
| [[p03_sp_sales_playbook_builder]] | related | 0.29 |
