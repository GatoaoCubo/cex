---
id: renewal_workflow_n06
kind: renewal_workflow
pillar: P12
nucleus: n06
title: "Renewal Workflow -- Automated Renewal and Retention Orchestration"
version: 1.0.0
quality: 9.0
tags: [renewal, workflow, retention, orchestration, commercial, automated]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_instruction_churn_prevention_playbook
  - bld_instruction_renewal_workflow
  - p10_lr_renewal_workflow_builder
  - bld_config_renewal_workflow
  - bld_examples_renewal_workflow
  - bld_output_template_renewal_workflow
  - bld_knowledge_card_renewal_workflow
  - bld_output_template_churn_prevention_playbook
  - renewal-workflow-builder
  - p12_sp_renewal_workflow_builder
---

# Renewal Workflow: Automated Renewal and Retention Orchestration

## Purpose

Automates the full renewal lifecycle: from early signal detection through close or win-back. Renewals are NOT passive events -- they are actively managed revenue moments with defined trigger sequences, escalation protocols, and success criteria.

## Workflow Architecture

```
DETECT: renewal_date - 30 days
    |
    v
ASSESS: pull customer entity -> health_score, churn_risk, expansion_potential
    |
    +-- health >= 70, risk low -> STANDARD track
    |
    +-- health 40-70, risk medium -> ENGAGEMENT track
    |
    +-- health < 40, risk high -> SAVE track
    |
    v
EXECUTE track-specific sequence
    |
    v
MEASURE outcome: renewed | upgraded | downgraded | churned
    |
    v
UPDATE entity + signal + log
```

## Track: STANDARD (health >= 70, risk: low)

```
Day -30: Renewal value email
  Subject: "Your [tier] renewal is coming up -- here's what you've built"
  Content:
    - Usage recap: "You ran [N] builds this month, saving ~[hours] hours"
    - Value delivered: top artifact types by frequency
    - Annual upgrade offer: "Switch to annual and get [months] months free"
  CTA: [Renew annual] | [Keep monthly]

Day -7: Renewal reminder
  Subject: "Your renewal renews in 7 days"
  Content: brief reminder + annual offer still available
  CTA: [Manage subscription]

Day 0: Stripe auto-charges (no action if payment succeeds)

Day +1: Success confirmation
  Subject: "You're all set for another [period]"
  Content: "Here's what's coming for [month]: [planned improvements]"
```

## Track: ENGAGEMENT (health 40-70, risk: medium)

```
Day -30: Personalized reactivation email
  Subject: "We noticed you haven't used [underutilized feature]"
  Content:
    - Specific usage gap identified
    - Tutorial or quick-win for that feature
    - "Before you renew, let us show you what you might be missing"
  CTA: [Book 15-min session] | [Watch tutorial]

Day -14: CSM review
  Action: CSM reviews entity, decides:
    - If fixable engagement gap: book customer call
    - If low value fit: let renew without touch (low priority save)
    - If confused/frustrated: proactive outreach

Day -7: Save offer (if engagement gap unresolved)
  Subject: "We want to make sure CEX is working for you"
  Content:
    - Acknowledge they may not be getting full value
    - Offer: 30-min onboarding session (value: $299, free for them)
    - Pair with: 1 month free credit if they complete the session
  CTA: [Book session + claim credit]

Day -3: Final renewal reminder + feature highlight
Day 0: Auto-renewal

Day +1-7: Activation check
  If session completed: monitor builds/week for next 14 days
  If no improvement: escalate to SAVE track for next renewal
```

## Track: SAVE (health < 40, risk: high)

```
Day -30: CSM priority assignment
  Action: CSM assigned within 24h of detection
  CSM brief includes:
    - Full entity dump (health, churn signals, usage history)
    - Recommended save offer
    - Decision: fight for renewal OR let churn gracefully

Day -21: CSM outreach call
  Script: "We noticed your usage has changed -- are we still solving the right problem for you?"
  Listen for: project ended | team change | budget cut | competitor switch
  Respond with: appropriate save play from churn_prevention_playbook

Day -14: Save offer deployed
  Based on stated reason:
    - Budget: annual at 20% off + 1 month free = ~37% effective discount
    - Project ended: pause option (2 months pause at 50% rate)
    - Missing feature: roadmap commitment + free PRO upgrade if feature lands
    - Competitor: competitive objection handling

Day -7: Follow-up if offer not accepted
  Options:
    a. Escalate to exec sponsor
    b. Downgrade to lower tier (preserve revenue)
    c. Accept churn gracefully + set win-back sequence

Day 0: Outcome logged
```

## Outcome Measurement

```yaml
renewal_outcomes:
  renewed_same_tier:
    outcome: base
    nrr_impact: 100% (neutral)
    follow_up: annual upgrade offer at day 60
  
  renewed_upgraded:
    outcome: expansion
    nrr_impact: >100% (positive)
    follow_up: activation check for new tier features
  
  renewed_downgraded:
    outcome: contraction
    nrr_impact: <100% (negative, better than churn)
    follow_up: engagement track for next renewal
  
  churned:
    outcome: lost
    nrr_impact: 0% (fully negative)
    follow_up: win-back sequence at 30, 60, 90 days
```

## Win-Back Sequence (Post-Churn)

```
Day 30 post-churn: "We've been busy since you left" email
  Content: top 3 improvements since they churned
  CTA: See what's new (no direct sales push)

Day 60: "Special offer for former [tier] customers"
  Content: 50% off first month + preserved data reactivation
  CTA: Come back at 50% off (48h limit)

Day 90: Final win-back
  Content: "Last chance to reclaim your [brand_config / builds / data] at [tier] pricing"
  CTA: Reactivate with 1 month free trial

Day 180: Archive + remove from active sequences
```

## Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Gross revenue retention | (MRR_renewed) / (MRR_up_for_renewal) | >90% |
| Net revenue retention | (renewed + expansion - contraction) / MRR_up | >110% |
| Renewal rate | accounts_renewed / accounts_up | >85% |
| Save rate | accounts_saved / save_attempts | >40% |
| Win-back rate | accounts_reactivated / churned | >10% |


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_churn_prevention_playbook]] | upstream | 0.42 |
| [[bld_instruction_renewal_workflow]] | upstream | 0.40 |
| [[p10_lr_renewal_workflow_builder]] | upstream | 0.39 |
| [[bld_config_renewal_workflow]] | upstream | 0.34 |
| [[bld_examples_renewal_workflow]] | upstream | 0.34 |
| [[bld_output_template_renewal_workflow]] | upstream | 0.33 |
| [[bld_knowledge_card_renewal_workflow]] | upstream | 0.33 |
| [[bld_output_template_churn_prevention_playbook]] | upstream | 0.31 |
| [[renewal-workflow-builder]] | related | 0.30 |
| [[p12_sp_renewal_workflow_builder]] | related | 0.28 |
