---
id: mental_model_revenue_flywheel
kind: mental_model
pillar: P01
nucleus: n06
title: "Mental Model -- Revenue Flywheel (Acquire -> Activate -> Retain -> Expand -> Measure)"
version: 1.0.0
quality: 9.0
updated: 2026-04-17
tags: [mental-model, flywheel, revenue, saas, growth, commercial, acquisition, retention, expansion]
---

# Mental Model: Revenue Flywheel

## Core Concept

The Revenue Flywheel is a compounding loop: each phase feeds the next, and a
stronger rotation reduces CAC, increases LTV, and compounds revenue without
proportional cost growth. This is the canonical commercial architecture for any
SaaS business. N06 implements it as a typed artifact stack -- every node in the
flywheel maps to one or more CEX kinds.

```
          ACQUIRE
         /        \
  MEASURE          ACTIVATE
    |                  |
  EXPAND            RETAIN
         \        /
          (loop back)
```

**Flywheel Law:** The flywheel compounds when NRR > 100%. At NRR > 110%, the
existing customer base generates more revenue than churn destroys -- you grow
even with zero new acquisition.

---

## Phase 1: ACQUIRE

**Goal:** Bring qualified leads into the funnel at minimum CAC.

**Governing metric:** CAC payback period (target: < 3 months for STARTER, < 9 months for ENTERPRISE)

| Channel | Mechanism | CEX Kind | Artifact |
|---------|-----------|----------|----------|
| Organic search | SEO content funnel | landing_page | P05 landing pages |
| Product-led | Freemium with hard limit | subscription_tier | enum_def_pricing_tiers.md |
| Referral | Peer recommendation | referral_program | referral_program_n06.md |
| Sales-assisted | Outbound + discovery | sales_playbook | P03 sales artifacts |
| Paid | Retargeting + intent | landing_page + roi_calculator | pricing page + calculator |

**Key lever:** Referral is the highest-ROI acquisition channel (K > 0.3 = viral growth).
Every satisfied customer is a distribution node. CAC via referral < $50 vs $300+ organic.

**Signal to next phase:** new_paid_signup event -> triggers ACTIVATE sequence.

---

## Phase 2: ACTIVATE

**Goal:** Customer reaches first value within 24 hours (first successful build).

**Governing metric:** Activation rate (% who complete >= 3 builds in 7 days). Target: > 70%.

| Step | Timeline | Action | CEX Kind |
|------|----------|--------|----------|
| Welcome | T+0 | Send first-task email + pre-fill brand_config template | onboarding_flow |
| First session | T+30min | 3-step checklist: brand_config -> first build -> share | prompt_template |
| Follow-up | T+24h (no build) | "Your first build is waiting" + deep link | action_prompt |
| Rescue | T+72h (no build) | 15-min onboarding call offer | handoff protocol |
| Gate | T+7d | >= 3 builds = ACTIVATED; < 3 = high-touch track | quality_gate |

**Failure mode:** Blank-page friction. Customer signs up but never configures brand.
Fix: pre-fill brand_config template on signup from company domain signals.

**Signal to next phase:** activation_gate_passed event -> moves customer to RETAIN phase.

---

## Phase 3: RETAIN

**Goal:** Maximize depth and breadth of engagement to prevent churn.

**Governing metric:** Monthly churn rate (target: < 2% MoM). Secondary: DAU/MAU ratio.

| Mechanism | Trigger | CEX Kind | Artifact |
|-----------|---------|----------|----------|
| Habit formation | Weekly digest email | schedule | renewal_workflow_n06.md |
| Health monitoring | Daily score recalculation | entity_memory | customer entity health_score |
| Churn intervention | health_score < threshold | churn_prevention_playbook | churn_prevention_playbook_n06.md |
| Feature depth | Underutilized nucleus detected | action_prompt | "Have you tried [nucleus]?" |
| Renewal workflow | Contract end - 30 days | workflow | renewal_workflow_n06.md |

**Churn signal taxonomy (from churn_prevention_playbook_n06.md):**

```yaml
behavioral: builds < 2/week, login < 2x/week, last_build > 14 days
financial: payment_failed, cancel_at_period_end, downgrade_attempt
lifecycle: trial_day_3_no_build, renewal_minus_30_days
```

**Intervention priority:** Payment failure recovery (PLAY 2) has highest ROI (5.25x).
Automate plays 1+2 at any ARR level. CSM plays 3+4 unlock at MRR > $300K.

**Signal to next phase:** Customer at >= 3 months, health_score >= 70 -> eligible for EXPAND.

---

## Phase 4: EXPAND

**Goal:** Grow revenue from existing customers without new acquisition cost.

**Governing metric:** Net Revenue Retention (NRR). Target: > 110%.

