---
id: bld_memory_canary_config
kind: knowledge_card
pillar: P10
title: "Memory: canary_config Builder Patterns"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: canary_config
quality: 6.6
tags: [memory, canary_config, P09]
llm_function: INJECT
tldr: "Recalled patterns and corrections for canary_config builder sessions."
density_score: null
---

# Memory: canary_config Builder

## Persistent Patterns
| Pattern | Frequency | Note |
|---------|-----------|------|
| Start with 5% or less initial traffic | HIGH | Risk management |
| Always define rollback trigger | HIGH | Gate H07 |
| stages_count must match list | HIGH | Gate H06 |
| Last stage must be 100% | HIGH | Completion gate H08 |

## Common Corrections
| Mistake | Correction |
|---------|-----------|
| User conflates with feature_flag | Teach: feature_flag is boolean; canary is traffic % |
| User conflates with ab_test_config | Teach: A/B uses statistics; canary uses metric threshold |
| User starts at 50% | Redirect: start at 5%; risk is proportional to traffic exposed |
| No rollback trigger | Block: add error_rate or latency threshold |
| Provider not specified | Default to argo_rollouts; ask user to confirm |
