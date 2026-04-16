---
kind: instruction
id: bld_instruction_faq_entry
pillar: P03
llm_function: REASON
purpose: Step-by-step production process for faq_entry
quality: 8.9
title: "Instruction Faq Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [faq_entry, builder, instruction]
tldr: "Step-by-step production process for faq_entry"
domain: "faq_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Phase 1: RESEARCH  
1. Identify high-frequency customer inquiries from support tickets.  
2. Analyze existing FAQs to avoid duplication and ensure coverage.  
3. Determine support deflection metric (e.g., % of resolved cases via this entry).  
4. Interview subject matter experts for accurate canonical answer content.  
5. Collect relevant internal links (KB articles, product docs, community forums).  
6. Verify compliance with company policies and legal requirements.  

## Phase 2: COMPOSE  
1. Outline structure: question, answer, related_topics, metric (per bld_schema_faq_entry.md).  
2. Draft question using active voice, avoiding jargon.  
3. Write canonical answer with step-by-step guidance (max 3 paragraphs, <=150 words).  
4. Embed hyperlinked references to related resources (validate URLs).  
5. Calculate support deflection metric using historical resolution data.  
6. Apply bld_output_template_faq_entry.md formatting for consistency.  
7. Add Schema.org FAQPage structured data snippet for rich-results eligibility.  
8. Review for clarity, conciseness, and alignment with brand tone.  
9. Finalize artifact with metadata (author, date, version).  

## Phase 3: VALIDATE  
- [ ] All required fields (question, answer, related_topics, metric) present per bld_schema_faq_entry.md.  
- [ ] Answer resolves issue without ambiguity or missing steps.  
- [ ] Schema.org FAQPage snippet included in output template.  
- [ ] Support deflection metric is accurate and up-to-date.  
- [ ] Artifact adheres to bld_schema_faq_entry.md and bld_output_template_faq_entry.md specs.
