---
id: kc_revenue_gap_map
kind: knowledge_card
pillar: P11
nucleus: n06
version: 1.0.0
created: "2026-04-18"
updated: "2026-04-18"
author: n06_commercial
domain: commercial_revenue_infrastructure
quality: 8.7
tags: [revenue_gap, P11, commercial, feedback_loop, N06, SaaS, monetization]
tldr: "N06 revenue gap map: P11 commercial kinds, current builder state, revenue blockers, and build priority."
density_score: 0.90
related:
  - n06_monetization_audit_2026_04_08
  - bld_architecture_kind
  - bld_knowledge_card_renewal_workflow
  - bld_collaboration_renewal_workflow
  - p12_sp_renewal_workflow_builder
  - kind-builder
  - bld_collaboration_churn_prevention_playbook
  - renewal-workflow-builder
  - bld_collaboration_kind
  - bld_examples_renewal_workflow
---

# N06 Revenue Gap Map -- P11 Commercial Feedback Kinds

Strategic Greed audit of P11_feedback kinds that belong to N06's commercial domain.
For each kind: current artifact state, what blocks revenue without it, build priority.

## Executive Summary

| Metric                 | Value     |
|------------------------|-----------|
| P11 kinds total        | 31        |
| N06 commercial kinds   | 8         |
| Builders complete      | 4 (churn, referral, renewal, expansion) |
| Builders missing       | 0 (all 8 now built as of BOOTSTRAP_SELF_W1) |
| Artifact instances     | varies per nucleus -- see per-kind below |
| Revenue at risk (est.) | 15-25% ARR per missing feedback loop |

---

## Kind 1: churn_prevention_playbook

| Property         | Value                                   |
|------------------|-----------------------------------------|
| Pillar           | P11                                     |
| Builder          | churn-prevention-playbook-builder (DONE)|
| Builder quality  | 8.8                                     |
| Instances in N06 | churn_prevention_playbook_n06.md        |
| Status           | Builder exists, 1 instance              |

**Revenue block without it**: No systematic early-warning system for at-risk accounts.
CSMs react to cancellation requests instead of intercepting 90 days earlier.
Industry benchmark: proactive churn intervention saves 15-40% of at-risk accounts.
At $1M ARR with 5% monthly churn, one playbook can protect $600K/yr.

**What to build next**: Per-segment playbooks (ENT vs SMB vs PLG), automated
Gainsight/ChurnZero CTA templates, health score weighting model per product line.

**Revenue lever**: Retention is 5x cheaper than acquisition. Every 1% churn reduction
on $1M ARR = $10K/mo saved = $120K ARR protected.

---

## Kind 2: referral_program

| Property         | Value                               |
|------------------|-------------------------------------|
| Pillar           | P11                                 |
| Builder          | referral-program-builder (DONE)     |
| Builder quality  | 8.8                                 |
| Instances in N06 | referral_program_n06.md             |
| Status           | Builder exists, 1 instance          |

**Revenue block without it**: Organic referral growth uncaptured. B2B SaaS referrals
convert at 3-5x higher rate than outbound (Gartner 2023). Without a structured
program, referrals happen but are untracked and unrewarded -- no flywheel.

**What to build next**: Referral attribution model (first-touch vs last-touch),
fraud detection rules (domain-match, cooldown periods), Tipalti/Stripe payout
automation, HubSpot CRM integration template.

**Revenue lever**: Viral coefficient > 1.0 creates compound growth. At $1M ARR
and k=1.2, referrals add $200K ARR per cohort without incremental CAC spend.

---

## Kind 3: renewal_workflow

| Property         | Value                                |
|------------------|--------------------------------------|
| Pillar           | P12 (orchestration)                  |
| Builder          | renewal-workflow-builder (DONE)      |
| Builder quality  | 8.9                                  |
| Instances in N06 | referral_program_n06.md (via P12)    |
| Status           | Builder exists, coverage thin        |

**Revenue block without it**: Renewals handled ad hoc. No GRR model per account,
no escalation triggers, no price increase playbook. Industry data: structured
renewal workflows improve GRR by 8-12% (CSM benchmarks 2024).

**What to build next**: Auto-renewal compliance matrix (CA/EU/AU regulations),
multi-year incentive pricing table, CSM capacity model (accounts per CSM tier).

**Revenue lever**: GRR is the denominator of NRR. Every 1% GRR improvement on
$2M ARR = $20K/yr base protected. At 95% GRR vs 87% = $160K/yr difference.

---

## Kind 4: expansion_play

| Property         | Value                               |
|------------------|-------------------------------------|
| Pillar           | P03 (prompt/trigger)                |
| Builder          | expansion-play-builder (DONE)       |
| Builder quality  | 8.9                                 |
| Instances in N06 | 0 dedicated instances               |
| Status           | Builder done, no instances yet      |

**Revenue block without it**: NRR capped at 100% (retention only). Expansion plays
are the mechanism to drive NRR above 100%. Best-in-class SaaS achieves 120-140%
NRR; without structured expansion plays, the ceiling is retention rate.

**What to build next**: Seat expansion play (usage threshold trigger), plan upgrade
play (PLG -- quota hit trigger), cross-sell play (adjacent product trigger),
executive sponsor play (new EB identified).

**Revenue lever**: Every 10% NRR improvement on $2M ARR = $200K incremental ARR
in year 2 without new customer acquisition.

---

## Kind 5: nps_survey (gap -- N06 should own commercial NPS)

