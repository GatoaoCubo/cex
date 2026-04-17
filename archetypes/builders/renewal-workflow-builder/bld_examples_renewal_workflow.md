---
kind: examples
id: bld_examples_renewal_workflow
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of renewal_workflow artifacts
quality: 9.1
title: "Examples Renewal Workflow"
version: "1.0.0"
author: wave6_n06
tags: [renewal_workflow, builder, examples, renewal, GRR, Gainsight, Salesforce]
tldr: "Golden and anti-examples of renewal_workflow artifacts"
domain: "renewal_workflow construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

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
