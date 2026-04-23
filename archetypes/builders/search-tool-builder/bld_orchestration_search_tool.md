---
kind: collaboration
id: bld_collaboration_search_tool
pillar: P12
llm_function: COLLABORATE
purpose: How search-tool-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
quality: 9.0
title: "Collaboration Search Tool"
version: "1.0.0"
author: n03_builder
tags: [search_tool, builder, examples]
tldr: "Golden and anti-examples for search tool construction, demonstrating ideal structure and common pitfalls."
domain: "search tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - search-tool-builder
  - p03_sp_search_tool_builder
  - bld_collaboration_function_def
  - bld_collaboration_retriever
  - bld_collaboration_embedder_provider
  - bld_collaboration_retriever_config
  - bld_collaboration_builder
  - bld_instruction_search_tool
  - bld_knowledge_card_search_tool
  - bld_collaboration_browser_tool
---

# Collaboration: search-tool-builder
## My Role in Crews
I am a SPECIALIST. I answer ONE question: "what search provider, what type of search, and what results does it return?"
I do not build local vector stores. I do not ingest files.
I specify external search integrations so agents can access current web information.
## Crew Compositions
### Crew: "Knowledge Access"
```
  1. search-tool-builder -> "external web/news search"
  2. retriever-builder -> "local vector store search"
  3. document-loader-builder -> "file ingestion and chunking"
```
### Crew: "Research Agent Toolkit"
```
  1. search-tool-builder -> "web search for current data"
  2. function-def-builder -> "callable function for search"
  3. browser-tool-builder -> "web navigation for deep content"
```
## Handoff Protocol
### I Receive
- seeds: search use case, preferred provider, search type, budget constraints
- optional: filtering needs, language requirements, result field preferences
### I Produce
- search_tool artifact (.md + .yaml compiled)
- committed to: `cex/P04_tools/examples/p04_search_{provider}.md`
### I Signal
- signal: complete (with quality score from QUALITY_GATES)
- if quality < 8.0: signal retry with failure reasons
## Builders I Depend On
None — independent builder (layer 0). Search tools are self-contained provider integrations.
## Builders That Depend On Me
| Builder | Why |
|---------|-----|
| agent-builder | Agents reference search tools for web access |
| function-def-builder | May wrap search tool as a function definition |
| retriever-builder | May fall back to search_tool when local results insufficient |

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[search-tool-builder]] | upstream | 0.54 |
| [[p03_sp_search_tool_builder]] | upstream | 0.47 |
| [[bld_collaboration_function_def]] | sibling | 0.43 |
| [[bld_collaboration_retriever]] | sibling | 0.41 |
| [[bld_collaboration_embedder_provider]] | sibling | 0.36 |
| [[bld_collaboration_retriever_config]] | sibling | 0.35 |
| [[bld_collaboration_builder]] | sibling | 0.34 |
| [[bld_instruction_search_tool]] | upstream | 0.34 |
| [[bld_knowledge_card_search_tool]] | upstream | 0.34 |
| [[bld_collaboration_browser_tool]] | sibling | 0.33 |
