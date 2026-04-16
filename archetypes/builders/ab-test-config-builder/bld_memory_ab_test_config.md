---
kind: memory
id: bld_memory_ab_test_config
pillar: P10
llm_function: INJECT
purpose: Accumulated production experience for ab_test_config artifact generation
memory_scope: project
observation_types: [user, feedback, project, reference]
quality: 9.0
title: "Memory Ab Test Config"
version: "1.0.0"
author: n03_builder
tags: [ab_test_config, builder, memory]
tldr: "Golden and anti-patterns for A/B test config construction: hypothesis-first, guardrail metrics mandatory, sample-size pre-computed, no peeking."
domain: "ab_test_config construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.87
---
# Memory: ab-test-config-builder

## Summary
A/B test configs fail when they chase outcomes instead of testing hypotheses. The most frequent defect is post-hoc metric selection -- analysts pick whatever moved after the test ran. The second is absent guardrails: a variant that lifts signup 5% and crashes retention 30% ships because retention was never measured. The third is underpowered tests: teams run a 2-week test on 500 users, get p=0.14, and declare "no effect" when the MDE required 40k users.

## Pattern
1. Lock hypothesis, primary_metric, and MDE BEFORE dispatching variants. No mid-test additions.
2. Define 2-3 guardrail_metrics (retention, latency, revenue-per-user) -- a variant is BLOCKED if any guardrail degrades beyond threshold even if primary wins.
3. Compute sample_size upfront via power analysis (alpha=0.05, power=0.80) -- Evan Miller or Optimizely sample-size calculators.
4. Choose statistical_method: frequentist (fixed-horizon, sequential testing e.g. mSPRT for Optimizely/Statsig) or Bayesian (posterior probability, GrowthBook default). Document which and why.
5. Randomize at the correct unit (user_id, not session) and seed with a stable hash (e.g., MurmurHash3) to ensure sticky assignment.
6. Set srm_check (Sample Ratio Mismatch) tolerance of <= 0.01 -- SRM failure invalidates the experiment.
7. Traffic_split must be explicit and integer-percent. No "remainder" allocations.

## Evidence
Kohavi et al. 2020 ("Trustworthy Online Controlled Experiments") formalized SRM, guardrails, and peeking risk. LinkedIn, Microsoft, and Booking.com publish failure rates: ~80% of A/B tests show no statistically significant effect, reinforcing need for MDE-first design. Statsig and GrowthBook docs explicitly require primary_metric + guardrail_metrics separation.

## Pitfalls
- **Peeking**: running Z-test daily and stopping at first p<0.05 inflates FPR from 5% to ~28% (fix: sequential testing / alpha-spending).
- **HTE ignored**: aggregate lift hides subgroup harm. Break down by segment before shipping.
- **Novelty effect**: week-1 lift fades. Require >= 2 business cycles (typically 14 days) when measuring engagement.
- **OEC drift**: picking a new Overall Evaluation Criterion mid-test invalidates pre-registration.
- **Confounding via overlapping experiments**: use layered experimentation (Google's rooted layers) or mutual exclusion.
