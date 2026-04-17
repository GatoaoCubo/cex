---
id: n00_reasoning_strategy_manifest
kind: knowledge_card
pillar: P03
nucleus: n00
title: "Reasoning Strategy -- Canonical Manifest"
version: 1.0
quality: null
tags: [manifest, reasoning_strategy, p03, n00, archetype, template]
---

<!-- 8F: F1=knowledge_card P03 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A reasoning_strategy is a prompting technique specifically designed for structured reasoning tasks, defining how an agent should think through problems: step-by-step decomposition, self-verification, alternative hypothesis generation, or confidence-weighted synthesis. It maps reasoning methodologies (chain-of-thought, tree-of-thought, reflexion, self-ask) to specific task types and quality targets. The output is a reusable reasoning protocol injected during F4 REASON to improve inference quality.

## Pillar
P03 -- prompt

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `reasoning_strategy` |
| pillar | string | yes | Always `P03` |
| title | string | yes | Human-readable name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| methodology | string | yes | CoT, ToT, self-ask, reflexion, self-consistency |
| task_types | list | yes | Which task categories this strategy improves |
| verification_step | boolean | yes | Whether strategy includes explicit self-check |
| confidence_scoring | boolean | no | Whether outputs include confidence estimates |

## When to use
- When the F4 REASON step requires a specific reasoning framework for complex analytical tasks
- When N01 Intelligence needs structured competitive analysis with explicit reasoning chains
- When building agents that must explain their reasoning for audit or governance purposes

## Builder
`archetypes/builders/reasoning_strategy-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind reasoning_strategy --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: rs_cot_analysis_n01
kind: reasoning_strategy
pillar: P03
nucleus: n01
title: "Chain-of-Thought Analysis Strategy"
version: 1.0
quality: null
---
methodology: CoT
task_types: [competitive_analysis, market_research, gap_identification]
verification_step: true
confidence_scoring: true
```

## Related kinds
- `reasoning_trace` (P03) -- output artifact produced when a reasoning_strategy executes
- `planning_strategy` (P03) -- higher-level strategy that selects which reasoning_strategy to apply
- `prompt_technique` (P03) -- individual techniques composed into a reasoning_strategy
- `llm_judge` (P07) -- evaluator that scores reasoning_strategy output quality
