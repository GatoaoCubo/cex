---
kind: knowledge_card
id: bld_knowledge_card_faq_entry
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for faq_entry production
quality: 9.2
title: "Knowledge Card Faq Entry"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [faq_entry, builder, knowledge_card]
tldr: "Domain knowledge for faq_entry production"
domain: "faq_entry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Domain Overview  
FAQ entries are structured artifacts used in customer support systems to centralize common questions and standardized responses. They aim to reduce agent workload by deflecting inquiries to self-service resources while ensuring consistency in communication. Modern implementations often integrate with knowledge management systems, analytics platforms, and AI-driven chatbots to optimize answer accuracy and user experience. Key considerations include linguistic clarity, cross-linking to related resources, and quantifying support deflection impact through metrics like resolution rate or time-to-answer.  

## Key Concepts  
| Concept | Definition | Source |  
|---|---|---|  
| FAQPage | Schema.org structured data type enabling Google rich results (expandable Q&A in SERPs) | Schema.org/FAQPage |  
| Rich Results | Enhanced Google SERP listings; FAQPage eligible when all questions visible on page | Google Search Central |  
| Canonical Answer | Authoritative, unambiguous response; max 150 words for optimal self-service resolution rate | ISO/IEC 25010:2011 |  
| Support Deflection | Reduction in agent-handled tickets via self-service; measured as % resolved without agent | Gartner "Customer Self-Service" Report (2022) |  
| Question Normalization | Standardizing phrasing using imperative verbs ("How do I...") to group similar queries | Knowledge Management Institute |  
| Answer Versioning | Tracking changes to canonical answers over time; use updated field + changelog | Git / KB platform versioning |  
| Accessibility Compliance | Ensuring content meets WCAG 2.1 standards (plain language, no jargon, alt text) | W3C WCAG 2.1 (2018) |  
| Deflection Rate | % of support inquiries resolved via self-service FAQ without agent escalation | Zendesk Support Benchmark Report |  

## Industry Standards  
- Schema.org FAQPage (structured data for Google rich results eligibility)  
- Google Search Central: FAQ rich results requirements (max 100 chars per Q, 1000 chars per A)  
- ISO/IEC 25010:2011 (System Quality Requirements)  
- WCAG 2.1 (Web Accessibility Guidelines)  
- Zendesk/Intercom KB structure patterns (self-service deflection best practices)  
- Gartner "Customer Self-Service" Report (support deflection benchmarks)  

## Common Patterns  
1. Use imperative verbs in questions (e.g., "How do I reset my password?").  
2. Embed hyperlinks to related FAQs or documentation.  
3. Include a support deflection metric (e.g., "Resolved 85% of cases in 2023").  
4. Structure answers with numbered steps for procedural queries.  
5. Avoid technical jargon unless aligned with user personas.  
6. Apply consistent categorization tags for searchability.  

## Pitfalls  
- Vague questions leading to low deflection rates.  
- Inconsistent answer phrasing across entries.  
- Missing version history for outdated answers.  
- Overloading answers with irrelevant links.  
- Ignoring accessibility standards (e.g., missing alt text for images).
