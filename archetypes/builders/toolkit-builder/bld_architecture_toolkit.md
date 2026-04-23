---
kind: architecture
id: bld_architecture_toolkit
pillar: P08
llm_function: CONSTRAIN
purpose: Component map of toolkit — inventory, dependencies, and architectural position
quality: 9.1
title: "Architecture Toolkit"
version: "1.0.0"
author: n03_builder
tags: [toolkit, builder, examples]
tldr: "Golden and anti-examples for toolkit construction, demonstrating ideal structure and common pitfalls."
domain: "toolkit construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_collaboration_toolkit
  - p03_ins_toolkit_builder
  - bld_tools_toolkit
  - toolkit-builder
  - p03_sp_toolkit_builder
  - bld_config_toolkit
  - p01_kc_toolkit
  - bld_knowledge_card_toolkit
  - bld_schema_toolkit
  - bld_memory_toolkit
---

# Architecture: toolkit in the CEX
## Component Inventory
| Name | Role | Owner | Status |
|------|------|-------|--------|
| frontmatter block | Metadata (id, kind, pillar, name, category, quality) | toolkit-builder | active |
| tool_definitions | List of tool entries with name, description, confirmation tier | toolkit-builder | active |
| confirmation_tiers | Permission levels: auto (read), confirm (write), deny (dangerous) | toolkit-builder | active |
| deny_lists | Per-tool agent denial entries with reasons | toolkit-builder | active |
| mcp_mapping | Tool-to-MCP-server endpoint mappings | toolkit-builder | active |
| category_metadata | Domain grouping and scope (nucleus/global/agent-specific) | toolkit-builder | active |
## Dependency Graph
```
toolkit  --consumed_by-->  agent/agent_group  --uses-->  tool_runtime
toolkit  --validated_by-->  skill_loader     --injects-->  agent_prompt
toolkit  --maps_to-->      mcp_server       --executes-->  tool_call
nucleus  --scoped_by-->    toolkit          --restricts-->  available_tools
```
| From | To | Type | Data |
|------|----|------|------|
| toolkit (P04) | agent/agent_group (P02) | configures | toolkit defines which tools the agent can access |
| toolkit | cex_skill_loader.py | consumed_by | skill loader reads toolkit to inject tool lists into prompts |
| toolkit | mcp_server | maps_to | MCP endpoint mapping enables remote tool execution |
| toolkit | quality_gate (P11) | validated_by | gate checks least-privilege compliance and tool count |
| nucleus config | toolkit | scopes | nucleus-level toolkit restricts tools for all agents in that nucleus |
| bld_tools_*.md ISOs | toolkit | references | builder ISOs reference toolkit for their tool permissions |
| cex_router.py | toolkit | queries | router checks toolkit to validate tool availability before dispatch |
## Boundary Table
| toolkit IS | toolkit IS NOT |
|------------|----------------|
| A permission bundle defining which tools an agent can access | Tool implementation code (that belongs in N05 operations) |
| Confirmation tiers (auto/confirm/deny) per operation risk level | Agent identity or persona definition (system_prompt P03) |
| Deny lists that override allow lists for explicit restrictions | Routing policy or dispatch rules (dispatch_rule P12) |
| MCP endpoint mapping for remote tool execution | Workflow steps or sequencing logic (workflow_primitive P12) |
| Scoped to one agent role or domain (max 15 tools) | A comprehensive registry of all tools in the system |
| Versioned and reviewable permission document | A runtime state that changes during execution |
## Layer Map
| Layer | Components | Purpose |
|-------|------------|---------|
| Identity | name, category, scope | Define what domain this toolkit covers and who it targets |
| Permission | tool_definitions, confirmation_tiers | Specify each tool and its access level |
| Restriction | deny_lists | Explicitly block tools for specific agents |
| Integration | mcp_mapping | Connect tools to execution endpoints |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_toolkit]] | upstream | 0.75 |
| [[p03_ins_toolkit_builder]] | upstream | 0.72 |
| [[bld_tools_toolkit]] | upstream | 0.72 |
| [[toolkit-builder]] | upstream | 0.70 |
| [[p03_sp_toolkit_builder]] | upstream | 0.67 |
| [[bld_config_toolkit]] | downstream | 0.63 |
| [[p01_kc_toolkit]] | upstream | 0.62 |
| [[bld_knowledge_card_toolkit]] | upstream | 0.62 |
| [[bld_schema_toolkit]] | upstream | 0.58 |
| [[bld_memory_toolkit]] | downstream | 0.55 |
