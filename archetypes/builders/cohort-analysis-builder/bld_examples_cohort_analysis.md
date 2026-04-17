---
kind: examples
id: bld_examples_cohort_analysis
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of cohort_analysis artifacts
quality: 8.9
title: "Examples Cohort Analysis"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [cohort_analysis, builder, examples]
tldr: "Golden and anti-examples of cohort_analysis artifacts"
domain: "cohort_analysis construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```yaml
kind: cohort_analysis
name: monthly_retention_by_acquisition_channel
description: "Tracks user retention rates and LTV by acquisition channel over time"
vendor: Looker
data_source: Snowflake
parameters:
  cohort_definition: "Users acquired in the same calendar month"
  time_period: "2023-01-01 to 2023-12-31"
  metrics:
    - name: "30_day_retention_rate"
      description: "Percentage of users active 30 days post-acquisition"
    - name: "customer_lifetime_value"
      description: "Predicted LTV calculated using cohort spend patterns"
```

## Anti-Example 1: Mixed with Benchmarking
```yaml
kind: cohort_analysis
name: retention_vs_benchmark
description: "Compares cohort retention to industry benchmarks"
vendor: Google Analytics
data_source: BigQuery
parameters:
  cohort_definition: "Users from Q3 2023"
  benchmark_data: "Third-party retention benchmarks"
  metrics:
    - name: "Benchmark_rank"
      description: "Cohort performance relative to industry peers"
```
## Why it fails: Combines cohort analysis with benchmarking (model evaluation), violating the boundary.

## Anti-Example 2: Billing-focused
```yaml
kind: cohort_analysis
name: usage_by_subscription_type
description: "Tracks feature usage by subscription plan"
vendor: Stripe
data_source: PostgreSQL
parameters:
  cohort_definition: "Users with active subscriptions"
  metrics:
    - name: "Monthly_revenue_per_user"
      description: "Average revenue per user by subscription tier"
```
## Why it fails: Focuses on billing metrics rather than retention/LTV, confusing with usage_report kind.
