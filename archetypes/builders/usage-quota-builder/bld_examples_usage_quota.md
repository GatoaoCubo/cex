---
kind: examples
id: bld_examples_usage_quota
pillar: P07
llm_function: GOVERN
purpose: Golden and anti-examples of usage_quota artifacts
quality: 8.8
title: "Examples Usage Quota"
version: "1.0.0"
author: wave1_builder_gen_v2
tags: [usage_quota, builder, examples]
tldr: "Golden and anti-examples of usage_quota artifacts"
domain: "usage_quota construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
---

## Golden Example
---
kind: usage_quota
spec:
  model: gpt-3.5-turbo
  max_tokens_per_month: 100000
  fair_use_policy: "Exceeding quota may result in throttling."
  reset_interval: "monthly"
  enforcement: "soft"
  description: "Token usage limit for OpenAI's GPT-3.5 Turbo model."
---

## Anti-Example 1: Missing quota specification
---
kind: usage_quota
spec:
  model: gpt-3.5-turbo
  description: "Token usage limit for OpenAI's GPT-3.5 Turbo model."
  enforcement: "soft"
---

## Why it fails
The example lacks a concrete quota value (e.g., `max_tokens_per_month`). Without a measurable limit, the configuration cannot enforce fair use or track consumption.

## Anti-Example 2: Confusing rate limits with quota
---
kind: usage_quota
spec:
  model: gpt-3.5-turbo
  max_requests_per_minute: 60
  max_tokens_per_month: 100000
---

## Why it fails
The configuration mixes rate limits (`max_requests_per_minute`) with usage quota. Rate limits (RPM) and usage quotas are distinct policies and should be managed in separate configurations.
