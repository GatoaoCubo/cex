---
id: n00_agent_manifest
kind: knowledge_card
pillar: P02
nucleus: n00
title: "Agent -- Canonical Manifest"
version: 1.0
quality: 9.0
tags: [manifest, agent, p02, n00, archetype, template]
density_score: 1.0
updated: "2026-04-17"
related:
  - bld_collaboration_agent
  - agent-builder
  - p01_kc_agent
  - bld_schema_agent_profile
  - bld_schema_runtime_state
  - bld_schema_nucleus_def
  - bld_schema_crew_template
  - bld_schema_reranker_config
  - bld_schema_capability_registry
  - bld_schema_usage_report
---

<!-- 8F: F1=knowledge_card P02 F2=knowledge-card-builder F3=kinds_meta+builder-manifest F4=plan F5=scan F6=produce F7=gate F8=save -->

## Purpose
Agent defines the complete persona, capability set, and behavioral configuration for an AI agent. It specifies the agent's identity (name, role, sin lens), available tools, memory configuration, reasoning strategy, and delegation rules. Agents are the primary actors in CEX missions -- each nucleus is itself an agent, and agents can spawn sub-agents.

## Pillar
P02 -- Model

## Schema (key fields)
| Field | Type | Required | Description |
|-------|------|----------|-------------|
| id | string | yes | Unique artifact identifier |
| kind | string | yes | Always `agent` |
| pillar | string | yes | Always `P02` |
| title | string | yes | Agent name and role |
| version | semver | yes | Artifact version |
| quality | float\|null | yes | Peer-review score (null until reviewed) |
| nucleus | string | yes | Owning nucleus (n01-n07) |
| sin_lens | string | yes | Cultural DNA (e.g., Analytical Envy) |
| model_ref | string | yes | Reference to model_card or model_provider |
| tools | list | yes | Available tool identifiers |
| memory_scope_ref | string | no | Reference to memory_scope artifact |
| max_sub_agents | int | no | Maximum parallel sub-agents (default 5) |

## When to use
- When defining a new specialized AI agent for a task domain
- When spawning a nucleus instance for a specific mission
- When configuring agent capabilities for a crew role

## Builder
`archetypes/builders/agent-builder/`

Run: `python _tools/cex_8f_runner.py "your intent" --kind agent --execute`

## Template variables (open for instantiation)
- `{{NUCLEUS_ROLE}}` -- which nucleus domain owns this
- `{{SIN_LENS}}` -- cultural DNA (sin) driving the agent's decisions
- `{{TARGET_AUDIENCE}}` -- the tasks and stakeholders the agent serves
- `{{DOMAIN_CONTEXT}}` -- task domain and operational environment

## Example (minimal)
```yaml
---
id: agent_n01_research_analyst
kind: agent
pillar: P02
nucleus: n01
title: "N01 Research Analyst Agent"
version: 1.0
quality: null
---
nucleus: n01
sin_lens: Analytical Envy
model_ref: model_card_claude_sonnet_4_6
tools: [cex_retriever, cex_query, web_search]
max_sub_agents: 5
```

## Related kinds
- `agent_profile` (P02) -- persona construction method for this agent
- `nucleus_def` (P02) -- formal nucleus definition this agent belongs to
- `memory_scope` (P02) -- memory configuration for agent state
- `role_assignment` (P02) -- binding this agent to a crew role

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_collaboration_agent]] | downstream | 0.43 |
| [[agent-builder]] | related | 0.41 |
| [[p01_kc_agent]] | sibling | 0.40 |
| [[bld_schema_agent_profile]] | downstream | 0.39 |
| [[bld_schema_runtime_state]] | downstream | 0.38 |
| [[bld_schema_nucleus_def]] | downstream | 0.38 |
| [[bld_schema_crew_template]] | downstream | 0.37 |
| [[bld_schema_reranker_config]] | downstream | 0.36 |
| [[bld_schema_capability_registry]] | downstream | 0.36 |
| [[bld_schema_usage_report]] | downstream | 0.36 |
