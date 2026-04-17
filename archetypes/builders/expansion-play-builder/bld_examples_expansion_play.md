---
kind: examples
id: bld_examples_expansion_play
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of expansion_play artifacts
quality: 9.1
title: "Examples Expansion Play"
version: "1.0.0"
author: wave6_n06
tags: [expansion_play, builder, examples, upsell, NRR, land-and-expand]
tldr: "Golden and anti-examples of expansion_play artifacts"
domain: "expansion_play construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

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
