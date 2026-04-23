---
id: referral_program_n06
kind: referral_program
pillar: P11
nucleus: n06
title: "Referral Program -- Customer Acquisition via Word-of-Mouth Engine"
version: 1.0.0
quality: 9.1
tags: [referral, acquisition, viral, growth, incentive, commercial]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_knowledge_card_referral_program
  - bld_instruction_referral_program
  - referral-program-builder
  - n06_funnel_cex_product
  - p03_sp_referral_program_builder
  - bld_examples_referral_program
  - n06_intent_resolution_depth_spec
  - bld_collaboration_referral_program
  - p11_qg_referral_program
  - bld_architecture_referral_program
---

# Referral Program: Word-of-Mouth Revenue Engine

## Strategic Intent

Referral programs exploit the highest-trust acquisition channel (peer recommendation) at the lowest CAC. For N06, referral is the primary viral growth loop: satisfied customers become distribution channels. Target: 30% of new paid signups via referral within 12 months.

## Program Structure

### Incentive Model: Dual-Sided

```
Referrer (existing customer) gets:
  - 1 month free on their plan for each referral who converts to paid
  - Credited to next invoice (no cash out needed)
  - Stackable: 5 referrals = 5 months free (PRO = $745 value)
  - Cap: 12 months credit per year per referrer

Referee (new customer) gets:
  - 1 month free on any paid plan (STARTER or PRO)
  - Applied automatically on first invoice
  - Not stackable with other promotions

Enterprise referrals:
  - Cash incentive: $500 for verified Enterprise conversion
  - Paid 30 days post conversion (fraud prevention)
```

### Rationale for Dual-Sided

- Single-sided (referrer only): incentivizes referrer but no pull for referee
- Single-sided (referee only): referee advantage but referrer loses motivation
- Dual-sided: creates social contract -- referrer has skin in game AND gifts value to friend

## Mechanics

### Unique Referral Code

```
Format: {plan_tier}-{customer_id_prefix}-{random_4}
Example: pro-a1b2-x9k3

Generation: on account creation + in dashboard
```

### Attribution Flow

```
1. Referrer shares link: app.cex.com/signup?ref=pro-a1b2-x9k3
2. Cookie set: ref_code = "pro-a1b2-x9k3" (30-day expiry)
3. Referee signs up -> ref_code persisted to customer.metadata.referral_code
4. Referee converts to paid -> webhook checkout.session.completed fires
5. N06 checks customer.metadata.referral_code
6. If referral_code valid -> credit referrer + send notification
7. Log to referral_ledger (referrer_id, referee_id, reward_type, date)
```

### Tracking Schema

```json
{
  "referral_id": "ref_20260417_a1b2_x9k3",
  "referrer_customer_id": "cus_abc123",
  "referee_customer_id": "cus_def456",
  "referral_code": "pro-a1b2-x9k3",
  "signup_date": "2026-04-17T10:00:00Z",
  "conversion_date": "2026-04-20T14:00:00Z",
  "reward_type": "credit_1_month",
  "reward_value_cents": 14900,
  "reward_status": "applied",
  "plan_at_conversion": "pro"
}
```

## Activation Points

Prompt referral sharing at high-delight moments:

| Trigger | Channel | Message |
|---------|---------|---------|
| First successful build completed | In-app banner | "Love what you just built? Share CEX with a colleague -- you both get a month free." |
| Builds quota at 50% usage | Email | "You're halfway through your builds. Know someone who'd love this? Share for free months." |
| Plan upgrade completed | In-app | "Welcome to PRO! As a thanks, here's your referral link..." |
| NPS score >= 9 | In-app | "You gave us 9/10 -- would you share CEX with your network?" |
| Monthly usage anniversary | Email | "1 year with CEX! Refer a friend and keep the momentum going." |

## Anti-Fraud Controls

| Fraud Type | Detection | Prevention |
|-----------|-----------|-----------|
| Self-referral | Same email domain or payment fingerprint | Block if referee_id == referrer_id OR same card |
| Fake signups | Trial account with no builds in 14 days | Only reward on paid conversion, not signup |
| Bulk code sharing | >10 conversions/month per referrer | Manual review trigger at 10+ |
| Refund gaming | Refund after reward credited | 30-day hold before credit release |

## Performance Metrics

| Metric | Formula | Target |
|--------|---------|--------|
| Referral rate | referred_signups / total_signups | >20% |
| Referral conversion | referred_paid / referred_signups | >40% |
| Viral coefficient (K) | referrals_sent per user * referral_conversion | >0.3 |
| CAC via referral | rewards_paid / referred_paid_customers | <$30 |
| Referral revenue share | referral_mrr / total_mrr | >25% |

## Cohort Impact Tracking

Referred customers vs organic:
- Churn rate (hypothesis: lower, 15-20% better retention)
- LTV (hypothesis: higher, better ICP match from peer recommendation)
- Time-to-activation (hypothesis: faster, pre-sold by referrer)
- Expansion rate (hypothesis: higher, team context from referrer)

Track via `cohort_analysis_n06.md` with `acquisition_channel = referral`.


## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_referral_program]] | upstream | 0.41 |
| [[bld_instruction_referral_program]] | upstream | 0.36 |
| [[referral-program-builder]] | related | 0.34 |
| [[n06_funnel_cex_product]] | related | 0.31 |
| [[p03_sp_referral_program_builder]] | upstream | 0.30 |
| [[bld_examples_referral_program]] | upstream | 0.28 |
| [[n06_intent_resolution_depth_spec]] | related | 0.27 |
| [[bld_collaboration_referral_program]] | downstream | 0.27 |
| [[p11_qg_referral_program]] | related | 0.26 |
| [[bld_architecture_referral_program]] | upstream | 0.26 |
