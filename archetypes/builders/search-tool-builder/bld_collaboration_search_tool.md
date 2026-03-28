---
kind: collaboration
id: bld_collaboration_search_tool
pillar: P12
llm_function: COLLABORATE
purpose: How search-tool-builder works in crews with other builders
pattern: each builder must know its ROLE in a team, what it RECEIVES and PRODUCES
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
