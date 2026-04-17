---
id: bld_memory_slo_definition
kind: knowledge_card
pillar: P10
title: "Memory: slo_definition Builder Patterns"
version: 1.0.0
created: "2026-04-17"
updated: "2026-04-17"
author: builder
domain: slo_definition
quality: 7.1
tags: [memory, slo_definition, P09]
llm_function: INJECT
tldr: "Recalled patterns and corrections for slo_definition builder sessions."
density_score: null
---

# Memory: slo_definition Builder

## Persistent Patterns
| Pattern | Frequency | Note |
|---------|-----------|------|
| target_percent < 100.0 always | HIGH | Gate H06 |
| Compute error_budget_minutes from formula | HIGH | Never guess |
| Specify both fast-burn (1h) and slow-burn (6h) alerts | HIGH | Google SRE standard |
| error_budget_policy is mandatory | HIGH | Gate H07 |

## Common Corrections
| Mistake | Correction |
|---------|-----------|
| User sets 100% SLO | Reject: explain error budget requires headroom; suggest 99.99% |
| User conflates SLO with SLA | Teach: SLA is contract with penalties; SLO is internal target |
| User omits burn rate thresholds | Add standard 14x/6x burn rates |
| User conflates with quality_gate | Redirect: quality_gate is build-time; slo_definition is runtime |

## Context Injection Priority
1. bld_schema_slo_definition.md
2. bld_knowledge_card_slo_definition.md (error budget math)
3. bld_examples_slo_definition.md
4. bld_quality_gate_slo_definition.md
