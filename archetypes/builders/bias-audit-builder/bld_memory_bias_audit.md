---
kind: learning_record
id: p10_lr_bias_audit_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for bias_audit construction
quality: 8.8
title: "Learning Record Bias Audit"
version: "1.0.0"
author: wave1_builder_gen
tags: [bias_audit, builder, learning_record]
tldr: "Learned patterns and pitfalls for bias_audit construction"
domain: "bias_audit construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

## Observation

This ISO drives a bias audit: measuring fairness across demographic slices.
Common issues include inconsistent metric definitions, overlooked contextual biases, and misalignment between evaluation criteria and stakeholder priorities. Artifacts often lack transparency in how fairness trade-offs are quantified.

## Pattern
Structured frameworks that explicitly map fairness criteria to domain-specific outcomes work well. Iterative validation with diverse stakeholder feedback improves alignment between audit goals and real-world impacts.

## Evidence
Reviewed artifacts using standardized fairness taxonomies (e.g., demographic parity, equalized odds) showed clearer interpretability compared to ad-hoc approaches.

## Recommendations
- Adopt standardized fairness taxonomies to ensure consistency across audits.
- Involve domain experts early to define context-specific fairness criteria.
- Document assumptions and limitations of chosen metrics transparently.
- Use synthetic data to stress-test audit methods against edge cases.
- Prioritize audits that track fairness outcomes over time, not just static snapshots.
| Common mistake: self-scoring | Always set quality: null |
| Common mistake: single-metric audit | Add fairness-specific metrics: DP, EO, PP |