| Lever | Trigger | CEX Kind | Artifact |
|-------|---------|----------|----------|
| Tier upgrade | quota exhausted, feature gate hit | expansion_play | expansion_play_n06.md |
| Annual conversion | Month 3+ usage + email | subscription_tier | subscription_tier_n06.md |
| Seat expansion | Second user invite | subscription_tier | upgrade trigger |
| Add-ons | Enterprise / power user | content_monetization | P11 monetization artifacts |

**Upgrade trigger hierarchy (from subscription_tier_n06.md):**

```
FREE -> STARTER:    builds_quota_exhausted OR brand_config_attempted
STARTER -> PRO:     api_access_requested OR second_seat_invited
PRO -> ENTERPRISE:  seats_at_capacity OR sso_requested OR compliance_doc_requested
```

**NRR math:** If NRR = 115%, a $1M ARR base becomes $1.15M next year with ZERO new customers.
At NRR = 120%, it doubles every 4 years from expansion alone.

**Signal to next phase:** Monthly + quarterly expansion data flows into MEASURE.

---

## Phase 5: MEASURE

**Goal:** Close the feedback loop so each flywheel rotation improves on the last.

**Governing metric:** All KPIs consolidated in eval_metric_commercial.md.

| Cadence | Metrics | CEX Kind | Artifact |
|---------|---------|----------|----------|
| Daily | active_users, builds, MRR, payment_failures, churn_signals | eval_metric | eval_metric_commercial.md |
| Weekly | health_score distribution, conversion funnel, channel_CAC | cohort_analysis | cohort_analysis_n06.md |
| Monthly | churn_rate, NRR, expansion_MRR, NPS | scoring_rubric | scoring_rubric_commercial.md |
| Quarterly | pricing review, ICP recalibration, commercial portfolio gap scan | self_improvement_loop | self_improvement_loop_n06.md |

**Feedback into ACQUIRE:** MEASURE identifies which acquisition channels produce
highest-LTV customers -> reallocate budget. Low-LTV channels get budget cuts.
High-referral customers -> increase referral program investment.

---

## Flywheel Acceleration Conditions

The flywheel compounds geometrically when all three conditions hold simultaneously:

| Condition | Metric | Why It Matters |
|-----------|--------|----------------|
| Viral growth | Referral K > 0.3 | Each customer brings 0.3+ new customers -- free acquisition |
| Expansion dominates | NRR > 110% | Existing base grows without new acquisition |
| Efficient top-of-funnel | CAC payback < 3 months | Paid acquisition scales profitably |

**At all three:** revenue compounds without proportional cost growth.
Missing even one: growth is linear, not exponential.

---

## Artifact Map: Kind -> Flywheel Phase

Every N06 artifact implements exactly one flywheel phase. This mapping makes
the commercial architecture auditable and improvable.

| Kind | Artifact | Flywheel Phase |
|------|----------|---------------|
| subscription_tier | subscription_tier_n06.md | ACQUIRE + EXPAND |
| referral_program | referral_program_n06.md | ACQUIRE |
| onboarding_flow | P03 onboarding artifacts | ACTIVATE |
| churn_prevention_playbook | churn_prevention_playbook_n06.md | RETAIN |
| renewal_workflow | renewal_workflow_n06.md | RETAIN |
| expansion_play | expansion_play_n06.md | EXPAND |
| roi_calculator | roi_calculator_n06.md | ACQUIRE (sales proof) |
| eval_metric | eval_metric_commercial.md | MEASURE |
| cohort_analysis | cohort_analysis_n06.md | MEASURE |
| self_improvement_loop | self_improvement_loop_n06.md | MEASURE -> ACQUIRE |
| workflow | workflow_revenue_loop.md | Orchestration of all phases |

---

## Portability Note

This mental model is business-model-agnostic. The five phases (Acquire, Activate,
Retain, Expand, Measure) apply to any SaaS product. The specific artifacts above
are CEX's implementation -- replace them with equivalent artifacts for any other
product domain. The flywheel structure and the governing metrics (CAC payback,
activation rate, churn rate, NRR) remain constant across industries.

## Related Artifacts

- `workflow_revenue_loop.md` -- full orchestration of all 5 phases (P12)
- `churn_prevention_playbook_n06.md` -- RETAIN phase intervention chain (P11)
- `subscription_tier_n06.md` -- ACQUIRE + EXPAND tier architecture (P11)
- `referral_program_n06.md` -- ACQUIRE viral growth engine (P11)
- `roi_calculator_n06.md` -- ACQUIRE sales proof model (P11)
- `eval_metric_commercial.md` -- MEASURE KPI dashboard (P07)
- `few_shot_examples_pricing_scenarios.md` -- worked examples for all phases (P01)
