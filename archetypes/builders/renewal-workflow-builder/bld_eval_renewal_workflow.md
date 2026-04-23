---
kind: quality_gate
id: p12_qg_renewal_workflow
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for renewal_workflow
quality: 9.1
title: "Quality Gate Renewal Workflow"
version: "1.0.0"
author: wave6_n06
tags: [renewal_workflow, builder, quality_gate, GRR, renewal, Gainsight]
tldr: "Quality gate with HARD and SOFT scoring for renewal_workflow"
domain: "renewal_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_renewal_workflow
  - bld_schema_renewal_workflow
  - bld_output_template_renewal_workflow
  - p03_qg_expansion_play
  - p11_qg_audit_log
  - bld_instruction_renewal_workflow
  - p05_qg_github_issue_template
  - p01_qg_graph_rag_config
  - p11_qg_ai_rmf_profile
  - p09_qg_marketplace_app_manifest
---

## Quality Gate

## Definition
| Metric                      | Threshold | Operator | Scope                          |
|-----------------------------|-----------|----------|--------------------------------|
| Stage owner assignment      | 100%      | equals   | All 3 stages have named owners |
| GRR scenario coverage       | 100%      | equals   | Full + contraction + churn     |

## HARD Gates
| ID  | Check                                               | Fail Condition                                          |
|-----|-----------------------------------------------------|---------------------------------------------------------|
| H01 | YAML frontmatter valid                              | Invalid YAML syntax or missing required fields          |
| H02 | ID matches pattern ^p12_rw_[a-z][a-z0-9_]+\.yaml$ | ID format mismatch                                      |
| H03 | kind field = "renewal_workflow"                     | Kind field incorrect or missing                         |
| H04 | renewal_stage field present and valid enum          | Missing or invalid (must be 90_day/60_day/30_day/closed)|
| H05 | days_to_renewal field present and positive integer  | Missing or negative/zero value                          |
| H06 | GRR_impact field present and valid enum             | Missing or invalid (must be full/contraction_*/churn)   |
| H07 | Escalation path defined with health score threshold | No escalation path or no health score threshold         |
| H08 | Auto-renewal compliance specifies jurisdiction      | Generic notice period without named jurisdiction        |

## SOFT Scoring
| Dim | Dimension                                              | Weight | Scoring Guide                                                              |
|-----|--------------------------------------------------------|--------|----------------------------------------------------------------------------|
| D01 | Stage completeness (owner + tasks + automation trigger)| 0.25   | All 3 elements per stage = 1.0, 2 = 0.5, <2 = 0                          |
| D02 | Price-increase playbook specificity                    | 0.25   | % range + timing + objections + discount authority = 1.0, 2-3 = 0.5, <2 = 0|
| D03 | Multi-year incentive structure                         | 0.20   | Discount range + approval authority = 1.0, one only = 0.5, missing = 0   |
| D04 | GRR model completeness (3 scenarios)                   | 0.15   | All 3 modeled with ARR impact = 1.0, 2 = 0.5, <2 = 0                     |
| D05 | Compliance accuracy (jurisdiction-specific notices)    | 0.15   | Named jurisdictions with specific days = 1.0, partial = 0.5, generic = 0  |

## Actions
| Level  | Score  | Action                                            |
|--------|--------|---------------------------------------------------|
| GOLDEN | >=9.5  | Auto-publish; used as golden example              |
| PUBLISH| >=8.0  | Auto-publish after RevOps + Legal review          |
| REVIEW | >=7.0  | Require CS VP and Legal manual review             |
| REJECT | <7.0   | Reject; return to builder for rework              |

## Bypass
| Conditions                          | Approver           | Audit Trail               |
|-------------------------------------|--------------------|---------------------------|
| Contract end < 14 days emergency    | VP CS + CFO        | Escalation log in Gainsight|

## Examples

