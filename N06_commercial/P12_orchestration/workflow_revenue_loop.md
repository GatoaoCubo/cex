---
id: workflow_revenue_loop
kind: workflow
pillar: P12
nucleus: n06
title: "Workflow -- Revenue Flywheel: Acquire, Activate, Retain, Expand, Measure"
version: 1.0.0
quality: null
tags: [workflow, revenue, flywheel, orchestration, commercial, growth]
---

# Workflow: Revenue Flywheel

## Purpose

Defines the end-to-end orchestration of N06's revenue-generating workflow. This is the master workflow -- it references and sequences all other N06 commercial artifacts. The flywheel: each phase feeds the next, creating compounding revenue.

## Flywheel Architecture

```
         ACQUIRE
        /        \
 MEASURE          ACTIVATE
   |                |
 EXPAND          RETAIN
        \        /
         (back to ACQUIRE)
```

## Phase 1: ACQUIRE

**Goal:** Bring qualified leads into the funnel at minimum CAC.

```yaml
acquire_channels:
  organic_search:
    artifact: landing_page (P05)
    content_types: [seo_article, comparison_page, use_case_page]
    owner: N02 (content) + N05 (SEO tech)
    
  referral:
    artifact: referral_program_n06.md (P11)
    mechanics: dual-sided credit
    target_k_factor: >0.3
    
  product_led:
    artifact: FREE tier (enum_def_pricing_tiers.md)
    mechanic: 10-build freemium with hard limit
    conversion_trigger: builds_exhausted OR feature_gate
    
  sales_assisted:
    artifact: sales_playbook_n06.md (P03)
    qualification: discovery_questions_n06.md (P03)
    target_deal_size: ENTERPRISE or PRO annual
    
  paid_acquisition:
    target: product-aware personas (retargeting + intent signals)
    landing: pricing page + ROI calculator
    bid_constraint: CAC < 90 days payback
```

**Acquire success metric:** new_paid_signups, channel_CAC, ICP_score_avg

---

## Phase 2: ACTIVATE

**Goal:** Get customer to first value within 24 hours. Value = first successful build.

```yaml
activation_sequence:
  T+0 (signup):
    - Create customer entity (entity_memory_customer.md)
    - Send "Welcome + first task" email
    - Pre-configure brand_config template (reduce blank-page friction)
    
  T+30min (first session):
    - Show 3-step onboarding checklist (max 3 steps)
    - Step 1: Set brand_config (5 min)
    - Step 2: Run first build (3 min with example template)
    - Step 3: Share or download output (1 min)
    
  T+24h (if no first build):
    - "Your first build is waiting" email
    - Deep link to pre-filled template
    
  T+72h (if still no build):
    - "Need help getting started?" email
    - CTA: 15-min onboarding call with CSM
    - Flag: churn_risk elevated to MEDIUM
    
  T+7d (activation gate):
    - If >= 3 builds: mark ACTIVATED, enter RETAIN phase
    - If < 3 builds: enter HIGH-TOUCH onboarding track
```

**Activate success metric:** time_to_first_build, activation_rate (3+ builds in 7 days)

---

## Phase 3: RETAIN

**Goal:** Maximize engagement depth and breadth to prevent churn.

```yaml
retention_mechanisms:
  habit_formation:
    - Weekly usage digest email (builds done, time saved)
    - Build streak recognition (3-day, 7-day, 30-day milestones)
    - Monthly value summary (total builds, top artifact types, ROI estimate)
    
  feature_depth:
    - "Have you tried [nucleus]?" prompts based on ICP use case
    - Feature tour for underutilized nuclei
    - Use case templates matched to industry/role
    
  health_monitoring:
    - Customer entity health_score recalculated daily
    - churn_prevention_playbook triggered on signals
    - renewal_workflow_n06 begins at -30 days
    
  community_and_social:
    - Case study candidates identified (10+ builds + 30d active)
    - Feature beta access for power users (health >= 80)
    - Referral program activation at high-NPS moments
```

**Retain success metric:** churn_rate, DAU/MAU ratio, health_score_distribution

---

## Phase 4: EXPAND

**Goal:** Grow revenue from existing customers through upgrades and cross-sells.

```yaml
expansion_levers:
  tier_upgrade:
    triggers: expansion_play_n06.md (quota, feature gate, seat limit)
    target: STARTER->PRO conversion_rate >30%
    
  annual_conversion:
    triggers: month 3+ usage + email offer
    target: monthly->annual conversion >45%
    
  seat_expansion:
    triggers: second user invite attempt
    target: seat expansion event -> Enterprise pipeline
    
  add_ons:
    opportunities: [brand_audit_service, strategy_session, training_bundle]
    target: 20% attach rate on ENTERPRISE
```

**Expand success metric:** expansion_MRR, NRR (target >110%)

---

## Phase 5: MEASURE

**Goal:** Close the feedback loop so each flywheel rotation improves on the last.

```yaml
measurement_cadence:
  daily:
    - active_users, builds_today, MRR_snapshot
    - payment_failure_count (bugloop_revenue.md)
    - churn_signals_detected
    
  weekly:
    - health_score_distribution
    - conversion_funnel (free->starter->pro->enterprise)
    - channel_CAC vs payback_period
    - N06 self_improvement_loop SCAN
    
  monthly:
    - full_cohort_analysis (cohort_analysis_n06.md)
    - NPS survey + segmentation
    - churn_rate by tier + channel
    - expansion_MRR vs churn_MRR -> NRR
    - P11 artifacts improvement review
    
  quarterly:
    - pricing_review (willingness_to_pay vs competitor)
    - ICP scoring recalibration
    - Commercial portfolio gap scan -> N06 self-assembly candidates
```

**All metrics flow to:** eval_metric_commercial.md -> self_improvement_loop_n06.md

---

## Flywheel Acceleration Levers

The flywheel compounds when:
1. **Referral K > 0.3**: each customer brings 0.3+ new customers (viral growth)
2. **NRR > 110%**: existing base grows without new acquisition
3. **Activation rate > 70%**: more signups convert to active users
4. **CAC < 90 days payback**: paid acquisition scales profitably

At all three: revenue compounds geometrically. This is the CEX commercial endgame.

## Related Artifacts

- `self_improvement_loop_n06.md` -- MEASURE phase feeds back to ACQUIRE improvements
- `eval_metric_commercial.md` -- all KPIs consolidated here
- `entity_memory_customer.md` -- tracks individual customer journey through all 5 phases
- `cohort_analysis_n06.md` -- analyzes cohort behavior across flywheel phases
