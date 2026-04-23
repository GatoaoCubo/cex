---
kind: collaboration
id: bld_collaboration_client
pillar: P12
llm_function: COLLABORATE
purpose: How api-client-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Api Client"
version: "1.0.0"
author: n03_builder
tags: [api_client, builder, examples]
tldr: "Golden and anti-examples for api client construction, demonstrating ideal structure and common pitfalls."
domain: "api client construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - api-client-builder
  - bld_collaboration_connector
  - p03_sp_client_builder
  - bld_collaboration_streaming_config
  - bld_collaboration_builder
  - bld_collaboration_interface
  - bld_collaboration_env_config
  - p01_kc_api_client
  - bld_collaboration_runtime_rule
  - bld_tools_client
---

# Collaboration: api-client-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what endpoints does this client consume, and how does it authenticate?"
I do not build bidirectional connectors. I do not define MCP servers.
I specify unidirectional API consumers so agents can call external services reliably.
## Crew Compositions
### Crew: "External Integration"
```
  1. api-client-builder -> "API consumer with endpoints and auth"
  2. connector-builder -> "bidirectional sync if needed"
  3. env-config-builder -> "API keys and secret configuration"
```
### Crew: "Service Consumer Stack"
```
  1. interface-builder -> "formal contract with the service"
  2. api-client-builder -> "client implementation against the contract"
  3. fallback-chain-builder -> "degradation when service is unavailable"
```
## Handoff Protocol
### I Receive
- seeds: service name, base URL, auth strategy (API key, OAuth, bearer)
- optional: endpoint list, rate limits, pagetion pattern, retry policy
### I Produce
- client artifact (.md + .yaml frontmatter)
- committed to: `cex/P04/examples/p04_client_{service}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
- interface-builder: provides formal contract that the client implements
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| connector-builder | May extend client into bidirectional integration |
| env-config-builder | Documents API keys and secrets the client requires |
| e2e-eval-builder | Tests full pipeline including external API calls |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[api-client-builder]] | upstream | 0.53 |
| [[bld_collaboration_connector]] | sibling | 0.41 |
| [[p03_sp_client_builder]] | upstream | 0.38 |
| [[bld_collaboration_streaming_config]] | sibling | 0.37 |
| [[bld_collaboration_builder]] | sibling | 0.37 |
| [[bld_collaboration_interface]] | sibling | 0.35 |
| [[bld_collaboration_env_config]] | sibling | 0.35 |
| [[p01_kc_api_client]] | upstream | 0.34 |
| [[bld_collaboration_runtime_rule]] | sibling | 0.33 |
| [[bld_tools_client]] | upstream | 0.33 |
