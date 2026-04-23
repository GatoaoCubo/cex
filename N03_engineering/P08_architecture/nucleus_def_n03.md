---
id: p02_nd_n03.md
kind: nucleus_def
pillar: P02
nucleus_id: N03
role: builder
sin_lens: "Inventive Pride"
cli_binding: claude
model_tier: opus
model_specific: claude-opus-4-6
context_tokens: 1000000
boot_script: boot/n03.ps1
agent_card_path: N03_engineering/agent_card_n03.md
pillars_owned:
  - P02
  - P05
  - P06
  - P08
crew_templates_exposed:
  - builder_bootstrap
  - kind_genesis
domain_agents:
  - agent_builder_architect
  - agent_schema_designer
fallback_cli: codex
title: "Nucleus Def N03"
version: "1.0.0"
author: n07_crewwiring
domain: "artifact construction, builders, scaffolds"
quality: 9.0
tags: [nucleus_def, n03, builder, composable]
tldr: "N03 is the builder nucleus: constructs all CEX artifacts via 8F. Claude Opus 1M context."
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.88
related:
  - p02_nd_n01.md
  - kc_nucleus_def
  - p02_nd_n04.md
  - bld_collaboration_kind
  - p02_nd_n06.md
  - p02_nd_n05.md
  - kind-builder
  - p02_nd_n02.md
  - p02_nd_n07.md
  - bld_collaboration_model_card
---

## Identity

| Field | Value |
|-------|-------|
| Nucleus ID | N03 |
| Role | builder |
| Sin Lens | Inventive Pride |
| CLI Binding | claude |
| Model Tier | opus |
| Model | claude-opus-4-6 |
| Context | 1M tokens |
| Boot Script | `boot/n03.ps1` |
| Agent Card | `N03_engineering/agent_card_n03.md` |

## Pillars Owned

| Pillar | Domain | Sample Kinds |
|--------|--------|--------------|
| P02 | model | agent, agent_card, role_assignment |
| P05 | output | output_template, formatter, diagram |
| P06 | schema | input_schema, validation_schema, type_def |
| P08 | architecture | component_map, interface, decision_record |

## Crew Templates Exposed

| Template | Role in Crew | Inputs | Outputs |
|----------|--------------|--------|---------|
| builder_bootstrap | architect | kind spec | 13-ISO builder package |
| kind_genesis | architect | new kind proposal | kinds_meta entry + builder + KC |

## Domain Agents

| Agent | Purpose | Path |
|-------|---------|------|
| agent_builder_architect | Builder design | `N03_engineering/P02_model/` |
| agent_schema_designer | Data contract design | `N03_engineering/P02_model/` |

## Boot Contract

- Boot file: `boot/n03.ps1`
- Task source: `.cex/runtime/handoffs/n03_task.md`
- Signal: `write_signal('n03', 'complete', {score})`

## Composability

| Direction | Nucleus | What Flows |
|-----------|---------|-----------|
| outbound | all | new builders + ISOs |
| outbound | N04 | kind KCs |
| inbound | N07 | construction handoffs |
| inbound | N01 | new-kind research |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p02_nd_n01.md]] | sibling | 0.45 |
| [[kc_nucleus_def]] | upstream | 0.44 |
| [[p02_nd_n04.md]] | sibling | 0.42 |
| [[bld_collaboration_kind]] | downstream | 0.39 |
| [[p02_nd_n06.md]] | sibling | 0.37 |
| [[p02_nd_n05.md]] | sibling | 0.37 |
| [[kind-builder]] | downstream | 0.37 |
| [[p02_nd_n02.md]] | sibling | 0.37 |
| [[p02_nd_n07.md]] | sibling | 0.37 |
| [[bld_collaboration_model_card]] | related | 0.35 |
