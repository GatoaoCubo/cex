---
kind: memory
id: p10_mem_customer_segment_builder
pillar: P10
llm_function: INJECT
purpose: Learned patterns and pitfalls for customer_segment construction
quality: 8.7
title: "Memory Customer Segment"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [customer_segment, builder, learning_record]
tldr: "Learned patterns and pitfalls for customer_segment construction"
domain: "customer_segment construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_customer_segment_builder
  - bld_instruction_customer_segment
  - customer-segment-builder
  - p10_mem_eval_metric_builder
  - p10_lr_judge_config_builder
  - p10_mem_prompt_optimizer_builder
  - p10_mem_self_improvement_loop_builder
  - p10_lr_churn_prevention_playbook_builder
  - p10_lr_playground_config_builder
  - bld_collaboration_customer_segment
---

## Observation
Common issues include over-reliance on demographics without aligning to business goals, vague definitions leading to misinterpretation, and inconsistent data sources causing fragmented segments.

## Pattern
Effective artifacts integrate firmographics (industry, size) with behavioral needs (pain points, goals), ensuring clarity and actionable insights. Cross-functional validation improves accuracy and relevance.

## Evidence
Reviewed artifacts showed success when combining firmographic filters with specific need-based criteria, validated by sales and product teams.

## Recommendations
- Align segment definitions with measurable business outcomes (e.g., revenue targets, market expansion).
- Use a mix of quantitative (data) and qualitative (interviews) inputs to capture nuanced needs.
- Document assumptions and data sources to ensure transparency and auditability.
- Regularly update segments to reflect market changes and new product capabilities.
- Avoid overly broad categories; prioritize specificity to guide targeted strategies.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_customer_segment_builder]] | upstream | 0.30 |
| [[bld_instruction_customer_segment]] | upstream | 0.30 |
| [[customer-segment-builder]] | upstream | 0.28 |
| [[p10_mem_eval_metric_builder]] | sibling | 0.26 |
| [[p10_lr_judge_config_builder]] | related | 0.24 |
| [[p10_mem_prompt_optimizer_builder]] | sibling | 0.21 |
| [[p10_mem_self_improvement_loop_builder]] | sibling | 0.21 |
| [[p10_lr_churn_prevention_playbook_builder]] | related | 0.20 |
| [[p10_lr_playground_config_builder]] | related | 0.20 |
| [[bld_collaboration_customer_segment]] | downstream | 0.20 |
