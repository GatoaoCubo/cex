---
kind: examples
id: bld_examples_churn_prevention_playbook
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of churn_prevention_playbook artifacts
quality: 8.9
title: "Examples Churn Prevention Playbook"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [churn_prevention_playbook, builder, examples]
tldr: "Golden and anti-examples of churn_prevention_playbook artifacts"
domain: "churn_prevention_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example  
---
**Title**: Churn Prevention Playbook for SaaS Retention  
**Author**: Customer Success Team  
**Date**: 2023-10-05  
**Version**: 1.2  

### Signal Detection  
- **Tools**: Salesforce (custom fields for usage metrics), Mixpanel (behavioral analytics)  
- **Signals**: 30-day inactivity, 20% drop in feature usage, support tickets with "billing" in subject line  

### Intervention Triggers  
- **Rules**:  
  - If user has 2+ inactive licenses in Salesforce AND Mixpanel shows 0 logins in 14 days → Auto-assign to CS Rep  
  - If NPS score < 5 in SurveyMonkey → Trigger email from HubSpot with CSM  

### Save-the-Account Scripts  
- **Script 1**:  
  ```python  
  # HubSpot API call to send personalized email  
  payload = {  
    "email": "user@example.com",  
    "subject": "We noticed you're not using [Feature X] – let’s fix that!",  
    "body": "Hi [Name], we see you haven’t used [Feature X] recently. Our team can help you get more value from it. Schedule a call here: [link]."  
  }  
  ```  
- **Script 2**:  
  ```sql  
  -- Query to identify at-risk accounts in Salesforce  
  SELECT Name, AccountId, LastLoginDate, NumberOfLicenses  
  FROM User  
  WHERE LastLoginDate < DATEADD(day, -30, GETDATE()) AND NumberOfLicenses > 5;  
  ```  

## Anti-Example 1: Vague Tool References  
---
**Title**: Generic Churn Playbook  
**Author**: Unknown  
**Date**: 2023-01-01  
**Version**: 0.1  

### Signal Detection  
- **Tools**: "Some CRM", "Generic analytics tool"  
- **Signals**: "Low engagement", "High support requests"  

### Intervention Triggers  
- **Rules**:  
  - If "user is unhappy" → "Send email"  

### Save-the-Account Scripts  
- **Script**: "Use [tool] to contact user"  

## Why it fails  
Lacks specificity in tools (no real vendor names) and actionable steps. "Low engagement" and "user is unhappy" are too vague to trigger automated workflows.  

## Anti-Example 2: Missing Key Sections  
---
**Title**: Churn Playbook (Incomplete)  
**Author**: Marketing Team  
**Date**: 2023-09-20  
**Version**: 0.5  

### Signal Detection  
- **Tools**: Google Analytics  
- **Signals**: 50% drop in monthly active users  

### Save-the-Account Scripts  
- **Script**: "Send a survey via Typeform"  

## Why it fails  
Omits intervention triggers entirely. Without defined rules for when to act, the playbook cannot activate interventions, leading to missed opportunities to retain customers.
