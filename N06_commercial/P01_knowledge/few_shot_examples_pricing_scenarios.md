---
id: few_shot_examples_pricing_scenarios
kind: knowledge_card
pillar: P01
nucleus: n06
title: "Few-Shot Examples -- N06 Pricing Decision Reasoning (4 Scenarios)"
version: 1.0.0
quality: 9.0
updated: 2026-04-17
tags: [few-shot, pricing, ltv, churn, referral, reasoning, examples, commercial]
type: few_shot_examples
---

# Few-Shot Examples: N06 Pricing Decision Reasoning

## Purpose

Four complete worked examples showing how N06 applies Strategic Greed reasoning
to pricing, LTV, churn, and referral design. Each example: problem -> 8F trace
-> structured output. Use these to ground any LLM operating in the commercial domain.

---

## Example 1: Design SaaS Pricing Tiers

**Problem statement:** A B2B SaaS product serves solo consultants, marketing teams,
and enterprise departments. Revenue goal: $1M ARR in 12 months. Design the tier architecture.

### 8F Trace Summary

| Stage | Action |
|-------|--------|
| F1 CONSTRAIN | kind=subscription_tier, pillar=P11, domain=saas-pricing |
| F2 BECOME | load subscription-tier-builder, strategic-greed lens: maximize each revenue stream |
| F3 INJECT | kc_ai_saas_monetization.md + enum_def_pricing_tiers.md + roi_calculator_n06.md |
| F4 REASON | 3 commercial tiers + FREE, differentiated by seats/API/support; annual discount lever |
| F5 CALL | competitor pricing scan, willingness-to-pay benchmarks, CAC payback constraint |
| F6 PRODUCE | 4-tier architecture with upgrade triggers and cannibalization guard |
| F7 GOVERN | validate: tiers differentiated? PRO vs ENTERPRISE gap >= $350? no STARTER cannibalizes PRO? |
| F8 COLLABORATE | save subscription_tier_n06.md, signal n06 complete |

### Structured Output

```yaml
tiers:
  FREE:
    monthly_price: 0
    purpose: "acquisition funnel -- create desire, limit to 10 builds"
    hard_limits: [builds_per_month=10, seats=1, no_brand_config, no_api]
    upgrade_trigger: builds_quota_exhausted OR brand_config_attempted

  STARTER:
    monthly_price: 49
    annual_price: 470  # 20% off = 2 months free framing
    purpose: "create dependency -- unlock brand_config, raise build limit"
    hard_limits: [builds_per_month=100, seats=1, no_api, no_n03]
    upgrade_trigger: api_access_requested OR second_seat_invited

  PRO:
    monthly_price: 149
    annual_price: 1430
    purpose: "team adoption -- API unlocked, 5 seats, full nucleus access"
    hard_limits: [seats=5, no_sso, no_sla]
    upgrade_trigger: seats_at_capacity OR sso_requested

  ENTERPRISE:
    monthly_price: 500
    billing: custom_annual
    purpose: "contracts -- SSO, SLA, unlimited seats, data residency"
    differentiators: [sso, 99.9_sla, unlimited_seats, custom_integrations]

revenue_path_to_1M_arr:
  starter_customers_needed: 1020 # at $49/mo avg = $49K/mo -> $588K ARR
  pro_customers_needed: 280      # at $149/mo avg -> $418K ARR
  enterprise_customers_needed: 0  # bonus upside
  total_arr: 1006000

cannibalization_guard:
  starter_vs_pro: "STARTER has no API, no N03, 1 seat -- power users MUST upgrade"
  pro_vs_enterprise: "PRO caps at 5 seats, no SSO, no SLA -- teams MUST upgrade"
```

**Key decision:** Annual discount (20%) presented as "2 months free" -- increases
upfront cash flow, reduces churn 35-60%, targets 45% annual conversion rate.

---

## Example 2: Calculate LTV for Enterprise Segment

**Problem statement:** Enterprise customer signs at $2,000/mo with 15% annual churn.
What is LTV? Is CAC of $8,000 acceptable? Calculate and frame for a board conversation.

### 8F Trace Summary

| Stage | Action |
|-------|--------|
| F1 CONSTRAIN | kind=knowledge_card (analysis), pillar=P01, domain=ltv-cac |
| F2 BECOME | N06 strategic-greed lens: maximize LTV visibility, challenge CAC assumptions |
| F3 INJECT | roi_calculator_n06.md, subscription_tier_n06.md, cohort_analysis patterns |
| F4 REASON | standard LTV formula + gross margin overlay + expansion MRR adjustment |
| F5 CALL | calculate 3 scenarios (base, optimistic, pessimistic) with NRR sensitivity |
| F6 PRODUCE | LTV table + CAC verdict + board-ready framing |
| F7 GOVERN | validate: gross margin applied? expansion MRR included? payback period shown? |
| F8 COLLABORATE | persist to entity_memory or knowledge_card |

### Structured Output

