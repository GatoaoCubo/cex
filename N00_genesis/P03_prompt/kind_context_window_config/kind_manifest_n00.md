---
id: n00_context_window_config_manifest
kind: knowledge_card
pillar: P03
nucleus: n00
title: "Context Window Config -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, context_window_config, p03, n00, archetype, template]
density_score: 1.0
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A context_window_config specifies token budget allocation, priority tiers, and overflow rules for a nucleus or builder run. It determines how the available context window is partitioned between system prompt, injected knowledge, conversation history, and generation headroom. The output ensures builders never exceed model limits and that the highest-value context always wins when capacity is scarce.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `context_window_config` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| total_tokens | integer | yes | Total context window size for target model |
| budget_allocation | map | yes | Token budget per slot: system, history, inject, generate |
| overflow_strategy | string | yes | truncate_oldest, summarize, or reject |
| priority_tiers | list | no | Ordered list of context slots by eviction priority |

## When to use
- When a nucleus or builder operates near model context limits and needs explicit budget management
- When multiple context sources (KCs, memory, history) compete for the same window
- When deploying to models with different context sizes (8K vs 200K vs 1M)

## Builder
`archetypes/builders/context_window_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind context_window_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: cwc_n01_sonnet_200k
kind: context_window_config
pillar: P03
nucleus: n01
title: "N01 Sonnet 200K Budget"
version: 1.0
quality: null
---
total_tokens: 200000
budget_allocation:
  system: 8000
  inject: 60000
  history: 100000
  generate: 32000
overflow_strategy: summarize
```

## Related kinds
- `constraint_spec` (P03) -- hard limits that context_window_config must respect
- `prompt_cache` (P10) -- cache layer that reduces effective token consumption
- `memory_summary` (P10) -- compressed history that fits within budget allocation
- `system_prompt` (P03) -- primary consumer of the system slot budget
