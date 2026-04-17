---
id: con_rate_limit_config_n02
kind: rate_limit_config
pillar: P09
nucleus: n02
title: Marketing Rate Limits
version: 1.0
quality: 9.0
tags: [config, rate_limit, budget, marketing, runtime]
density_score: 1.0
---


<!-- 8F: F1 constrain=P09/rate_limit_config F2 become=rate_limit_config-builder F3 inject=nucleus_def_n02+n02_rules+kc_rate_limit_config+P09_schema
     F4 reason=throttle_cost_and_provider_pressure_for_marketing_runs F5 call=shell_command,apply_patch F6 produce=4048 bytes
     F7 govern=frontmatter_sections_ascii_density_linecount F8 collaborate=N02_marketing/P09_config/con_rate_limit_config_n02.md -->

# Purpose

| Item | Definition |
|------|------------|
| Mission fit | Throughput and budget limits for N02 model usage |
| Creative Lust lens | Desire-rich systems can over-generate variants; limits keep attraction profitable instead of reckless |
| Primary use | Bound requests, tokens, and daily spend for marketing workflows |
| Scope | N02 drafting, refinement, and review loops |
| Why limits matter | High-velocity experimentation can seduce the operator into runaway cost |

## Values

| Profile | Provider | RPM | TPM | Daily Budget USD | Backoff |
|---------|----------|-----|-----|------------------|---------|
| draft_fast | openai | 24 | 120000 | 12 | exponential_jitter |
| review_strict | openai | 12 | 60000 | 8 | exponential_jitter |
| batch_variant | openai | 8 | 90000 | 10 | exponential_jitter |
| fallback_low | anthropic | 6 | 40000 | 6 | exponential_jitter |

## Allocation Rules

| Rule | Value |
|------|-------|
| default_profile | draft_fast |
| max_parallel_jobs | 2 |
| conservation_trigger | 80 percent of daily budget |
| hard_stop_trigger | 100 percent of daily budget |
| retry_limit_on_429 | 4 |
| cooldown_after_hard_stop | 24h |

## Budget Intent

| Workflow | Preferred Profile | Why |
|----------|-------------------|-----|
| single artifact drafting | draft_fast | Keeps ideation lively without opening floodgates |
| validator or rule review | review_strict | Lower volume, higher precision |
| multi-variant ad generation | batch_variant | Supports controlled A/B exploration |
| provider degradation mode | fallback_low | Maintains delivery when primary capacity tightens |

## Rationale

| Decision | Reason |
|----------|--------|
| Separate draft and review profiles | Seductive ideation and strict governance have different throughput needs |
| Two parallel jobs max | Enough speed for wave work without creating token spikes |
| Exponential jitter only | Prevents synchronized retries during provider stress |
| Budget caps under 12 USD per profile | Keeps nucleus experimentation disciplined |
| Conservation trigger at 80 percent | Encourages graceful slowdown before a hard stop |

## Example

```yaml
rate_limit_run:
  workflow: multi_variant_ad_generation
  profile: batch_variant
  provider: openai
  rpm: 8
  tpm: 90000
  daily_budget_usd: 10
  backoff: exponential_jitter
```

| Example Event | Expected Action | Result |
|---------------|-----------------|--------|
| Spend reaches 81 percent | switch to review_strict or fallback_low | slowdown |
| Four 429 errors in a row | stop retries | preserve quota |
| Warm day with low spend | keep draft_fast | normal throughput |
| Hard budget hit | suspend generation | zero overspend |

## Monitoring Signals

| Signal | Threshold | Response |
|--------|-----------|----------|
| rpm_usage | > 90 percent for 3 min | reduce concurrency |
| tpm_usage | > 85 percent for 2 min | shorten batch size |
| spend_today | > 80 percent | enter conservation mode |
| spend_today | >= 100 percent | hard stop and alert |

## Properties

| Property | Value |
|----------|-------|
| Kind | rate_limit_config |
| Pillar | P09 |
| Nucleus | n02 |
| Provider count | 2 |
| Profile count | 4 |
| Backoff style | exponential_jitter |
| Budget control | hard cap plus conservation mode |
| Main risk prevented | runaway spend from variant overproduction |
| Operational mood | bold but bounded |
| Save path | N02_marketing/P09_config/con_rate_limit_config_n02.md |
