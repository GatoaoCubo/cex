---
kind: config
id: bld_config_capability_registry
pillar: P09
llm_function: CONSTRAIN
purpose: Naming, paths, limits for capability_registry production
quality: 8.9
title: "Config Capability Registry"
version: "1.0.0"
author: n04_wave8
tags: [capability_registry, builder, config, agent-discovery]
tldr: "Naming, paths, limits for capability_registry production"
domain: "capability_registry construction"
created: "2026-04-14"
updated: "2026-04-14"
density_score: 0.85
related:
  - p03_sp_capability_registry_builder
  - capability-registry-builder
  - bld_architecture_kind
  - bld_examples_capability_registry
  - kind-builder
  - bld_output_template_capability_registry
  - spec_infinite_bootstrap_loop
  - bld_collaboration_capability_registry
  - bld_collaboration_kind
  - bld_instruction_capability_registry
---

## Naming Convention
Pattern: `p08_cr_{{registry_name}}.md`
Examples:
- `p08_cr_builder_sub_agents.md` -- full index of .claude/agents/
- `p08_cr_nucleus_domain_agents.md` -- all N0x_*/agents/ entries
- `p08_cr_nucleus_cards.md` -- all 8 nucleus agent cards
- `p08_cr_full.md` -- combined registry (all three layers)
- `p08_cr_knowledge_domain.md` -- scoped to knowledge/RAG agents

## Paths
Artifacts stored in: `P08_architecture/registries/p08_cr_{{registry_name}}.md`
Builder ISOs stored in: `archetypes/builders/capability-registry-builder/`
Sub-agent definition: `.claude/agents/capability-registry-builder.md`

## Limits
max_bytes: 5120
max_entries_per_section: 300
max_turns: 6
effort_level: 4

## Index Sources
| Source                  | Path Pattern                              | Count (approx) |
|-------------------------|-------------------------------------------|----------------|
| Builder sub-agents      | `.claude/agents/*-builder.md`             | 252            |
| Nucleus domain agents   | `N0[1-6]_*/agents/agent_*.md`            | 16             |
| Nucleus agent cards     | `N0[1-7]_*/agent_card_n0[1-7].md`        | 7              |

## Hooks
pre_build: "python _tools/cex_query.py --list-agents"
post_build: "python _tools/cex_compile.py {path}"
on_error: null
on_quality_fail: "re-run with --strict-validate flag"

## Refresh Policy
Re-index whenever: new builder added | agent deprecated | quality score updated | pillar reassigned.
Recommended cadence: after each WAVE dispatch cycle.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p03_sp_capability_registry_builder]] | upstream | 0.39 |
| [[capability-registry-builder]] | upstream | 0.39 |
| [[bld_architecture_kind]] | upstream | 0.38 |
| [[bld_examples_capability_registry]] | upstream | 0.33 |
| [[kind-builder]] | upstream | 0.32 |
| [[bld_output_template_capability_registry]] | upstream | 0.31 |
| [[spec_infinite_bootstrap_loop]] | related | 0.30 |
| [[bld_collaboration_capability_registry]] | downstream | 0.29 |
| [[bld_collaboration_kind]] | downstream | 0.28 |
| [[bld_instruction_capability_registry]] | upstream | 0.28 |
