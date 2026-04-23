---
kind: tools
id: bld_tools_agent_card
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for agent_card production
quality: 9.0
title: "Tools Agent Card"
version: "1.0.0"
author: n03_builder
tags: [agent_card, builder, examples]
tldr: "Golden and anti-examples for agent card construction, demonstrating ideal structure and common pitfalls."
domain: "agent card construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_spawn_config
  - bld_tools_workflow
  - bld_tools_input_schema
  - bld_tools_system_prompt
  - bld_tools_mcp_server
  - bld_tools_validator
  - bld_tools_retriever_config
  - bld_tools_pattern
  - bld_tools_memory_scope
  - bld_tools_cli_tool
---

# Tools: agent-card-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing agent_cards in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P08_architecture/_schema.yaml | Field definitions for agent_card |
| CEX Examples | P08_architecture/examples/ | Real agent_card artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | P08_agent_card seeds |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, overlaps |
| PRIME files | records/agent_groups/{name}/PRIME_{NAME}.md | Existing agent_group definitions |
| MCP configs | .mcp-{sat}.json | Per-agent_group MCP server configs |
| Spawn scripts | records/framework/powershell/spawn_*.ps1 | Boot and spawn patterns |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet for agent_cards.
Manually check each QUALITY_GATES.md gate against produced artifact:
- [ ] YAML parses without error
- [ ] id matches p08_ac_ prefix
- [ ] name is non-empty
- [ ] model is valid LLM identifier
- [ ] mcps is list
- [ ] role is non-empty
- [ ] quality is null
- [ ] All 7 body sections present

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_spawn_config]] | sibling | 0.66 |
| [[bld_tools_workflow]] | sibling | 0.62 |
| [[bld_tools_input_schema]] | sibling | 0.61 |
| [[bld_tools_system_prompt]] | sibling | 0.61 |
| [[bld_tools_mcp_server]] | sibling | 0.61 |
| [[bld_tools_validator]] | sibling | 0.61 |
| [[bld_tools_retriever_config]] | sibling | 0.60 |
| [[bld_tools_pattern]] | sibling | 0.59 |
| [[bld_tools_memory_scope]] | sibling | 0.59 |
| [[bld_tools_cli_tool]] | sibling | 0.59 |