## Golden Example
```yaml
---
id: p12_rw_acme_corp_2026.yaml
kind: renewal_workflow
pillar: P12
title: "Acme Corp Renewal Workflow -- 2026-06-30"
contract_id: "SF-OPP-2024-0892"
renewal_stage: 90_day
days_to_renewal: 91
GRR_impact: full
multi_year_flag: true
current_ARR: "$240,000"
renewal_ARR: "$252,000"
health_score: 78
price_increase_pct: "5%"
auto_renewal: true
notice_period_days: 30
quality: null
---

# 90-Day Stage (Owner: CSM - Sarah Chen)
Tasks:
  - Send renewal intent email (relationship-first, no price discussion)
  - Review health score 78 -- above threshold, no escalation needed
  - Flag for multi-year: tenure 3yr + health 78 -- present 2yr offer at 60-day
  - Confirm economic buyer (CTO - James Liu) and procurement contact (Tom Walsh)
Automation: Gainsight CTA "Renewal 90 Days" fired 2026-04-01

# Price Increase Playbook
Announcement: 60-day stage -- 5% uplift ($240K -> $252K)
CSM Discount Authority: up to 2% ($5,040 max)
Manager Discount Authority: up to 4% ($9,600 max)
VP Discount Authority: up to 5% (full waiver)

# GRR Model
| Scenario     | ARR Impact | Notes                   |
|--------------|------------|-------------------------|
| Full Renewal | $252,000   | 5% uplift applied       |
| Contraction  | -$48,000   | Remove 20 seats risk    |
| Churn        | -$240,000  | Full loss scenario      |
| Net GRR      | 95%+       | Full renewal expected   |
```

## Anti-Example 1: Missing Escalation Triggers
```yaml
---
kind: renewal_workflow
renewal_stage: 90_day
---
# Stages
90-day: Send email, check in with customer
60-day: Send proposal
30-day: Try to close
Escalation: Escalate if needed
```
**Why it fails**: "If needed" is not an escalation trigger. There is no health score threshold, no named escalation owner, no SLA. CSMs will not know when or to whom to escalate. High-risk renewals will slip through without executive involvement.

## Anti-Example 2: Generic Compliance Language
```yaml
auto_renewal: true
notice_period_days: 30
```
Without specifying jurisdiction, "30 days" may be non-compliant. California requires 30 days for auto-renewal. EU GDPR may require different notice. Australia has its own consumer law requirements. Generic notice periods create legal exposure.

## Anti-Example 3: Expansion Play Misclassified as Renewal
```yaml
---
kind: renewal_workflow
title: "Acme Corp Renewal and Upsell"
---
# Renewal
Renew the current contract AND add 20 seats at renewal.
```
**Why it fails**: Seat upsell is an expansion_play, not a renewal_workflow. Renewal workflows protect existing ARR (GRR). Expansion plays grow net-new ARR within existing accounts (NRR > 100%). Conflating the two creates accountability confusion between CS (owns renewal) and AE (owns expansion).

## Golden Example 2 -- SMB High-Volume Low-Touch Renewal Workflow

