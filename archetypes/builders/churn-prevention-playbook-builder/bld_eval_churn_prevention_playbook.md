---
kind: quality_gate
id: p03_qg_churn_prevention_playbook
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for churn_prevention_playbook
quality: 9.1
title: "Quality Gate Churn Prevention Playbook"
version: "1.0.0"
author: n05_wave6
tags: [churn_prevention_playbook, builder, quality_gate]
tldr: "Quality gate with HARD and SOFT scoring for churn_prevention_playbook"
domain: "churn_prevention_playbook construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_churn_prevention_playbook
  - bld_instruction_churn_prevention_playbook
  - churn-prevention-playbook-builder
  - p12_qg_renewal_workflow
  - bld_output_template_churn_prevention_playbook
  - p03_sp_churn_prevention_playbook_builder
  - p11_qg_nps_survey
  - p03_qg_expansion_play
  - p05_qg_interactive_demo
  - p05_qg_user_journey
---

## Quality Gate

## Definition
| Metric                        | Threshold | Operator | Scope                              |
|-------------------------------|-----------|----------|------------------------------------|
| Gainsight/ChurnZero alignment | 100%      | equals   | All playbook artifacts             |
| Save script completeness      | 4 sections| min      | opening + discovery + objections + close |

## HARD Gates
| ID  | Check                                                       | Fail Condition                         |
|-----|-------------------------------------------------------------|----------------------------------------|
| H01 | YAML frontmatter valid                                      | Invalid YAML or missing required fields|
| H02 | ID matches `^p03_cpp_[a-z][a-z0-9_]+\.md$`                 | Pattern mismatch                       |
| H03 | kind = `churn_prevention_playbook`                         | Wrong or missing kind                  |
| H04 | health_score_model present with >= 3 components             | Incomplete health model                |
| H05 | intervention_triggers covers red-zone AND pre-renewal       | Missing trigger coverage               |
| H06 | Save script has opening, discovery, objections, close       | Incomplete script structure            |
| H07 | Win-back sequence has >= 3 touchpoints                      | Insufficient win-back coverage         |

## SOFT Scoring
| Dim | Dimension                                           | Weight | Scoring Guide                                                  |
|-----|-----------------------------------------------------|--------|----------------------------------------------------------------|
| D01 | Health score model completeness                     | 0.25   | 5 components (usage, NPS, support, engagement, contract) = 1.0, 3-4 = 0.7, <3 = 0.3 |
| D02 | Churn reason taxonomy coverage                      | 0.20   | All 4 reasons (product, budget, competitor, champion) = 1.0, 2-3 = 0.6, <2 = 0.2 |
| D03 | Objection handler specificity                       | 0.20   | Named objections with scripts = 1.0, generic = 0.5, absent = 0|
| D04 | Escalation path completeness                        | 0.15   | CSM -> VP CS -> exec = 1.0, CSM -> mgr only = 0.6, single hop = 0.2 |
| D05 | Win-back sequence quality                           | 0.20   | 3+ touchpoints + personalization hooks = 1.0, generic = 0.5, absent = 0 |

## Actions
| Score   | Threshold | Action                              |
|---------|-----------|-------------------------------------|
| GOLDEN  | >=9.5     | Auto-publish, no review             |
| PUBLISH | >=8.0     | Auto-publish after validation       |
| REVIEW  | >=7.0     | Require CS Director review          |
| REJECT  | <7.0      | Reject -- rebuild with save script  |

## Bypass
| Condition                  | Approver     | Audit Trail              |
|----------------------------|--------------|--------------------------|
| Emergency churn spike      | VP CS        | Incident log             |

## Examples

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

## Golden Example 2 -- B2C Fitness App Mobile Churn Prevention

---
id: cpp_fitpulse_b2c_mobile_2026
kind: churn_prevention_playbook
pillar: P07
title: "FitPulse B2C Churn Prevention Playbook -- Mobile Subscription"
product: FitPulse iOS/Android
segment: B2C
subscription_type: monthly ($14.99/mo) and annual ($99/yr)
MRR_at_risk_threshold: "$4,500/cohort"
version: "2.1"
author: growth_team
created: "2026-04-01"
quality: null

### Signal Detection

Tools: Amplitude (mobile behavioral analytics), Braze (push + in-app messaging),
Stripe (billing events), Delighted (NPS mobile survey), Firebase (session tracking)

Signal thresholds that classify a subscriber as at-risk:

