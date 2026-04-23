---
kind: knowledge_card
id: bld_knowledge_card_nps_survey
pillar: P01
llm_function: INJECT
purpose: Domain knowledge for nps_survey production
quality: 9.2
title: "Knowledge Card Nps Survey"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [nps_survey, builder, knowledge_card]
tldr: "Domain knowledge for nps_survey production"
domain: "nps_survey construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_nps_survey_builder
  - nps-survey-builder
  - bld_instruction_nps_survey
  - kc_nps_survey
  - bld_examples_nps_survey
  - p11_qg_nps_survey
  - kc_user_journey
  - bld_collaboration_nps_survey
  - bld_tools_nps_survey
  - customer-segment-builder
---

## Domain Overview  
Net Promoter Score (NPS) surveys are a cornerstone of customer experience (CX) measurement, enabling organizations to gauge loyalty and predict growth. The core mechanism involves a single question ("How likely are you to recommend [company/product] to a friend?") on a 0–10 scale, with responses segmented into promoters (9–10), passives (7–8), and detractors (0–6). NPS is widely adopted across industries for its simplicity and correlation with revenue growth, as highlighted in Reichheld’s seminal 2003 Harvard Business Review paper. Follow-up questions, segmentation, and response routing enhance actionable insights, while cadence ensures consistent feedback without survey fatigue.  

## Key Concepts  
| Concept               | Definition                                                                 | Source                                  |  
|----------------------|----------------------------------------------------------------------------|-----------------------------------------|  
| NPS Question         | Core 0–10 scale question measuring likelihood to recommend                | Reichheld (2003)                        |  
| Scale                | 0–10 numerical scale for quantifying sentiment                             | Net Promoter System (Bain & Company)    |  
| Follow-up Questions  | Additional questions to gather qualitative feedback on responses           | Bernd Schmitt (2018)                    |  
| Segmentation         | Grouping respondents by demographics, product usage, or tenure            | ISO 10520:2014 (Customer Satisfaction)  |  
| Cadence              | Frequency of survey deployment (e.g., quarterly, post-interaction)        | Forrester CX Best Practices (2020)      |  
| Response Routing     | Directing responses to specific teams (e.g., support, product) based on NPS | Salesforce Einstein Analytics (2021)    |  
| Promoters/Detractors  | Categorization of respondents based on NPS score                          | Reichheld & Sackmann (2011)             |  
| Open-Ended Feedback  | Qualitative input collected post-NPS question                             | American Customer Satisfaction Index (ACSI) |  
| Survey Timing        | Strategic placement (e.g., post-purchase, post-support)                   | Customer Experience Journal (2019)      |  
| Response Rate Optimization | Techniques to minimize drop-offs (e.g., concise design, incentives) | Nielsen Norman Group (2022)             |  

## Industry Standards  
- Net Promoter System (Bain & Company)  
- ISO 10520:2014 (Customer Satisfaction Measurement)  
- American Customer Satisfaction Index (ACSI)  
- Forrester CX Best Practices (2020)  
- Harvard Business Review: "One Question That Can Transform Your Business" (Reichheld, 2003)  

## Common Patterns  
1. Use a single, standardized NPS question with 0–10 scale.  
2. Route detractor responses to customer success teams for immediate action.  
3. Segment surveys by product line or customer tier for targeted analysis.  
4. Deploy surveys post-interaction (e.g., after support, purchase).  
5. Include open-ended follow-ups for qualitative insights.  
6. Schedule recurring cadence (e.g., quarterly) to track trends.  

## Pitfalls  
- Overloading surveys with too many questions, reducing completion rates.  
- Failing to align segmentation with business goals (e.g., irrelevant groupings).  
- Ignoring detractor feedback, missing critical retention opportunities.  
- Inconsistent cadence leading to survey fatigue or skewed data.  
- Not leveraging response routing to prioritize high-impact feedback.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_nps_survey_builder]] | downstream | 0.49 |
| [[nps-survey-builder]] | downstream | 0.48 |
| [[bld_instruction_nps_survey]] | downstream | 0.45 |
| [[kc_nps_survey]] | sibling | 0.39 |
| [[bld_examples_nps_survey]] | downstream | 0.29 |
| [[p11_qg_nps_survey]] | downstream | 0.28 |
| [[kc_user_journey]] | sibling | 0.28 |
| [[bld_collaboration_nps_survey]] | downstream | 0.28 |
| [[bld_tools_nps_survey]] | downstream | 0.28 |
| [[customer-segment-builder]] | downstream | 0.27 |
