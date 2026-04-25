---
id: p01_kc_cex_lp04_tools
kind: knowledge_card
8f: F3_inject
pillar: P01
title: "CEX LP04 Tools — What the LLM Uses (10 Types of Tool)"
version: 1.0.0
created: 2026-03-25
updated: 2026-03-25
author: builder_agent
domain: cex_taxonomy
quality: 9.2
tags: [cex, lp04, tools, call, skill, mcp, hook, plugin]
tldr: "P04 Tools groups 10 types of tool that extend the LLM beyond text via the CALL function"
when_to_use: "Classify tooling artifacts or understand how P04 connects the LLM to the external world"
keywords: [skill, mcp-server, hook, plugin, connector, daemon, component, cli-tool]
long_tails:
  - "What types of tool exist in CEX"
  - "Difference between skill and component in CEX"
axioms:
  - "ALWAYS register tools in the agent before using"
  - "NEVER expose a tool without explicit permission (P09 governs)"
linked_artifacts:
  primary: p01_kc_cex_lp03_prompt
  related: [p01_kc_cex_lp02_model, p01_kc_cex_lp01_knowledge]
density_score: 1.0
data_source: "https://arxiv.org/abs/2305.16504"
related:
  - p01_kc_cex_function_call
  - p01_kc_lp04_tools
  - api-client-builder
  - mcp-server-builder
  - p01_kc_mcp_server
  - cli-tool-builder
  - p01_kc_cex_lp03_prompt
  - p01_kc_cex_lp02_model
  - p01_kc_cex_lp01_knowledge
  - db-connector-builder
---

## Quick Reference

topic: LP04 Tools | scope: 10 artifact types | criticality: high
llm_function: CALL (+ GOVERN for hook/daemon)
analogy: toolbox

## Key Concepts

- P04 answers: "what external tools can I invoke?"
- skill is the core type (rich capability with phases and trigger)
- Dominant function CALL: LLM invokes tool during generation
- mcp_server exposes tools + resources via MCP protocol
- hook executes code on pre/post event (GOVERN, not CALL)
- component is the smallest composable pipeline unit
- Without P04 the LLM only generates text; with P04 it interacts with the world
- P04 is constrained by P02 (identity defines tools)
- client is a unidirectional consumer of external API
- connector is bidirectional (client is unidirectional)
- daemon persists in background (cli_tool executes and terminates)
- scraper extracts web data (do not confuse with client/API)
- plugin is a pluggable extension without structured phases
- XAgent (Tsinghua): tools in isolated Docker = security
- ToolBench catalogs 16,000+ real APIs with benchmarks
- P04 interacts with P09 (permissions) and P07 (evaluation)

## Phases

1. Registration: declare tool in agent or mcp_server
2. Permission: P09 Config governs access and limits
3. Invocation: LLM decides CALL during generation (ReAct loop)
4. Execution: tool runs and returns result to context
5. Monitoring: P07 Evals tests and evaluates performance

## Golden Rules

- ALWAYS declare tools before using (explicit registration)
- ALWAYS isolate tools in containers when possible
- NEVER give unrestricted access to tools (least privilege)
- NEVER use daemon when cli_tool suffices (complexity)
- ALWAYS prefer mcp_server over connector for new tools

## Comparison

| Type | Purpose | Persistent | Core |
|------|---------|------------|------|
| skill | Capability with phases + trigger | no | yes |
| mcp_server | MCP server (tools + resources) | yes | yes |
| hook | Pre/post processing on event | no | yes |
| plugin | Pluggable extension | yes | no |
| client | Unidirectional API client | no | no |
| cli_tool | Command-line tool | no | no |
| scraper | Web data extractor | no | no |
| connector | External bidirectional connector | no | no |
| daemon | Persistent background process | yes | no |
| component | Atomic pipeline block | no | no |

## Flow

```
[Agent (P02)] -- registra --> [skill / mcp_server / tool]
       |
[user_prompt (P03)] -- trigger --> [CALL decision]
       |
[ReAct loop] -- Thought --> Action --> Observation
       |                       |
       |              [tool executa]
       |                       |
       +<-- resultado volta ao contexto
       |
[Output (P05)] -- informado por tool results
```

## References

- source: https://arxiv.org/abs/2305.16504
- source: https://arxiv.org/abs/2307.16789
- deepens: p01_kc_cex_lp03_prompt
- related: p01_kc_cex_lp02_model


## Anti-Patterns

- Applying this artifact without understanding the domain context
- Treating this as a standalone reference without checking linked artifacts
- Ignoring version constraints when integrating

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[p01_kc_cex_function_call]] | sibling | 0.32 |
| [[p01_kc_lp04_tools]] | sibling | 0.28 |
| [[api-client-builder]] | downstream | 0.25 |
| [[mcp-server-builder]] | downstream | 0.25 |
| [[p01_kc_mcp_server]] | sibling | 0.24 |
| [[cli-tool-builder]] | downstream | 0.24 |
| [[p01_kc_cex_lp03_prompt]] | sibling | 0.24 |
| [[p01_kc_cex_lp02_model]] | sibling | 0.24 |
| [[p01_kc_cex_lp01_knowledge]] | sibling | 0.23 |
| [[db-connector-builder]] | downstream | 0.21 |
