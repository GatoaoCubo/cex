---
kind: quality_gate
id: p03_qg_expansion_play
pillar: P11
llm_function: GOVERN
purpose: Quality gate with HARD and SOFT scoring for expansion_play
quality: 9.1
title: "Quality Gate Expansion Play"
version: "1.0.0"
author: wave6_n06
tags: [expansion_play, builder, quality_gate, NRR, upsell, land-and-expand]
tldr: "Quality gate with HARD and SOFT scoring for expansion_play"
domain: "expansion_play construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - bld_examples_expansion_play
  - p12_qg_renewal_workflow
  - bld_instruction_expansion_play
  - p11_qg_audit_log
  - bld_schema_expansion_play
  - p05_qg_github_issue_template
  - bld_output_template_expansion_play
  - p03_sp_expansion_play_builder
  - p01_qg_graph_rag_config
  - p07_qg_cohort_analysis
---

## Quality Gate

## Definition
| Metric                        | Threshold | Operator | Scope                        |
|-------------------------------|-----------|----------|------------------------------|
| Expansion trigger specificity | 100%      | equals   | All quantified, time-bounded |
| NRR model completeness        | 100%      | equals   | Expansion + contraction + churn |

## HARD Gates
| ID  | Check                                              | Fail Condition                                          |
|-----|----------------------------------------------------|---------------------------------------------------------|
| H01 | YAML frontmatter valid                             | Invalid YAML syntax or missing required fields          |
| H02 | ID matches pattern ^p03_ep_[a-z][a-z0-9_]+\.md$  | ID format mismatch                                      |
| H03 | kind field = "expansion_play"                      | Kind field incorrect or missing                         |
| H04 | expansion_type field present and valid enum        | Missing or invalid (must be seat_upsell/tier_upgrade/cross_sell/usage_ramp) |
| H05 | trigger_type field present and valid enum          | Missing or invalid trigger type                         |
| H06 | NRR_target field present and numeric              | Missing or non-numeric (e.g., "good NRR" fails)         |
| H07 | Account map contains minimum 2 stakeholders        | Only 1 or zero stakeholders identified                  |
| H08 | Talk track has hook + ask + next step sections     | Missing any of the three required sections              |

## SOFT Scoring
| Dim | Dimension                                            | Weight | Scoring Guide                                                           |
|-----|------------------------------------------------------|--------|-------------------------------------------------------------------------|
| D01 | Trigger quantification (specific threshold + window) | 0.25   | Specific % + time window = 1.0, one dimension only = 0.5, vague = 0   |
| D02 | NRR model accuracy (all 3 components present)        | 0.25   | All 3 (expansion, contraction, churn) = 1.0, 2 = 0.5, <2 = 0          |
| D03 | Talk track quality (hook-value-case-ask-next)        | 0.20   | All 5 sections = 1.0, 3-4 = 0.5, <3 = 0                               |
| D04 | Account map depth (buyer + champion + blocker)       | 0.15   | 3+ stakeholders = 1.0, 2 = 0.5, 1 = 0                                 |
| D05 | QBR alignment (customer metrics, not internal)       | 0.15   | Customer-facing metrics only = 1.0, mixed = 0.5, internal only = 0    |

## Actions
| Level  | Score  | Action                                      |
|--------|--------|---------------------------------------------|
| GOLDEN | >=9.5  | Auto-publish; used as golden example        |
| PUBLISH| >=8.0  | Auto-publish after AE/CSM lead review       |
| REVIEW | >=7.0  | Require RevOps or CS lead manual review     |
| REJECT | <7.0   | Reject; return to builder for rework        |

## Bypass
| Conditions                     | Approver        | Audit Trail              |
|--------------------------------|-----------------|--------------------------|
| Emergency QBR prep (<48h)      | VP CS or VP Sales| Escalation log in CRM   |

## Examples

## Golden Example
```markdown
---
id: p03_ep_acme_seat_upsell_q2.md
kind: expansion_play
pillar: P03
title: "Acme Corp -- Seat Upsell Expansion Play Q2 2026"
account_segment: ENT
expansion_type: seat_upsell
trigger_type: usage_threshold
NRR_target: ">120%"
current_ARR: "$240,000"
expansion_ARR: "$48,000"
quality: null
---

## Expansion Trigger
| Signal              | Threshold                  | Time Window | Alert Owner |
|---------------------|----------------------------|-------------|-------------|
| Seat utilization    | >85% of 120 licensed seats | 21 days     | CSM (Sarah) |
| Active users/week   | >100 WAU (of 120 licensed) | 14 days     | CSM (Sarah) |

## Account Map
| Role           | Name            | Influence | Action               |
|----------------|-----------------|-----------|----------------------|
| Economic Buyer | CTO - James Liu | High      | Budget sign-off $50K+|
| Champion       | VP Eng - Ana M. | High      | Internal advocacy    |
| Blocker        | Procurement - T.| Medium    | PO process 30-day SLA|

## NRR Model
| Component      | ARR Impact  | Notes                           |
|----------------|-------------|----------------------------------|
| Beginning ARR  | $240,000    | Annual contract value            |
| Expansion ARR  | +$48,000    | 20 additional seats x $2,400/yr  |
| Contraction    | -$0         | No identified risk               |
| Projected NRR  | 120%        | $288K / $240K                    |
```

