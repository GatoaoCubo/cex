---
kind: config
id: bld_config_spawn_config
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Spawn Config"
version: "1.0.0"
author: n03_builder
tags: [spawn_config, builder, examples]
tldr: "Golden and anti-examples for spawn config construction, demonstrating ideal structure and common pitfalls."
domain: "spawn config construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_knowledge_card_spawn_config
  - p01_kc_spawn_config
  - bld_output_template_spawn_config
  - p03_sp_spawn-config-builder
  - bld_collaboration_spawn_config
  - p11_qg_spawn_config
  - bld_config_agent_card
  - p01_kc_mcp_server
  - bld_schema_spawn_config
  - p07_bm_agent_group_boot_time
---
# Config: spawn_config Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p12_spawn_{mode_slug}.yaml` | `p12_spawn_shaka_solo_research.yaml` |
| Builder directory | kebab-case | `spawn-config-builder/` |
| Frontmatter fields | snake_case | `mcp_config`, `prompt_strategy` |
| Mode slug | snake_case, lowercase | `shaka_solo_research`, `grid_wave_1` |
Rule: id MUST equal filename stem.
## File Paths
- Output: `cex/P12_orchestration/examples/p12_spawn_{mode_slug}.yaml`
- Compiled: `cex/P12_orchestration/compiled/p12_spawn_{mode_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 3072 bytes
- Total (frontmatter + body): ~4500 bytes
- Density: >= 0.80
## Mode Enum
| Value | When to use | Script |
|-------|-------------|--------|
| solo | 1 agent_group, 1 task | spawn_solo.ps1 |
| grid | 2-6 agent_groups, parallel tasks | spawn_grid.ps1 |
| continuous | >6 tasks, auto-refill slots from queue | spawn_grid.ps1 -mode continuous |
## Baseline Flags (mandatory)
| Flag | Purpose |
|------|---------|
| --dangerously-skip-permissions | Skip tool permission prompts |
| --no-chrome | Prevent Chrome extension loading |
| -p | Non-interactive mode (skip workspace trust) |
## Agent_group-Model Routing
| Agent_group | Model | MCP Config |
|-----------|-------|------------|
| shaka | sonnet | .mcp-shaka.json |
| lily | sonnet | .mcp-lily.json |
| edison | opus | .mcp-edison.json |
| pytha | sonnet | .mcp-pytha.json |
| atlas | opus | .mcp-atlas.json |
| york | sonnet | .mcp-york.json |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_knowledge_card_spawn_config]] | downstream | 0.38 |
| [[p01_kc_spawn_config]] | downstream | 0.37 |
| [[bld_output_template_spawn_config]] | upstream | 0.33 |
| [[p03_sp_spawn-config-builder]] | upstream | 0.31 |
| [[bld_collaboration_spawn_config]] | downstream | 0.31 |
| [[p11_qg_spawn_config]] | downstream | 0.30 |
| [[bld_config_agent_card]] | sibling | 0.30 |
| [[p01_kc_mcp_server]] | upstream | 0.29 |
| [[bld_schema_spawn_config]] | upstream | 0.28 |
| [[p07_bm_agent_group_boot_time]] | upstream | 0.28 |
