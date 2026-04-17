---
kind: examples
id: bld_examples_usage_report
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of usage_report artifacts
quality: 8.8
title: "Examples Usage Report"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [usage_report, builder, examples]
tldr: "Golden and anti-examples of usage_report artifacts"
domain: "usage_report construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
```yaml
kind: usage_report
name: monthly_usage_202310
spec:
  provider: aws
  service: bedrock
  model: Claude-3
  period: 2023-10
usage:
  total_invocations: 15234
  input_tokens: 4567890
  output_tokens: 1234567
  cost_usd: 1234.56
  peak_hour: "14:30"
  user_ids: ["user123", "user456"]
timestamp: "2023-11-01T08:00:00Z"
```

## Anti-Example 1: Missing required fields
```yaml
kind: usage_report
name: monthly_usage_202310
usage:
  total_invocations: 15234
```
## Why it fails
Lacks provider/service/model metadata required for billing attribution. Missing cost metrics and timestamp violate spec completeness.

## Anti-Example 2: Including budget data
```yaml
kind: usage_report
name: monthly_usage_202310
spec:
  provider: google
  service: aiplatform
  model: PaLM-2
  period: 2023-10
usage:
  total_invocations: 15234
  budget_limit: 2000
  actual_cost: 1234.56
```
## Why it fails
Mixes usage analytics with cost_budget spec data. The budget_limit field belongs to a different CEX kind and introduces scope contamination.