```yaml
---
id: p12_rw_smb_lowtouch_template_2026.yaml
kind: renewal_workflow
pillar: P12
title: "SMB Low-Touch Renewal Workflow -- Template 2026"
segment: SMB
touch_model: low-touch
account_count_in_cohort: 847
current_ARR_per_account: "$12,000"
renewal_ARR_per_account: "$12,960"
price_increase_pct: "8%"
auto_renewal: true
auto_renewal_default: opt-out
notice_period_days: 45
multi_year_incentive_pct: "15%"
multi_year_ARR: "$11,016/yr (15% off x 2yr)"
health_score_nps_trigger: 6
GRR_target: "91%"
quality: null
---

# SMB Low-Touch Philosophy
At $12K ARR, CSM-to-account ratios cannot sustain white-glove renewal.
One CSM owns 180+ accounts. Every stage is automated-first; human intervention
fires ONLY when NPS < 6 or health score < 55.

# Gainsight Automated Playbook Configuration

playbook_name: "SMB Annual Renewal -- Low Touch 2026"
trigger: "days_to_renewal = 45"
owner_field: "account.csm_owner"
auto_advance_stages: true

## Stage 1: 45-Day Automated Notice (Owner: Gainsight automation)

Day 0 (D-45):
  action: send_email
  template: "smb_renewal_notice_45d"
  sender: "{{account.csm_owner.first_name}} at StackFlow"
  subject: "Your StackFlow subscription renews on {{renewal_date}}"
  body_highlights:
    - "Auto-renews at $12,960/yr (8% price adjustment from $12,000)"
    - "Cancel or change by {{cancel_by_date}} to avoid charge"
    - "Lock in 2 years now: $11,016/yr -- save $1,944/yr"
    - "Questions? Reply to this email or book 15 min: {{csm_calendar_link}}"
  compliance_notice: >
    "Per our Terms of Service (Section 9.2), auto-renewal applies unless
    cancelled 30+ days before renewal date. This notice satisfies the 45-day
    advance notice requirement."
  gainsight_log: "CTA: SMB Renewal Notice Sent -- D45"

## Stage 2: 30-Day Multi-Year Push (Owner: Gainsight automation)

Day 15 (D-30):
  action: send_email
  condition: "no cancellation request received AND no multi-year signed"
  template: "smb_multiyear_offer_30d"
  subject: "Save $1,944/yr -- 2-year option closes {{offer_expiry}}"
  offer:
    annual_current: "$12,960/yr"
    multi_year_rate: "$11,016/yr"
    discount: "15% off"
    min_term: "2 years"
    payment_options: ["annual upfront x2", "annual upfront x1 with year-2 locked"]
    stripe_coupon: "MULTIYEAR15_2026"
    offer_expiry: "renewal_date minus 14 days"
  gainsight_log: "CTA: Multi-Year Offer Sent -- D30"

## Stage 3: Health Check Gate (Owner: Gainsight rules engine, daily)

health_score_check:
  frequency: daily
  threshold_human_intervention: 55
  action_if_below_threshold:
    - create_gainsight_cta: "At-Risk SMB -- Human Review Required"
    - assign_to: "account.csm_owner"
    - sla_hours: 24
    - cta_priority: red

nps_check:
  trigger: "in-product NPS survey response received"
  threshold_human_intervention: 6
  action_if_below_threshold:
    - create_gainsight_cta: "NPS Detractor -- SMB Renewal at Risk"
    - assign_to: "account.csm_owner"
    - sla_hours: 8
    - cta_priority: red
    - pre_populate_email_draft: true

CSM save script for NPS < 6 accounts:
  objective: "understand friction before discussing renewal"
  opening: >
    "Hi {{first_name}}, I saw your recent feedback score and wanted to reach
    out before your renewal. I would rather understand what is not working
    than lose you. Can we spend 15 minutes this week?"
  CSM_discount_authority: "up to 2 months free extension (not a price cut)"
  escalation_to_manager: "if CSM cannot resolve in 48h"

## Stage 4: 14-Day Final Sequence (Owner: Gainsight automation)

Day 31 (D-14):
  action: send_email
  condition: "no cancellation AND no reply to prior emails"
  template: "smb_final_reminder_14d"
  subject: "14 days until your StackFlow subscription renews"
  body: >
    "Your subscription renews automatically on {{renewal_date}} at $12,960/yr.
    No action needed to continue. To cancel or make changes, contact us
    by {{cancel_by_date}}: support@stackflow.io or reply to this email."
  gainsight_log: "CTA: Final Reminder Sent -- D14"

## Stage 5: Renewal Event (Owner: Stripe + Gainsight)

renewal_day:
  stripe_action: "subscription.cycle -- charge {{renewal_ARR}} annually"
  gainsight_action: "close CTA as Won, update ARR field, fire renewal_complete signal"
  csm_notification: "Slack #renewals-smb: Account {{account_name}} renewed at $12,960 [auto]"

cancellation_before_renewal:
  stripe_action: "subscription.cancel_at_period_end = true"
  gainsight_action: "close CTA as Lost, tag churn_reason from cancellation survey"
  cancellation_survey: "Typeform -- 3 questions, required before self-serve cancel"
  churn_reason_taxonomy: [price, missing_feature, switching_competitor, no_longer_needed, budget_cut]

# GRR Model -- SMB Cohort 847 Accounts

| Scenario              | Account Count | ARR Impact      | GRR Contribution |
|-----------------------|---------------|-----------------|------------------|
| Auto-renew (no touch) | 721 (85%)     | +$9,346,560     | baseline         |
| Multi-year converted  | 68 (8%)       | +$749,088/yr    | GRR uplift       |
| NPS save (CSM)        | 25 (3%)       | +$324,000 saved | churn prevention |
| Churn (lost)          | 33 (4%)       | -$396,000       | GRR drag         |
| Net GRR               | --            | 91.4%           | target: 91%      |

Revenue math:
  beginning_ARR_cohort: "$10,164,000"
  renewed_ARR: "$9,296,640"
  net_GRR: "91.5%"

# Price Increase Communication

8% increase rationale (included in 45-day email):
  - "Infrastructure and AI feature investment in 2025 drove costs up 12%"
  - "Your rate has been flat for 2 years"
  - "8% increase = $960/yr -- less than one additional user license"
  - "Lock in 2 years now to avoid next year's potential increase"

Objection handling (CSM playbook for NPS-flagged accounts):
  "too expensive":
    response: "I understand. The 2-year lock removes exposure to any future increase.
               At $11,016/yr you save $1,944 versus staying monthly. Want me to
               send the order form now?"
    authority: "CSM can offer 1 month free on top of multi-year. Manager can offer 2."
  "switching to competitor":
    response: "Which tool are you evaluating? I want to understand if there is
               a feature gap we can close before renewal."
    escalation: "CSM flags to product team within 24h -- logged in Gainsight"
```

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
