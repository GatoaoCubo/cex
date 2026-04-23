---
kind: knowledge_card
id: bld_knowledge_card_expansion_play
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for expansion_play production
quality: 9.2
title: "Knowledge Card Expansion Play"
version: "1.0.0"
author: wave6_n06
tags: [expansion_play, builder, knowledge_card, upsell, NRR, land-and-expand, QBR]
tldr: "Domain knowledge for expansion_play production"
domain: "expansion_play construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - expansion-play-builder
  - p03_sp_expansion_play_builder
  - bld_instruction_expansion_play
  - bld_examples_expansion_play
  - p10_mem_expansion_play_builder
  - bld_tools_expansion_play
  - bld_output_template_expansion_play
  - bld_schema_expansion_play
  - kc_expansion_play
  - p03_qg_expansion_play
---

## Domain Overview
Expansion plays are structured commercial motions designed to grow net revenue within existing customer accounts. The land-and-expand model -- pioneered by Snowflake, Datadog, Slack, and Twilio -- starts with a small initial contract (land) and systematically grows ARR through usage-triggered upsells and feature cross-sells (expand). The key revenue metric is Net Revenue Retention (NRR): an NRR >120% means the existing customer base grows revenue faster than churn removes it, effectively making expansion a lower-CAC growth engine than new logo acquisition.

Expansion plays are triggered by product usage signals (seat utilization, feature adoption, API call volume) and executed through AE/CSM collaboration at QBRs, business reviews, or trigger-based outreach. The economic buyer (budget authority) and champion (internal advocate) must both be mapped before executing the play.

## Key Concepts
| Concept                   | Definition                                                                    | Source                               |
|---------------------------|-------------------------------------------------------------------------------|--------------------------------------|
| NRR (Net Revenue Retention)| (Beginning ARR + Expansion - Contraction - Churn) / Beginning ARR            | SaaStr Annual Benchmarks             |
| Land-and-Expand           | Sales motion: small initial contract, systematic upsell through adoption      | Snowflake / Datadog PLG model        |
| Seat Upsell               | Expansion by adding licensed users beyond current contract limit              | Gartner SaaS Pricing Guide           |
| Feature Cross-Sell        | Expansion by attaching adjacent SKUs based on usage pattern match             | Forrester Revenue Growth Framework   |
| QBR (Quarterly Business Review)| Executive-level meeting reviewing value delivered and growth opportunities | TSIA Customer Success Framework      |
| Account Mapping           | Identification of economic buyer, champion, blocker, and procurement contact  | MEDDIC/MEDDPICC Sales Methodology    |
| Usage Threshold Trigger   | Automated alert when usage metric crosses defined threshold for N days         | Gainsight/ChurnZero PX Analytics     |
| Expansion ARR             | Net-new ARR from existing customers; included in NRR numerator                | OpenView SaaS Metrics Benchmark      |

## Industry Standards
- SaaStr NRR benchmarks: world-class >130%, good >120%, median 100-110%
- TSIA Customer Success maturity model (expansion as CS-owned motion)
- MEDDIC/MEDDPICC: account mapping methodology for expansion qualification
- Gainsight CS Operations: usage-triggered expansion CTA automation
- Forrester Revenue Operations: AE/CS expansion ownership model
- OpenView PLG metrics: product-led expansion signal definitions

## Common Patterns
1. Seat threshold at 80% utilization for 14+ days is the most reliable upsell trigger (Datadog model).
2. Feature cross-sell attach rates are highest when trigger SKU has >60% adoption in current license.
3. QBR is the highest-conversion venue for expansion conversations -- 3x conversion vs. cold outreach.
4. Multi-stakeholder account maps increase expansion close rates by 40% (CSO Insights data).
5. NRR >120% requires net expansion ARR to exceed both contraction and churn by >20% of beginning ARR.
6. AE-CSM co-sell motions outperform single-owner expansion by 25% in ENT accounts.

## Pitfalls
- Vague triggers: "when the account seems ready" -- unmeasurable, unautomatable, unforecastable.
- Missing NRR model: expansion plays without NRR accounting cannot contribute to board-level metrics.
- Champion-only account map: champion leaves = play collapses; always map the economic buyer too.
- Conflating expansion with renewal: different metrics (NRR vs. GRR), owners, and timing.
- QBR with internal metrics: customers disengage when QBR content uses vendor metrics, not customer success metrics.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[expansion-play-builder]] | downstream | 0.68 |
| [[p03_sp_expansion_play_builder]] | downstream | 0.64 |
| [[bld_instruction_expansion_play]] | downstream | 0.60 |
| [[bld_examples_expansion_play]] | downstream | 0.46 |
| [[p10_mem_expansion_play_builder]] | downstream | 0.41 |
| [[bld_tools_expansion_play]] | downstream | 0.41 |
| [[bld_output_template_expansion_play]] | downstream | 0.40 |
| [[bld_schema_expansion_play]] | downstream | 0.39 |
| [[kc_expansion_play]] | sibling | 0.39 |
| [[p03_qg_expansion_play]] | downstream | 0.37 |
