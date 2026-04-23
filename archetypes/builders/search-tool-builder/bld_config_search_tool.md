---
kind: config
id: bld_config_search_tool
pillar: P09
llm_function: CONSTRAIN
purpose: Naming conventions, file paths, size limits, operational constraints
pattern: CONFIG restricts SCHEMA, never contradicts it
effort: medium
max_turns: 25
disallowed_tools: []
fork_context: null
hooks:
  pre_build: null
  post_build: null
  on_error: null
  on_quality_fail: null
permission_scope: nucleus
quality: 9.0
title: "Config Search Tool"
version: "1.0.0"
author: n03_builder
tags: [search_tool, builder, examples]
tldr: "Golden and anti-examples for search tool construction, demonstrating ideal structure and common pitfalls."
domain: "search tool construction"
created: "2026-04-07"
updated: "2026-04-07"
density_score: 0.90
related:
  - bld_instruction_search_tool
  - bld_knowledge_card_search_tool
  - bld_collaboration_search_tool
  - p03_sp_search_tool_builder
  - search-tool-builder
  - bld_examples_search_tool
  - bld_schema_search_tool
  - bld_output_template_search_tool
  - p11_qg_search_tool
  - bld_config_memory_scope
---
# Config: search_tool Production Rules
## Naming Convention
| Scope | Convention | Example |
|-------|-----------|---------|
| Artifact files | `p04_search_{provider_slug}.md` | `p04_search_tavily_web.md` |
| Compiled files | `p04_search_{provider_slug}.yaml` | `p04_search_tavily_web.yaml` |
| Builder directory | kebab-case | `search_tool-builder/` |
| Frontmatter fields | snake_case | `search_type`, `max_results` |
| Provider slug | snake_case, lowercase, no hyphens | `tavily_web`, `serper_google` |
Rule: id MUST equal filename stem. Hyphens in id = HARD FAIL.
## File Paths
- Output: `cex/P04_tools/examples/p04_search_{provider_slug}.md`
- Compiled: `cex/P04_tools/compiled/p04_search_{provider_slug}.yaml`
## Size Limits (aligned with SCHEMA)
- Body: max 2048 bytes
- Total (frontmatter + body): ~4000 bytes
- Density: >= 0.80 (no filler)
## Search Type Enum
| Value | Description | When to use |
|-------|-------------|-------------|
| web | Traditional web search | General queries, fact-checking |
| semantic | Meaning-based search | Content similarity, concept search |
| hybrid | Combined web + semantic | Research requiring both approaches |
| news | News-specific search | Current events, recent articles |
| images | Image search | Visual content discovery |
## Provider Environment Variables
| Provider | Env Var | Notes |
|----------|---------|-------|
| Tavily | TAVILY_API_KEY | Required for all queries |
| Serper | SERPER_API_KEY | Required for all queries |
| Perplexity | PERPLEXITY_API_KEY | Required for all queries |
| Brave | BRAVE_API_KEY | Optional (free tier available) |
| Exa | EXA_API_KEY | Required for all queries |
| Google | GOOGLE_API_KEY + GOOGLE_CSE_ID | Two keys required |
Rule: NEVER hardcode API keys. Always reference env vars.

## Related Artifacts

| Artifact | Relationship | Score |
|----------|-------------|-------|
| [[bld_instruction_search_tool]] | upstream | 0.39 |
| [[bld_knowledge_card_search_tool]] | upstream | 0.39 |
| [[bld_collaboration_search_tool]] | downstream | 0.39 |
| [[p03_sp_search_tool_builder]] | upstream | 0.39 |
| [[search-tool-builder]] | upstream | 0.37 |
| [[bld_examples_search_tool]] | upstream | 0.34 |
| [[bld_schema_search_tool]] | upstream | 0.34 |
| [[bld_output_template_search_tool]] | upstream | 0.31 |
| [[p11_qg_search_tool]] | downstream | 0.28 |
| [[bld_config_memory_scope]] | sibling | 0.26 |