## Anti-Example 1: Vague Triggers
```markdown
---
kind: expansion_play
title: Acme Upsell Play
---
## Trigger
The account seems to be using the product heavily and the team is growing.
Consider reaching out when the timing feels right.
```
**Why it fails**: "Seems to be using heavily" and "when timing feels right" are not quantified triggers. There is no threshold, no time window, no owner. This cannot be automated or measured. The play will never fire reliably.

## Anti-Example 2: Missing NRR Model
```markdown
---
kind: expansion_play
NRR_target: "good"
---
## Expansion
Adding 20 seats will increase revenue and help us hit NRR targets.
```
**Why it fails**: "Good" is not a numeric NRR target. No beginning ARR, no expansion ARR, no contraction risk modeled. RevOps cannot forecast from this. The play provides zero commercial accountability.

## Anti-Example 3: Churn Play Misclassified as Expansion
```markdown
---
kind: expansion_play
title: "Acme Retention Play"
expansion_type: seat_upsell
---
## Trigger
Account health score dropped to 45. We need to save this account.
```
**Why it fails**: Health score 45 is a churn risk signal, not an expansion trigger. This belongs in churn_prevention_playbook, not expansion_play. Expansion plays require positive usage signals -- seats being consumed, adoption growing, value being realized.

## Golden Example 2 -- Product-Led Growth Plan Upgrade Expansion (Free to Pro)

```markdown
---
id: p03_ep_plg_free_to_pro_upgrade.md
kind: expansion_play
pillar: P03
title: "FeedbackLoop PLG -- Free to Pro Tier Upgrade Expansion Play"
account_segment: SMB_PLG
expansion_type: plan_upgrade
trigger_type: feature_quota_threshold
growth_motion: product-led
current_ARR: "$0"
expansion_ARR: "$3,600"
NRR_target: ">110% (cohort blended, free-to-paid included as 0 base)"
conversion_target_rate: "18% of free accounts hitting trigger within 90 days"
quality: null
---

## Expansion Context -- PLG Motion

FeedbackLoop is a B2B feedback collection SaaS. Free tier is the acquisition
layer. Pro tier ($300/mo or $3,600/yr) unlocks unlimited surveys, AI analysis,
custom branding, and API access. Expansion ARR = $0 -> $3,600 per converted
account. NRR model treats free accounts as 0 base, so every conversion is
net-new ARR with no contraction risk.

This play fires entirely in-product and via Stripe. No CSM involvement
at trigger time. Human SDR engages only if 3 in-app prompts fired with
no conversion after 14 days.

## Expansion Trigger

| Signal                    | Threshold              | Time Window | Measurement Tool     |
|---------------------------|------------------------|-------------|----------------------|
| Survey responses received | >= 80% of 100/mo quota | 30 days     | FeedbackLoop internal DB |
| AI analysis runs          | >= 8 of 10/mo quota    | 30 days     | FeedbackLoop internal DB |
| Active team members       | >= 3 users on free acct| 7 days      | FeedbackLoop internal DB |

Trigger logic (all three conditions OR any single condition reaching 100%):
```sql
SELECT account_id, survey_count_30d, ai_runs_30d, active_users_7d
FROM account_usage_daily
WHERE (survey_count_30d >= 80 OR ai_runs_30d >= 8 OR active_users_7d >= 3)
  AND plan_tier = 'free'
  AND created_at < CURRENT_DATE - INTERVAL '7 days'
ORDER BY survey_count_30d DESC;
```

Event published: `usage.quota_threshold_hit` -> triggers upgrade_nudge_flow

## In-App Upgrade Prompt Sequence

Prompt fires at the moment of quota threshold hit (real-time, via Segment event).

### Prompt A -- Soft nudge (first hit, in-app banner)

Location: top of dashboard, dismissible
Copy:
```
"You are at 80% of your monthly survey limit.
Pro removes the cap -- unlimited surveys, AI analysis, and custom branding.
[See what Pro includes ->]  [Not now]"
```
Deep link: /upgrade/pro (Stripe Checkout session, pre-filled plan=pro_annual)
Dismiss behavior: hide for 3 days, re-show if another threshold hit occurs
Amplitude event logged: `upgrade_prompt_A_shown`

### Prompt B -- Value anchor (D+3 if no conversion, modal)

Trigger: Prompt A dismissed AND 3 days elapsed AND still on free plan
Location: full-screen modal on next login
Copy:
```
"You have collected 840 responses this month.
That is 84% of your free plan limit (1,000 max).

