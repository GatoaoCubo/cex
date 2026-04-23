---
id: kc_nps_survey
kind: knowledge_card
title: NPS Survey Configuration
version: 1.0.0
quality: 8.6
pillar: P01
language: en
density_score: 0.96
related:
  - bld_instruction_nps_survey
  - bld_knowledge_card_nps_survey
  - bld_output_template_nps_survey
  - p03_sp_nps_survey_builder
  - bld_examples_nps_survey
  - nps-survey-builder
  - bld_collaboration_integration_guide
  - kc_competitive_matrix
  - email_sequence_template
  - n06_kc_icp_frameworks
---

# NPS Survey Configuration

## Question
Standard prompt:  
"On a scale from 0 to 10, how likely are you to recommend our product to a friend or colleague?"  
Variations:  
- "How likely are you to recommend [Product Name] to a colleague?"  
- "On a scale of 1-10, how likely are you to recommend [Product Name]?"

## Scale
0-10 scale:  
0 = "Not at all likely"  
10 = "Extremely likely"  
Categorization:  
- Detractors (0-6)  
- Passives (7-8)  
- Promoters (9-10)  

## Follow-up
- Send thank-you message with branded logo  
- Offer incentive (e.g., discount code) for promoters  
- Provide resource link for detractors (e.g., support portal)  

## Segmentation
- Target new users with onboarding-specific questions  
- Prioritize high-value customers for follow-up  
- Segment by product usage frequency  

## Cadence
- Primary frequency: Every 3 months  
- Trigger surveys after key interactions (e.g., purchase, support resolution)  
- Avoid more than 1 survey per 90 days  

## Response Routing
- Detractors → Customer Success Team  
- Promoters → Loyalty Program  
- Passives → Product Team for improvement insights  
- All responses → CRM system for analysis

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_nps_survey]] | downstream | 0.47 |
| [[bld_knowledge_card_nps_survey]] | sibling | 0.37 |
| [[bld_output_template_nps_survey]] | downstream | 0.27 |
| [[p03_sp_nps_survey_builder]] | downstream | 0.27 |
| [[bld_examples_nps_survey]] | downstream | 0.23 |
| [[nps-survey-builder]] | downstream | 0.23 |
| [[bld_collaboration_integration_guide]] | downstream | 0.20 |
| [[kc_competitive_matrix]] | sibling | 0.20 |
| [[email_sequence_template]] | downstream | 0.18 |
| [[n06_kc_icp_frameworks]] | sibling | 0.17 |