| Signal                      | Threshold              | Time Window | Risk Level |
|-----------------------------|------------------------|-------------|------------|
| Push open rate              | < 10% (vs. avg 38%)    | 14 days     | Medium     |
| Session frequency           | < 2 sessions/week      | 21 days     | Medium     |
| Session frequency           | 0 sessions             | 7 days      | High       |
| Workout completion rate     | < 30% of started       | 14 days     | High       |
| In-app NPS response         | score < 6              | immediately | Critical   |
| Failed payment              | 1st retry              | immediately | Critical   |
| Billing page visit          | 2+ visits, no action   | 7 days      | High       |

Amplitude cohort query:
```sql
-- At-risk cohort: no session in 7 days AND push open < 10% last 14 days
SELECT user_id, last_session_date, push_open_rate_14d, subscription_type
FROM amplitude_user_properties
WHERE last_session_date < CURRENT_DATE - INTERVAL '7 days'
  AND push_open_rate_14d < 0.10
  AND subscription_status = 'active'
ORDER BY last_session_date ASC;
```

### Intervention Triggers and Playbooks

**Playbook A -- Re-engagement (Medium risk, session drop)**

Trigger: < 2 sessions/week for 21 days AND push open rate >= 10%
Channel: Braze push notification (personalized, behavior-based)
Owner: Automated (no human CSM -- B2C scale)

Braze campaign config:
```json
{
  "campaign_name": "re_engagement_session_drop",
  "trigger": "custom_event: at_risk_medium",
  "delay_hours": 0,
  "message": {
    "push_title": "Your streak is waiting, {{first_name}}",
    "push_body": "You crushed it last month. 10 minutes today keeps momentum alive.",
    "deep_link": "fitpulse://home/recommended_workout"
  },
  "frequency_cap": "1 per 3 days",
  "abort_condition": "user_opened_app_since_trigger"
}
```

**Playbook B -- Save offer (High risk, 7-day zero session)**

Trigger: 0 sessions in 7 days AND subscription renewal within 30 days
Channel: Braze in-app message on next open + email fallback (72h if no open)
Offer: Price lock at current rate for 12 months if upgrades to annual, or 20% off renewal
Owner: Automated -- Braze Canvas flow

In-app message copy:
```
"We miss you, {{first_name}}. Life gets busy -- we get it.
Lock in your current rate forever: upgrade to annual today.
$99/yr vs. $179.88 if you stay monthly. Your choice."
[CTA: "Lock my rate"] [Secondary: "Maybe later"]
```

Stripe upgrade flow: Braze webhook -> internal API -> Stripe subscription.update
(prorate remaining monthly, apply annual coupon PRICLOCK2026, set cancel_at_period_end=false)

**Playbook C -- NPS-triggered human save (Critical, NPS < 6)**

Trigger: Delighted mobile NPS survey response score < 6
Owner: CS Specialist (human) within 4 business hours
Channel: In-app message + direct email from CS rep
SLA: First response within 4h, resolution within 48h

Delighted -> Zapier -> Zendesk ticket (tagged: nps_detractor, churn_risk)
Zendesk auto-assigns to CS queue "mobile_save_team"

CS rep script opening:
```
Subject: "We heard your feedback, {{first_name}} -- I want to help"
Body: "Hi {{first_name}}, I'm [CS rep name] at FitPulse. I saw your recent
feedback and wanted to reach out personally. Your experience matters to us.
Can you share what's been frustrating? I have authority to make it right."
```

CS rep discount authority: up to 3 months free or full refund on last charge

**Playbook D -- Failed payment recovery**

Trigger: Stripe payment_intent.payment_failed (1st retry)
Channel: Braze push (immediate) + email (24h if no update)
Owner: Automated (Stripe dunning + Braze)

Braze dunning message:
```json
{
  "push_title": "Payment issue -- tap to fix",
  "push_body": "We could not process your FitPulse subscription. Update your card to keep your streak.",
  "deep_link": "fitpulse://account/billing"
}
```

Stripe dunning schedule: retry D+3, D+7, D+14 then cancel and send win-back email

### Save Rate Targets and Measurement

| Cohort              | Monthly Churn Without Playbook | Target Save Rate | Expected Churn Reduction |
|---------------------|-------------------------------|------------------|--------------------------|
| Medium risk (A)     | 18%                           | 35% saved        | -6.3 ppt                 |
| High risk (B)       | 42%                           | 25% saved        | -10.5 ppt                |
| NPS detractor (C)   | 65%                           | 40% saved        | -26 ppt                  |
| Failed payment (D)  | 55%                           | 60% recovered    | -33 ppt                  |

Amplitude dashboard: "Churn Prevention Funnel" tracks trigger -> message delivered ->
CTA clicked -> subscription active at D+30 per playbook.

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