```
ENTERPRISE SEGMENT: LTV / CAC ANALYSIS

Inputs:
  MRR:          $2,000/month ($24,000 ARR)
  Churn:        15% annual = 1.25% monthly
  Gross margin: 75% (assumed SaaS standard)
  NRR:          110% (expansion revenue from existing accounts)

Formula:
  LTV = (ARPU * Gross Margin) / Churn Rate (monthly)
  LTV = ($2,000 * 0.75) / 0.0125 = $120,000

With NRR adjustment (NRR > 100% means expansion outpaces churn):
  Effective churn = max(0, churn_rate - (NRR - 1) / 12)
                  = max(0, 0.0125 - 0.00083) = 0.01167
  LTV_adjusted    = $1,500 / 0.01167 = $128,536

CAC Verdict:
  CAC:              $8,000
  LTV/CAC ratio:    $120,000 / $8,000 = 15.0x
  Benchmark:        LTV/CAC >= 3x = acceptable | >= 5x = strong | >= 10x = excellent
  Verdict:          EXCELLENT (15x). CAC of $8,000 is conservative.

Payback:
  Payback period = CAC / (MRR * gross_margin)
                 = $8,000 / ($2,000 * 0.75) = 5.3 months
  Benchmark:     SaaS payback < 12 months = healthy

Board framing:
  "Each enterprise customer we sign costs $8,000 to acquire and returns
   $120,000 in lifetime value -- a 15x ratio. At current churn (15% annual),
   we recover CAC in 5.3 months. If we reduce churn to 10%, LTV climbs
   to $180,000 (22.5x). Every point of churn we prevent is worth $8,000
   in LTV -- more than the entire CAC of a new customer."
```

**Key insight:** Churn reduction has higher ROI than new acquisition at this LTV/CAC ratio.
N06 routes this insight to churn_prevention_playbook as the primary investment signal.

---

## Example 3: Model Churn Intervention ROI

**Problem statement:** Current monthly churn is 3.5%. We can invest $5,000/month
in a CSM team. How do we model whether it pays? Which intervention plays yield the best return?

### 8F Trace Summary

| Stage | Action |
|-------|--------|
| F1 CONSTRAIN | kind=churn_prevention_playbook, pillar=P11, domain=retention-economics |
| F2 BECOME | strategic-greed: every churned customer is a CAC write-off plus lost LTV |
| F3 INJECT | churn_prevention_playbook_n06.md + subscription_tier_n06.md + roi_calculator_n06.md |
| F4 REASON | model: MRR impact of 1% churn reduction, CSM cost vs ARR defended |
| F5 CALL | compute intervention ROI by play, rank by ARR defended per dollar spent |
| F6 PRODUCE | intervention portfolio with ROI per play and recommended investment mix |
| F7 GOVERN | validate: does model include expansion MRR? is CSM cost fully loaded? |
| F8 COLLABORATE | update churn_prevention_playbook + signal n06 |

### Structured Output

```
CHURN INTERVENTION ROI MODEL

Baseline:
  MRR:             $100,000
  Monthly churn:   3.5% = $3,500 MRR lost/month
  Annual churn:    ~40% = $40,000+ ARR lost
  Avg customer LTV: $6,000 (blended across tiers)

CSM Investment: $5,000/month

Intervention plays ranked by ARR defended per dollar:

Play 1: Reactivation email sequence (PLAY 1 in churn_prevention_playbook)
  Cost: $200/month (tooling + automation time)
  Targets: dormant users (estimated 15% of churn candidates)
  Save rate: 35% (benchmark from playbook)
  MRR defended: 0.15 * 0.035 * $100K * 0.35 = $184/month
  ROI: $184 / $200 = 0.92x (break-even, worth running for brand)

Play 2: Payment failure recovery (PLAY 2)
  Cost: $100/month (SMS + tooling)
  Payment failure accounts for ~25% of churn
  Recovery rate: 60% with proactive outreach
  MRR defended: 0.25 * 0.035 * $100K * 0.60 = $525/month
  ROI: $525 / $100 = 5.25x  [HIGHEST ROI -- RUN FIRST]

Play 3: CSM save calls (PLAY 3 -- soft cancel)
  Cost: $2,500/month (0.5 FTE CSM)
  Soft cancels: ~20% of monthly churn
  Save rate: 45% (benchmark PRO/ENTERPRISE)
  MRR defended: 0.20 * 0.035 * $100K * 0.45 = $315/month
  ROI: $315 / $2,500 = 0.13x  -- negative alone

Play 4: Proactive health monitoring + outreach
  Cost: $1,200/month (tooling + CSM time for high-risk accounts)
  At-risk accounts: 25% of base, flagged by health_score
  Prevention rate: 50% of flagged accounts
  MRR defended: 0.25 * 0.035 * $100K * 0.50 = $438/month
  ROI: $438 / $1,200 = 0.37x

Recommended investment mix ($5,000/month budget):
  Play 2 (payment recovery):    $100  -> $525 MRR defended (5.25x)
  Play 4 (health monitoring):  $1,200 -> $438 MRR defended
  Play 1 (email reactivation):  $200  -> $184 MRR defended
  Play 3 (CSM saves -- PRO+):  $2,500 -> $315 MRR defended
  Remaining:                   $1,000 -> tooling/reporting

Total MRR defended: $1,462/month = $17,544 ARR
Total cost: $5,000/month = $60,000/year
Net ARR gain vs cost: -$42,456 (year 1)
Break-even month: 42,456 / (17,544 - 5,000*0) = approx month 29

Verdict: The CSM team does not pay back in year 1 at this MRR base.
Scale trigger: CSM team ROI-positive when MRR > $300,000.
Current recommendation: automate plays 1+2 only ($300/month) until MRR >= $300K.
```

