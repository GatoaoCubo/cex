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
