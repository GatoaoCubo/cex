---
kind: collaboration
id: bld_collaboration_mcp_server
pillar: P04
llm_function: COLLABORATE
purpose: How mcp-server-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Mcp Server"
version: "1.0.0"
author: n03_builder
tags: [mcp_server, builder, examples]
tldr: "Golden and anti-examples for mcp server construction, demonstrating ideal structure and common pitfalls."
domain: "mcp server construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - mcp-server-builder
  - bld_collaboration_streaming_config
  - bld_memory_mcp_server
  - p03_ins_mcp_server
  - p01_kc_mcp_server
  - bld_collaboration_agent
  - p03_sp_mcp_server_builder
  - p11_qg_mcp_server
  - bld_collaboration_boot_config
  - bld_collaboration_toolkit
---

# Collaboration: mcp-server-builder
## My Role in Crews
I am an INFRASTRUCTURE SPECIALIST. I answer ONE question: "what tools and resources does this server expose, and how does it transport them?"
I define MCP server contracts with transport selection, tool schemas, resource URI patterns, and auth strategies. I do NOT define skills (reusable capability phases), connectors (bidirectional integrations), clients (API consumers), or daemons (background processes without MCP protocol).
## Crew Compositions
### Crew: "Agent Tool Stack"
```
  1. knowledge-card-builder -> "domain knowledge about the service being wrapped"
  2. mcp-server-builder     -> "MCP server spec: tools, resources, transport, auth"
  3. skill-builder          -> "skill that wraps mcp_server tool calls into reusable phases"
  4. agent-builder          -> "agent wired to boot with this mcp_server"
```
### Crew: "Infrastructure Bootstrap"
```
  1. mcp-server-builder   -> "MCP server spec for each capability domain"
  2. spawn-config-builder -> "boot config injecting MCP server into agent startup"
  3. quality-gate-builder -> "validation criteria for tool call outputs"
```
### Crew: "Tool Audit"
```
  1. mcp-server-builder -> "current mcp_server spec under review"
  2. validator-builder  -> "validates tool schemas against JSON-Schema spec"
  3. knowledge-card-builder -> "captures findings and learnings from the audit"
```
## Handoff Protocol
### I Receive
- seeds: server name, domain, transport type (stdio/SSE/HTTP), tools to expose, auth requirements
- optional: existing service API docs or CLI reference, connector artifact to wrap, agent consuming the server
### I Produce
- mcp_server artifact (Markdown + YAML, complete frontmatter, tools_provided with JSON-Schema, resources_provided with URI templates, max 5KB)
- committed to: `cex/P04_tools/examples/p04_mcp_{server_slug}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with specific gate failures
## Builders I Depend On
- knowledge-card-builder: domain knowledge about the service being wrapped informs tool design
- spawn-config-builder: consumes my output to wire the MCP server into agent boot
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| skill-builder       | skills wrap mcp_server tool calls into reusable orchestrated phases |
| agent-builder       | agents declare which mcp_servers they boot with in their capabilities |
| spawn-config-builder | boot config references mcp_server transport type and auth strategy |
| validator-builder   | validates tool call schemas against the mcp_server spec |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[mcp-server-builder]] | related | 0.52 |
| [[bld_collaboration_streaming_config]] | sibling | 0.43 |
| [[bld_memory_mcp_server]] | downstream | 0.42 |
| [[p03_ins_mcp_server]] | upstream | 0.42 |
| [[p01_kc_mcp_server]] | upstream | 0.41 |
| [[bld_collaboration_agent]] | sibling | 0.40 |
| [[p03_sp_mcp_server_builder]] | upstream | 0.39 |
| [[p11_qg_mcp_server]] | downstream | 0.38 |
| [[bld_collaboration_boot_config]] | sibling | 0.37 |
| [[bld_collaboration_toolkit]] | sibling | 0.37 |
