---
kind: knowledge_card
id: bld_knowledge_card_discovery_questions
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for discovery_questions production
quality: 9.1
title: "Knowledge Card Discovery Questions"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [discovery_questions, builder, knowledge_card]
tldr: "Domain knowledge for discovery_questions production"
domain: "discovery_questions construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_discovery_questions_builder
  - discovery-questions-builder
  - bld_instruction_discovery_questions
  - p10_mem_discovery_questions_builder
  - bld_knowledge_card_sales_playbook
  - bld_examples_discovery_questions
  - p03_sp_sales_playbook_builder
  - bld_tools_discovery_questions
  - kc_discovery_questions
  - bld_output_template_discovery_questions
---

## Domain Overview
Discovery questions in MEDDIC/BANT frameworks are structured to uncover buyer motivations, decision dynamics, and deal viability. These questions bridge the gap between sales qualification and solution design, ensuring alignment with the buyer’s strategic goals and organizational constraints. By tailoring questions to buyer personas (e.g., CFO, IT manager) and deal stages (e.g., needs analysis, proposal), sales teams can identify pain points, budget limits, and decision influencers. Unlike general sales playbooks, discovery questions focus on actionable insights rather than broad strategies, enabling personalized engagement.

## Key Concepts
| Concept               | Definition                                                                 | Source                              |
|----------------------|----------------------------------------------------------------------------|-------------------------------------|
| MEDDIC               | Framework for qualifying deals via Metrics, Economic Buyer, etc.          | Neil Rackham, *MEDDIC Selling*     |
| BANT                 | Qualification criteria: Budget, Authority, Need, Timeline.                | *The Challenger Sale*              |
| Pain Points          | Specific problems hindering the buyer’s operations or goals.              | Harvard Business Review            |
| Economic Buyer       | Individual with authority to approve spending.                            | *MEDDIC Selling*                   |
| Decision Criteria    | Metrics used to evaluate solutions (e.g., ROI, risk reduction).           | CEB Buying Process                 |
| Champion             | Internal advocate who supports the solution.                              | *MEDDIC Selling*                   |
| Deal Stage           | Progression in the sales cycle (e.g., discovery, proposal).               | Salesforce Sales Cloud             |
| Buyer Persona        | Detailed profile of a target customer (e.g., technical buyer, executive). | HubSpot                            |

## Industry Standards
- MEDDIC Selling (Neil Rackham)
- BANT Framework (Salesforce, HubSpot)
- CEB Buying Process (now Gartner)
- Harvard Business Review: “The Sales Process”
- *The Challenger Sale* by Matthew Dixon & Patrick Allen
- RFC 7231 (HTTP/1.1: Semantics and Content) – for API-based discovery tools

## Common Patterns
1. Align questions with the buyer’s role and stage (e.g., CFO: ROI; IT: integration).
2. Use open-ended questions to uncover unspoken needs (e.g., “What challenges are you facing?”).
3. Map pain points to business outcomes (e.g., “How does this impact your quarterly goals?”).
4. Probe for decision criteria early (e.g., “What metrics will determine success?”).

## Pitfalls
- Assuming all buyers follow the same decision process.
- Overloading with technical jargon that alienates non-expert stakeholders.
- Failing to adapt questions based on persona (e.g., asking a CEO about implementation details).
- Neglecting to tie questions to measurable outcomes (e.g., “How do you prioritize vendors?”).
- Relying on generic questions instead of persona-specific insights.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_discovery_questions_builder]] | downstream | 0.57 |
| [[discovery-questions-builder]] | related | 0.55 |
| [[bld_instruction_discovery_questions]] | downstream | 0.53 |
| [[p10_mem_discovery_questions_builder]] | downstream | 0.51 |
| [[bld_knowledge_card_sales_playbook]] | sibling | 0.47 |
| [[bld_examples_discovery_questions]] | downstream | 0.47 |
| [[p03_sp_sales_playbook_builder]] | downstream | 0.40 |
| [[bld_tools_discovery_questions]] | downstream | 0.40 |
| [[kc_discovery_questions]] | sibling | 0.39 |
| [[bld_output_template_discovery_questions]] | downstream | 0.36 |