Pro teams collect 10x more feedback and analyze it with AI in seconds.
Start Pro today: $300/mo or $3,600/yr (save $360).

[Start Pro -- $300/mo]  [Get annual and save $360]  [I'll stay on free]"
```
Stripe Checkout: two CTAs launch separate Stripe sessions (monthly vs. annual)
Amplitude event logged: `upgrade_prompt_B_shown`, `upgrade_modal_cta_clicked`

### Prompt C -- Scarcity + SDR handoff trigger (D+7 if no conversion)

Trigger: Prompt B dismissed AND 7 days elapsed AND >= 1 quota hit this month
Location: in-app notification + email from SDR
Copy (in-app):
```
"Your team hit the survey limit 2 times this month.
Every time you hit the cap, you are leaving feedback uncollected.
A FeedbackLoop specialist can show you how Pro teams use this data.
[Book 15 minutes ->]  [Upgrade directly ->]"
```
Email (sent from SDR named sender via HubSpot):
```
Subject: "You maxed out FeedbackLoop twice -- I want to help"
Body: "Hi Sarah, I noticed your team hit the free plan limit twice
this month. That means missed responses at critical moments.
I have 15 minutes open tomorrow -- want me to show you what Pro unlocks?
[Book now] or reply with a time that works."
```
Amplitude event logged: `upgrade_prompt_C_shown`
HubSpot: contact property `plg_upgrade_sdl_flag = true`, auto-create task for SDR

## Stripe Upgrade Flow

Stripe Checkout config:
```json
{
  "mode": "subscription",
  "line_items": [
    {
      "price": "price_pro_monthly_300",
      "quantity": 1
    }
  ],
  "allow_promotion_codes": true,
  "billing_address_collection": "required",
  "success_url": "https://app.feedbackloop.io/upgrade/success?session_id={CHECKOUT_SESSION_ID}",
  "cancel_url": "https://app.feedbackloop.io/dashboard?upgrade_cancelled=true",
  "metadata": {
    "account_id": "acct_STRIPE_SESSION_ID_DYNAMIC",
    "trigger_source": "plg_quota_threshold",
    "prompt_version": "C"
  }
}
```

On `checkout.session.completed` webhook:
- FeedbackLoop API: account.plan = pro, quota_limits = null (unlimited)
- Amplitude: `plan_upgraded` event (properties: from=free, to=pro, source=plg_in_app)
- HubSpot: deal created "PLG Upgrade -- [account.name]" Stage=Closed Won, ARR=$3,600
- Slack #plg-conversions: "New Pro conversion: [account.name] via [prompt.version]"

## NRR Model -- PLG Cohort (Free Accounts Hitting Trigger)

| Component              | Value        | Notes                                        |
|------------------------|--------------|----------------------------------------------|
| Cohort size (monthly)  | 340 accounts | free accounts hitting quota threshold         |
| Conversion rate target | 18%          | industry benchmark: 15-22% for PLG B2B SaaS  |
| Monthly conversions    | ~61 accounts | 340 x 18%                                    |
| Expansion ARR/account  | $3,600/yr    | Pro annual (incentivized over monthly)        |
| Monthly expansion ARR  | $220,000/yr  | 61 x $3,600                                  |
| Beginning ARR (free)   | $0           | free accounts have no ARR base                |
| NRR (cohort blended)   | N/A          | free-to-paid: tracked as new ARR, not NRR     |
| Blended NRR (all accts)| 118%         | including expansion from existing paid accts  |

Annual target: 730 free-to-Pro conversions = $2.6M new ARR from PLG motion alone.

## Funnel Measurement (Amplitude)

| Funnel Stage              | Event                          | Target Rate |
|---------------------------|--------------------------------|-------------|
| Trigger hit               | usage.quota_threshold_hit      | 100% (baseline) |
| Prompt A shown            | upgrade_prompt_A_shown         | 100% of trigger |
| Prompt A CTA clicked      | upgrade_cta_A_clicked          | >= 22%          |
| Checkout started          | checkout_session_created       | >= 18%          |
| Plan upgraded             | plan_upgraded                  | >= 15%          |
| Still Pro at D+90         | subscription.active (D+90)     | >= 85%          |

Amplitude dashboard: "PLG Upgrade Funnel" with weekly cohort view.
A/B test: Prompt B copy variant (value anchor vs. social proof -- "2,400 teams use Pro").
```

### H_RELATED: Cross-Reference Check (HARD)
- [ ] `related:` frontmatter field populated (min 3 entries)
- [ ] `## Related Artifacts` section present in artifact body
- [ ] At least 1 upstream and 1 downstream or sibling reference
- Gate: REJECT if < 3 entries (auto-populated by cex_wikilink.py at F6.5)
