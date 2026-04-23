---
kind: tools
id: bld_tools_workflow
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for workflow production
quality: 9.0
title: "Tools Workflow"
version: "1.0.0"
author: n03_builder
tags: [workflow, builder, examples]
tldr: "Golden and anti-examples for workflow construction, demonstrating ideal structure and common pitfalls."
domain: "workflow construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_spawn_config
  - bld_tools_system_prompt
  - bld_tools_retriever_config
  - bld_tools_agent_card
  - bld_tools_chain
  - bld_tools_memory_scope
  - bld_tools_action_prompt
  - bld_tools_cli_tool
  - bld_tools_prompt_version
  - bld_tools_path_config
---

# Tools: workflow-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing workflows in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P12_orchestration/_schema.yaml | Field definitions, workflow kind |
| ADW files | records/pool/workflows/ADW_*.md | ~240 existing implicit workflows |
| Signal Builder | archetypes/builders/signal-builder/ | Signal conventions and schema |
| Spawn Config Builder | archetypes/builders/spawn-config-builder/ | Spawn parameter patterns |
| Agent_group PRIMEs | records/agent_groups/*/PRIME_*.md | Agent_group capabilities and routing |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P12_workflow |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, steps_count match,
body has all 4 required sections, signals reference signal conventions, no prompt chaining leaked.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_spawn_config]] | sibling | 0.63 |
| [[bld_tools_system_prompt]] | sibling | 0.60 |
| [[bld_tools_retriever_config]] | sibling | 0.59 |
| [[bld_tools_agent_card]] | sibling | 0.59 |
| [[bld_tools_chain]] | sibling | 0.59 |
| [[bld_tools_memory_scope]] | sibling | 0.57 |
| [[bld_tools_action_prompt]] | sibling | 0.57 |
| [[bld_tools_cli_tool]] | sibling | 0.57 |
| [[bld_tools_prompt_version]] | sibling | 0.57 |
| [[bld_tools_path_config]] | sibling | 0.56 |
