---
kind: knowledge_card
id: bld_knowledge_card_customer_segment
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for customer_segment production
quality: 9.2
title: "Knowledge Card Customer Segment"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [customer_segment, builder, knowledge_card]
tldr: "Domain knowledge for customer_segment production"
domain: "customer_segment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - customer-segment-builder
  - n06_kc_icp_frameworks
  - p03_sp_customer_segment_builder
  - bld_collaboration_customer_segment
  - p03_sp_discovery_questions_builder
  - p02_qg_customer_segment
  - bld_instruction_customer_segment
  - bld_output_template_customer_segment
  - bld_knowledge_card_discovery_questions
  - p10_mem_customer_segment_builder
---

## Domain Overview
Customer segmentation defines distinct groups of organizations or individuals sharing firmographic traits (e.g., industry, size, revenue) and unmet needs. In B2B contexts, this informs Ideal Customer Profile (ICP) development, aligning product/service offerings with market demand. Segmentation uses the STP framework (Segmentation, Targeting, Positioning) combined with firmographic and technographic signals. PLG (product-led growth) ICPs add behavioral triggers: activation milestones, usage frequency, and feature adoption patterns. Qualification frameworks like BANT and MEDDIC convert segment definitions into actionable sales criteria.

## Key Concepts
| Concept | Definition | Source |
|---------|-----------|--------|
| Firmographics | Organizational attributes (industry, revenue, location) for segmentation | Dun & Bradstreet |
| Technographics | Technology stack signals used to infer fit and readiness | Bombora, G2 Crowd |
| ICP (Ideal Customer Profile) | Profile of the most valuable customer type based on fit and potential | HubSpot ICP Framework |
| STP Framework | Segmentation, Targeting, Positioning -- market strategy structure | Kotler (1967) |
| BANT | Budget, Authority, Need, Timeline -- sales qualification framework | IBM (1950s), SPIN updated |
| MEDDIC | Metrics, Economic Buyer, Decision Criteria, Decision Process, Identify Pain, Champion | Jack Napoli (1996) |
| Jobs-to-be-Done (JTBD) | Theory of what "jobs" customers hire a product to accomplish | Christensen et al. (2015) |
| PLG ICP Signals | Product usage signals (activation, DAU/WAU, feature depth) that indicate fit | OpenView Partners |
| RFM Model | Recency, Frequency, Monetary value for behavioral segmentation | Marketing Science Institute (1990) |
| TAM/SAM/SOM | Total/Serviceable/Obtainable Addressable Market sizing | CB Insights |
| CAC / LTV | Customer Acquisition Cost and Lifetime Value -- segment economics | HBR, SaaStr |

## ICP Qualification Frameworks (Comparative)

| Framework | Best For | Key Signals | Limitation |
|-----------|---------|------------|-----------|
| BANT | Transactional B2B, outbound | Budget confirmed, authority identified | Over-relies on self-reported data |
| MEDDIC | Enterprise/complex sales | Economic buyer mapped, champion active | High effort, not for SMB |
| PLG ICP | Product-led growth | Activation rate, feature depth, DAU | Requires product telemetry |
| JTBD | Innovation/new market | Customer-stated desired outcomes | Qualitative, hard to operationalize |
| RFM | B2C, e-commerce | Purchase recency, frequency, spend | Backward-looking, not predictive |

## Industry Standards
- STP Framework (Segmentation, Targeting, Positioning) -- Kotler (1967)
- BANT qualification framework -- IBM origin, widely adopted by Salesforce, HubSpot
- MEDDIC/MEDDPICC -- Napoli (1996), used by enterprise SaaS leaders
- RFM Model -- Marketing Science Institute
- Technographic segmentation -- Bombora intent data, G2 buyer intent
- PLG ICP signals -- OpenView Partners SaaS benchmarks

## Common Patterns
1. Use firmographics (industry, employee count, revenue) to create initial segment filter.
2. Layer technographics (current tools, integrations in use) to refine ICP fit score.
3. Apply BANT or MEDDIC to qualify prospects within the segment.
4. For PLG motions: track activation milestones as in-product ICP signals.
5. Run JTBD interviews on best-fit customers to validate need hypotheses.
6. Score segments by LTV:CAC ratio; prioritize segments where ratio exceeds 3:1.

## Pitfalls
- Conflating ICP with persona: ICP = organizational fit, persona = individual behavior.
- Using static firmographics without technographic enrichment -- misses tech-fit signals.
- Ignoring PLG signals for product-led companies: usage data outperforms demographic data.
- Over-segmenting: more than 5-7 primary segments dilutes go-to-market resources.
- Failing to validate segments against win/loss data from actual closed deals.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[customer-segment-builder]] | downstream | 0.49 |
| [[n06_kc_icp_frameworks]] | sibling | 0.34 |
| [[p03_sp_customer_segment_builder]] | downstream | 0.33 |
| [[bld_collaboration_customer_segment]] | downstream | 0.32 |
| [[p03_sp_discovery_questions_builder]] | downstream | 0.27 |
| [[p02_qg_customer_segment]] | downstream | 0.25 |
| [[bld_instruction_customer_segment]] | downstream | 0.25 |
| [[bld_output_template_customer_segment]] | downstream | 0.24 |
| [[bld_knowledge_card_discovery_questions]] | sibling | 0.23 |
| [[p10_mem_customer_segment_builder]] | downstream | 0.23 |
