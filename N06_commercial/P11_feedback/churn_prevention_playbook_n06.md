---
id: churn_prevention_playbook_n06
kind: churn_prevention_playbook
pillar: P03
nucleus: n06
title: "Churn Prevention Playbook -- Retention Intervention by Signal and Tier"
version: 1.0.0
quality: 9.0
tags: [churn, retention, playbook, intervention, commercial, revenue-defense]
density_score: 1.0
related:
  - bld_output_template_churn_prevention_playbook
  - bld_examples_churn_prevention_playbook
  - p12_wf_cf_email_launch
  - email_sequence_template
  - kc_churn_prevention_playbook
  - bld_instruction_churn_prevention_playbook
  - n06_funnel_cex_product
  - bld_config_renewal_workflow
  - kc_subscription_tier
  - bld_collaboration_churn_prevention_playbook
---

# Churn Prevention Playbook

## Strategic Frame

Revenue defense is revenue generation. Every churned customer is a CAC write-off plus lost LTV. Strategic Greed demands we protect ARR with the same aggression we acquire it. This playbook defines the intervention chain: detect signal -> triage by tier -> execute play -> measure outcome.

## Churn Signal Taxonomy

```yaml
signals:
  behavioral:
    - builds_per_week < 2          # declining engagement
    - login_frequency < 2x_week   # disengagement
    - last_build_age > 14_days     # dormancy
    - support_tickets > 3_open    # frustration
    - feature_adoption < 30pct    # underutilization
  
  financial:
    - invoice.payment_failed       # payment failure (Stripe event)
    - subscription.cancel_at_period_end: true  # soft cancel
    - downgrade_attempt            # plan reduction request
    - refund_request               # strong churn signal
  
  lifecycle:
    - trial_day_3_no_build         # low-engagement trial
    - trial_day_10_no_brand_config # not set up
    - day_60_no_api_call           # PRO unused key feature
    - renewal_minus_30_days        # pre-renewal risk window
```

## Triage Matrix (Signal x Tier)

| Signal | FREE | STARTER | PRO | ENTERPRISE |
|--------|------|---------|-----|------------|
| builds < 2/week | email (activate) | email (reactivate) | CSM outreach | CSM + exec escalation |
| payment failed | email (update card) | email + SMS | CSM call | CSM + billing concierge |
| soft cancel | upgrade prompt | save offer 20% off | CSM save call | exec + custom offer |
| dormancy 14d | reactivation email | reactivation + case study | CSM scheduled |  CSM + QBR trigger |
| support 3+ tickets | auto-escalate | priority queue | CSM owns | dedicated resolution |

## Intervention Plays

### PLAY 1: Reactivation Email Sequence

Trigger: login_frequency < 2x/week AND builds < 2/week

```
Day 0: "We miss you" email
  Subject: "[Name], 3 builds you could do in 10 minutes"
  Body: Personalized use cases based on their industry + past builds
  CTA: "Start building now" (deep link to builder)

Day 3: Value reminder
  Subject: "What [similar company] built with CEX this week"
  Body: Social proof + specific artifact type relevant to their role
  CTA: "Try this template"

Day 7: Risk check
  Subject: "Are we solving the right problem for you?"
  Body: 3-question survey + direct calendar link for 15-min call
  CTA: "Tell us what's blocking you"

Day 14: Save offer (STARTER and above only)
  Subject: "We'd like to earn your trust back"
  Body: 30% off next 3 months + personal onboarding session
  CTA: "Claim offer" (limited time, expires 48h)
```

### PLAY 2: Payment Failure Recovery

Trigger: `invoice.payment_failed` Stripe event

```
Hour 0: Email -- "Payment issue on your CEX account"
  Tone: neutral, not accusatory
  CTA: "Update payment method" (link to Stripe customer portal)

Hour 24: Reminder email
  Escalate: SMS if mobile number on file

Hour 48: Account warning
  Email: "Access pauses in 24 hours"
  CTA: Update card OR contact support for alternative

Hour 72: Downgrade to FREE (not delete)
  Preserve all builds and brand_config
  Email: "Your account is paused -- data safe for 30 days"
  CTA: "Reactivate in 1 click"

Day 30: Final warning before data archive
Day 60: Archive (recoverable by support for 6 months)
```

### PLAY 3: Soft Cancel Save Sequence

Trigger: `cancel_at_period_end: true` set on subscription

```
Immediate: In-app exit survey
  "What's the main reason for canceling?"
  Options: [Too expensive | Missing feature | Switching to competitor | 
            Not using it enough | Project ended | Other]

Based on response:
  Too expensive:
    - Offer annual switch (20% off)
    - Offer pause (2-month pause at 50% price) if available
    
  Missing feature:
    - Connect to roadmap item if planned
    - Offer workaround walkthrough
    - Route to product team feedback

  Switching to competitor:
    - Run competitive differentiation script
    - Offer 1:1 comparison session
    
  Not using enough:
    - Offer onboarding session
    - Activate use-case-specific templates
    
  Project ended:
    - Offer pause option
    - Offer downgrade to FREE (preserve data)
```

### PLAY 4: Trial-to-Paid Conversion Defense

Trigger: Trial day 10 with <3 builds OR no brand_config

```
Day 1: Welcome + quick-win task (immediate value)
Day 3: "Your first build" reminder (if not done)
Day 7: Check-in email + book onboarding call
Day 10: "See what you built" recap + upgrade push
Day 12: Extended trial offer (if no conversion): +7 days for completing onboarding
Day 14: Trial end -- upgrade or downgrade to FREE (not delete)
```

## Measurement Framework

| Metric | Formula | Target |
|--------|---------|--------|
| Monthly churn rate | churned_customers / start_customers | <2% MoM |
| Churn save rate | saves / save_attempts | >35% |
| Reactivation rate | reactivated / dormant_targeted | >15% |
| Net Revenue Retention | (MRR_end - churn_MRR + expansion_MRR) / MRR_start | >110% |
| Average save value | saved_ARR / save_attempts | >$400 |

## Escalation Decision Tree

```
Payment failed?
  -> YES: Start PLAY 2 immediately
  -> NO: Continue...

Cancel requested?
  -> YES: Start PLAY 3 + in-app save immediately
  -> NO: Continue...

Engagement falling (builds < 2/week for 2 weeks)?
  -> YES: Start PLAY 1 (reactivation)
  -> NO: Continue...

Trial day > 10 and not converted?
  -> YES: Start PLAY 4 (trial conversion)
  -> NO: No intervention needed
```


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_output_template_churn_prevention_playbook]] | downstream | 0.33 |
| [[bld_examples_churn_prevention_playbook]] | downstream | 0.32 |
| [[p12_wf_cf_email_launch]] | downstream | 0.29 |
| [[email_sequence_template]] | downstream | 0.27 |
| [[kc_churn_prevention_playbook]] | upstream | 0.27 |
| [[bld_instruction_churn_prevention_playbook]] | related | 0.26 |
| [[n06_funnel_cex_product]] | downstream | 0.26 |
| [[bld_config_renewal_workflow]] | downstream | 0.23 |
| [[kc_subscription_tier]] | upstream | 0.23 |
| [[bld_collaboration_churn_prevention_playbook]] | downstream | 0.22 |