| Property         | Value                              |
|------------------|------------------------------------|
| Pillar           | P11                                |
| Builder          | nps-survey-builder (DONE -- N03)   |
| Builder quality  | 9.0+ (N03 built)                   |
| N06 ownership    | MISSING -- no commercial NPS logic |
| Status           | Builder exists but commercial adaptation absent |

**Revenue block without it**: NPS data collected but not connected to commercial
action. Detractor (NPS 0-6) = churn risk. Passive (7-8) = expansion opportunity.
Promoter (9-10) = referral candidate. Without commercial NPS routing, survey
results sit in a dashboard and drive no revenue action.

**What to build next**: NPS routing rules (detractor -> CSM CTA, passive ->
expansion play, promoter -> referral ask), Typeform/Delighted -> HubSpot
automation template, NPS-by-segment analysis artifact.

**Revenue lever**: Closing the loop on NPS detractors reduces churn by 15-20%.
At $1M ARR and 5% churn, NPS-driven save program = $75-100K ARR protected.

---

## Kind 6: cohort_analysis (gap -- revenue cohorts missing)

| Property         | Value                              |
|------------------|------------------------------------|
| Pillar           | P11                                |
| Builder          | cohort-analysis-builder (DONE -- N01) |
| N06 ownership    | MISSING -- no revenue cohort lens  |
| Status           | Intelligence builder exists, no commercial artifact |

**Revenue block without it**: No ARR cohort tracking. Cannot answer: "of customers
acquired in Q1 2025, what % churned, expanded, or contracted by Q1 2026?"
Without revenue cohort analysis, LTV modeling is guesswork.

**What to build next**: ARR cohort waterfall template (new/expansion/contraction/
churn), LTV by acquisition channel, payback period calculator by segment.

**Revenue lever**: ARR cohort visibility enables accurate LTV-to-CAC modeling.
Misallocated acquisition spend from bad cohort data typically wastes 20-30% of
marketing budget.

---

## Kind 7: roi_calculator (partial -- instance exists)

| Property         | Value                             |
|------------------|-----------------------------------|
| Pillar           | P11                               |
| Builder          | roi-calculator-builder (DONE)     |
| Instances in N06 | roi_calculator_n06.md (EXISTS)    |
| Status           | Builder + instance -- good coverage|

**Current state**: roi_calculator_n06.md covers N06 internal ROI. Need a
customer-facing ROI calculator artifact for sales/CS motions.

**Revenue lever**: Customer-facing ROI calculators improve deal close rates by
18-25% (Forrester 2023). At $500K pipeline, 20% lift = $100K additional closed ARR.

---

## Kind 8: subscription_tier (partial -- instance exists)

| Property         | Value                               |
|------------------|-------------------------------------|
| Pillar           | P11                                 |
| Builder          | subscription-tier-builder (DONE)    |
| Instances in N06 | subscription_tier_n06.md (EXISTS)   |
| Status           | Builder + instance -- good coverage |

**Current state**: subscription_tier_n06.md defines CEX tiers. Expansion needed:
annual vs monthly pricing uplift model, usage-based pricing overlay, enterprise
custom pricing guardrails.

**Revenue lever**: Annual billing improves cash flow 12x and reduces churn by
30-40% (annual contracts = lock-in). At $1M ARR, converting 20% from monthly
to annual = $200K cash flow improvement in year 1.

---

## Priority Build Queue (post-BOOTSTRAP_SELF_W1)

| Priority | Kind              | Action                              | Revenue Impact |
|----------|-------------------|-------------------------------------|----------------|
| P1       | expansion_play    | Build 3 instance variants           | NRR > 100%     |
| P1       | churn_prevention  | SMB/ENT/PLG playbook variants       | $120K+ ARR saved|
| P2       | nps_survey        | Commercial routing rules artifact   | $75-100K protected|
| P2       | referral_program  | Attribution + fraud rules           | k > 1.0 flywheel|
| P3       | cohort_analysis   | ARR waterfall + LTV template        | Marketing efficiency|
| P3       | roi_calculator    | Customer-facing calc                | 20% close rate lift|
| P4       | renewal_workflow  | Auto-renewal compliance matrix      | GRR +8-12%     |
| P4       | subscription_tier | Annual pricing model overlay        | $200K cash flow |

---

## Revenue Compounding Model

Each closed gap compounds:

```
Year 1 with all gaps closed (est.):
  Churn protection (15%):     $150K ARR saved (base $1M)
  Referral flywheel (k=1.2):  $200K new ARR
  NRR expansion plays:        $200K incremental ARR
  Renewal workflow (GRR+5%):  $50K ARR protected
  NPS commercial routing:     $75K ARR protected
  ------------------------------------------
  Total Year 1 impact:        ~$675K ARR on $1M base
  Effective growth multiplier: 1.675x (vs baseline)
```

Strategic Greed conclusion: every feedback loop missing from N06 is a revenue
drain. The 8 commercial P11 kinds are not documentation -- they are the commercial
nervous system that converts a generic SaaS into a compounding revenue machine.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[n06_monetization_audit_2026_04_08]] | upstream | 0.29 |
| [[bld_architecture_kind]] | upstream | 0.28 |
| [[bld_knowledge_card_renewal_workflow]] | sibling | 0.28 |
| [[bld_collaboration_renewal_workflow]] | downstream | 0.27 |
| [[p12_sp_renewal_workflow_builder]] | downstream | 0.26 |
| [[kind-builder]] | upstream | 0.25 |
| [[bld_collaboration_churn_prevention_playbook]] | downstream | 0.24 |
| [[renewal-workflow-builder]] | downstream | 0.24 |
| [[bld_collaboration_kind]] | downstream | 0.22 |
| [[bld_examples_renewal_workflow]] | upstream | 0.22 |
