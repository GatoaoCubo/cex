---
kind: examples
id: bld_examples_nps_survey
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of nps_survey artifacts
quality: 8.9
title: "Examples Nps Survey"
version: "1.0.0"
author: n05_wave6
tags: [nps_survey, builder, examples]
tldr: "Golden and anti-examples of nps_survey artifacts"
domain: "nps_survey construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example -- Transactional NPS (Post-Support)
```yaml
---
id: p11_nps_post_support_close.yaml
kind: nps_survey
pillar: P11
survey_type: transactional
cadence: post_support_close
quality: null
---
question: "On a scale of 0 to 10, how likely are you to recommend Acme to a colleague?"
scale:
  min: 0
  max: 10
follow_up:
  promoter: "What made this support experience great?"
  passive: "What one thing would have made this better?"
  detractor: "What went wrong and how can we fix it?"
filters:
  - field: ticket_resolved
    operator: "="
    value: true
  - field: tenure_days
    operator: ">="
    value: 30
exclusion_rules:
  - surveyed_within_days: 90
routing:
  promoter: success_team_referral_queue
  passive: nurture_30d_sequence
  detractor: support_escalation_p1
```

## Anti-Example 1: Non-Bain Scale
```yaml
question: "Rate your experience from 1 to 5"
scale:
  min: 1
  max: 5
```
Why it fails: Uses 1-5 scale instead of Bain standard 0-10. Score calculation
(% promoters - % detractors) is meaningless without the 0-10 range. H04 HARD gate rejects.

## Anti-Example 2: Missing Routing for Passive Band
```yaml
routing:
  promoter: referral_queue
  detractor: escalation_queue
  # passive band absent
```
Why it fails: Passive respondents (7-8) have no destination. They represent 40-60% of
typical responses. H06 HARD gate rejects -- all three bands must be explicitly routed.

## Anti-Example 3: Cohort Analysis Confusion
```yaml
kind: nps_survey
body: |
  "Analyse 90-day NPS trend by customer cohort.
   Compute churn correlation. Generate retention forecast."
```
Why it fails: This is cohort_analysis, not nps_survey. The nps_survey kind configures
survey mechanics only. Analysis belongs in a separate cohort_analysis artifact (P07).
