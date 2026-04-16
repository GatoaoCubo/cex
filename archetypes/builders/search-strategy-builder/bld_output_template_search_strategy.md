---
kind: output_template
id: bld_output_template_search_strategy
pillar: P05
llm_function: PRODUCE
purpose: Template with vars for search_strategy production
quality: 9.1
title: "Output Template Search Strategy"
version: "1.0.0"
author: wave1_builder_gen
tags: [search_strategy, builder, output_template]
tldr: "Template with vars for search_strategy production"
domain: "search_strategy construction"
created: "2026-04-13"
updated: "2026-04-13"
density_score: 0.85
---

```yaml
id: p04_ss_{{slug}}                # e.g. p04_ss_adaptive_beam_search
kind: search_strategy
pillar: P04
title: "{{Strategy Name}}"
version: "1.0.0"
created: "{{YYYY-MM-DD}}"
updated: "{{YYYY-MM-DD}}"
author: "{{nucleus_or_team}}"
domain: "{{domain, e.g. inference serving, edge AI, batch processing}}"
quality: null                      # NEVER self-score
tags: [search_strategy, "{{domain_tag}}", "{{compute_tag}}"]
tldr: "{{One concrete sentence: allocation approach, resource type, latency target}}"
strategy_type: "{{static|dynamic|adaptive}}"
target_entity: "{{GPU cluster|edge node|serverless function|...}}"
```

## Overview
<!-- Purpose: what compute allocation problem this strategy solves.
     Scope: which inference loads it applies to (batch vs. real-time, query sizes).
     Contrast: how it differs from static allocation or alternative strategies. -->

## Objectives
| Goal | Target | Constraint |
|------|--------|------------|
| Latency | p99 < `{{N}}`ms | Under `{{load_condition}}` |
| Throughput | > `{{N}}` QPS | With <= `{{resource_budget}}` |
| Utilization | GPU > `{{N}}`% | No OOM, no cold-start >`{{N}}`s |

## Methodology
<!-- Step-by-step allocation logic.
     Decision points: what signals trigger reallocation.
     Algorithms: Pareto-frontier, bin-packing, cost-benefit. -->
1. Classify query complexity: `{{classifier approach}}`
2. Look up resource tier: `{{tier table or formula}}`
3. Allocate: {{allocation call, e.g. Kubernetes resource request}}
4. Fallback: `{{what happens on OOM or timeout}}`

## Parameters
| Parameter | Type | Default | Range | Notes |
|-----------|------|---------|-------|-------|
| `{{param}}` | float | {{default}} | [{{min}}, {{max}}] | `{{tuning guidance}}` |
| timeout_ms | int | 500 | [50, 5000] | Hard SLA cutoff |

## Constraints
- Resource hard limits: CPU <= `{{N}}` cores, RAM <= `{{N}}` GB
- Latency SLA: p99 <= `{{N}}`ms
- Strategy enum: must be one of static, dynamic, or adaptive

## Evaluation Metrics
| Metric | Target | Measurement Method |
|--------|--------|-------------------|
| Allocation efficiency | >= 90% | Used / Allocated |
| SLA compliance | >= 99.9% | Requests within latency target |
| Cost per request | <= $`{{N}}` | Cloud billing / request count |