**Key decision:** N06 defers CSM investment until $300K MRR -- automated plays (1+2) first.
Saves $57,000/year in premature scaling. Revisit at next ARR milestone.

---

## Example 4: Structure Referral Program Incentives

**Problem statement:** Current viral coefficient K=0.08. Target K=0.30.
Design incentive structure to triple referral conversion rate. Budget: $50 max CAC via referral.

### 8F Trace Summary

| Stage | Action |
|-------|--------|
| F1 CONSTRAIN | kind=referral_program, pillar=P11, domain=viral-growth |
| F2 BECOME | strategic-greed: referral = lowest CAC channel, peer trust as distribution |
| F3 INJECT | referral_program_n06.md + subscription_tier_n06.md + input_schema_checkout.md |
| F4 REASON | K-factor formula, dual-sided incentive optimization, fraud prevention |
| F5 CALL | model K-factor sensitivity to incentive value, find minimum viable reward |
| F6 PRODUCE | incentive structure with mechanics, attribution flow, anti-fraud controls |
| F7 GOVERN | validate: dual-sided? fraud controls? K-factor modeled? CAC constraint respected? |
| F8 COLLABORATE | update referral_program_n06.md + signal n06 |

### Structured Output

```
REFERRAL INCENTIVE DESIGN: K-FACTOR ENGINEERING

Current state:
  K = referrals_sent_per_user * referral_conversion_rate
  K = 0.20 * 0.40 = 0.08

Target: K >= 0.30
  Option A: increase referrals_sent to 0.75 (keep conversion 0.40)
  Option B: increase conversion to 0.75 (keep referrals_sent 0.20)
  Option C: both to 0.55 * 0.55 = 0.30 [recommended -- balanced]

Incentive structure to achieve K=0.30:

Referrer (existing customer):
  Reward:    1 month free per successful conversion ($49-$149 value)
  Trigger:   share at high-delight moments (post-first-build, NPS >= 9, upgrade)
  Stacking:  up to 12 months/year (max $1,788 annual credit -- Enterprise)
  Why works: intrinsic motivation (gift to friend) + extrinsic (personal value)

Referee (new customer):
  Reward:    1 month free on first paid plan
  Applied:   automatically on first invoice (zero friction)
  Why works: lowers trial-to-paid friction (one free month = lower perceived risk)

Enterprise referral bonus:
  Reward:    $500 cash, paid 30 days post-conversion
  Trigger:   Enterprise plan conversion only
  Rationale: Enterprise deals worth $6,000+ LTV; $500 = 8.3% CAC of $6,000

K-factor impact model:
  With dual-sided reward:
    referrals_sent: 0.20 -> 0.55 (NPS trigger + delight moments)
    conversion:     0.40 -> 0.55 (1-month free for referee reduces friction)
    New K = 0.55 * 0.55 = 0.30  [TARGET ACHIEVED]

CAC check:
  Referrer cost: avg $99 credit (blended STARTER/PRO avg)
  Referee cost:  avg $99 credit
  Total reward:  $198 per conversion
  CAC target:    $50 (cash) + $198 (credit) = $248 blended
  Vs organic CAC: $300-$500 (paid acquisition benchmark)
  Verdict:       referral CAC well within budget

Anti-fraud layer:
  - Block same-card or same-email-domain self-referrals
  - Reward triggers on paid conversion only (not free signup)
  - Manual review at 10+ conversions/month per referrer
  - 30-day hold before credit released (refund-gaming prevention)

Attribution implementation:
  URL: /signup?ref={tier}-{customer_id_prefix}-{random_4}
  Cookie TTL: 30 days
  Schema field: customer.metadata.referral_code
  Webhook: checkout.session.completed -> verify -> credit -> notify
```

**Key insight:** Dual-sided incentives double K-factor by attacking both send rate
and conversion rate simultaneously. Total blended CAC ($248) is lower than
paid acquisition ($300-$500) with higher LTV (peer-matched ICP fit).

---

## Usage Notes

These examples are grounded in the actual N06_commercial artifact stack:
- `subscription_tier_n06.md` -- tier structure and upgrade triggers
- `churn_prevention_playbook_n06.md` -- intervention plays and save rates
- `referral_program_n06.md` -- K-factor mechanics and attribution
- `roi_calculator_n06.md` -- value proof model and objection handlers

When an LLM receives a pricing or commercial question, match to the closest
example above and adapt the 8F trace for the specific context.
