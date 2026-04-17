---
kind: memory
id: p10_mem_usage_report_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for usage_report construction
quality: 8.7
title: "Learning Record Usage Report"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [usage_report, builder, learning_record]
tldr: "Learned patterns and pitfalls for usage_report construction"
domain: "usage_report construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Observation
Inconsistent metric definitions across reports often lead to misalignment with billing/CFO requirements. Overlooking granular user segmentation causes incomplete insights for resource planning.

## Pattern
Standardized templates with clear ownership ensure consistency. Cross-functional collaboration during spec drafting improves alignment with business goals.

## Evidence
Reviewed 12 usage_report specs; 8 included unified metric definitions and 5 had stakeholder validation checkpoints.

## Recommendations
- Define metrics using shared glossaries to avoid ambiguity.
- Include user segmentation criteria in spec templates.
- Require CFO and billing teams to co-own report validation.
- Automate data lineage tracking for auditability.
- Separate usage analytics from cost modeling specs to prevent scope creep.
