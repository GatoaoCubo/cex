---
kind: knowledge_card
id: bld_knowledge_card_renewal_workflow
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for renewal_workflow production
quality: 9.2
title: "Knowledge Card Renewal Workflow"
version: "1.0.0"
author: wave6_n06
tags: [renewal_workflow, builder, knowledge_card, renewal, GRR, Gainsight, Salesforce, multi-year]
tldr: "Domain knowledge for renewal_workflow production"
domain: "renewal_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Domain Overview
Renewal workflows are automated, stage-gated processes that manage the contract lifecycle from 90 days before expiration through close. Their primary metric is Gross Revenue Retention (GRR): the percentage of beginning ARR retained after renewal, excluding expansion. World-class GRR is >90% for enterprise SaaS. Renewal workflows are the operational backbone of CS teams, executed through Gainsight (health scoring + CTA automation) and Salesforce (opportunity management + contract amendments).

The 90/60/30-day cadence is the industry standard: 90 days for relationship building and intent signaling, 60 days for commercial negotiation and price-increase announcement, 30 days for close and contract execution. Multi-year contracts (2-3 year commitments) are the highest-value renewal outcome -- they lock ARR, reduce churn risk, and often allow for price escalation across years.

## Key Concepts
| Concept                   | Definition                                                                      | Source                                  |
|---------------------------|---------------------------------------------------------------------------------|-----------------------------------------|
| GRR (Gross Revenue Retention)| Retained ARR / Beginning ARR (excludes expansion, includes contraction/churn)  | SaaStr GRR Benchmarks                   |
| Renewal Stage             | Gate in the 90/60/30-day workflow with defined owner, tasks, and automation     | Gainsight Renewal Center design         |
| Auto-Renewal              | Contractual clause that renews automatically unless customer opts out            | CFPB SaaS Contract Standards            |
| Price Escalation Clause   | Contractual right to increase price annually (CPI-linked or flat percentage)    | IACCM Contract Design Standards         |
| Multi-Year Contract       | 2+ year commitment in exchange for pricing incentives or stability              | Salesforce Enterprise Sales Playbook    |
| Gainsight CTA             | Automated customer success task triggered by health score or date event         | Gainsight PX Documentation              |
| Health Score              | Composite signal of product adoption, support tickets, NPS, engagement (0-100) | Gainsight / Totango CS frameworks       |
| Notice Period             | Jurisdiction-required advance notice before auto-renewal activation             | US State Law / EU Consumer Rights Dir.  |

## Industry Standards
- SaaStr GRR benchmarks: world-class >95%, good >90%, median 85-90% for enterprise SaaS
- Gainsight Renewal Center: stage-based CTA automation with health score triggers
- Salesforce CPQ: contract amendment and renewal opportunity management
- IACCM (International Association for Contract Management): price escalation clause design
- US State Auto-Renewal Laws: California (ARL), New York, Illinois -- 30-day notice minimums
- EU Consumer Rights Directive: Article 16 on auto-renewal transparency
- TSIA Renewal Operations: 90/60/30 cadence as industry benchmark

## Common Patterns
1. 90-day relationship-first outreach (no commercial pressure) increases renewal probability by 15% vs. 60-day cold proposals.
2. Multi-year conversion rates peak when health score is 75+ AND customer tenure exceeds 2 years.
3. Price increases of 5-8% have <10% pushback rate when announced at 90-day with value narrative.
4. Gainsight CTA automation reduces CSM administrative overhead by 30% in renewal workflows.
5. Escalation at health score <60 (not <40) allows enough time to intervene; <40 is typically too late.
6. GRR improvement from 85% to 90% on $10M ARR base = $500K retained annually -- highest ROI CS investment.

## Pitfalls
- Starting renewal at 30 days: insufficient time for negotiation, legal review, and procurement PO.
- Generic auto-renewal language: non-compliance with state-specific notice laws creates contract voidability.
- No escalation health threshold: CSMs self-judge risk, leading to inconsistent escalation and late VP involvement.
- Price increase without value narrative: framed as cost increase rather than value recognition -- increases churn risk.
- Multi-year offer without discount authority: CSM promises discounts they cannot approve, damages trust.
- Conflating renewal with expansion: different ARR metrics (GRR vs. NRR), different owners, different timing.
