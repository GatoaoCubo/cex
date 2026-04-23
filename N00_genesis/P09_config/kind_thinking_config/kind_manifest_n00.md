---
id: n00_thinking_config_manifest
kind: knowledge_card
pillar: P09
nucleus: n00
title: "Thinking Config -- Canonical Manifest"
version: 1.0
quality: 8.9
tags: [manifest, thinking_config, p09, n00, archetype, template]
density_score: 1.0
related:
  - bld_schema_thinking_config
  - bld_config_thinking_config
  - p03_sp_thinking_config_builder
  - bld_collaboration_thinking_config
  - bld_knowledge_card_effort_profile
  - bld_memory_thinking_config
  - thinking-config-builder
  - bld_schema_reranker_config
  - bld_instruction_thinking_config
  - bld_schema_sandbox_spec
---

<!-- 8F: F1=knowledge_card P09 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
A thinking_config defines extended thinking and budget token settings for Claude models that support it. It controls how many tokens are allocated for the model's internal reasoning chain before producing output, enabling deeper analysis for complex architectural decisions, research synthesis, and quality evaluation tasks where chain-of-thought depth improves output quality.

## Pillar
P09 -- config

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `thinking_config` |
| pillar | string | yes | Always `P09` |
| title | string | yes | Human-readable config name |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| enabled | boolean | yes | Whether extended thinking is active |
| budget_tokens | integer | yes | Max tokens for internal reasoning (0 = disabled) |
| min_budget_tokens | integer | no | Minimum budget to guarantee non-trivial reasoning |
| thinking_model | string | no | Model identifier (must support thinking) |
| stream_thinking | boolean | no | Whether to stream thinking blocks to output |
| apply_to | list | no | Which 8F stages use extended thinking (F4, F7...) |

## When to use
- Enabling deep reasoning for N01 research synthesis on complex market analysis
- Configuring extended thinking for N03 architectural decisions (F4 REASON stage)
- Setting up thinking budget for N07 mission planning across many nuclei and waves

## Builder
`archetypes/builders/thinking_config-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind thinking_config --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA driving the artifact
- `{{TARGET_AUDIENCE}}` -- who this serves
- `{{DOMAIN_CONTEXT}}` -- business/technical context

## Example (minimal)
```yaml
---
id: thinking_config_n01_research
kind: thinking_config
pillar: P09
nucleus: n01
title: "N01 Research Extended Thinking Config"
version: 1.0
quality: null
---
enabled: true
budget_tokens: 8000
min_budget_tokens: 1000
thinking_model: claude-opus-4-6
stream_thinking: false
apply_to: [F4, F7]
```

## Related kinds
- `effort_profile` (P09) -- effort profiles that enable/disable thinking based on task level
- `cost_budget` (P09) -- thinking tokens count against budget, must be tracked
- `experiment_config` (P09) -- experiments comparing thinking vs. standard output quality

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_schema_thinking_config]] | upstream | 0.49 |
| [[bld_config_thinking_config]] | related | 0.40 |
| [[p03_sp_thinking_config_builder]] | upstream | 0.39 |
| [[bld_collaboration_thinking_config]] | downstream | 0.38 |
| [[bld_knowledge_card_effort_profile]] | sibling | 0.37 |
| [[bld_memory_thinking_config]] | downstream | 0.37 |
| [[thinking-config-builder]] | related | 0.37 |
| [[bld_schema_reranker_config]] | upstream | 0.36 |
| [[bld_instruction_thinking_config]] | upstream | 0.36 |
| [[bld_schema_sandbox_spec]] | upstream | 0.34 |
