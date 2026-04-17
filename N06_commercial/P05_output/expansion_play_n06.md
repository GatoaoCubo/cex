---
id: expansion_play_n06
kind: expansion_play
pillar: P05
nucleus: n06
title: "Expansion Play -- Upsell and Cross-Sell Trigger Conditions"
version: 1.0.0
quality: 9.0
tags: [expansion, upsell, cross-sell, revenue, upgrade, commercial, growth]
density_score: 1.0
---

# Expansion Play: Upsell and Cross-Sell Trigger Conditions

## Strategic Intent

Expansion revenue is the highest-margin revenue in SaaS: zero CAC, no competition, existing trust. Every trigger in this artifact represents a moment where the customer has self-selected into readiness for the next tier. N06's job is to make the upgrade feel inevitable, not pushed.

## Expansion Trigger Matrix

### Category 1: Usage-Based Triggers

| Trigger | Threshold | Action | Channel |
|---------|-----------|--------|---------|
| Builds quota | 80% consumed | In-app quota bar + upgrade CTA | In-app |
| Builds quota | 100% (blocked) | Upgrade modal (full-screen) | In-app |
| API calls | First API call attempt (FREE/STARTER) | Feature gate + upgrade prompt | In-app |
| Builds velocity | >5 builds/day for 3 consecutive days | "Power user" upgrade email | Email |
| Login streak | 7 consecutive days | Engagement-based upgrade nudge | Email |

### Category 2: Feature Access Triggers

| Feature Attempted | Locked At | Unlocked At | Action |
|------------------|-----------|-------------|--------|
| API access | FREE, STARTER | PRO | Gate modal + feature tour |
| N03 nucleus access | FREE, STARTER | PRO | Gate + show what N03 can build |
| N07 nucleus access | FREE-PRO | ENTERPRISE | Sales touchpoint trigger |
| SSO setup | FREE-PRO | ENTERPRISE | Sales touchpoint trigger |
| Audit log | FREE, STARTER | PRO | Gate + compliance framing |
| Custom integrations | FREE-PRO | ENTERPRISE | Sales touchpoint trigger |
| Data residency | FREE-PRO | ENTERPRISE | Compliance-specific gate |

### Category 3: Team Growth Triggers

| Trigger | Threshold | Action | Channel |
|---------|-----------|--------|---------|
| Seat invite | Attempting to add user beyond limit | Upgrade modal | In-app |
| Share link | Sharing output externally 3x/week | "Your team needs this" prompt | Email |
| Multiple users same org | Detected same domain 2nd signup | "Your colleague is here" upgrade nudge | Email + In-app |

### Category 4: Engagement Depth Triggers

| Trigger | Signal | Action |
|---------|--------|--------|
| Feature breadth | Using 1 of 6 available nuclei for 30 days | "Have you tried N01 for research?" |
| High NPS (9-10) | NPS survey response | Referral ask + annual upgrade offer |
| Case study candidate | 10+ builds + 30+ days active | CSM outreach for case study + relationship |
| High build quality | Average build quality > 8.5 | "Your work is exceptional" + PRO invite |

### Category 5: Lifecycle Triggers

| Stage | Trigger | Action |
|-------|---------|--------|
| Day 7 (trial) | Has 5+ builds | "You're on a roll" + upgrade push |
| Day 30 (STARTER) | 50+ builds in first month | Power user recognition + PRO offer |
| Day 90 (PRO) | High usage + small team | Enterprise discovery touchpoint |
| Renewal -30 days | Annual renewal approaching | Annual renewal + expansion offer |

## Play Execution Scripts

### PLAY: Quota Threshold In-App

```
Condition: builds_used >= 0.8 * builds_quota
Render: persistent banner (NOT modal, NOT blocking)
Message: "[builds_used] of [builds_quota] builds used this month.
          Upgrade to PRO for unlimited builds + API access. $[price_diff]/month more."
CTA: [Upgrade to PRO] | [View usage]
Dismiss: allowed, but re-shows if quota hits 90%
```

### PLAY: Feature Gate Modal

```
Condition: customer attempts locked feature
Render: modal (blocking for 3 seconds, then dismissible)
Message: "[Feature name] is available on [unlock_tier].
          Here's what you can do with it: [1-sentence use case].
          Upgrade for $[price]/month."
CTA: [Upgrade to [tier]] | [Learn more]
Analytics: track which features are gated most often -> roadmap signal
```

### PLAY: Sales Touchpoint (Enterprise)

```
Condition: SSO requested OR 5+ seat invites OR compliance doc requested
Action: 
  1. Log event to CRM
  2. Route to CSM queue (priority: HIGH)
  3. Send automated: "Our Enterprise team will be in touch in 24h"
  4. CSM receives: customer profile + usage data + trigger event
Timeline: CSM contact within 24 hours (business hours)
```

## Cross-Sell Plays (Adjacent Revenue)

| Existing Customer | Cross-Sell Offer | Revenue Potential |
|------------------|-----------------|-------------------|
| STARTER building brand materials | Brand audit service ($99 one-time) | High conversion, high value |
| PRO using N06 heavily | Custom pricing strategy session ($299) | Low volume, high ticket |
| Any tier hitting limits | Credits pack (build more this month) | Bridges upgrade gap |
| ENTERPRISE | Annual training + onboarding bundle | ARPU expansion |

## Measurement

| Metric | Formula | Target |
|--------|---------|--------|
| Expansion MRR | MRR from upgrades this month | >20% of new MRR |
| Trigger-to-upgrade rate | upgrades / trigger_events | >15% |
| Time-from-trigger-to-upgrade | avg days from trigger to upgrade | <7 days |
| Feature-gate conversion | upgrades from feature gates / total gates | >8% |

## Related Artifacts

- `subscription_tier_n06.md` -- source of tier features and price points
- `action_prompt_upsell.md` -- message templates for each play
- `entity_memory_customer.md` -- trigger events logged to customer entity
- `eval_metric_commercial.md` -- expansion MRR tracked here
