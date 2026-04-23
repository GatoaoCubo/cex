---
kind: tools
id: bld_tools_search_tool
pillar: P04
llm_function: CALL
purpose: Tools and APIs available for search_tool production
quality: 9.1
title: "Tools Search Tool"
version: "1.0.0"
author: n03_builder
tags: [search_tool, builder, examples]
tldr: "Golden and anti-examples for search tool construction, demonstrating ideal structure and common pitfalls."
domain: "search tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_tools_cli_tool
  - bld_tools_retriever_config
  - bld_tools_client
  - bld_tools_memory_scope
  - bld_tools_function_def
  - bld_tools_code_executor
  - bld_tools_mcp_server
  - bld_tools_prompt_version
  - bld_tools_runtime_rule
  - bld_tools_path_config
---

# Tools: search-tool-builder
## Production Tools
| Tool | Purpose | When | Status |
|------|---------|------|--------|
| brain_query [MCP] | Search existing search_tool artifacts in pool | Phase 1 (check duplicates) | CONDITIONAL |
| validate_artifact.py | Generic artifact validator | Phase 3 | [PLANNED] |
| cex_forge.py | Generate artifact from seeds | Alternative compose | [PLANNED] |
## Data Sources
| Source | Path/URL | Data |
|--------|----------|------|
| CEX Schema | P04_tools/_schema.yaml | Field definitions, search_tool kind |
| CEX Examples | P04_tools/examples/ | Real search_tool artifacts |
| SEED_BANK | archetypes/SEED_BANK.yaml | Seeds for P04_search_tool |
| TAXONOMY | archetypes/TAXONOMY_LAYERS.yaml | Layer position, runtime layer |
| Tavily Docs | tavily.com/docs | Provider reference |
| Serper Docs | serper.dev/docs | Provider reference |
| Brave Docs | brave.com/search/api | Provider reference |
| Exa Docs | exa.ai/docs | Provider reference |
## Tool Permissions

| Category | Tools | Status |
|----------|-------|--------|
| ALLOWED | Read, Write, Edit, Bash, Glob, Grep | Explicitly permitted |
| DENIED | (none) | Explicitly blocked |
| EFFECTIVE | Bash, Edit, Glob, Grep, Read, Write | ALLOWED minus DENIED |

## Interim Validation
No automated validator exists yet. Manually check each QUALITY_GATES.md gate against
the produced artifact. Key checks: YAML parses, id pattern, provider specified,
body <= 2048 bytes, quality == null, max_results >= 1, no API keys.

## Pipeline Integration

1. Created via 8F pipeline from F1-Focus through F8-Furnish
2. Scored by cex_score across three structural layers
3. Compiled by cex_compile for structural validation
4. Retrieved by cex_retriever for context injection
5. Evolved by cex_evolve when quality regresses below target

## Metadata

```yaml
id: bld_tools_search_tool
pipeline: 8F
scoring: hybrid_3_layer
```

```bash
python _tools/cex_score.py --apply bld-tools-search-tool.md
```

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_tools_cli_tool]] | sibling | 0.66 |
| [[bld_tools_retriever_config]] | sibling | 0.64 |
| [[bld_tools_client]] | sibling | 0.64 |
| [[bld_tools_memory_scope]] | sibling | 0.64 |
| [[bld_tools_function_def]] | sibling | 0.64 |
| [[bld_tools_code_executor]] | sibling | 0.63 |
| [[bld_tools_mcp_server]] | sibling | 0.63 |
| [[bld_tools_prompt_version]] | sibling | 0.62 |
| [[bld_tools_runtime_rule]] | sibling | 0.61 |
| [[bld_tools_path_config]] | sibling | 0.61 |
